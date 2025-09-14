from inventario import Inventario

def menu_principal():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        # Muestra las opciones del menú
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Lógica para añadir un producto...
            pass
        elif opcion == '2':
            # Lógica para eliminar un producto...
            pass
        # ... y así con el resto de las opciones...
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()