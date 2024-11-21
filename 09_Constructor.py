#................................................
#   DE LA CRUZ GÓMEZ LUIS FERNANDO
#   PARADIGMAS DE LA PROGRAMACIÓN
#   MATEMÁTICA ALGORÍTMICA
#   ESFM IPN    OCTUBRE 2024
#................................................


#........................
#   CLASE COMPUTADORA
#........................
class Computadora: 
    marca: str = None
    caácidad: int = 0
    ram: int = 0

    #....................
    # Constructor
    #....................
    def __init__(self, marca:str, capacidad:int, ram: int):
        print(f"Accediendo al constructor de la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram

    def imprimirInfoPC(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")
        #.................
        #   DESTRICTOR
        #.................
        def __del__(self):
            print(f"Se eliminó la computadora: {self.marca}")

#.....................
#   Clase persona
#.....................
class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None
    
    #.............................
    #   Constructor de persona
    #.............................
    def __init__(selg, nombre: str, apellidos: str, edad: int, direccion: str, marca: str, capacidad: int, ram: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direcciom = direccion
        self.Computadora = Computadora, capacidad ram)
        print(f"--- Accedifmos al constructor de la persona: {nombres} {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"--- Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion}")
        self.COmputadora.imprimirInfoPC()
    #..................
    #   DESTRUCTOR
    #..................
   def __del__(self):
       print(f"--- Eliminamos a la persona... {self.nombres} {self.apellidos}")

#...............................
#   FUNCIÓN 1 ES EL PROGRAMA
#...............................

def funcion1():
    persona = Persona("Caelos", "Perez", 40, "Xochimilco", "Lenovo", 700, 8)
    print("\n")
    persona.imprimirInfo()
    print("\n")
    persona2= Persona("Magdalena", "Carrillo", 35, "Jalapa", "IBM", 200, 4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")

#........................
#   Llamar a funcion1
#........................
funcion1()
