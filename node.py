from __future__ import annotations
from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def PrintPreorder(self,node):
        if node == None:
            return
        print(node.data)
        node.PrintPreorder(node.left)
        node.PrintPreorder(node.right)

    def PrintPostorder(self,node):
        if node == None:
            return
        node.PrintPostorder(node.left)
        node.PrintPostorder(node.right)
        print(node.data)

    def PrintInorder(self,node):
        if node == None:
            return
        node.PrintInorder(node.left)
        print(node.data)
        node.PrintInorder(node.right)

    def mayor(self,node,numero):
        if node == None:
            return
        if node.data > numero:
            numero = node.data
            print("el mayor es",numero)
        node.mayor(node.left,numero)
        node.mayor(node.right,numero)

    def minimo(self,node,numero):
        if node == None:
            return
        if node.data < numero:
            numero = node.data
            print("el menor es", numero)
        node.minimo(node.left,numero)
        node.minimo(node.right,numero)