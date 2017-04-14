class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()

d.addFront(3)
d.addFront(True)
d.addFront(27)
d.addRear('Sherpa')
d.addRear('London')
d.addFront('The Lion')


print(d.size())
print(d.items)
print(d.removeRear())
print(d.removeFront())
print(d.items)