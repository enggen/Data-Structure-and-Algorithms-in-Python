class Node:
    def __init__(self, data):
        self.data = data
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


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)

    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addAfterValue(self, data, node):
        newNode = node
        currentNode = self.head

        while currentNode.next != None or currentNode.data != data:
            if currentNode.data == data:
                newNode.next = currentNode.next
                currentNode.next = newNode
                self.length += 1
                return
            else:
                currentNode = currentNode.next
        print("The data provide is not present")

    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print('The position does not exist. Please enter a valid position')
        else:
            while currentnode.next != None or count < pos:
                count += 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def addLast(self, node):
        currentnode = self.head

        while currentnode.next != None:
            currentnode = currentnode.next

        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.length += 1

    def printList(self):
        nodeList = []
        currentnode = self.head

        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next

        print(nodeList)

    def deleteValue(self, data):
        currentnode = self.head
        previousnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        print("The data provided is not present")

    def deleteBeg(self):
        if self.length == 0:
            print('The list is empty')
        else:
            self.head = self.head.next
            self.length -= 1

    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print('The position does not exist.')
        elif pos == 1:
            self.deleteBeg()
        else:
            while currentnode.next != None or count < pos:
                count += 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def getLength(self):
        return self.length





n1 = Node(7)
n2 = Node(9)
n3 = Node(5)
n4 = Node(11)
n5 = Node(23)
n6 = Node(71)
n7 = Node(99)


ll = LinkedList()
ll.addNode(n1)
ll.addNode(n2)
ll.addNode(n3)
ll.addNode(n4)
ll.addNode(n5)
ll.addNode(n6)
ll.addNode(n7)

ll.printList()
ll.deleteValue(23)
# ll.deleteAtPos(4)
# ll.deleteAtPos(1)
ll.printList()
print(ll.getLength())






