# Tuplas

mi_tupla = (1, "Jesus", 90.5, "Mexico", 0.2)
print(mi_tupla[1])
print(mi_tupla[2:5])

# Listas 

mi_lista = ["cadena de texto", 15, 2.5, "Jesus", 30]
print(mi_lista[0])
mi_lista[0] = "Hola"
print(mi_lista)

mi_lista.append (999)
mi_lista.append (15)
mi_lista.remove (15)
mi_lista.pop (0)
print(mi_lista)

# Diccionarios

mi_diccionario = {"x": "123"}
print(mi_diccionario["x"])

persona = {"nombre":"", "nacionalidad":"", "peso":""}
persona_0 = {"nombre": "Juan", "nacionalidad":"Alemana", "peso":"74"}
persona_1 = {"nombre": "Oscar", "nacionalidad":"Mexico", "peso":"69"}
print(persona_0["peso"])
persona_0["peso"] = 78
print(persona_0)

