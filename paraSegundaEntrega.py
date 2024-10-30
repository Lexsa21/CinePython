"""
-----------------------------------------------------------------------------------------------
Título: TP Cuatrimestral - Sistema de Gestión de Cine 
Fecha: 14/10/24
Autor: Equipo 10

Descripción: El sistema de gestión del cine permite administrar las funciones y 
ventas de un complejo de cines. Permite controlar las películas que se van a proyectar, 
en qué fecha y horario. Además, se van a poder gestionar ventas, y así ir modificando 
la disponibilidad de las butacas.  También emite informes generales. Por último, el programa 
permite gestionar el complejo de cines, modificando los cines existentes. 

Pendientes: 
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def generarId(movies):
    """Genera un ID único para una película."""
    number_id = max(map(int, movies.keys()), default=0) + 1
    movie_id = f"{number_id:04d}"
    return movie_id, number_id

def esHorario(time):
    """Valida que el horario tenga el formato HH:MM y sea un horario válido."""
    if len(time) != 5 or time[2] != ":":
        return False

    horas, minutos = time.split(":")
    if not (horas.isdigit() and minutos.isdigit()):
        return False

    return 0 <= int(horas) < 24 and 0 <= int(minutos) < 60

def agregarPelicula(movies, id_mapping):
    """- Función que agrega una película al diccionario movies
       - Parámetro: 
            movies (dicc): Diccionario donde se almacenan las películas
            id_mapping (dicc): Diccionario para relacionar números con IDs
       - Retorno:
            movies (dicc): Diccionario donde se almacenan las películas actualizado """
            
    movie_id, number_id = generarId(movies)
    title = input("Ingresa el título de la película: ")
    
    format_type = input("Ingresa el formato (2D/3D): ")
    while format_type.lower() not in ["2d", "3d"]:
        format_type = input("Error. Ingresa el formato (2D/3D): ")
        
    language = input("Ingresa el idioma (Español/Subtitulado): ")
    while language.lower() not in ["español", "subtitulado"]:
        language = input("Error. Ingresa el idioma (Español/Subtitulado): ")

    movies[movie_id] = {
        'title': title,
        'format': format_type,
        'language': language,
        'schedule': [],
        'activo': True
    }
    
    id_mapping[number_id] = movie_id

    while True:
        day = input("Ingresa el día de la semana para la proyección (o 'fin' para terminar): ")
        if day.lower() == 'fin':
            break
        if day.lower() not in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
            continue
        
        time = input("Ingresa la hora (ej. 14:00): ")
        while not esHorario(time):
            time = input("Error. Ingresa la hora (ej. 14:00): ")
            
        schedule_entry = f"{day} a las {time}"
        movies[movie_id]['schedule'].append(schedule_entry)

    print(f"¡Película '{title}' agregada con éxito con ID: {movie_id}!")
    
    return movies

def modificarPelicula(movies, id_mapping):
    """- Función que modifica una película del diccionario movies
       - Parámetro: 
            movies (dicc): Diccionario donde se almacenan las películas
            id_mapping (dicc): Diccionario para relacionar números con IDs
       - Retorno:
            movies (dicc): Diccionario donde se almacenan las películas actualizado  """
        
    movie_number = input("Ingresa el número de la película a modificar: ")
    if movie_number.isdigit() and int(movie_number) in id_mapping:
        movie_id = id_mapping[int(movie_number)]
        movie = movies[movie_id]
        
        title = input(f"Ingresa el nuevo título de la película ({movie['title']}): ")
        if title:  # Si el usuario no ingresa nada, conserva el valor original
            movie['title'] = title

        format_type = input(f"Ingresa el nuevo formato (2D/3D) ({movie['format']}): ")
        while format_type and format_type.lower() not in ["2d", "3d"]:
            format_type = input("Error. Ingresa el formato (2D/3D): ")
        if format_type:
            movie['format'] = format_type

        language = input(f"Ingresa el nuevo idioma (Español/Subtitulado) ({movie['language']}): ")
        while language and language.lower() not in ["español", "subtitulado"]:
            language = input("Error. Ingresa el idioma (Español/Subtitulado): ")
        if language:
            movie['language'] = language

        print(f"¡Película '{movie_id}' modificada con éxito!")
    else:
        print("Número de película no encontrado.")
        
    return movies

def inactivarPelicula(movies, id_mapping):
    """- Función que inactiva una película del diccionario movies
       - Parámetro: 
            movies (dicc): Diccionario donde se almacenan las películas
            id_mapping (dicc): Diccionario para relacionar números con IDs
       - Retorno:
            movies (dicc): Diccionario donde se almacenan las películas actualizado  """
            
    movie_number = input("Ingresa el número de la película a eliminar: ")
    if movie_number.isdigit() and int(movie_number) in id_mapping:
        movie_id = id_mapping[int(movie_number)]
        movies[movie_id]['activo'] = False
        print(f"¡Película '{movie_id}' inactivada con éxito!")
    else:
        print("Número de película no encontrado.")
    
    return movies
    
def modificarPrecioEntrada():
    print("Esta opción no está implementada en este ejemplo.")

def listarPeliculas(movies):
    """- Función que lista todas las películas disponibles
       - Parámetro: 
            movies (dicc): Diccionario donde se almacenan las películas
       - Retorno:
            None  """
            
    if movies:
        print("\nLista de todas las películas:")
        for i, (movie_id, info) in enumerate(movies.items(), start=1):
            if movies[movie_id]['activo']:
                print(f"Número: {i}, ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
                if info['schedule']:
                    print("  Horarios:")
                    for entry in info['schedule']:
                        print(f"    - {entry}")
                else:
                    print("  No hay horarios asignados.")
    else:
        print("No hay películas disponibles.")
        
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    
    #-------------------------------------------------
    # Inicialización de variables
    #------------------------------------------------------------------------------------------
    
    movies = {
        '0000000000001': {'title': 'Spiderman', 'format': '2D', 'language': 'Español', 'schedule': ['Martes a las 14:00'], 'activo': True},
        '0000000000002': {'title': 'Avengers: Endgame', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Miércoles a las 18:00'], 'activo': True},
        '0000000000003': {'title': 'Coco', 'format': '2D', 'language': 'Español', 'schedule': ['Jueves a las 16:00'], 'activo': True},
        '0000000000004': {'title': 'Toy Story 4', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Viernes a las 17:00'], 'activo': True},
        '0000000000005': {'title': 'El Rey León', 'format': '2D', 'language': 'Español', 'schedule': ['Sábado a las 15:00'], 'activo': True},
        '0000000000006': {'title': 'Jurassic World', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Domingo a las 19:00'], 'activo': True},
        '0000000000007': {'title': 'Frozen II', 'format': '2D', 'language': 'Español', 'schedule': ['Lunes a las 13:00'], 'activo': True},
        '0000000000008': {'title': 'Dumbo', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Martes a las 16:00'], 'activo': True},
        '0000000000009': {'title': 'Aquaman', 'format': '2D', 'language': 'Español', 'schedule': ['Miércoles a las 14:00'], 'activo': True},
        '0000000000010': {'title': 'Parasite', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Jueves a las 20:00'], 'activo': True},
        '0000000000011': {'title': 'El Exorcista', 'format': '2D', 'language': 'Español', 'schedule': ['Viernes a las 21:00'], 'activo': True},
        '0000000000012': {'title': 'The Shining', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Sábado a las 22:00'], 'activo': True},
        '0000000000013': {'title': 'Inception', 'format': '2D', 'language': 'Español', 'schedule': ['Domingo a las 12:00'], 'activo': True},
        '0000000000014': {'title': 'Avatar', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Lunes a las 15:00'], 'activo': True},
        '0000000000015': {'title': 'Titanic', 'format': '2D', 'language': 'Español', 'schedule': ['Martes a las 18:00'], 'activo': True},
        '0000000000016': {'title': 'The Matrix', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Miércoles a las 19:00'], 'activo': True},
        '0000000000017': {'title': 'Interstellar', 'format': '2D', 'language': 'Español', 'schedule': ['Jueves a las 17:00'], 'activo': True},
        '0000000000018': {'title': 'Gladiator', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Viernes a las 20:00'], 'activo': True},
        '0000000000019': {'title': 'The Godfather', 'format': '2D', 'language': 'Español', 'schedule': ['Sábado a las 18:00'], 'activo': True},
        '0000000000020': {'title': 'Pulp Fiction', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Domingo a las 21:00'], 'activo': True},
        '0000000000021': {'title': 'Forrest Gump', 'format': '2D', 'language': 'Español', 'schedule': ['Lunes a las 16:00'], 'activo': True},
        '0000000000022': {'title': 'Fight Club', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Martes a las 14:00'], 'activo': True},
        '0000000000023': {'title': 'The Dark Knight', 'format': '2D', 'language': 'Español', 'schedule': ['Miércoles a las 18:00'], 'activo': True},
        '0000000000024': {'title': 'Schindler\'s List', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Jueves a las 16:00'], 'activo': True},
        '0000000000025': {'title': 'Goodfellas', 'format': '2D', 'language': 'Español', 'schedule': ['Viernes a las 17:00'], 'activo': True},
        '0000000000026': {'title': 'The Social Network', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Sábado a las 15:00'], 'activo': True},
        '0000000000027': {'title': 'Braveheart', 'format': '2D', 'language': 'Español', 'schedule': ['Domingo a las 19:00'], 'activo': True},
        '0000000000028': {'title': 'The Silence of the Lambs', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Lunes a las 13:00'], 'activo': True},
        '0000000000029': {'title': 'Saving Private Ryan', 'format': '2D', 'language': 'Español', 'schedule': ['Martes a las 16:00'], 'activo': True},
        '0000000000030': {'title': 'The Usual Suspects', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Miércoles a las 14:00'], 'activo': True},
    }
    
    id_mapping = {i: k for i, k in enumerate(movies.keys(), 1)}
    
    #-------------------------------------------------
    # Menú principal
    #------------------------------------------------------------------------------------------
    while True:
        print("---------------------------")
        print("SISTEMA DE GESTIÓN DE CINE")
        print("---------------------------")
        print("[1] Gestión de Películas y Entradas")
        print("[2] Venta de Entradas")
        print("[3] Informes Generales")
        print("[4] Gestión de Complejo de Cines")
        print("[0] Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del sistema.")
            break
            
        # Opción 1: GESTIÓN DE PELÍCULAS Y ENTRADAS
        elif opcion == "1":   
            # Menú de Películas y Entradas
            while True:
                print("\n---------------------------")
                print("GESTIÓN DE PELÍCULAS Y ENTRADAS")
                print("---------------------------")
                print("[1] Agregar Película")
                print("[2] Modificar Película")
                print("[3] Eliminar Película")
                print("[4] Modificar valor de la entrada")
                print("[5] Listar todas las películas")
                print("[0] Volver al menú")
                opcionPeliculas = input("Seleccione una opción: ")

                if opcionPeliculas == "0": break
                if opcionPeliculas == "1": movies = agregarPelicula(movies, id_mapping)
                elif opcionPeliculas == "2": movies = modificarPelicula(movies, id_mapping)
                elif opcionPeliculas == "3": movies = inactivarPelicula(movies, id_mapping)
                elif opcionPeliculas == "4": modificarPrecioEntrada()
                elif opcionPeliculas == "5": listarPeliculas(movies)
                
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        # Opción 2: VENTA DE ENTRADAS
        elif opcion == "2":   
            # Menú de Venta de Entradas
            while True:
                print("\n---------------------------")
                print("VENTA DE ENTRADAS")
                print("---------------------------")
                print("[1] Generar Entrada")
                print("[2] Eliminar Venta")
                print("[0] Volver al menú")
                opcionEntradas = input("Seleccione una opción: ")

                if opcionEntradas == "0": break
                # Implementación de Generar Entrada y Eliminar Venta aquí...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        # Opción 3: INFORMES GENERALES
        elif opcion == "3":   
            # Menú de Informes Generales
            while True:
                print("\n---------------------------")
                print("INFORMES GENERALES")
                print("---------------------------")
                print("[1] Emitir Informe de Ventas")
                print("[2] Emitir Listado de Películas Disponibles")
                print("[3] Emitir Informe de Butacas Disponibles")
                print("[0] Volver al menú")
                opcionInformes = input("Seleccione una opción: ")

                if opcionInformes == "0": break
                # Implementación de los informes aquí...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        # Opción 4: GESTIÓN DE COMPLEJO DE CINES
        elif opcion == "4":   
            # Menú de Gestión de Complejo de Cines
            while True:
                print("\n---------------------------")
                print("GESTIÓN DE COMPLEJO DE CINES")
                print("---------------------------")
                print("[1] Listar Cines")
                print("[2] Agregar Nuevo Cine")
                print("[3] Eliminar Cine")
                print("[4] Modificar Cine")
                print("[0] Volver al menú")
                opcionCines = input("Seleccione una opción: ")

                if opcionCines == "0": break
                # Implementación de gestión de cines aquí...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

if __name__ == "__main__":
    main()


"""Se optimizo lineas de codigo del menu principal"""
"""se cambio la cantidad de 0 al generar un id"""
"""se cambio editar pelicula para saber que pelicula estamos cambiando"""
""" se cambio la funcion generar id, En vez de convertir y formatear el ID cada vez, considera usar solo el número como clave en el diccionario movies y formatearlo solo para mostrarlo. Así reduces el largo de la clave y simplificas la generación de ID."""
""" se cambio validacion de horarios, El valor esHorario = True es redundante ya que la función retorna True al final si el horario es válido, así que se elimino y se retorna False directamente en los casos de error."""


"""
La línea de código id_mapping = {i: k for i, k in enumerate(movies.keys(), 1)} crea un diccionario llamado id_mapping que relaciona números secuenciales con los IDs de las películas almacenadas en el diccionario movies. cómo funciona:

movies.keys(): Esto obtiene todas las claves del diccionario movies, que en este contexto son los IDs de las películas. Por ejemplo, si movies tiene IDs como '0000000000001', '0000000000002', etc., movies.keys() devolverá un iterable con esos IDs.

enumerate(movies.keys(), 1): La función enumerate toma un iterable y devuelve pares de índice y valor. En este caso, comienza a contar desde 1 (debido al segundo argumento 1), por lo que generará pares como (1, '0000000000001'), (2, '0000000000002'), etc. Cada número (el índice) se asociará con un ID de película.

{i: k for i, k in ...}: Este es un "diccionario por comprensión". Está construyendo un nuevo diccionario donde i es el número secuencial (el índice de enumerate) y k es el ID de la película. Por lo tanto, por cada par generado por enumerate, se añadirá una entrada en el nuevo diccionario id_mapping.

"""

"""En resumen, esta línea de código crea un diccionario que mapea números secuenciales (comenzando desde 1) a los IDs de las películas, lo que facilita referenciar películas mediante un número en lugar de usar directamente su ID, mejorando así la usabilidad del sistema."""