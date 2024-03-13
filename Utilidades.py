from sympy import symbols, parse_expr

#Utilizando la libreria SymPy voy a evaluar la expresion para reemplazar las letras por numeros
def obtener_variables(expresion):
    return list(set([str(s) for s in parse_expr(expresion).free_symbols]))

def evaluar_expresion(expresion, valores):
    variables = obtener_variables(expresion)
    for var in variables:
        if var not in valores:
            valores[var] = float(input(f"Ingrese el valor para {var}: "))
    expr = parse_expr(expresion)
    expr = expr.subs(valores)
    return expr