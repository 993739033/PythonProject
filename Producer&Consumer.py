#Created By MainBack
from queue import Queue
import time
import random
from threading import Thread

class Producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name = name)
        self.data = queue
    def run(self) -> None:
        while True:
            self.data.put("生产品")
            # self.getName(),
            print("producer 生产+1 当前库存",self.data.qsize())
            time.sleep(random.random()*2+1)

class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name = name)
        self.data = queue
    def run(self) -> None:
        while True:
            p = self.data.get()
            # self.getName(),
            print("consumer 消费-1 当前库存",self.data.qsize(),"消费物品:",p)
            time.sleep(random.random()*2)

if __name__=="__main__":
    queue = Queue(5)
    p=Producer("producer1",queue)
    c=Consumer("consumer1",queue)
    p.start()
    c.start()

