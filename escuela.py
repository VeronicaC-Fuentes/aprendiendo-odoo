class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre  # Guardamos el nombre
        self.nota = nota      # Guardamos la nota
        self.estado = "Cursando" # Todos empiezan cursando

    def calificar(self):
        if self.nota >= 11:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"
        print(f"El alumno {self.nombre} ha sido calificado como: {self.estado}")

# Esto simula la base de datos de Odoo
lista_alumnos = []

# Creando alumnos (Objetos)
alumno1 = Alumno("Cesar", 15)
alumno2 = Alumno("Robert", 20)
alumno3 = Alumno("Vero", 5)

# Guardándolos en la base de datos (Lista)
lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)


print("---- INICIANDO SISTEMA DE CALIFICACION ----")

for estudiante in lista_alumnos:
    estudiante.calificar()