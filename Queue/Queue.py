class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(4)
q.enqueue('Mt.8848')
q.enqueue(90)
q.enqueue(27)
q.enqueue(True)

print(q.size())
print(q.items)
print(q.dequeue())
print(q.dequeue())
print(q.items)