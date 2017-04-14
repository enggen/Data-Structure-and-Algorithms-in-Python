class Stack(object):
    def __init__(self, limit=10):
        self.stk = limit * []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print('Stack after Push', self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        newStk = list(self.stk)
        self.limit = 2 * self.limit
        self.stk = newStk

s = Stack(4)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.pop())
print('\n', s.pop())

