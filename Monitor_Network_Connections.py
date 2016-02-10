import subprocess


class Connection:

    def __init__(self, protocol, local_adress, foreign_adress, state, pid, connection_maker):
        self.protocol = protocol
        self.local_adress = local_adress
        self.foreign_adress = foreign_adress
        self.state = state
        self.pid = pid
        self.connection_maker = connection_maker

    def get_protocol(self):

        return self.protocol

    def get_local_adress(self):

        return self.local_adress.split(":")[0]

    def get_local_port(self):

        return self.local_adress.split(":")[1]

    def get_foreign_adress(self):

        return self.foreign_adress.split(":")[0]

    def get_foreign_port(self):

        return self.foreign_adress.split(":")[1]

    def get_state(self):

        return self.state

    def get_pid(self):

        return self.pid

    def get_connection_maker(self):

        return self.connection_maker

    def set_connection_maker(self, connection_maker):
        self.connection_maker = connection_maker


class NetworkConnections:
    def __init__(self):
        pass

    def monitors_network_connections(self):
        # calling Netstat function to monitor network connections
        network_connections_objects_to_return = []
        network_connections_data = self.netstat()
        network_connections_list = network_connections_data.split("\r\n")
        # Remove the items from the list that are not "connections"
        # Always the first four items and the last item
        for i in range(4):
            network_connections_list.remove(network_connections_list[0])
        network_connections_list.remove('')
        # For every item in the list the "Make_Object_Network_Connection" function is called to change the
        #  item to a Connection object
        for network_connection in network_connections_list:
            connection = self.make_object_network_connection(network_connection)
        #------ Every object is appended to a list if the connection is external
            network_connections_objects_to_return.append(connection)
        return network_connections_objects_to_return

    def make_object_network_connection(self, network_connection):
        splited_network_connections = network_connection.split(' ')
        while '' in splited_network_connections:
            splited_network_connections.remove('')
        protocol = splited_network_connections[0]
        if protocol == "TCP":
            local_adress = splited_network_connections[1]
            foreign_adress = splited_network_connections[2]
            state = splited_network_connections[3]
            pid = splited_network_connections[4]
            connection_maker = None
            New_Connection = Connection(protocol, local_adress, foreign_adress, state, pid, connection_maker)
        else:
            local_adress = splited_network_connections[1]
            foreign_adress = splited_network_connections[2]
            pid = splited_network_connections[3]
            connection_maker = None
            New_Connection = Connection(protocol, local_adress, foreign_adress, "", pid, connection_maker)
        return New_Connection

    def netstat(self):
        Temp = subprocess.Popen(["netstat", "-nao"], stdout=subprocess.PIPE, shell=True)
        (output, errput) = Temp.communicate()
        return output









