#...........................................................
# Del directorio aplicacion, el subiderctorio repositorio,
# el archivo basededatos.py : Trae el objeto Basededaros
#...........................................................
from aplicaicon.repositorio.basededatos import BaseDeDatos

#...........................................................
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo s3.py : trae el objeto S3
#...........................................................
from aplicacion.repositorio.s3 import S3

#.....................................................................
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#.....................................................................
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#.......................................................
# Del directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py : trae el objeto Usuario
#.......................................................
from aplicacion.modelos.usuario import Usuario

#.............................................................................
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#.............................................................................
from aplicacion. negocios.manejodeinscripciones import ManejoDeInscripciones

#...................
# Crear el Usuario
#...................
usuario = Usiario("Roberto","Jimenez",18)

#.....................
# Crear el objeto s3
#.....................
repositorioS3 = S3("321321321","sdf435223","MiCubeta")

#..............................................................
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#..............................................................
manejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#..............................
# Crear el objeto basededatos
#..............................
repositorioBaseDeDatos= BaseDeDatos("localhost","admin","admin123")

#.............................................................
# Interface isncribirUsario del objeto ManejoDeInscripciones
#.............................................................
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")