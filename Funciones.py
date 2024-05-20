# Hacer una función donde manden 3 parametros, el primero y el segundo serán numeros 
# y el tercero será el tipo de operacion uqe quieras realizar.

# Si la operación es suma, sumaras y regresaras el resultado para imprimirlo, 
# el mismo caso para la división, multiplicación y resta 

def operation (numero_1, numero_2, ope):
    if ope == "suma": 
        return numero_1 + numero_2
    elif ope == "resta": 
        return numero_1 - numero_2 
    elif ope == "multiplication": 
        return numero_1 * numero_2
    elif ope == "division": 
        return numero_1 / numero_2
    else: 
        print ("operación invalida")
res= operation (2, 4, "division")
print(f"el resultado de la operación es {res}")
