
from generaltaskthread import *

class PrintTask(Task):
    def __init__(self):
        Task.__init__(self)
    def run(self):
        print("[%s] just print information ... Task Id(%d)"
              %(self.get_current_thread_name(), self.taskid));

t1 = TaskThread(name="thread1")
t2 = TaskThread(name="thread2")

t1.start()
t2.start()

t1.addtask(PrintTask())
id2 = t1.addtask(PrintTask())
t1.canceltask(id2)
t2.addtask(PrintTask())

from time import sleep
sleep(1)

t1.stop()
t2.stop()
