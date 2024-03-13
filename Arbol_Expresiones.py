from Pila import Pila


# Creamos el nodo del arbol

class NodoArbol(object):
    dato = None
    izquierdo = None
    derecho = None


class ArbolExpresiones(object):
    # Clase con los metodos para manejar el arbol
    def __init__(self):
        self.raiz = None

    def arbol_vacio(self):
        return self.raiz == None

    def reiniciar(self):
        self.raiz = None

#Imprime el recorrido del arbol que se seleccione
    def imprimir(self, tipo):
        cadena = ""
        if tipo == 0:
            cadena = self.__preorden(self.raiz)
        elif tipo == 1:
            cadena = self.__postorden(self.raiz)
        elif tipo == 2:
            cadena = self.__inorden(self.raiz)
        return cadena

    # Acá vamos a crear las cadenas con los recorridos del arbol
    def __preorden(self, sub_arbol):
        cadena = ""
        if sub_arbol != None:
            cadena += sub_arbol.dato + " -> " + self.__preorden(sub_arbol.izquierdo) + self.__preorden(sub_arbol.derecho)
        return cadena

    def __postorden(self, sub_arbol):
        cadena = ""
        if sub_arbol != None:
            cadena += self.__postorden(sub_arbol.izquierdo) + self.__postorden(
                sub_arbol.derecho) + sub_arbol.dato + " -> "
        return cadena

    def __inorden(self, sub_arbol):
        cadena = ""
        if sub_arbol != None:
            cadena += self.__inorden(sub_arbol.izquierdo) + sub_arbol.dato + " -> " + self.__inorden(sub_arbol.derecho)
        return cadena

    def __crear_sub_arbol(self, operando2, operando1, operador):
        # acá le decimos que la raiz del sub arbol es el operador y los numeros seran los hijos de la raiz
        operador.izquierdo = operando1
        operador.derecho = operando2
        return operador

    # con esto le daremos una prioridad a cada tipo de operador
    def __prioridad(self, caracter):
        if caracter in ["^"]:
            prioridad = 3
        elif caracter in ["*", "/"]:
            prioridad = 2
        elif caracter in ["+", "-"]:
            prioridad = 1
        else:
            prioridad = 0
        return prioridad

    # Nos indica si el caracter leido es un operador
    def __es_operador(self, caracter):
        return caracter in ["(", ")", "^", "*", "/", "+", "-"]

    def crear_arbol(self, cadena):
        pila_operandos = Pila()
        pila_operadores = Pila()

        for caracter in cadena:
            token = NodoArbol()  # El token podrá recibir nodos de arbol como dato
            token.dato = caracter

            if not self.__es_operador(caracter):
                pila_operandos.insertar(token)
            else:
                if caracter in ["("]:
                    pila_operadores.insertar(token)
                elif caracter in [")"]:
                    tope = pila_operadores.tope_pila()
                    while not pila_operadores.pila_vacia() and tope.dato not in ["("]:
                        operando2 = pila_operandos.eliminar()
                        operando1 = pila_operandos.eliminar()
                        operador = pila_operadores.eliminar()
                        nuevo_operando = self.__crear_sub_arbol(operando2, operando1, operador)
                        pila_operandos.insertar(nuevo_operando)
                        tope = pila_operadores.tope_pila()
                    operador = pila_operadores.eliminar()
                else:
                    tope = pila_operadores.tope_pila()
                    while not pila_operadores.pila_vacia() and self.__prioridad(caracter) <= self.__prioridad(
                            tope.dato):
                        operando2 = pila_operandos.eliminar()
                        operando1 = pila_operandos.eliminar()
                        operador = pila_operadores.eliminar()
                        nuevo_operando = self.__crear_sub_arbol(operando2, operando1, operador)
                        pila_operandos.insertar(nuevo_operando)
                        tope = pila_operadores.tope_pila()
                    pila_operadores.insertar(token)

        while not pila_operadores.pila_vacia():
            operando2 = pila_operandos.eliminar()
            operando1 = pila_operandos.eliminar()
            operador = pila_operadores.eliminar()
            nuevo_operando = self.__crear_sub_arbol(operando2, operando1, operador)
            pila_operandos.insertar(nuevo_operando)

        self.raiz = pila_operandos.eliminar()

 #Iba a utilizar esta forma para evaluar la expresion pero por las variables se me complicó jeje
    def evaluar(self):
        return self.__evalua_expresion(self.raiz)

    def __evalua_expresion(self, sub_arbol):
        resultado = 0.0
        if not self.__es_operador(sub_arbol.dato):
            return float(sub_arbol.dato)
        else:
            if sub_arbol.dato in ["^"]:
                resultado += self.__evalua_expresion(sub_arbol.izquierdo) ** self.__evalua_expresion(sub_arbol.derecho)
            elif sub_arbol.dato in ["*"]:
                resultado += self.__evalua_expresion(sub_arbol.izquierdo) * self.__evalua_expresion(sub_arbol.derecho)
            elif sub_arbol.dato in ["/"]:
                resultado += self.__evalua_expresion(sub_arbol.izquierdo) / self.__evalua_expresion(sub_arbol.derecho)
            elif sub_arbol.dato in ["+"]:
                resultado += self.__evalua_expresion(sub_arbol.izquierdo) + self.__evalua_expresion(sub_arbol.derecho)
            elif sub_arbol.dato in ["-"]:
                resultado += self.__evalua_expresion(sub_arbol.izquierdo) - self.__evalua_expresion(sub_arbol.derecho)

        return resultado
