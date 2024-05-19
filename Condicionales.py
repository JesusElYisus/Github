#if

x=1
y=2 

if x == y:
   print("verdadero")

#if else

a = 20
if a > 10: 
    print ("si es mayor")
else: 
    print ("Es mayor")

#lista 
    
list = [1, 2, 3, 4]
if 2 in list: 
    print ("existe")
else: 
    print ("no existe")

#Else if 
    
result = None 

x = 10
y = 2

if y < 0: 
    result = x / y 
elif y == 0: 
    result = y 
else: 
    result = f"no se puede dividir {x} entre {y}"
    print (result)

#condiciones anidadas 
    
x = 28 

if x < 0: 
    print(f"{x} es menor que cero")
elif x > 0: 
    print(f"{x} es mayor que cero")
else: 
    print(f"{x} es cero")

edad = int(input("¿cuantos años tienes"))
if edad < 18: 
    print ("Es usted menor de edad")
else: 
    print ("es usted mayor de edad")