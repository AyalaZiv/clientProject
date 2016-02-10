import subprocess



class Process:

    def __init__(self, name, pid, mem_usage):
        self.name = name
        self.pid = pid
        self.mem_usage = mem_usage

    def get_name(self):

        return self.name

    def get_pid(self):

        return self.pid

    def get_mem_usage(self):

        return self.mem_usage


class ProcessProfile:
    def monitor_processes(self):
        processes_objects_to_return = []
        processes_data = self.tasklist()
        processes_list = processes_data.split("\r\n")
        #----------     Remove the items from the list that are not "Processes"
        #---------- Always the first five items
        for i in range(5):
            processes_list.remove(processes_list[0])
        processes_list.remove('')
        for proc in processes_list:
            process = self.make_object_process(proc)
            #------ Every object is appended to a list if the connection is external
            processes_objects_to_return.append(process)
        return processes_objects_to_return

    def make_object_process(self, proc):
        splited_process = proc.split(' ')
        while '' in splited_process:
            splited_process.remove('')
        new_process = Process(splited_process[0], splited_process[1], splited_process[4])
        return new_process

    def tasklist(self):
        Temp = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE, shell=True)
        (output, errput) = Temp.communicate()
        return output



