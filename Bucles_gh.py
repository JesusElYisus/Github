# Bucle While 

contador = 0 

while contador <= 10: 
    print (f"{contador * 3 }")
    contador += 1
print ("he finalizado la tabla del 3")

# Otro Ejemplo 

values = [5, 1, 9, 2, 7, 4]

found = False
index = 0 
value_to_find = 7 
longitud = len(values) 

while not found and index < longitud: 
    value = values [index]
    if value == value_to_find: 
        found = True 
    else: 
        index += 1 

if found: 
    print (f"el numero {value_to_find} ha sido encontrado en el indice")
else: 
    print (f"en numero {value_to_find} no se encuentra de la lista de datos") 

# Otro Ejemplo 

array = ["a", "b", "c", "d", "e", "f"]

for letter in array: 
    print (f"letra actual: {letter}")
    if letter == "d" : 
        print ("se encontro la letra d")
        break 
    
    
# Que un usuario ingrese una palabra y ustedes en el sistema pongan 
#una letra constante, si la letra indicada existe terminen el bucle e 
#indiuen al usuario que la letra esta en la palabra 

letra = "a"

palabra = input("Ingresa una palabra")

for letter in palabra: 
    if letra == letter: 
        print(f"la letra {letra} esta en la palabra")
        break
     