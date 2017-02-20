# py_generaltaskthread
A simple  Task / TaskThread  to make the use of async execution eaiser in Python

```shellscripts
class PrintTask(Task):
    def __init__(self):
        Task.__init__(self)
    def run(self):
        print("[%s] just print information ... Task Id(%d)"
              %(self.get_current_thread_name(), self.taskid));

t1 = TaskThread(name="thread1")
t2 = TaskThread(name="thread2")

# Start the threads
t1.start()
t2.start()

# Add task
t1.addtask(PrintTask())
id2 = t1.addtask(PrintTask())
# Cancel task by id
t1.canceltask(id2)
t2.addtask(PrintTask())

# Wait to see the results
from time import sleep
sleep(1)

# Close the thread
t1.stop()
t2.stop()
```
