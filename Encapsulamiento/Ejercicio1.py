class CuentaBancaria:
    """Modelo de una cuenta bancaria con encapsulamiento."""
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        # Atributo privado de saldo
        self.__saldo = saldo_inicial
    
    def depositar(self, monto):
        """Deposita una cantidad positiva en la cuenta."""
        if monto <= 0:
            print("[!] Monto inválido para depositar.")
            return
        self.__saldo += monto
        print(f"[+] Depósito de ${monto:.2f} realizado. Saldo actual: ${self.__saldo:.2f}")
    
    def retirar(self, monto):
        """Retira una cantidad de dinero si hay saldo suficiente."""
        if monto <= 0:
            print("[!] Monto inválido para retirar.")
            return
        if monto > self.__saldo:
            print("[!] Fondos insuficientes. Retiro no realizado.")
        else:
            self.__saldo -= monto
            print(f"[-] Retiro de ${monto:.2f} realizado. Saldo actual: ${self.__saldo:.2f}")
    
    def consultar_saldo(self):
        """Devuelve el saldo disponible en la cuenta."""
        return self.__saldo



cuenta = CuentaBancaria("Alice", saldo_inicial=100)
print(f"Saldo inicial: ${cuenta.consultar_saldo():.2f}")
cuenta.depositar(50)
cuenta.retirar(30)

cuenta.__saldo=200.15 #Se crea un nuevo Atributo Público
cuenta.retirar(150)  # intento de retiro excesivo
print(f"Saldo final: ${cuenta.consultar_saldo():.2f}")

print(f"Saldo creado: ${cuenta.__saldo:.2f}") #muestra el valor de la nuevo atributo público variable
# Intentar acceso directo al saldo (debe fallar o no existir):
print("Acceso directo al atributo privado:", hasattr(cuenta, "__saldo"))



"""
Saldo inicial: $100.00
[+] Depósito de $50.00 realizado. Saldo actual: $150.00
[-] Retiro de $30.00 realizado. Saldo actual: $120.00
[!] Fondos insuficientes. Retiro no realizado.
Saldo final: $120.00
Acceso directo al atributo privado: False
"""

"""
Saldo inicial: $100.00
[+] Depósito de $50.00 realizado. Saldo actual: $150.00
[-] Retiro de $30.00 realizado. Saldo actual: $120.00
[!] Fondos insuficientes. Retiro no realizado.
Saldo final: $120.00
Saldo creado: $200.15
Acceso directo al atributo privado: True
"""