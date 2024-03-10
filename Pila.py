class NodoPila(object):
    dato = None
    siguiente = None

class Pila(object):
    def __init__(self):
        self.tope = None

    def vaciar(self):
        self.tope = None

    def insertar(self, dato):
        nodo = NodoPila()
        nodo.dato = dato
        nodo.siguiente = self.tope
        self .tope = nodo

    def eliminar(self):
        x = self.tope.dato
        elimina_nodo = self.tope
        self.tope = self.tope.siguiente
        elimina_nodo.siguiente = None
        return  x

    def pila_vacia(self):
        return self.tope is None

    def tope_pila(self):
        if self.tope is not None:
            return self.tope.dato
        else:
            return None

    def imprime_pila(self):
        auxiliar = Pila()
        cadena = ""
        while not self.pila_vacia():
            dato = self.eliminar()
            cadena += str(dato) + "\n"
            auxiliar.insertar(dato)

        while not auxiliar.pila_vacia():
            dato = auxiliar.eliminar()
            self.insertar(dato)

        return cadena