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
    """- Función que genera un ID único
       - Parámetro: 
            movies (dicc): Diccionario donde se almacenan las películas
       - Retorno:
            movie_id (str): ID único para la película """
            
    if movies == {}:
        movie_id = f"{1:013d}"
        number_id = 1
    else:
        ultima_clave = list(movies.keys())[-1]
        number_id = int(ultima_clave) + 1
        movie_id = f"{number_id:013d}"
    
    return movie_id, number_id

def esHorario(time):
    """- Función que valida horarios
       - Parámetro: 
            time (str): Horario
       - Retorno:
            esHorario (bool): True o False dependiendo si el horario es válido o no """
    
    esHorario = True
    
    if len(time) != 5 or time[2] != ":":
        return False
        
    horas, minutos = time.split(":")
    
    if not (horas.isdigit() and minutos.isdigit()):
        return False
    
    horas = int(horas)
    minutos = int(minutos)
    
    if not (0 <= horas < 24 and 0 <= minutos < 60):
        return False
    
    return esHorario

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
    while format_type.lower() != "2d" and format_type.lower() != "3d":
        format_type = input("Error. Ingresa el formato (2D/3D): ")
        
    language = input("Ingresa el idioma (Español/Subtitulado): ")
    while language.lower() != "español" and language.lower() != "subtitulado":
        language = input("Error. Ingresa el idioma (Español/Subtitulado): ")

    # Almacenar información de la película en el diccionario
    movies[movie_id] = {
        'title': title,
        'format': format_type,
        'language': language,
        'schedule': [],  # Inicializar la lista de horarios
        'activo': True
    }
    
    # Actualizar el mapeo de ID
    id_mapping[number_id] = movie_id

    # Establecer horarios de proyección
    while True:
        
        day = input("Ingresa el día de la semana para la proyección (o 'fin' para terminar): ")
        while day.lower() != "lunes" and day.lower() != "martes" and day.lower() != "miércoles" and day.lower() != "jueves" and day.lower() != "viernes" and day.lower() != "sábado" and day.lower() != "domingo" and day.lower() != "fin":
            day = input("Error. Ingresa el día de la semana para la proyección (o 'fin' para terminar): ")    
        if day.lower() == 'fin':
            break
        
        time = input("Ingresa la hora (ej. 14:00): ")
        while esHorario(time) == False:
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
           
        title = input("Ingresa el nuevo título de la película: ")
        
        format_type = input("Ingresa el nuevo formato (2D/3D): ")
        while format_type.lower() != "2d" and format_type.lower() != "3d":
            format_type = input("Error. Ingresa el formato (2D/3D): ")
            
        language = input("Ingresa el nuevo idioma (Español/Subtitulado): ")
        while language.lower() != "español" and language.lower() != "subtitulado":
            language = input("Error. Ingresa el idioma (Español/Subtitulado): ")

        # Actualizar información de la película
        movie_id = id_mapping[int(movie_number)]
        movies[movie_id] = {
            'title': title,
            'format': format_type,
            'language': language,
            'schedule': movies[movie_id]['schedule'],  # Mantener horarios existentes
            'activo': True
        }
        print(f"¡Película '{movie_id}' modificada con éxito!")
        
    else:
        print("ID de película no encontrado.")
        
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
    '0000000000008': {'title': 'Dumbo', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Martes a las 20:00'], 'activo': True},
    '0000000000009': {'title': 'Avatar', 'format': '2D', 'language': 'Español', 'schedule': ['Miércoles a las 21:00'], 'activo': True},
    '0000000000010': {'title': 'Fast & Furious 9', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Jueves a las 22:00'], 'activo': True},
    '0000000000011': {'title': 'La La Land', 'format': '2D', 'language': 'Español', 'schedule': ['Viernes a las 19:00'], 'activo': True},
    '0000000000012': {'title': 'Shrek', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Sábado a las 12:00'], 'activo': True},
    '0000000000013': {'title': 'Zootopia', 'format': '2D', 'language': 'Español', 'schedule': ['Domingo a las 10:00'], 'activo': True},
    '0000000000014': {'title': 'Guardians of the Galaxy', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Lunes a las 16:00'], 'activo': True},
    '0000000000015': {'title': 'Finding Nemo', 'format': '2D', 'language': 'Español', 'schedule': ['Martes a las 17:00'], 'activo': True},
    '0000000000016': {'title': 'Transformers', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Miércoles a las 20:00'], 'activo': True},
    '0000000000017': {'title': 'The Incredibles', 'format': '2D', 'language': 'Español', 'schedule': ['Jueves a las 18:00'], 'activo': True},
    '0000000000018': {'title': 'Star Wars: The Force Awakens', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Viernes a las 21:00'], 'activo': True},
    '0000000000019': {'title': 'Inside Out', 'format': '2D', 'language': 'Español', 'schedule': ['Sábado a las 13:00'], 'activo': True},
    '0000000000020': {'title': 'Batman v Superman', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Domingo a las 22:00'], 'activo': True},
    '0000000000021': {'title': 'Wonder Woman', 'format': '2D', 'language': 'Español', 'schedule': ['Lunes a las 15:00'], 'activo': True},
    '0000000000022': {'title': 'Pirates of the Caribbean', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Martes a las 19:00'], 'activo': True},
    '0000000000023': {'title': 'Sonic the Hedgehog', 'format': '2D', 'language': 'Español', 'schedule': ['Miércoles a las 16:30'], 'activo': True},
    '0000000000024': {'title': 'Despicable Me 3', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Jueves a las 19:30'], 'activo': True},
    '0000000000025': {'title': 'Kung Fu Panda', 'format': '2D', 'language': 'Español', 'schedule': ['Viernes a las 11:00'], 'activo': True},
    '0000000000026': {'title': 'Spider-Man: No Way Home', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Sábado a las 20:00'], 'activo': True},
    '0000000000027': {'title': 'The Lion King', 'format': '2D', 'language': 'Español', 'schedule': ['Domingo a las 14:30'], 'activo': True},
    '0000000000028': {'title': 'Ant-Man', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Lunes a las 12:00'], 'activo': True},
    '0000000000029': {'title': 'The Secret Life of Pets', 'format': '2D', 'language': 'Español', 'schedule': ['Martes a las 10:30'], 'activo': True},
    '0000000000030': {'title': 'Monsters, Inc.', 'format': '3D', 'language': 'Subtitulado', 'schedule': ['Miércoles a las 15:45'], 'activo': True},
    } # Diccionario para almacenar la información de las películas
    
    id_mapping = {
    1: '0000000000001', 2: '0000000000002', 3: '0000000000003', 4: '0000000000004', 5: '0000000000005', 6: '0000000000006',
    7: '0000000000007', 8: '0000000000008', 9: '0000000000009', 10: '0000000000010', 11: '0000000000011', 12: '0000000000012',
    13: '0000000000013', 14: '0000000000014', 15: '0000000000015', 16: '0000000000016', 17: '0000000000017', 18: '0000000000018',
    19: '0000000000019', 20: '0000000000020', 21: '0000000000021', 22: '0000000000022', 23: '0000000000023', 24: '0000000000024',
    25: '0000000000025', 26: '0000000000026', 27: '0000000000027', 28: '0000000000028', 29: '0000000000029', 30: '0000000000030'
    }  # Mapa para relacionar números con IDs
    
    #-------------------------------------------------
    # Bloque de menú
    #------------------------------------------------------------------------------------------
    while True:
        
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Gestión de Películas y Entradas")
            print("[2] Venta de Entradas")
            print("[3] Informes Generales")
            print("[4] Gestión de Complejo de Cines")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        
        #Opción 0: SALIR DEL PROGRAMA
        
        if opcion == "0": 
            exit()

        # Opción 1: GESTIÓN DE PELÍCULAS Y ENTRADAS
        
        elif opcion == "1":   
            
            # Menú de Películas y Entradas
            
            while True:
                opcionesPeliculas = 6
                while True:
                    print()
                    print("---------------------------")
                    print("GESTIÓN DE PELÍCULAS Y ENTRADAS")
                    print("---------------------------")
                    print("[1] Agregar Película")
                    print("[2] Modificar Película")
                    print("[3] Eliminar Película")
                    print("[4] Modificar valor de la entrada")
                    print("[5] Listar todas las películas")
                    print("---------------------------")
                    print("[0] Volver al menú")
                    print()
            
                    opcionPeliculas = input("Seleccione una opción: ")
                    if opcionPeliculas in [str(i) for i in range(0, opcionesPeliculas)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                
                if opcionPeliculas == "0": #Volver al menú
                    break
                    
                elif opcionPeliculas == "1": #Agregar Película
                    movies = agregarPelicula(movies, id_mapping)
                    
                elif opcionPeliculas == "2": #Modificar Película
                    movies = modificarPelicula(movies, id_mapping)
                    
                elif opcionPeliculas == "3": #Eliminar Película
                    movies = inactivarPelicula(movies, id_mapping)
                    
                elif opcionPeliculas == "4": #Modificar valor de la entrada
                    modificarPrecioEntrada()
                    
                elif opcionPeliculas == "5": #Listar todas las películas
                    listarPeliculas(movies)
                    
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
                
        # Opción 2: VENTA DE ENTRADAS
        
        elif opcion == "2":   
            
            # Menú de Venta de Entradas
            
            while True:
                opcionesEntradas = 3
                while True:
                    print()
                    print("---------------------------")
                    print("VENTA DE ENTRADAS")
                    print("---------------------------")
                    print("[1] Generar Entrada")
                    print("[2] Eliminar Venta")
                    print("---------------------------")
                    print("[0] Volver al menú")
                    print()
            
                    opcionEntradas = input("Seleccione una opción: ")
                    if opcionEntradas in [str(i) for i in range(0, opcionesEntradas)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                
                if opcionEntradas == "0": #Volver al menú
                    break
                    
                elif opcionEntradas == "1": #Generar Entrada
                    ...
                    
                elif opcionEntradas == "2": #Eliminar Venta
                    ...
                    
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
            
        # Opción 3: INFORMES GENERALES
        
        elif opcion == "3":   
            
            # Menú de Informes Generales
            
            while True:
                opcionesInformes = 4
                while True:
                    print()
                    print("---------------------------")
                    print("INFORMES GENERALES")
                    print("---------------------------")
                    print("[1] Emitir Informe de Ventas")
                    print("[2] Emitir Listado de Películas Disponibles")
                    print("[3] Emitir Informe de Butacas Disponibles")
                    print("---------------------------")
                    print("[0] Volver al menú")
                    print()
            
                    opcionInformes = input("Seleccione una opción: ")
                    if opcionInformes in [str(i) for i in range(0, opcionesInformes)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                
                if opcionInformes == "0": #Volver al menú
                    break
                    
                elif opcionInformes == "1": #Emitir Informe de Ventas
                    ...
                    
                elif opcionInformes == "2": #Emitir Listado de Películas Disponibles
                    ...
                
                elif opcionInformes == "3": #Emitir Informe de Butacas Disponibles
                    ...
                    
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
        
        # Opción 4: GESTIÓN DE COMPLEJO DE CINES
                
        elif opcion == "4":   
            
            # Menú de Gestión de Complejo de Cines
            
            while True:
                opcionesCines = 5
                while True:
                    print()
                    print("---------------------------")
                    print("GESTIÓN DE COMPLEJO DE CINES")
                    print("---------------------------")
                    print("[1] Listar Cines")
                    print("[2] Agregar Nuevo Cine")
                    print("[3] Eliminar Cine")
                    print("[4] Modificar Cine")
                    print("---------------------------")
                    print("[0] Volver al menú")
                    print()
            
                    opcionCines = input("Seleccione una opción: ")
                    if opcionCines in [str(i) for i in range(0, opcionesCines)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                
                if opcionCines == "0": #Volver al menú
                    break
                    
                elif opcionCines == "1": #Listar Cines
                    ...
                    
                elif opcionCines == "2": #Agregar Nuevo Cine
                    ...
                    
                elif opcionCines == "3": #Eliminar Cine
                    ...
                    
                elif opcionCines == "4": #Modificar Cine
                    ...
                    
                input("\nPresione ENTER para volver al menú.")
                print("\n\n")
        

# Punto de entrada al programa
if __name__ == "__main__":
    main()
    
    
    


