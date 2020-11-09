import random

class RandomInteger:
    def __init__(self):
        self.n = 0
        self.count=0
    
    def __next__(self):
        self.n =random.randint(1,1000)
        if self.count <= 9:
            self.count+=1
            return self.n
        else:
            raise StopIteration
    
    def __iter__(self):
        return self

ri = RandomInteger()
for i in ri:
    print(i)
