class Androide:
    def __init__(self, nombre, modelo):
        # Atributos "privados" (convención: __ indica que no deben tocarse directamente fuera de la clase)
        self.__nombre = nombre
        self.__modelo = modelo
        self.__bateria = 100  # inicia con batería al 100%
    
    # Métodos públicos para interactuar con el objeto:
    def saludar(self):
        """Método público: el androide se presenta."""
        print(f"[*] {self.__nombre} (modelo {self.__modelo}) saluda cordialmente.")
    
    def ver_bateria(self):
        """Método público: devuelve el nivel de batería actual."""
        return self.__bateria
    
    def recargar(self):
        """Método público: recarga la batería al 100%."""
        self.__bateria = 100
        print(f"[+] {self.__nombre}: Bater\u00eda recargada al 100%.")
    
    def realizar_tarea(self, tarea):
        """Método público: el androide realiza una tarea consumiendo batería."""
        if self.__bateria <= 0:
            print(f"[!] {self.__nombre}: No puedo realizar '{tarea}', bater\u00eda agotada.")
        else:
            self.__bateria -= 10
            print(f"[*] {self.__nombre} est\u00e1 realizando '{tarea}'. Bater\u00eda restante: {self.__bateria}%.")


robot = Androide("RX-99", "Explorador")
robot.saludar()
print("Nivel de bater\u00eda (via m\u00e9todo):", robot.ver_bateria(), "%")

robot.realizar_tarea("mapear terreno")
robot.realizar_tarea("tomar muestras")
print("Nivel de bater\u00eda tras tareas:", robot.ver_bateria(), "%")

# Intentemos acceder directamente al atributo de bater\u00eda (no recomendado)
try:
    print(robot.__bateria)
except AttributeError as e:
    print("Error al acceder directamente a __bateria:", e)
    
robot.recargar()
print("Nivel de bater\u00eda final:", robot.ver_bateria(), "%")





