#----------------------------------------------------------------------------------------------
# MÓDULOS

#----------------------------------------------------------------------------------------------

# Diccionario para almacenar la información de las películas
movies = {}
next_id = 1  # Contador para el siguiente ID disponible
available_ids = []  # Lista para IDs disponibles de películas eliminadas
id_mapping = {}  # Mapa para relacionar números con IDs

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def mostrar_menu():
    print("\n[1] Gestión de Películas y Entradas:")
    print("[1] Agregar película")
    print("[2] Modificar película")
    print("[3] Eliminar película")
    print("[4] Modificar valor de la entrada")
    print("[5] Listar todas las películas")
    print("[0] Regresar al menú")

def generar_id():
    global next_id
    if available_ids:
        # Reutilizar un ID disponible
        movie_id = available_ids.pop(0)
    else:
        # Generar un nuevo ID
        movie_id = f"{next_id:013d}"
        next_id += 1
    return movie_id

def agregar_pelicula():
    movie_id = generar_id()  # Generar un ID único
    title = input("Ingresa el título de la película: ")
    format_type = input("Ingresa el formato (2D/3D): ")
    language = input("Ingresa el idioma (Inglés/Subtitulado): ")

    # Almacenar información de la película en el diccionario
    movies[movie_id] = {
        'title': title,
        'format': format_type,
        'language': language,
        'schedule': []  # Inicializar la lista de horarios
    }
    
    # Actualizar el mapeo de ID
    id_mapping[next_id - 1] = movie_id

    # Establecer horarios de transmisión
    while True:
        day = input("Ingresa el día de la semana para la transmisión (o 'fin' para terminar): ")
        if day.lower() == 'fin':
            break
        time = input("Ingresa la hora (ej. 14:00): ")
        schedule_entry = f"{day} a las {time}"
        movies[movie_id]['schedule'].append(schedule_entry)

    print(f"¡Película '{title}' agregada con éxito con ID: {movie_id}!")

def modificar_pelicula():
    movie_id = input("Ingresa el ID de la película a modificar: ")
    if movie_id in movies:
        title = input("Ingresa el nuevo título de la película: ")
        format_type = input("Ingresa el nuevo formato (2D/3D): ")
        language = input("Ingresa el nuevo idioma (Inglés/Subtitulado): ")

        # Actualizar información de la película
        movies[movie_id] = {
            'title': title,
            'format': format_type,
            'language': language,
            'schedule': movies[movie_id]['schedule']  # Mantener horarios existentes
        }
        print(f"¡Película '{movie_id}' modificada con éxito!")
    else:
        print("ID de película no encontrado.")

def eliminar_pelicula():
    movie_number = input("Ingresa el número de la película a eliminar: ")
    if movie_number.isdigit() and int(movie_number) in id_mapping:
        movie_id = id_mapping[int(movie_number)]
        del movies[movie_id]
        available_ids.append(movie_id)  # Añadir el ID a los disponibles
        del id_mapping[int(movie_number)]  # Eliminar el mapeo
        print(f"¡Película '{movie_id}' eliminada con éxito!")
    else:
        print("Número de película no encontrado.")

def modificar_precio_entrada():
    print("Esta opción no está implementada en este ejemplo.")

def listar_peliculas():
    if movies:
        print("\nLista de todas las películas:")
        for i, (movie_id, info) in enumerate(movies.items(), start=1):
            print(f"Número: {i}, ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
            if info['schedule']:
                print("  Horarios:")
                for entry in info['schedule']:
                    print(f"    - {entry}")
            else:
                print("  No hay horarios asignados.")
    else:
        print("No hay películas disponibles.")

def manejar_opcion(opcion):
    if opcion == '1':
        agregar_pelicula()
    elif opcion == '2':
        modificar_pelicula()
    elif opcion == '3':
        eliminar_pelicula()
    elif opcion == '4':
        modificar_precio_entrada()
    elif opcion == '5':
        listar_peliculas()
    elif opcion == '0':
        print("Regresando al menú...")
        return False
    else:
        print("Opción inválida, por favor intenta de nuevo.")
    return True

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if not manejar_opcion(opcion):
            break

# Punto de entrada al programa
if __name__ == "__main__":
    main()
    
    
    

"""
Mapping de IDs: Se ha añadido un diccionario id_mapping para relacionar los números de las películas (sin ceros a la izquierda) con sus IDs completos.
Eliminar Película: La función eliminar_pelicula() ahora permite al usuario ingresar solo el número de la película.
Listado de Películas: Se actualiza el listado para mostrar un número secuencial en lugar del ID completo.
"""
#Falta cambiar eliminar por estado activo inactivo y tema butacas