# Created By MainBack
import os
import multiprocessing
from multiprocessing import Process
import time

print(os.linesep)
print(os.sep)
print(os.name)
print(os.getcwd())
print(os.listdir())
# 创建后无法再次创建
# os.mkdir("path1")
# os.makedirs("path2/path3")
# 文件再次删除也会报错
# os.rmdir("path1")
# os.removedirs("path2/path3")
print(os.walk(os.getcwd()))
with open(r"test.txt") as file:
    print(file.readlines())

print(os.path.abspath("test.txt"))


def child1(name):
    print("子线程开始执行", os.getpid(), os.getppid(), name)


class SubProcess(Process):
    def __init__(self, interval, name=""):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    def run(self) -> None:
        print(os.getpid())
        print("startTime:", time.time())
        time.sleep(self.interval)
        print("endTime:", time.time())


if __name__ == "__main__":
    print(">>>>")
    p1 = Process(target=child1, args=("p1",))
    p1.start()
    p2 = SubProcess(10, "p2")
    p2.start()
