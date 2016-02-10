from Monitor_Network_Connections import *
from Process_Profile import *
from Network import *
#-----------------------------------------------------------------------------------------------------------------------


def creating_processes_list():
    processes = ProcessProfile()
    processes_list = processes.monitor_processes()
    return processes_list


def creating_connections_list():
    Connections = NetworkConnections()
    connections_list = Connections.monitors_network_connections()
    return connections_list


def filter_connections(con_list):
    filtered_con_list = []
    for con in con_list:
        local_addr = con.get_local_adress()
        if local_addr != "127.0.0.1" and local_addr != "[" and local_addr != "0.0.0.0":
            filtered_con_list.append(con)
    for connect in filtered_con_list:
        set_connection_maker(connect, filtered_con_list)
    return filtered_con_list


def filter_processes_list(con_list, processes_list):
    filtered_proc_list = []
    for proc in processes_list:
        pid = proc.get_pid()
        for con in con_list:
            pidd = con.get_pid()
            if pid == pidd:
                filtered_proc_list.append(proc)


    return filtered_proc_list


def set_connection_maker(connection, connection_list):
    local_ip = connection.get_local_port()
    for con in connection_list:
        foreign_port = con.get_foreign_port()
        if foreign_port == local_ip:
            connection.set_connection_maker("No")
    if connection.get_connection_maker() == None:
        connection.set_connection_maker("Yes")

connections_list = creating_connections_list()
filtered_con_list = filter_connections(connections_list)
proc_list = creating_processes_list()
filtered_proc_list = filter_processes_list(filtered_con_list, proc_list)



obb = NetWorkClient()
obb.run()
pickled = pickle.dumps(filtered_con_list)
obb.send(pickled)



