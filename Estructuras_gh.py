# Hacer un ejercicio donde le pidan al usuario un numero, el sistema 
# tendra que generar uno aleatorio, el usuario tendra que ingresar el
# numero hasta que adivine cual es el generado por el sistema, si es mas
# alto deberá decirle que el numero es menor, y si es más bajo deberá 
# decirle que es mayor, hasta que adivine el numero en cuestion 

import random 

numero_random = random.randint(1,10)
numero_usuario = 0

while numero_usuario != numero_random: 
    numero_usuario = int(input("coloque un numero")) 
    if numero_usuario < numero_random:
        print("su numero es menor")
    elif numero_usuario > numero_random:
        print("su numero es menor")
    elif numero_usuario == numero_random: 
        print("su numero es el mismo")
