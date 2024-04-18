from typing import Optional, TypeVar
from node import Node

T = TypeVar('T')


class BinaryTree:
    def __init__(self, data: T):
        self.__root: Optional[Node] = Node(data)

    def getNode(self,rmp):
        remplazo2 = rmp
        remplazo = rmp
        aux = rmp.right

        while aux != None:
            remplazo2 = remplazo
            remplazo = aux
            aux = aux.left

        if remplazo != rmp.right:
            remplazo2.left = remplazo.right
            remplazo.right = rmp.right

        return remplazo

    def insertar(self,elemento, *args):
        nodo = Node(elemento)
        if self.__root.data == None:
            self.__root = nodo
        else:
            aux = self.__root
            while True:
                aux2 = aux
                if elemento < aux.data:
                    aux = aux.left
                    if aux == None:
                        aux2.left = nodo
                        return
                else:
                    aux = aux.right
                    if aux == None:
                        aux2.right = nodo
                        return

    def buscar(self,elemento):
        aux = self.__root
        while aux.data != elemento:
            if elemento < aux.data:
                aux = aux.left
            else:
                aux = aux.right

            if aux == None:
                return None
        return aux

    def eliminar(self,elemento):
        aux = self.__root
        aux2 = self.__root
        is_left = True
        while(aux.data != elemento):
            aux2 = aux
            if(elemento<aux.data):
                is_left = True
                aux = aux.left
            else:
                is_left = False
                aux = aux.right
            if aux == None:
                return None

        if aux.left == None and aux.right == None:
            if aux == self.__root:
                self.__root = None
            else:
                if is_left:
                    aux2.left = None
                else:
                    aux2.right = None

        elif aux.right == None:
            if aux == self.__root:
                self.__root = aux.left
            else:
                if is_left:
                    aux2.left = aux.left
                else:
                    aux2.right = aux.left

        elif aux.left == None:
            if aux == self.__root:
                self.__root = aux.right
            else:
                if is_left:
                    aux2.left = aux.right
                else:
                    aux2.right = aux.left

        else:
            reemplazo = self.getNode(aux)
            if aux == self.__root:
                self.__root = reemplazo

            elif is_left:
                aux2.left = reemplazo

            else:
                aux2.right = reemplazo

            reemplazo.left = aux.left
        return

    def Preorder(self):
        self.__root.PrintPreorder(self.__root)

    def Inorder(self):
        self.__root.PrintInorder(self.__root)

    def Postorder(self):
        self.__root.PrintPostorder(self.__root)

    def Mayor(self):
        self.__root.mayor(self.__root,0)

    def Minimo(self):
        self.__root.minimo(self.__root,1000)