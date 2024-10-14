"""
- registrar alumnos
- generar fichas de matricula
- mostrara la lista de todos los matriculados
- filtrar matricula por programa de estudio
"""
lista_alumnos=[]
nombre=input("Ingrese el nombre del alumno: ")
apellido=input("Ingrese el apellido del alumno: ")
lista_alumnos.append(nombre)
lista_alumnos.append(apellido)
alumno={
    "nombre":nombre,
    "apellido":apellido
    }
print(lista_alumnos)