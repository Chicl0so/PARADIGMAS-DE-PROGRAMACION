#:::::::::::::::::::::::::::::::::
# DE LA CRUZ GÓMEZ LUIS FERNANDO
#:::::::::::::::::::::::::::::::::

'''
    MATEMÁTICA ALGORÍTMICA
    PARADIMAS DE PROGRAMACIÓN
    ESFM IPN SEPTIEMBRE 2024
'''

#:::::::::::::::::::::
# Conjunto en python
#:::::::::::::::::::::
even_nums = {2,4,6,8,10}    # Conunto de números pares
print(even_nums)

#El bool no es parte del conjunto
emp = {1, 'Steve',10.5, True]   # Conjunto de diferentes objetos
print(emp)

nums = {1,2,3,4,4,5,5}
print(nums)

#::::::::::::::::::::::::::::::::::::::::::::::::
# De diccionario a conjunto: conjunto de llaves
#::::::::::::::::::::::::::::::::::::::::::::::::
d= {1: 'uno', 2: 'dos'}
s = set(d)
print(s)
s.add(100)
print(s)

s.update(nums)
print(s)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s2  # Unión
print(su)

si= s1&s2   # Intersección
print(si)

sr = s1-s2  # Diferencia de conjuntos
print(sr)

sp = s2-s1 
print(sp)

ss = s1^s2  # Diferencia simétrica
print(ss)

#::::::::::::::::::::::
# Uso de diccionarios
#::::::::::::::::::::::
capitales = {"USA": "Washingtong DC", "France": "Paris", "India":"New Delhi"}
print(capitales)

#::::::::::::::
# llave:valor
#::::::::::::::
# Diccionario vacío
d = {}

# Llave entera, valor string
numeros = {1:"uno", 2:"dos", 3:"tres"}

# Llave real, valor string
decimales = {1.5:"uno y medio",2.5:"dos y medio", 3.5: "tres y medio"}

# Llave tupla, valor string
cosas = {("Parker","Reynolds","Camlin"):"pluma",("LG","Whirpool","Samsung"): "refrigerador"}

# Llave string, valor int
romanos = {'I':1, 'II':2, 'III':3, 'IV':4. 'V':5}
print(romanos)
print(romanos["I"])

print(capitales.get("India"))
print(capitales.get("india"))

# Reportar valor y llave
for k in capitales: 
    print("key = " + k + ", value = " + capitales[k])
# Nuevo dato para el diccionario
capitales["Mexico"] = "CDMX"
print(capitales=

# Borrar dato del diccionario 
del capitales["Mexico"]
print(capitales)

# Borrar todo el diccionario
del capitales

# Reportar llaves
print(romanos.keys())

# Reportar valores
print(romanos.values())

# Juicio de llave (esta o no está la llave del diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" in romanos)
