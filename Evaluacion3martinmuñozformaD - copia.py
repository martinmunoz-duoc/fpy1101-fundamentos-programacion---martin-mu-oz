
# ==========================================
# SISTEMA DE GESTION DE EMPLEADOS
# ==========================================

empleados = []


# ==========================================
# FUNCION MOSTRAR MENU
# ==========================================

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Agregar empleado")
    print("2. Buscar empleado")
    print("3. Eliminar empleado")
    print("4. Actualizar estado")
    print("5. Mostrar empleados")
    print("6. Salir")
    print("====================================")


# ==========================================
# FUNCION LEER OPCION
# ==========================================

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Ingrese una opcion entre 1 y 6.")

        except ValueError:
            print("Error: ingrese un numero entero.")


# ==========================================
# FUNCION AGREGAR EMPLEADO
# ==========================================

def agregar_empleado():
    print("\n--- AGREGAR EMPLEADO ---")

    nombre = input("Nombre completo: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacio.")
        nombre = input("Nombre completo: ").strip()

    while True:
        try:
            edad = int(input("Edad: "))

            if edad > 0:
                break

            print("La edad debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un numero entero.")

    while True:
        try:
            salario = float(input("Salario mensual: "))

            if salario > 0:
                break

            print("El salario debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un numero decimal.")

    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
        "activo": False
    }

    empleados.append(empleado)

    print("Empleado agregado correctamente.")


# ==========================================
# FUNCION BUSCAR EMPLEADO
# ==========================================

def buscar_empleado():
    print("\n--- BUSCAR EMPLEADO ---")

    nombre = input("Nombre a buscar: ").strip().lower()

    for empleado in empleados:

        if empleado["nombre"].lower() == nombre:
            print("Empleado encontrado:")
            print(empleado)
            return

    print("Empleado no encontrado.")


# ==========================================
# FUNCION ELIMINAR EMPLEADO
# ==========================================

def eliminar_empleado():
    print("\n--- ELIMINAR EMPLEADO ---")

    nombre = input("Nombre a eliminar: ").strip().lower()

    for empleado in empleados:

        if empleado["nombre"].lower() == nombre:
            empleados.remove(empleado)

            print("Empleado eliminado correctamente.")
            return

    print("Empleado no encontrado.")


# ==========================================
# FUNCION ACTUALIZAR ESTADO
# ==========================================

def actualizar_estado():
    print("\n--- ACTUALIZAR ESTADO ---")

    nombre = input("Nombre del empleado: ").strip().lower()

    for empleado in empleados:

        if empleado["nombre"].lower() == nombre:

            if empleado["edad"] >= 18:
                empleado["activo"] = True
                print("Empleado activo.")

            else:
                print("No cumple la edad requerida.")

            return

    print("Empleado no encontrado.")


# ==========================================
# FUNCION MOSTRAR EMPLEADOS
# ==========================================

def mostrar_empleados():
    print("\n--- LISTA DE EMPLEADOS ---")

    if len(empleados) == 0:
        print("No hay empleados registrados.")

    else:
        for empleado in empleados:

            print("-------------------------")
            print("Nombre:", empleado["nombre"])
            print("Edad:", empleado["edad"])
            print("Salario:", empleado["salario"])
            print("Activo:", empleado["activo"])


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    mostrar_menu()

    opcion = leer_opcion()

    if opcion == 1:
        agregar_empleado()

    elif opcion == 2:
        buscar_empleado()

    elif opcion == 3:
        eliminar_empleado()

    elif opcion == 4:
        actualizar_estado()

    elif opcion == 5:
        mostrar_empleados()

    elif opcion == 6:
        print("Programa finalizado.")
        break

# LINEAS 1 A 5:
# Se crea una lista vacia llamada empleados para guardar los datos de los empleados.

# LINEAS 6 A 17:
# Se crea la funcion mostrar_menu mediante print para mostrar las opciones del menu principal al usuario.

# LINEAS 18 A 35:
# Se crea la funcion leer_opcion con un while para repetir la pregunta, try para intentar convertir la opcion en entero, if para validar que este entre 1 y 6, else para detectar opciones incorrectas y except para controlar errores si no se ingresa un numero entero.

# LINEAS 36 A 77:
# Se crea la funcion agregar_empleado para registrar nuevos empleados, solicitando nombre, edad y salario. Se utilizan while para validar que los datos no esten vacios o sean mayores que cero, try y except para controlar errores. Finalmente, se guardan los datos en un diccionario y se agregan a la lista empleados.

# LINEAS 78 A 96:
# Se crea la funcion buscar_empleado para encontrar un empleado por su nombre, utilizando input, strip y lower para limpiar y comparar el texto. Se utiliza un for para recorrer la lista, un if para comprobar si existe y return para finalizar la busqueda.

# LINEAS 97 A 115:
# Se crea la funcion eliminar_empleado para buscar un empleado por su nombre y eliminarlo de la lista mediante remove. Se utiliza for para recorrer los empleados, if para comprobar coincidencias y return para finalizar.

# LINEAS 116 A 139:
# Se crea la funcion actualizar_estado para buscar un empleado y cambiar su estado a activo si cumple con la edad requerida de 18 años o mas. Se utilizan for, if y else para comprobar las condiciones.

# LINEAS 140 A 161:
# Se crea la funcion mostrar_empleados para mostrar todos los empleados registrados. Se utiliza if para comprobar si la lista esta vacia y else con for para recorrer y mostrar los datos de cada empleado.

# LINEAS 162 A 187:
# Se crea el programa principal mediante un while True para mantener el menu funcionando. Se utiliza mostrar_menu y leer_opcion para recibir las opciones, y una estructura if y elif para ejecutar la funcion correspondiente. Finalmente, con la opcion 6 se muestra un mensaje de finalizacion y break para cerrar el programa.