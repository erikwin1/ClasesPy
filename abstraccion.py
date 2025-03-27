class Androide:
    """Clase que representa un androide genérico."""

    def __init__(self, nombre, modelo):
        # Atributos esenciales de todo androide
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100  # Nivel de batería inicial (porcentaje)
    
    def saludar(self):
        """El androide se presenta indicando su nombre y modelo."""
        print("[*] (",self.nombre,"modelo",self.modelo,") dice: Hola, un gusto conocerte.")
    
    def recargar(self):
        """Recarga la batería del androide al 100%."""
        self.bateria = 100
        print("[+] Batería recargada. Nivel de batería actual: ",self.bateria,"%")
    
    def realizar_tarea(self, tarea):
        """Realiza la tarea indicada si hay batería suficiente."""
        if self.bateria <= 0:
            print("[!] {",self.nombre,": No puedo realizar ",tarea,", batería agotada.")
        else:
            # Simular consumo de batería por la tarea
            self.bateria -= 10
            print("[*] ",self.nombre," está realizando la tarea: ",tarea,". Batería restante: ",self.bateria,"%.")


# Creación de instancias de Androide
androide1 = Androide("AL-1X", "Asistente Doméstico")
androide2 = Androide("XR-42", "Vigilante")

# Usando los métodos abstractos definidos (presentación, realizar tarea, recarga)
androide1.saludar()         # El androide1 se presenta
androide1.realizar_tarea("limpiar la casa")
androide1.realizar_tarea("cocinar la cena")
androide1.recargar()        # recargamos la batería después de varias tareas
androide1.realizar_tarea("cantar una canción")

print()  # línea en blanco para separar salidas

androide2.saludar()         # El androide2 se presenta
androide2.realizar_tarea("patrullar el perímetro")