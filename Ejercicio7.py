class Alumno:
    nombre = None
    nota = None
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")
    def aprobatoria(self):
        if self.nota > 5:
            print("Felicidades tiene calificacion aprobatoria")
        else:
            print("Lo siento su calificacion es reprobatoria")

Alumno1 = Alumno()
Alumno2 = Alumno()

Alumno1.datos("Jose", 8)
Alumno2.datos("Fabian", 4)

Alumno1.imprimir()
Alumno1.aprobatoria()
Alumno2.imprimir()
Alumno2.aprobatoria()
