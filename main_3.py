
lista_alumno=[]
def mensaje_menu():
    menu_opsiones="""
--------Bienbenido al sistema-----------
--------Registra alumno---------
1. Escribe (s) si deseas agregar un nuevo alumnn
2. Escribe (n) si  deseas salir del sistema
Escribe la accion que desea realizar: """
    return menu_opsiones

def ingresar_datos_alumno():
    id=len(lista_alumno)+1
    cui=int(input("Ingrese el nuevo numero de su dni: "))
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apeliido del alumno: ")
    numero_celular=int(input("Ingrese su numero de celular: "))
    programa_estudio=input("Ingrese el programa de estudio: ")
    ciclo_academico=input("ingrese su ciclo academico: ")
    email=input("Ingrese su email: ")
    guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)


def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno={
    "id":id,
    "cui":cui,
    "nombre":nombre,
    "apellido":apellido,
    "numero_celilar":numero_celular,
    "programa_estudio":programa_estudio,
    "ciclo_academico":ciclo_academico,
    "email":email,
}

while True:
    menu_opsiones=input(mensaje_menu())
    if menu_opsiones.lower()=="n":
        print("Saliendo del sistema")
        break
    elif menu_opsiones.lower() == "s":
        ingresar_datos_alumno()

    else:
        print("Opsion erronea")



