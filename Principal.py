from Arbol_Expresiones import ArbolExpresiones

print("Este es un Arbol Binario")
print("Por el momento solo puedo evaluar numeros de un solo digito")
un_arbol = ArbolExpresiones()
expresion = input("Ingresa una expresión aritmetica: ")
un_arbol.crear_arbol(expresion)
print(un_arbol.imprimir(2))
print("El resultado de la expresion es: ", un_arbol.evaluar())