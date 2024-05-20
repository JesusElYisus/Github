#Aritmeticos

suma = 2 + 4 
multiplicacion = 3 * 3
resta = 3 - 2 
division = 9 / 3 

print(suma, multiplicacion, resta, division)

# Logicos

a = True
b = False

print (a & b)

# Comparadores 

x = 3
y = 4

print(x-y)

hola = "Hola"
hola_2 = "Mundo"

concatenacion = hola + hola_2

print(concatenacion) 

#Ejercicio: 

monto_bruto = 50
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100 
print(monto_interes)

tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
print(importe_bonificacion)

monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print(monto_neto)