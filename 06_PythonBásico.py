#.....................................
#   De la Cruz Gómez Luis Fernando
#.....................................
#   Matemática Algorítmica 
#   Paradigmas de Programación
#   ESFM IPN    Septiembre 2024
#.....................................

#........................
#   Mi primer función
#........................
def saludo:():
    #.......................................
    # Documentación rápida de la función
    #.......................................
    """Esta función saluda"""
    print (' ¡Quiúboles!, ¿cómo estás?')

#..........................
# Llamado de la función
#..........................
saludo()

#.................................
# Se ejecuta pero no se asigna
#.................................
salida = saludo()

#......................
# Estp no funciona
#......................
print(salida)

#...........................
# Mostrar documentación
#...........................
#help(saludo)

#..........................
# Función con argumento
#..........................
def salu2(nombre):
    """Esta fucnión te saluda por tu nombre"""
    print ("¡Qué onda ese ", nombre, "!")
salu2("Julian")
salu2("Ángel")

#...............................................
# Ahorrar trabajo del intérprete
# nombre:str    la variable nombre es un str
#...............................................
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("¡Qué ond ese ", nombre, "!")
saludos("Julián")
a = 123
print (type(a))
saludos(a)

#..................................
# Función con muchos argumentos
#..................................
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ", ", nombre2, ", ", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#...............................................
# Función con cualquier número de argumentos
#...............................................
def muchos_saludos(*nombres):
    """Esta funcuón saluda a todos los que quieras"""
    i = 0
    """
        end =    es para ponelo corrido
    """
    print("Hola ", end= "")
    while len(nombres) > i:
        # Último nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1
muchos_saludos("Nicole", "Enrique", "Alejandro", "Iván", "Zaid", "Joel", "Servín", "Alexis", "Joel")
def greet(firsname, lastname):
    print("Hello", firstname, lastname)

#.................................................
# Llamar la función con argumentos en desorden
#.................................................
greet(lastname= "Jobs", fistname= "Steve")

#.........................................
# Función con argumentos escondidos **
#.........................................
def greet(**person):
    #.......................................................
    # persona tiene características firstname y lastname
    #.......................................................
    print("Hello ", person["firstname"], person["lastname"])

greet(firstname= 'Steve', lastname = 'Jobs')
greet(lastname= 'Jobs', firstname= 'Steve')
greet(firstname= 'Bill', lastname = 'Gates', age = 55)  # Se pueden pasar más parámetros de los necesarios

#....................................
# Función con valores por defecto
#....................................
def greet(name = 'Guest'):
    print('Hello', name)

greet() # Utiliza el valot dado de antemano
greet('Steve')

#..........................
# Función con resultado
#..........................

