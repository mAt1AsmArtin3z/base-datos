def main():
    calificaciones = []
    
    while True:
        entrada = input("Ingresa una calificación (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            break
        
        try:
            calificacion = float(entrada)
            calificaciones.append(calificacion)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if calificaciones:
        calificacion_maxima = max(calificaciones)
        calificacion_minima = min(calificaciones)
        promedio = sum(calificaciones) / len(calificaciones)
        
        print(f"Calificación más alta: {calificacion_maxima:.2f}")
        print(f"Calificación más baja: {calificacion_minima:.2f}")
        print(f"Promedio de calificaciones: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones.")

if __name__ == "__main__":
    main()
