"""
- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio
"""
lista_alumnos=[]
#inicio de problema
#necesito poder agregar mas alumnos sin neceisdad de crear tantas variables
#posible solucion cre o encerar el codigo en un cliclo while
nombre=input("Ingrese el nombre del alumno: ")
apellido=input("Ingrese el apeliido del alumno: ")
nombre2=input("Ingrese el nombre del alumno: ")
apellido2=input("Ingrese el apeliido del alumno: ")
alumno={
    "nombre":nombre,
    "apellido":apellido
}
alumno2={
    "nombre":nombre2,
    "apellido":apellido2
}
lista_alumnos.append(alumno)
lista_alumnos.append(alumno2)
#fin del problema

#deseo mostrar un menu con las opciones de agregar un nuevo alumnos y salir del programa.
print(lista_alumnos)