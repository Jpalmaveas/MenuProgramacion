"""
Este es un programa basico que gestiona compras.
Proporciona un menú interactivo con opciones para agregar compras, mostrar compras,
mostrar el total gastado y salir del programa.
"""
def agregar_compra(compras, total_gastado):
    """
    Agrega una compra a la lista de compras y actualiza el total gastado.

    Parameters:
    - compras (list): La lista de compras actual.
    - total_gastado (float): El total gastado hasta el momento.

    Returns:
    - float: El nuevo total gastado después de agregar la compra.
    """
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado = sum(compras)  # Actualiza total_gastado sumando todos los elementos en compras
    print("Compra agregada correctamente.")
    return total_gastado

def mostrar_compras(compras):
    """
    Muestra la lista de compras.

    Parameters:
    - compras (list): La lista de compras a mostrar.
    """
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, monto in enumerate(compras, 1):
            print(f"{i}. Monto: {monto}")

def mostrar_total(total_gastado):
    """
    Muestra el total gastado.

    Parameters:
    - total_gastado (float): El total gastado a mostrar.
    """
    print(f"Total gastado: ${total_gastado:.2f}")

def main():
    """
    Función principal que gestiona compras.
    Proporciona un menú interactivo con opciones para agregar compras, mostrar compras,
    mostrar el total gastado y salir del programa.
    """
    compras = []
    total_gastado = 0

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
