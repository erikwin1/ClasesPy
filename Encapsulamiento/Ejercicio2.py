class Temperatura:
    def __init__(self, celsius=0.0):
        self.__celsius = 0.0
        self.establecer_celsius(celsius)
    
    def establecer_celsius(self, grados):
        if grados < -273.15:
            print("[!] Temperatura inválida: por debajo del cero absoluto.")
        else:
            self.__celsius = grados
    
    def obtener_celsius(self):
        return self.__celsius
    
    def obtener_fahrenheit(self):
        return (self.__celsius * (9.0/5.0)) + 32.0
    
    def mostrar_info(self):
        print(f"Temperatura: {self.__celsius:.2f} °C = {self.obtener_fahrenheit():.2f} °F")



temp = Temperatura()
temp.mostrar_info()

temp.establecer_celsius(25)
print("Celsius:", temp.obtener_celsius())
print("Fahrenheit:", temp.obtener_fahrenheit())

temp.establecer_celsius(-300)
temp.mostrar_info()



"""
Temperatura: 0.00 °C = 32.00 °F
Celsius: 25
Fahrenheit: 77.0
[!] Temperatura inválida: por debajo del cero absoluto.
Temperatura: 25.00 °C = 77.00 °F
"""