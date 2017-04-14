class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            print('Stack Overflow!')
        else: self.stk.append(item)
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

s = Stack(4)
s.push(9)
s.push(3)
s.push(4)
s.push('Shard')

print(s.stk)

print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())

print('\n', s.stk)