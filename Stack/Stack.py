class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()

s.push(True)
s.push(34)
s.push('KTM')

print(s.size())
print(s.items)
print(s.pop())