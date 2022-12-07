from math import ldexp
from tkinter import N


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def maxDepth(node):
    if node is None:
        return -1
    else:
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1


def inOrder(root):
    if root:
        print(inOrder(root.left))

        print(root.data)

        inOrder(root.right)

def printPreOrder(root):
    if root:
        print(root.data)
        printPreOrder(root.left)
        printPreOrder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)

        print(root.data),


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder") 
inOrder(root)

print("Preorder ") 
printPreOrder(root)

printPostOrder("Post Order ")
printPostOrder(root)