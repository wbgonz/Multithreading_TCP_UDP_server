
#!/usr/bin/python


import threading
import time

exitFlag = 0

# The program executes in roughly 10 seconds.
# This is consistent with the two threads that have a total delay of 10s
# thread1 executes the while loop 10 times with a delay of 10 seconds
# Thread2 executes it 5 times with a delay of 2s making it a total of 10s
# this shows the program is running in parallel since  if it was running serially the
# running time would take 20s to execute.


#  The time class is used to time the thread execution
# the threading class is used to create a myThread class using inherritance of Thread
#  The __init__ method is overridden to suit our thread similarly the run method is overridden to account
#  for our thread runnig behaviour of our thread

class myThread(threading.Thread):

    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s %d" % (threadName, time.ctime(time.time()), counter))
        print(threading.active_count())
        counter -= 1

# the time taken is roughly 25s similarly as above this is consistent with the delays given


# Create new threads
thread1 = myThread(1, "Thread-1", 25, 1)
thread2 = myThread(2, "Thread-2", 12, 2)
thread3 = myThread(2, "Thread-3", 8, 3)
thread4 = myThread(2, "Thread-4",  6, 4)
thread5 = myThread(2, "Thread-5",  5, 5)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

print("Exiting Main Thread")
