from abc import ABC, abstractmethod
class abs(ABC):
    def print(self, x):
        print(x)
    def task(self):
        print("we are inside abstractmethod")
class test(abs):
    def task(self):
        print("we are inside test class")
ob=test()
ob.task()
ob.print(100)