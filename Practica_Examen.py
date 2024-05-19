# Practica 1: Contar la cantidad de letras en una palabra ingresada por el usuario

palabra = input ("diga una palabra ")
contador = 0  

for numero in palabra: 
    contador += 1 
    

print (f"la palabra tiene {contador} de letras")

# Practica 2: Lista promedio de calificaciones 

lista = [7, 8, 9, 10, 8, 9]

promedio = sum(lista)/len(lista)

print(promedio)

# Practica 3: Mensiona el elemento mas grande de una lista

lista = [13, 15, 17, 8, 11, 10]

mayor = max(lista)

print(mayor)

# Practica 4: Cual es la palabra más larga de una lista de palabras 

lista = ["carro", "ferrocarril", "avion", "barco"]
palabragde = 0 
grande = ""

for palabra in lista:
    if palabragde < len(palabra): 
        grande = palabra 
        palabragde = len(palabra)
print(f"la palabra más grande es {grande}" )

# Practica 5: hacer una suma a partir de dos números ingresados por un usuario 

digito1 = int(input("diga un numero mi estimado usuario_"))
digito2 = int(input("diga otro numero, si no es mucha molestia, por favor_"))

suma = digito1 + digito2

print(f"mi estimado usuarion el resultado es el sigueinte: {suma}")

# Practica 6: una resta y te diga si el resultado es un numero positivo o negativo.

digito1 = int(input("diga un numero"))
digito2 = int(input("diga otro numero"))

resta = digito1 - digito2 

if resta >= 0: 
    print(f"el resultado es {resta} y es positivo")
else: 
    print(f"el resultado es {resta} y es negativo")

# Practica 7: A partir de 1 número aleatorio del uno al 10 y otro ingresado por el usuario, 
# dónde si son iguales le diga que será acreedor a un cupón.

import random 

numrandom = random.randint(1,10)
numusuario = 0 

while numusuario != numrandom: 
    numusuario = int(input("mi amo, ingrese un numero:_"))
    if numusuario < numrandom: 
        print("lo siento, no ha ganado nada")
    elif numusuario > numrandom: 
        print("lo siento, no ha ganado nada")
    elif numusuario == numrandom:
        print("¡¡¡¡¡FELICIDADES!!!!! usted ha ganado el cupon")

# Practica 8: Solicitar ver una película a partir de una lista dada por el sistema, 
# dónde considere su edad, 2 películas deberán ser para mayores de 18 años

peliculas ={"1":"avengers", 
            "2":"Toy Story", 
            "3" : "Deadpool", 
            "4":"Kingsman: Secret service", 
            "5":"rapido y furioso"}



pelis= int(input(f"Elija el numero de la película que quiere ver {peliculas}:_"))



if pelis == 1:
        print("Avengers, la película es para todo publico")
elif pelis == 2: 
        print("Toy Story, pelicula para toda la familia")
elif pelis == 3:
        print("Deadpool, la pelicula es para mayores de 18")
elif pelis == 4:
        print("Kingsman: Secret Service, la pelicula es para mayores de 18")
elif pelis == 5: 
        print("Rapido y Furioso, la película es recomendable de 15 años en adelante")

# Practica 9: Haz un programa que calcule el IMC (índice de masa corporal), 
# solicitándole al usuario tu altura y peso

altura_usuario = float((input("¿cual es su altura en metros?:_")))
peso_usuario = float(input("¿Cual es su peso en kilogramos?:_"))

Masa_corporal = peso_usuario / altura_usuario ** altura_usuario 

print(f"su masa corporal es {Masa_corporal}")

# Practica 10: Haz un programa que ayude a calcular la calificación de un examen, 
# dónde el usuario deberá ingresar, el total de preguntas, 
# la cantidad de preguntas con respuestas correctas 
# y la cantidad con respuestas incorrectas

preguntas_total = int(input("¿Cuantas preguntas son?:_"))
preguntas_correctas = int(input("de esas preguntas, ¿cuantas son correctas?:_"))
preguntas_incorrectas = preguntas_total - preguntas_correctas

calificacion_final = preguntas_correctas / preguntas_total * 100

print(f"usted tiene {preguntas_correctas}") 
print(f"tiene {preguntas_incorrectas}")
print(f"su calificación es {calificacion_final}/100")
