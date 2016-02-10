

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

        return self.local_adress

    def get_foreign_adress(self):

        return self.foreign_adress

    def get_state(self):

        return self.state

    def get_pid(self):

        return self.pid

    def get_connection_maker(self):

        return self.connection_maker

    def set_connection_maker(self, connection_maker):
        self.connection_maker = connection_maker


