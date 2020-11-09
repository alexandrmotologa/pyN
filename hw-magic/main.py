# class RandomInput:
#     def __init__(self):
#         self.n = 0
    
#     def __next__(self):
#         self.n +=2
#         self.count=0
#         if self.count <= 9:
#             return self.n
#         else:
#             raise StopIteration
    
#     def __iter__(self):
#         return self

# c_object = RandomInput()
# for e in c_object:
#     print(e)


import random
for x in range(10):
    print (random.randint(1,1000))