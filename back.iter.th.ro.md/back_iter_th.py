import threading
from time import sleep

i = 0
lock = threading.Lock()


class BackCounter(threading.Thread):
    global count

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global lock
        global i

        while i < count-2:
            lock.acquire()
            i += 1
            print(f" {self.name:7s} >> {count+1 - i:5}")
            sleep(0.1)
            lock.release()


count = 10

bc1 = BackCounter("first")
bc2 = BackCounter("second")
bc3 = BackCounter("third")
bc1.start()
bc2.start()
bc3.start()
