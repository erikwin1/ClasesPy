import os
class Androide:
    	# El método __init__ es el constructor: inicializa los 			atributos del objeto.
    def __init__(self, nombre, modelo, bat):
        self.nombre = nombre    # atributo de instancia 'nombre’
        self.modelo = modelo    # atributo de instancia 'modelo'
        self.__bateria = bat    #encapsula

    def Saludar(self):  # Un método de instancia que hace que el androide salude.
        print("Hola, soy", self.nombre,", modelo", self.modelo,", Bateria",self.__bateria)
        input("ingrese cualquier caracter para volver: ")
    def Caminar(self):
        self.__bateria -= 10
        print(self.nombre,"esta caminando, queda",self.__bateria," de bateria")
        input("ingrese cualquier caracter para volver: ")


androide1 = Androide("C3PO", "Asistente", 100)


def cls():
    os.system('cls' )

def salir():
    exit()
def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Saludar")
    print("2. caminar")
    print("3. Salir")
    return input("Elige una opción: ")
    

def main():
    cls()
    opcion= mostrar_menu()
    cls()
    switch ={
        "1":androide1.Saludar,
        "2":androide1.Caminar,
        "3":salir
    }
    func= switch.get(opcion,main)
    func()
    main()
main()
"""
androide1.Saludar()
androide1.Caminar()

print("Datos del androide:",androide1.nombre)"""