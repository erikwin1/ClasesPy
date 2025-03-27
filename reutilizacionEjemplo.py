
class Bateria:
    """Clase reutilizable que modela una batería recargable."""
    def __init__(self, capacidad=100):
        self.capacidad = capacidad    # capacidad máxima de la batería
        self.nivel = capacidad       # nivel actual de carga (inicialmente llena)
    
    def recargar_completa(self):
        """Recarga la batería al máximo."""
        self.nivel = self.capacidad
        # No imprime nada; dejamos que el usuario de la clase decida si informa
    
    def consumir(self, cantidad):
        """
        Consume cierta cantidad de batería.
        Devuelve True si pudo consumir completamente, False si la batería se agotó antes.
        """
        if cantidad < 0:
            return False  # no consumir negativo
        if cantidad > self.nivel:
            # No hay suficiente carga para consumir todo lo pedido
            self.nivel = 0
            return False
        else:
            self.nivel -= cantidad
            return True
    
    def obtener_nivel(self):
        """Devuelve el nivel de carga actual (en las mismas unidades de capacidad)."""
        return self.nivel





class Androide:
    def __init__(self, nombre, modelo, capacidad_bateria=100):
        self.nombre = nombre
        self.modelo = modelo
        # Composición: el androide tiene una Bateria como parte de sus atributos
        self.bateria = Bateria(capacidad=capacidad_bateria)
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}, modelo {self.modelo}.")
    
    def ver_bateria(self):
        nivel = self.bateria.obtener_nivel()
        print(f"Nivel de batería de {self.nombre}: {nivel}/{self.bateria.capacidad}")
        return nivel
    
    def recargar(self):
        self.bateria.recargar_completa()
        print(f"{self.nombre}: \u26a1 Batería recargada al 100%.")
    
    def realizar_tarea(self, tarea):
        # Supongamos que cada tarea consume 10 unidades de batería
        consumo = 10
        exito = self.bateria.consumir(consumo)
        if exito:
            print(f"{self.nombre} realiza '{tarea}'. (Batería -{consumo}, nivel actual: {self.bateria.obtener_nivel()})")
        else:
            print(f"{self.nombre} no puede realizar '{tarea}': batería insuficiente.")


rob = Androide("AT-43", "Explorador", capacidad_bateria=50)
rob.ver_bateria()
rob.realizar_tarea("analizar terreno")
rob.realizar_tarea("sacar foto")
rob.realizar_tarea("enviar datos")
rob.realizar_tarea("patrullar")  # varias tareas hasta agotar
rob.ver_bateria()
rob.recargar()
rob.ver_bateria()



Nivel de batería de AT-43: 50/50
AT-43 realiza 'analizar terreno'. (Batería -10, nivel actual: 40)
AT-43 realiza 'sacar foto'. (Batería -10, nivel actual: 30)
AT-43 realiza 'enviar datos'. (Batería -10, nivel actual: 20)
AT-43 realiza 'patrullar'. (Batería -10, nivel actual: 10)
Nivel de batería de AT-43: 10/50
AT-43: \u26a1 Batería recargada al 100%.
Nivel de batería de AT-43: 50/50
