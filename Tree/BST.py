class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)

        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
def deleteNode(root, data):
    if root.data == data:
        if root.right and root.left:
            [psucc, succ] = findMin(root.right, root)

            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            if root.left:
                return root.left
            else:
                return root.right

    else:
        if root.data > data:
            if root.left:
                root.left = deleteNode(root.right, data)
            else:
                if root.right:
                    root.right = deleteNode(root.right, data)

    return root

def findMin(root, parent):
    if root.left:
        return findMin(root.left, root)
    else:
        return [parent, root]
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


root = BSTNode(3)
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(9))
insertNode(root, BSTNode(11))
inOrderTraversal(root)
print('\n')
preOrderTraversal(root)






