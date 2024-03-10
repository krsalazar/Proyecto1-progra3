from Arbol_Expresiones import ArbolExpresiones

un_arbol = ArbolExpresiones()
un_arbol.crear_arbol("(2*3)+(8/2)")
print(un_arbol.imprimir(2))
print("El resultado de la expresion es: ", un_arbol.evaluar())