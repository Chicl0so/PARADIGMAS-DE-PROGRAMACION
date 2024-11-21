#------------------------------------------------
#   DE LA CRUZ GÓMEZ LUIS FERNANDO
#------------------------------------------------

'''
    MATEMÁTICA ALGORÍTIMICA
    ESFM IPN
    SEPTIEMBRE DE 2024
'''

#-------------------------------------------------------
#   Input permite obtener datos del usuario en promter
#-------------------------------------------------------
nombre= input("Dame tu nombre: ")
print("Hola como estás", nombre)

#-------------------------------------------------------
#   Los enteros son de precisión ilimitada
#-------------------------------------------------------
y = 5000000000000000000000000000000000000000000000
print(y)

#--------------------------------------------------------------------
#   Se pueden delimitar números con guión con bajo pero no con coma
#--------------------------------------------------------------------
y = 5_000_000
print(y)
#-------------------------------------------------------
#   La función int() cambia strings y floats a enteros
#-------------------------------------------------------

#---------------------------------------------------------
#    La notación científica de flotantes utilizada e o E
#---------------------------------------------------------
#   1.2 x 10^{-9}
#--------------------------------------------------------
y = 1.2E-9
print(y)

#-----------------------------------------------------------
#   La función float() convierte strings y enteros a floats
#------------------------------------------------------------
y = float("14.3")
print(y)

'''
    Los complejos se escriben con la raíz de menos uno
    j siempre con un  número como prefijo
    no acepta la j suelta
'''
z = 1+1j
# Suma +
# Resta -
#multiplicación *
# División /
# Modulo %
# Exponente **
# // Función piso
# Funciones para trandormar números int() float() complex()
# Operaciones abs() round() pow()
priny(round(3.1459,4))

#------------------------------
#   Strings de varias lineas
#------------------------------
parrafo = """ EN el bosque de la china
la chinita se perdió"""
print(parrafo)
#-------------------------------------------------
#   La función len() obtiene el tamaño dek strin
#-------------------------------------------------
n = len(parrafo)
print(n)

'''
    Las letras em im string ocupan lugares como en un arreglo
    (también de atrás para adelante comenzando en -1 el último)
'''
palabra = "hola"
print(palabra[0])
print(palabra[-4])


