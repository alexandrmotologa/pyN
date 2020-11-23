import threading
from time import sleep


class MyCountingThread(threading.Thread):

    def __init__(self, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        print("#" * 10)
        for i in range(self.count):
            print(f" {self.name} >> {i}")
            sleep(0.1)


t1 = MyCountingThread("first", 5)
t2 = MyCountingThread("second", 10)
t3 = MyCountingThread("third", 15)


t1.start()
t2.start()
t3.start()
