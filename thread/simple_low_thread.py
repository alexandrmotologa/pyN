import _thread
from time import sleep


def count(name, count):
    print("#"*10)
    for i in range(count):
        print(f" {name} >> {i}")
        sleep(0.1)


_thread.start_new_thread( count, ("first", 5))
_thread.start_new_thread( count, ("second", 10))
sleep(3)
