
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


# Create new threads
thread1 = myThread(1, "Thread-1", 10, 1)
thread2 = myThread(2, "Thread-2", 5, 2)


# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
