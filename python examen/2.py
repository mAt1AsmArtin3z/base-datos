import sqlite3

conn = sqlite3.connect('EESTN5.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

alumnos_data = [
    ('Juan', 20),
    ('María', 22),
    ('Pedro', 21),
    ('Ana', 19),
    ('Luis', 23),
    ('Sofía', 24),
    ('Carlos', 18),
    ('Elena', 20)
]

cursor.executemany('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', alumnos_data)

cursor.execute('SELECT * FROM alumnos')
resultados = cursor.fetchall()

print("Lista de alumnos:")
for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")

conn.commit()
conn.close()