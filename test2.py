# Created By MainBack
import random
import sys
print(sys.path)

list1 = list(range(0, 10))

print(list1)
list3 = (2,)
print(type(list3))

string1 = "sdfjkjsadfk@jsdfaosdfjlas"
print(string1.find("@"))
print(string1.index("a"))
print(string1.rfind("@"))

list1 = ("sd", "sdfs")
list2 = ["sdfg", "gasdg", "Ag"]
dict1 = {list1: list2}
print(dict1)

dict2 = dict((("sdf", "sdf"), ("asdf", "asdf")))
# print(dict2.get("sdf"))

for index, value in dict2.items():
    print(index, value)


class Test1:
    def __init__(self):
        print("call init")
        print(self.__name3)
        print(self._name1)
        print(self.name)

    name = "sdf"
    _name1 = "sdfg"
    __name3 = "asdgasdg"


test1 = Test1()
print(test1.name)
print(test1._name1)
print(test1._Test1__name3)

print(random.randint(0,10))
# file = open(r"C:\Users\99373\Desktop\kanna.jpg")
file = open(r"C:\Users\99373\Desktop\test.txt","r")
print(file.read())
file.close()
# 以下自动关闭打开的文件
with open(r"C:\Users\99373\Desktop\test.txt","r") as file2:
    alllines = file2.readlines()
    print(file2.read())
    print(type(alllines))

