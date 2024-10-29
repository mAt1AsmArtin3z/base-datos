alumnos = [
    "Juan",
    "María",
    "Pedro",
    "Ana",
    "Luis",
    "Sofía",
    "Carlos",
    "Elena"
]

notas = {
    "Juan": [8, 7, 9, 10, 6, 8],
    "María": [10, 9, 8, 9, 7, 10],
    "Pedro": [6, 5, 7, 8, 9, 6],
    "Ana": [9, 10, 10, 9, 8, 9],
    "Luis": [7, 6, 5, 8, 7, 6],
    "Sofía": [10, 10, 9, 9, 10, 9],
    "Carlos": [8, 7, 8, 7, 6, 7],
    "Elena": [9, 9, 10, 9, 8, 9]
}


print("Promedios de notas de los alumnos:")
for alumno, notas_alumno in notas.items():
    promedio = sum(notas_alumno) / len(notas_alumno)
    print(f"{alumno}: {promedio:.2f}")