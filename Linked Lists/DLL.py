class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def __str__(self):
        return "Node[Data = %s]" % (self.data,)


class DoubleyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if (self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data, None, current)
            self.tail = current.next

    def delete(self, data):
        current = self.head

        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True

        if current == None:
            return False

        if self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        while current != None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next

        return False


    def fwd_print(self):
        current = self.head
        if current == None:
            print('No element')
            return False
        while (current != None):
            print(current.data)
            current = current.next
        return True

    def rev_print(self):
        current = self.tail
        if (self.tail == None):
            print('No elements')
            return False
        while current != None:
            print(current.data)
            current = current.prev

l = DoubleyLinkList()

l.insert(3)
l.insert(4)
l.insert(7)
l.insert(11)

l.fwd_print()

print('\n')


l.rev_print()

l.delete(11)
l.fwd_print()



