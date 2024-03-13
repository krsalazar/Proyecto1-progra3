from Arbol_Expresiones import ArbolExpresiones
from Utilidades import *

print("Este es un Arbol Binario")
print("Por el momento solo puedo evaluar numeros de un solo digito")
un_arbol = ArbolExpresiones()
expresion = input("Ingresa una expresión aritmetica: ")
try:
        variables = obtener_variables(expresion)
        valores = {}
        for var in variables:
            valores[var] = float(input(f"Ingrese el valor para {var}: "))
        resultado = evaluar_expresion(expresion, valores)
except Exception as e:
        print(f"Error: {e}")
un_arbol.crear_arbol(expresion)
print("Recorrido del árbol preorden:\n", un_arbol.imprimir(0))
print("Recorrido del árbol postorden:\n", un_arbol.imprimir(1))
print("Recorrido del árbol inorden:\n", un_arbol.imprimir(2))
print("El resultado es: ", resultado)

#Esto ya no me funcionó :(
#print("El resultado de la expresion es: ", un_arbol.evaluar())

