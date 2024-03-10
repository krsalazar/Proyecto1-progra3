from Pila import Pila

class NodoArbol(object):
    dato = None
    izquierdo = None
    derecho = None

class ArbolExpresiones(object):
    def __init__(self):
        self.raiz = None

    def arbol_vacio(self):
        return self.raiz == None