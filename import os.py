import os

def limpiar_pantalla():
    os.system('cls' )

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Saludar")
    print("2. Decir adiós")
    print("3. Salir")
    return input("Elige una opción: ")
    

def main():
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu()
        os.system('cls' )

        
        if opcion == '1':
            print("¡Hola!")
        elif opcion == '2':
            print("¡Adiós!")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
        
        input("\nPresiona ENTER para continuar...")

main()
