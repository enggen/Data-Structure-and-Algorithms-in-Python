class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            print('Stack Underflow!')
            return 0
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

our_list = ['first', 'Second', 'Third', 'Fourth']
s = Stack(our_list)

print('\n', s.pop())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())