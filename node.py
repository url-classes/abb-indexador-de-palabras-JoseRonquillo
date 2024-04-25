from __future__ import annotations
from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, data: T, procedencia: str):
        self.data = data
        self.procedencia = procedencia
        self.recurrencia = 1
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def sum(self):
        self.recurrencia += 1

    def proce(self, procedencia):
        if self.procedencia != procedencia:
            self.procedencia += " ; " + str(procedencia)

    def is_leaf(self):
        return self.left is None and self.right is None

    def PrintPreorder(self, node):
        if node is None:
            return
        print(f"{node.data}, recurrencia: {self.recurrencia}, procedencia(s): {self.procedencia}")
        node.PrintPreorder(node.left)
        node.PrintPreorder(node.right)

    def PrintPostorder(self,node):
        if node is None:
            return
        node.PrintPostorder(node.left)
        node.PrintPostorder(node.right)
        print(f"{node.data}, recurrencia: {self.recurrencia}, procedencia(s): {self.procedencia}")

    def PrintInorder(self, node):
        if node is None:
            return
        node.PrintInorder(node.left)
        print(f"{node.data}, recurrencia: {self.recurrencia}, procedencia(s): {self.procedencia}")
        node.PrintInorder(node.right)

