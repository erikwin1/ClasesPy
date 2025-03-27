
class Bateria:
    def __init__(self, capacidad=100):
        self.capacidad = capacidad
        self.nivel = capacidad  # comienza llena
    
    def recargar_completa(self):
        self.nivel = self.capacidad
    
    def consumir(self, cantidad):
        if cantidad < 0:
            return False
        if cantidad > self.nivel:
            self.nivel = 0
            return False
        else:
            self.nivel -= cantidad
            return True
    
    def obtener_nivel(self):
        return self.nivel

#Ahora las clases Linterna y Radio usando composición con Bateria:

class Linterna:
    def __init__(self, capacidad_bateria=100):
        self.bateria = Bateria(capacidad_bateria)
        self.encendida = False
    
    def encender(self):
        if self.encendida:
            print("La linterna ya está encendida.")
            return
        # Consumo inicial para encender
        if self.bateria.consumir(5):
            self.encendida = True
            print("Linterna encendida. (Consumo 5 de batería)")
        else:
            print("No hay suficiente batería para encender la linterna.")
    
    def apagar(self):
        if not self.encendida:
            print("La linterna ya está apagada.")
        else:
            self.encendida = False
            print("Linterna apagada.")
    
    def ver_bateria(self):
        nivel = self.bateria.obtener_nivel()
        print(f"Batería de linterna: {nivel}/{self.bateria.capacidad}")
        return nivel

class Radio:
    def __init__(self, capacidad_bateria=100):
        self.bateria = Bateria(capacidad_bateria)
        self.encendida = False
    
    def encender(self):
        if self.encendida:
            print("La radio ya está encendida.")
            return
        if self.bateria.consumir(3):
            self.encendida = True
            print("Radio encendida. (Consumo 3 de batería)")
        else:
            print("No hay batería para encender la radio.")
    
    def apagar(self):
        if not self.encendida:
            print("La radio ya está apagada.")
        else:
            self.encendida = False
            print("Radio apagada.")
    
    def cambiar_estacion(self):
        if not self.encendida:
            print("No puedes cambiar de estación con la radio apagada.")
        else:
            # Supongamos que cambiar estación consume 1 de batería
            if self.bateria.consumir(1):
                print("Cambiando de estación... (Consumo 1 de batería)")
            else:
                print("Batería insuficiente para cambiar de estación.")
                self.encendida = False  # podría apagarse si se queda sin batería
    
    def ver_bateria(self):
        nivel = self.bateria.obtener_nivel()
        print(f"Batería de radio: {nivel}/{self.bateria.capacidad}")
        return nivel
"""En ambas clases:
Se instancia self.bateria = Bateria(...).
Los métodos encender consumen algo de batería (diferente cantidad para linterna vs radio, simulando distintos requerimientos).
La Radio tiene un método adicional cambiar_estacion que también consume un poco cuando la radio está encendida.
ver_bateria muestra la carga restante usando la batería encapsulada.
Probemos ambas:"""
linterna = Linterna(capacidad_bateria=20)  # linterna con poca batería para probar
radio = Radio(capacidad_bateria=10)       # radio con poca batería

linterna.ver_bateria()
linterna.encender()
linterna.ver_bateria()
linterna.apagar()
linterna.encender()  # volver a encender para gastar de nuevo
linterna.ver_bateria()
linterna.apagar()
print("---")
radio.ver_bateria()
radio.encender()
radio.cambiar_estacion()
radio.cambiar_estacion()
radio.ver_bateria()
radio.apagar()


"""Posible salida:

Batería de linterna: 20/20
Linterna encendida. (Consumo 5 de batería)
Batería de linterna: 15/20
Linterna apagada.
Linterna encendida. (Consumo 5 de batería)
Batería de linterna: 10/20
Linterna apagada.
---
Batería de radio: 10/10
Radio encendida. (Consumo 3 de batería)
Cambiando de estación... (Consumo 1 de batería)
Cambiando de estación... (Consumo 1 de batería)
Batería de radio: 5/10
Radio apagada."""


"""Notemos que la clase Bateria es reutilizada por ambos objetos, cada uno con su propia instancia independiente. La lógica de consumo y recarga es común y no la duplicamos: si quisiéramos mejorar la clase Bateria (por ejemplo, agregar método para carga parcial), ambas clases podrían beneficiarse sin más cambios. </details> Ejercicio 2: Reutilización en instancias múltiples. En este ejercicio reflexivo, se pide identificar en el siguiente escenario dónde ocurre reutilización de código: Tenemos una clase Persona que define atributos y métodos (ej: nombre, edad, saludar, etc.). En un programa, creamos 100 objetos Persona. ¿Estamos duplicando código 100 veces? Explicar por qué o por qué no, mencionando cómo Python (o cualquier lenguaje OOP) maneja las instancias en relación a la definición de la clase. (No es necesario código para este ejercicio, solo la explicación.) <details> <summary><strong>Explicación esperada</strong></summary> Cuando definimos una clase, el código de sus métodos existe solo una vez en la memoria del programa. Al crear 100 instancias (objetos) de esa clase, cada objeto almacena sus propios datos (atributos), pero reutiliza los métodos definidos en la clase. No se crea una copia separada de la función saludar() para cada objeto; todos los objetos comparten la misma lógica. Internamente, cuando invocamos objeto.saludar(), el lenguaje busca la definición de saludar en la clase Persona (una única definición) y la ejecuta, usando los datos del objeto específico. Por tanto, no duplicamos el código de los métodos 100 veces, sino que reutilizamos la definición común. Lo único que se repite en las 100 instancias son los valores de sus atributos (por ejemplo, cada Persona tiene su propio nombre y edad almacenados). Este es un principio fundamental de la orientación a objetos: múltiples objetos pueden existir basados en una sola definición de clase, lo cual es una forma intrínseca de reutilización de código. En resumen, definir una clase y crear muchas instancias es una forma de "escribir una vez, usar muchas". Esto ahorra código y facilita mantenimiento: si quisiéramos cambiar el comportamiento de saludar, lo hacemos en la clase Persona una vez, y automáticamente todos los objetos actuales y futuros usarán el nuevo comportamiento. </details>
Con estos ejercicios hemos repasado cómo la POO nos permite reutilizar código eficientemente, ya sea a través del uso repetido de una clase en múltiples objetos, o estructurando las clases para compartir componentes o heredar características. Ahora, profundizaremos en la Herencia, que es un mecanismo formal de reutilización y organización de clases en jerarquías.
Herencia
Teoría de la Herencia
La herencia es un mecanismo de la POO que permite crear una nueva clase basada en otra clase existente. La nueva clase (llamada subclase o clase derivada) hereda los atributos y métodos de la clase existente (llamada superclase o clase base), y además puede añadir nuevas propiedades o comportamientos, o modificar (sobreescribir) algunos de los existentes. En términos conceptuales, la herencia modela una relación "es un(a)":
Un AndroideProfesor es un Androide.
Un Círculo es un FiguraGeométrica.
Un Administrador es un Empleado.
Estas relaciones implican que la subclase tiene todo lo que la superclase tiene (características generales), y posiblemente más cosas o comportamientos especializados. Beneficios de la herencia:
Reutilización de código: No tenemos que escribir desde cero las partes comunes en las subclases; las heredan de la superclase.
Organización jerárquica: Ayuda a organizar conceptos de general a específico. La superclase captura lo general, las subclases lo particular.
Polimorfismo: Las subclases pueden ser tratadas como instancias de la superclase, lo que habilita polimorfismo (lo veremos en la siguiente sección).
Ejemplo teórico: Supongamos que tenemos la clase base Androide genérica. Ahora queremos crear dos tipos específicos de androides:
AndroideDomestico: orientado a tareas del hogar.
AndroideIndustrial: orientado a tareas de manufactura.
Ambos son androides, por lo que heredarán la estructura básica (nombre, modelo, batería, etc.). Pero pueden agregar:
El AndroideDomestico podría tener un método cocinar() o atributo lista_tareas_hogar.
El AndroideIndustrial podría tener un atributo fuerza_carga o método soldar().
Además, podrían comportarse diferente en algún método heredado. Quizá redefinir cómo se presenta (saludar) para incluir su tipo. Con herencia, definimos class AndroideDomestico(Androide): ... y class AndroideIndustrial(Androide): ... en Python (la sintaxis entre paréntesis indica la superclase). En Java: class AndroideDomestico extends Androide. En C#: class AndroideDomestico : Androide.
Ejemplo práctico en Python (Herencia con Androide)
Continuando nuestro caso, implementemos herencia. Tomaremos una versión sencilla de Androide como superclase base, y luego derivaremos un par de subclases. Definición de la clase base Androide:
"""

class Androide:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
    
    def saludar(self):
        print(f"Saludos, soy {self.nombre}, modelo {self.modelo}.")
    
    def realizar_tarea(self, tarea):
        print(f"{self.nombre} está realizando la tarea genérica: {tarea}.")


"""Esta clase es similar a anteriores pero más minimalista (para centrarnos en herencia):
Tiene nombre y modelo.
Un método saludar genérico.
Un método realizar_tarea genérico (quizá un androide genérico no sabe hacer nada específico, pero lo definimos).
Definición de subclases:
AndroideDomestico, que hereda de Androide:
Además del nombre y modelo heredados, tendrá un atributo específico, por ejemplo habitacion_asignada (simulando que este androide trabaja en cierto lugar de la casa).
Puede tener un método nuevo, digamos cocinar(plato).
Puede sobrescribir (override) el método realizar_tarea para personalizarlo.
AndroideGuardia (por variar, en lugar de industrial, hagamos uno guardia de seguridad), que hereda de Androide:
Atributo específico: por ejemplo zona_vigilancia.
Método nuevo: patrullar(area).
Sobrescribir saludar para que se identifique como guardia, por ejemplo.
Implementación:"""


class AndroideDomestico(Androide):
    def __init__(self, nombre, modelo, habitacion_asignada):
        # Llamamos al constructor de la superclase Androide para inicializar nombre y modelo
        super().__init__(nombre, modelo)
        self.habitacion_asignada = habitacion_asignada
    
    def cocinar(self, plato):
        print(f"{self.nombre} está cocinando {plato} en la habitación {self.habitacion_asignada}.")
    
    def realizar_tarea(self, tarea):
        # Sobrescribimos realizar_tarea con un comportamiento más específico para tareas domésticas
        tareas_domesticas = ["limpiar", "ordenar", "cocinar", "lavar"]
        if tarea in tareas_domesticas:
            print(f"{self.nombre} (doméstico) está realizando la tarea de hogar: {tarea}.")
        else:
            # Si la tarea no es doméstica, llamamos al comportamiento genérico de la superclase
            super().realizar_tarea(tarea)

class AndroideGuardia(Androide):
    def __init__(self, nombre, modelo, zona_vigilancia):
        super().__init__(nombre, modelo)
        self.zona_vigilancia = zona_vigilancia
    
    def patrullar(self):
        print(f"{self.nombre} patrulla la zona {self.zona_vigilancia}.")
    
    def saludar(self):
        # Sobrescribimos el saludo para incluir que es guardia
        print(f"{self.nombre} reportándose. Soy un androide guardia modelo {self.modelo}, vigilando {self.zona_vigilancia}.")


"""Puntos clave:
Usamos super().__init__(...) para invocar el constructor de Androide y no repetir la asignación de nombre y modelo (reutilizamos esa parte).
AndroideDomestico añade habitacion_asignada y método cocinar.
AndroideDomestico.realizar_tarea sobrescribe el método de la superclase: verifica si la tarea es del hogar, si sí la ejecuta con mensaje específico, si no, llama a super().realizar_tarea(tarea) para usar la implementación genérica.
AndroideGuardia añade zona_vigilancia y método patrullar.
AndroideGuardia.saludar sobrescribe para un saludo especial estilo guardia.
Ahora probemos el comportamiento de herencia:"""

# Instancias de diferentes tipos de androides
androide_base = Androide("XJ-1", "Genérico")
chef_bot = AndroideDomestico("Chef-99", "Doméstico", habitacion_asignada="Cocina")
guard_bot = AndroideGuardia("Guardian-7", "Seguridad", zona_vigilancia="Entrada Principal")

# Usar métodos heredados y propios
androide_base.saludar()
chef_bot.saludar()         # heredado de Androide (no lo sobrescribimos en Domestico)
chef_bot.cocinar("sopa")
chef_bot.realizar_tarea("limpiar")
chef_bot.realizar_tarea("vigilar")  # tarea no doméstica, debería delegar al super
guard_bot.saludar()        # sobrescrito en Guardia
guard_bot.realizar_tarea("vigilar") # no sobrescribimos realizar_tarea en Guardia, usará el genérico
guard_bot.patrullar()


"""Salida esperada:
Saludos, soy XJ-1, modelo Genérico.
Saludos, soy Chef-99, modelo Doméstico.
Chef-99 está cocinando sopa en la habitación Cocina.
Chef-99 (doméstico) está realizando la tarea de hogar: limpiar.
Chef-99 está realizando la tarea genérica: vigilar.
Guardian-7 reportándose. Soy un androide guardia modelo Seguridad, vigilando Entrada Principal.
Guardian-7 está realizando la tarea genérica: vigilar.
Guardian-7 patrulla la zona Entrada Principal."""



"""Observemos:
chef_bot.saludar() usó la implementación heredada de Androide porque no la cambiamos en AndroideDomestico.
chef_bot.realizar_tarea("limpiar") usó la implementación sobrescrita (tarea doméstica reconocida).
chef_bot.realizar_tarea("vigilar") no estaba en la lista doméstica, entonces su método sobrescrito llamó a super().realizar_tarea, que imprimió el mensaje genérico.
guard_bot.saludar() usó su versión sobrescrita (menciona que es guardia).
guard_bot.realizar_tarea("vigilar") no tiene override en AndroideGuardia, así que cayó automáticamente en la versión de la superclase Androide.
Ambas subclases pudieron usar los atributos nombre y modelo sin tener que definirlos de nuevo; los heredaron.
Herencia en Java y C#
La sintaxis difiere pero el concepto es igual. Mencionemos algunas particularidades:
Java: Usa extends para heredar. Las subclases llaman al constructor padre con super(...) en la primera línea del suyo. Java soporta herencia simple (una sola superclase directa). Métodos se pueden sobrescribir; para marcarlo se usa la anotación @Override encima del método sobrescrito (opcional pero recomendado para verificar). Java por defecto permite override de cualquier método no marcado como final. Las variables de instancia privadas del padre existen en el hijo pero no son accesibles directamente (tendrías que usar getters o protected).
C#: Usa : para heredar. Por defecto, los métodos en C# no son sobrescribibles a menos que se declaren virtual en la superclase, y entonces la subclase use override. Esto es una diferencia importante: hay que planificar qué métodos serán polimórficos. C# también tiene herencia simple (una clase base). Propiedades y métodos se manejan similar con virtual/override. No es obligatorio [Override] attribute como en Java, se usa la palabra clave.
Ejemplo en Java:

class Androide {
    protected String nombre;
    protected String modelo;
    public Androide(String nombre, String modelo) {
        this.nombre = nombre;
        this.modelo = modelo;
    }
    public void saludar() {
        System.out.println("Saludos, soy " + nombre + ", modelo " + modelo + ".");
    }
    public void realizarTarea(String tarea) {
        System.out.println(nombre + " esta realizando la tarea generica: " + tarea + ".");
    }
}

class AndroideDomestico extends Androide {
    private String habitacionAsignada;
    public AndroideDomestico(String nombre, String modelo, String habitacion) {
        super(nombre, modelo);
        this.habitacionAsignada = habitacion;
    }
    public void cocinar(String plato) {
        System.out.println(nombre + " esta cocinando " + plato + " en la habitacion " + habitacionAsignada + ".");
    }
    @Override
    public void realizarTarea(String tarea) {
        if(tarea.equals("limpiar") || tarea.equals("cocinar") || tarea.equals("lavar") || tarea.equals("ordenar")) {
            System.out.println(nombre + " (domestico) realiza la tarea del hogar: " + tarea + ".");
        } else {
            super.realizarTarea(tarea);
        }
    }
}

class AndroideGuardia extends Androide {
    private String zonaVigilancia;
    public AndroideGuardia(String nombre, String modelo, String zona) {
        super(nombre, modelo);
        this.zonaVigilancia = zona;
    }
    public void patrullar() {
        System.out.println(nombre + " patrulla la zona " + zonaVigilancia + ".");
    }
    @Override
    public void saludar() {
        System.out.println(nombre + " reportandose. Androide guardia modelo " + modelo + ", vigilando " + zonaVigilancia + ".");
    }
}"""


"""
Uso en Java:
Androide base = new Androide("XJ-1", "Generico");
AndroideDomestico chef = new AndroideDomestico("Chef-99", "Domestico", "Cocina");
AndroideGuardia guard = new AndroideGuardia("Guardian-7", "Seguridad", "Entrada Principal");

base.saludar();
chef.saludar();
chef.cocinar("sopa");
chef.realizarTarea("limpiar");
chef.realizarTarea("vigilar");
guard.saludar();
guard.realizarTarea("vigilar");
guard.patrullar();"""

"""Ejemplo en C#:
class Androide {
    public string Nombre { get; set; }
    public string Modelo { get; set; }
    public Androide(string nombre, string modelo) {
        Nombre = nombre;
        Modelo = modelo;
    }
    public virtual void Saludar() {
        Console.WriteLine($"Saludos, soy {Nombre}, modelo {Modelo}.");
    }
    public virtual void RealizarTarea(string tarea) {
        Console.WriteLine($"{Nombre} está realizando la tarea genérica: {tarea}.");
    }
}

class AndroideDomestico : Androide {
    public string HabitacionAsignada { get; set; }
    public AndroideDomestico(string nombre, string modelo, string habitacion) 
        : base(nombre, modelo) {
        HabitacionAsignada = habitacion;
    }
    public void Cocinar(string plato) {
        Console.WriteLine($"{Nombre} está cocinando {plato} en la habitación {HabitacionAsignada}.");
    }
    public override void RealizarTarea(string tarea) {
        string[] tareasDomesticas = {"limpiar", "ordenar", "cocinar", "lavar"};
        if(Array.Exists(tareasDomesticas, t => t == tarea)) {
            Console.WriteLine($"{Nombre} (doméstico) está realizando la tarea del hogar: {tarea}.");
        } else {
            base.RealizarTarea(tarea);
        }
    }
}

class AndroideGuardia : Androide {
    public string ZonaVigilancia { get; set; }
    public AndroideGuardia(string nombre, string modelo, string zona) 
        : base(nombre, modelo) {
        ZonaVigilancia = zona;
    }
    public void Patrullar() {
        Console.WriteLine($"{Nombre} patrulla la zona {ZonaVigilancia}.");
    }
    public override void Saludar() {
        Console.WriteLine($"{Nombre} reportándose. Androide guardia modelo {Modelo}, vigilando {ZonaVigilancia}.");
    }
}"""


"""En este código C#:
Marcamos Saludar y RealizarTarea de Androide como virtual para permitir override.
Usamos override en las subclases donde corresponde.
Propiedades autoimplementadas para Nombre, Modelo, etc. en lugar de campos, para simplicidad.
Nota: Ni Java ni C# soportan herencia múltiple de clases (una clase solo puede extender de una base, pero puede implementar múltiples interfaces). Python sí permite herencia múltiple, pero es un caso avanzado que no cubriremos aquí.
Ejercicios de Herencia
Ahora, pongamos en práctica la herencia con ejercicios. Ejercicio 1: Crea una clase base Animal con un método hacer_sonido() (puede ser abstracto o genérico que imprima algo básico). Luego crea al menos dos subclases Perro y Gato que hereden de Animal e implementen hacer_sonido() de forma específica (por ejemplo, el perro ladra, el gato maúlla). Añade algún atributo específico a cada subclase (por ejemplo, raza para Perro, color para Gato) y un método propio de cada una (por ejemplo, traer_pelota() en Perro, cazar_raton() en Gato). Finalmente, crea instancias de Perro y Gato y demuestra que:
Llamar a hacer_sonido() en cada uno produce la salida específica.
Puedes acceder a métodos propios como traer_pelota() y cazar_raton() en los objetos correctos.
Si tu lenguaje lo permite (Python sí), también demuestra que una lista de Animal puede contener Perro y Gato y al iterar y llamar hacer_sonido() se comporta polimórficamente (aunque el polimorfismo se explicará en la siguiente sección, se puede intuir aquí)."""

"""Solución en Python"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")
        
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    def hacer_sonido(self):
        print(f"{self.nombre} dice: \u201cGuau guau\u201d")  # ladrido
    def traer_pelota(self):
        print(f"{self.nombre} está trayendo la pelota.")
        
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    def hacer_sonido(self):
        print(f"{self.nombre} dice: \u201cMiau\u201d")  # maullido
    def cazar_raton(self):
        print(f"{self.nombre} está cazando un ratón.")



"""Explicación: Animal es genérico. Perro y Gato heredan. Ambos sobrescriben hacer_sonido() con su sonido característico. Perro agrega atributo raza y método traer_pelota(). Gato agrega color y método cazar_raton(). Probemos:"""


firulais = Perro("Firulais", "Labrador")
misifu = Gato("Misifu", "Blanco")

firulais.hacer_sonido()   # Ladrido
misifu.hacer_sonido()     # Maullido

firulais.traer_pelota()
misifu.cazar_raton()

# Polimorfismo básico: lista de Animal con perro y gato
animales: list[Animal] = [firulais, misifu]
for animal in animales:
    animal.hacer_sonido()

"""Salida esperada:

Firulais dice: “Guau guau”
Misifu dice: “Miau”
Firulais está trayendo la pelota.
Misifu está cazando un ratón.
Firulais dice: “Guau guau”
Misifu dice: “Miau”
La última parte demuestra que aunque iteramos como Animal, Python invoca el método apropiado de cada objeto (Perro o Gato), gracias a la herencia y a que en Python todos los métodos son virtuales por naturaleza (polimorfismo dinámico). En Java/C#, necesitaríamos usar referencias del tipo de la superclase para similar efecto y asegurarnos de declarar hacer_sonido() como método polimórfico (virtual/override o no final). </details> 

Ejercicio 2: Supongamos una clase base abstracta Figura con un método abstracto area(). 
Implementa subclases Rectangulo y Circulo que extiendan Figura e implementen el método area() adecuadamente (para rectángulo basealtura, para círculo πradio^2). 
Añade también un método descripcion() en Figura (concretamente implementado en la base o abstracto, a tu elección) que indique de qué tipo de figura se trata. 
Prueba creando una lista de Figura con diferentes figuras y calculando sus áreas. (Este ejercicio se enfoca en herencia para estructuras matemáticas.)
 Solución en Python, En Python no tenemos clases abstractas obligatorias como en Java, pero podemos simularlo. Aquí lo haremos de forma simple sin abc:"""

import math

class Figura:
    def area(self):
        """Metodo a ser implementado por subclases."""
        raise NotImplementedError("Debe implementarse el metodo area() en la subclase")
    def descripcion(self):
        return "Figura geométrica genérica"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def descripcion(self):
        return "Rectángulo de base {} y altura {}".format(self.base, self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)
    def descripcion(self):
        return "Círculo de radio {}".format(self.radio)
"""Explicación: Figura.area lanza un error si no se implementa (simula abstracto). Rectangulo y Circulo dan su fórmula en area(). También sobreescriben descripcion() para más detalle. Prueba:"""



figuras = [Rectangulo(3, 4), Circulo(5), Rectangulo(2, 10)]
for fig in figuras:
    print(fig.descripcion(), "- Área:", round(fig.area(), 2))


"""Salida esperada:
Rectángulo de base 3 y altura 4 - Área: 12
Círculo de radio 5 - Área: 78.54
Rectángulo de base 2 y altura 10 - Área: 20
En lenguajes como Java/C#, Figura sería una clase abstracta (Java: abstract class Figura { abstract double area(); }). Rectangulo y Circulo usarían extends Figura e implementarían area(). La lista de Figura con instancias de subclases mostrando polimorfismo es un preludio al siguiente tema de Polimorfismo. </details>
Con la herencia hemos visto cómo estructurar clases de forma jerárquica y reutilizar código de clases base en clases derivadas. También hemos insinuado el concepto de sobreescritura de métodos (override) en subclases. A continuación, profundizaremos en el Polimorfismo, que se apoya en la herencia para permitir tratar objetos de distintas clases de manera uniforme.
Polimorfismo
Teoría del Polimorfismo
El término polimorfismo proviene del griego y significa "muchas formas". En POO, se refiere a la capacidad de que objetos de diferentes clases relacionadas (por herencia) respondan de manera distinta al mismo mensaje (llamada de método). En esencia:
Un mismo método (por ejemplo hacer_sonido() o realizar_tarea()) puede tener múltiples implementaciones según el tipo específico del objeto que lo invoque.
Si diferentes clases comparten una interfaz común (por heredar de una clase base o implementar la misma interfaz), pueden ser usadas indistintamente en contexto de esa interfaz, y cada una ejecutará su comportamiento específico.
Polimorfismo se manifiesta típicamente de dos formas:
Polimorfismo de subtipos (dinámico o de tiempo de ejecución): Es el descrito arriba. Ejemplo: una variable de tipo Androide base puede referirse a un AndroideDomestico o AndroideGuardia y al llamar saludar() se ejecuta la versión específica de la subclase. Esto requiere herencia y sobrescritura de métodos. En lenguajes estáticos, también requiere que los métodos sean declarados virtuales/override correctamente.
Polimorfismo de sobrecarga (estático o de tiempo de compilación): Es cuando existen múltiples funciones/métodos con el mismo nombre pero distinta firma (parámetros), y se elige cuál usar según los tipos o número de argumentos. Esto en realidad es "sobrecarga" y lo veremos en la siguiente sección por separado, ya que en el enunciado se trata como concepto aparte (Sobrecarga). En algunos textos lo llaman "polimorfismo estático", pero para evitar confusión, acá nos enfocamos en el polimorfismo mediante herencia (dinámico).
Ejemplo conceptual: Polimorfismo dinámico ya lo vimos en los ejercicios anteriores:
Una lista de Animal con perros y gatos, todos responden a hacer_sonido() de forma diferente.
Un array de Figura con círculos y rectángulos, todos responden a area() apropiadamente.
¿Por qué es útil? Porque permite escribir código más genérico. Por ejemplo, una función procesarFigura(Figura fig) podría llamar fig.area() sin saber si es círculo o rectángulo; gracias al polimorfismo, funcionará correctamente para cualquier subtipo de Figura. En Python, el polimorfismo es muy natural debido a su tipado dinámico y duck typing: no hace falta herencia; si dos objetos tienen el método area(), puedes tratarlos polimórficamente llamando obj.area() en ambos sin importar su clase. Pero en el contexto clásico de OOP, nos centramos en polimorfismo vía herencia. En Java/C#, el polimorfismo se da al asignar, por ejemplo, Androide ref = new AndroideDomestico(...); (una referencia de tipo base apuntando a objeto de subclase), y luego llamar ref.realizarTarea("limpiar"); ejecutará la versión de AndroideDomestico si el método está override. Esto se suele llamar "envío dinámico" o "late binding" de métodos.
Ejemplo práctico (Polimorfismo con Androides)
Retomemos las clases de Androide del apartado de Herencia (Androide base, AndroideDomestico, AndroideGuardia). Vamos a crear una función que reciba una lista de objetos de tipo Androide (podrían ser base o cualquiera de sus subclases) y les ordene realizar una tarea en común, por ejemplo "vigilar". Observaremos cómo cada objeto ejecuta su propia versión de realizar_tarea:
"""
# Supongamos que ya tenemos definidas las clases Androide, AndroideDomestico, AndroideGuardia como antes.
# Creamos una lista heterogénea de androides:
androides = [
    Androide("XZ-0", "Genérico"),
    AndroideDomestico("Maid-1", "Doméstico", "Salon"),
    AndroideGuardia("Sec-7", "Seguridad", "Almacén")
]

# Enviar a todos los androides la misma tarea "vigilar"
for a in androides:
    a.realizar_tarea("vigilar")

"""Salida esperada
XZ-0 está realizando la tarea genérica: vigilar.
Maid-1 está realizando la tarea genérica: vigilar.
Sec-7 está realizando la tarea genérica: vigilar.
¿Por qué todos imprimieron "tarea genérica"? Porque en nuestro diseño actual, AndroideDomestico.realizar_tarea solo cambia comportamiento para ciertas tareas domésticas, pero "vigilar" no está en su lista, así que llama a la versión genérica; y AndroideGuardia no sobreescribió realizar_tarea. Así que en este caso particular, los tres ejecutaron el método de Androide (sea directamente o vía super). Si hubiéramos asignado una tarea "limpiar", esperaríamos que el AndroideDomestico la maneje especialmente:
"""


for a in androides:
    a.realizar_tarea("limpiar")
"""Salida:
plaintext
Copiar
Editar
XZ-0 está realizando la tarea genérica: limpiar.
Maid-1 (doméstico) está realizando la tarea de hogar: limpiar.
Sec-7 está realizando la tarea genérica: limpiar.
Aquí se ve el polimorfismo: las tres variables a son del mismo tipo estático (Androide base) pero en tiempo de ejecución cada una invoca su propia versión del método, en particular la segunda que es un AndroideDomestico ejecutó la suya sobrescrita. Otro ejemplo, polimorfismo con el método saludar:"""


for a in androides:
    a.saludar()
"""Salida:
plaintext
Copiar
Editar
Saludos, soy XZ-0, modelo Genérico.
Saludos, soy Maid-1, modelo Doméstico.
Sec-7 reportándose. Soy un androide guardia modelo Seguridad, vigilando Almacén.
Aquí el último, Sec-7, usó su método sobrescrito de guardia, mientras los otros dos usaron la implementación de Androide (porque Domestico no lo sobreescribió, y el base es base). Este comportamiento de "múltiples formas de responder al mismo método" es polimorfismo.
Polimorfismo y tipos en Python vs Java/C#
En Python, no tuvimos que declarar la lista como List[Androide] ni nada; simplemente funciona. En Java/C#, esa lista tendría que ser, por ejemplo, List<Androide> en Java (o Androide[]) y llenar con subclases está permitido implícitamente. Luego al iterar y llamar métodos, se produce polimorfismo siempre que los métodos sean virtuales/override. Un detalle en C#: si un método en la base no es virtual, la subclase puede ocultarlo con new keyword, pero la llamada polimórfica no ejecutará la versión nueva a través de referencia base, sino la base (básicamente no es polimorfismo real). Por eso en C# marcamos virtual/override para intencionalmente habilitar polimorfismo.
Duck typing (mención breve)
Polimorfismo en Python también puede entenderse mediante duck typing: "si algo camina como pato y suena como pato, trátalo como pato". Es decir, no importa la clase, mientras tenga el método que necesitas. Por ejemplo:"""


class Persona:
    def saludar(self):
        print("Hola, soy una persona.")

class Perro:
    def saludar(self):
        print("Guau! (el perro te saluda moviendo la cola)")

cosas = [Persona(), Perro()]
for c in cosas:
    c.saludar()
"""Salida:
plaintext
Copiar
Editar
Hola, soy una persona.
Guau! (el perro te saluda moviendo la cola)
Aquí Persona y Perro no comparten una superclase común con saludar (más allá de object base), pero Python igual permite llamar saludar() en ambos. Esto es polimorfismo también, aunque no basado en herencia, sino en protocolo (cualquier objeto con método saludar vale). En Java/C#, para lograr algo así sin herencia necesitarías interfaces comunes.
Ejercicios de Polimorfismo
Estos ejercicios se centran en aprovechar polimorfismo ya sea con herencia o en Python mediante duck typing. Ejercicio 1: Dada la jerarquía de clases Animal -> Perro, Gato del ejercicio anterior de Herencia, crea una función hacer_cantar_coro(animales) que reciba una lista de animales (pueden ser perros o gatos mezclados) y que llame al método hacer_sonido() de cada uno para que "canten" en coro. Comprueba que se llama la implementación correcta de cada subclase. Luego, agrega otra subclase Pajaro a Animal con su propio sonido (p. ej. "Pío") y muestra que la misma función puede manejarlo sin cambios. <details> <summary><strong>Solución orientativa</strong></summary> Reutilizando la solución de herencia del ejercicio de Animal:"""


class Pajaro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre)
        self.especie = especie
    def hacer_sonido(self):
        print(f"{self.nombre} dice: \u201cPío pío\u201d")
    def volar(self):
        print(f"{self.nombre} el {self.especie} está volando.")
"""La función polimórfica:"""

def hacer_cantar_coro(animales):
    for animal in animales:
        animal.hacer_sonido()
"""Prueba:"""

animales = [Perro("Firulais", "Labrador"), Gato("Minina", "Negro"), Pajaro("Piolin", "Canario")]
hacer_cantar_coro(animales)
"""Salida:"""
"""Firulais dice: “Guau guau”
Minina dice: “Miau”
Piolin dice: “Pío pío”
Y podemos comprobar que incluso sin conocer la subclase, la función genérica los hizo "cantar" correctamente. Si quisiéramos extender a Pajaro, no necesitamos cambiar hacer_cantar_coro, solo añadimos la clase Pajaro con hacer_sonido definido. </details> Ejercicio 2: Imagina una interfaz (o clase base abstracta) ReproductorMusical con un método reproducir(). Implementa dos clases que la representen: ReproductorMP3 y Tocadiscos. ReproductorMP3.reproducir() imprimirá algo como "Reproduciendo MP3..." y Tocadiscos.reproducir() algo como "Reproduciendo vinilo...". Luego crea una lista con objetos de ambos tipos pero referenciados como ReproductorMusical (en Python simplemente mezclados en una lista, en Java/C# usando la interfaz). Itera y llama reproducir() a cada uno para ver el polimorfismo. (En Python no tenemos interfaces explícitas, puedes solo asegurarte de que ambas clases tienen el método reproducir, o simular con herencia de una base común.) <details> <summary><strong>Solución en Python (simulada interfaz)</strong></summary>"""

class ReproductorMusical:
    def reproducir(self):
        raise NotImplementedError

class ReproductorMP3(ReproductorMusical):
    def reproducir(self):
        print("Reproduciendo archivo MP3...")
        
class Tocadiscos(ReproductorMusical):
    def reproducir(self):
        print("Reproduciendo disco de vinilo...")
"""Lista polimórfica y uso:"""

reproductores = [ReproductorMP3(), Tocadiscos(), ReproductorMP3()]
for r in reproductores:
    r.reproducir()
"""Salida:"""
"""Reproduciendo archivo MP3...
Reproduciendo disco de vinilo...
Reproduciendo archivo MP3...
Esto demuestra que los objetos de diferentes clases (ReproductorMP3 y Tocadiscos), cuando se les pide reproducir() a través del mismo tipo base (implícito o explícito), ejecutan su comportamiento específico. En Java, esto sería logrado con interface ReproductorMusical { void reproducir(); } que ambas clases implementan. </details>
Con polimorfismo concluimos los cuatro pilares clásicos de la POO (Abstracción, Encapsulamiento, Herencia, Polimorfismo). Queda por abordar el concepto de Sobrecarga, que si bien no es uno de los "pilares" fundamentales, es una característica presente en muchos lenguajes OO (especialmente estáticos) que permite definir métodos con el mismo nombre para distintos propósitos, mejorando la flexibilidad de la interfaz de clases. Vamos a desarrollarlo a continuación.
Sobrecarga
Teoría de la Sobrecarga
La sobrecarga de métodos (o funciones) consiste en definir múltiples funciones con el mismo nombre pero diferentes parámetros (ya sea en número, tipo o ambos). El compilador o intérprete decidirá cuál invocar según cómo fue llamada. Esto es distinto a la sobrescritura de herencia; la sobrecarga ocurre generalmente en la misma clase (o relacionadas, en algunos lenguajes con polimorfismo estático). Lenguajes con sobrecarga: Java, C#, C++ soportan sobrecarga nativamente. Python no admite sobrecarga de métodos por nombre de la misma manera; definir dos métodos con el mismo nombre en una clase resulta en que el último reemplaza al primero. Sin embargo, Python permite lograr efectos similares usando parámetros opcionales o *args/**kwargs, o usando diferentes funciones con nombres distintos. Ejemplo conceptual: Supongamos una clase Calculadora donde queremos un método sumar. Podríamos sobrecargar sumar(int a, int b) para sumar dos enteros y sumar(String a, String b) para concatenar dos textos, o sumar(int a, int b, int c) para sumar tres enteros, etc. En Java/C#, serían métodos distintos con mismo nombre y firmas diferentes. En Python, tendríamos que combinar esa lógica en un solo método usando tipo dinámico o tener nombres distintos. Otro ejemplo: en una clase Androide, podríamos querer un método mover() que:
Si se llama sin argumentos, mueve un paso adelante.
Si se llama con un entero, mueve ese número de pasos.
Si se llama con dos enteros (x, y), se mueve a esa posición (coordenadas).
En Java/C#, se lograría definiendo mover(), mover(int pasos) y mover(int x, int y). En Python, podríamos hacer def mover(self, x=None, y=None) y luego lógica interna para decidir. Sobrecarga de operadores: Es un caso especial, en lenguajes como Python y C++ uno puede redefinir operadores (+, -, etc.) para clases. En Python se hace implementando métodos especiales como __add__. C# permite sobrecargar operadores también (operator+). Java no permite custom operator overloading (solo los prelanzados en el lenguaje). Dado que la pregunta menciona sobrecarga como concepto, nos centraremos en la sobrecarga de métodos.
Ejemplo práctico de Sobrecarga en Python (simulación)
Aunque Python no soporta declarar sobrecargas separadas, podemos ilustrar la intención usando un método con parámetros opcionales. Tomemos el ejemplo del método mover para un androide:
Implementaremos en Python un método mover() que usa la firma def mover(self, x=None, y=None, pasos=None). Según cuáles argumentos no sean None, determinará la acción.
Sin argumentos (x,y,pasos todos None): mueve un paso.
Si se pasa pasos=n: mueve n pasos.
Si se pasan x e y: se mueve a coordenada (x,y).
(Se podrían combinar casos, pero para simplicidad, no mezclaremos pasos con x,y en la misma llamada).
También mostraremos cómo sería en Java y C# con verdaderas sobrecargas."""


class AndroideMovil:
    def mover(self, x=None, y=None, pasos=None):
        if x is not None and y is not None:
            print(f"El androide se desplaza a la posición ({x}, {y}).")
        elif pasos is not None:
            print(f"El androide avanza {pasos} pasos.")
        else:
            print("El androide da un paso hacia adelante.")

"""Aquí AndroideMovil.mover se comporta distinto según cómo se llame: Probemos distintas llamadas:"""

bot = AndroideMovil()
bot.mover()            # sin argumentos
bot.mover(pasos=3)     # especificando pasos
bot.mover(x=10, y=5)   # especificando coordenadas
"""Salida esperada:"""

"""El androide da un paso hacia adelante.
El androide avanza 3 pasos.
El androide se desplaza a la posición (10, 5).
Si intentamos pasarle tanto pasos como x,y, nuestro método actual prioriza la primera condición que encuentre (x and y). Podemos mejorar la lógica o documentar que la sobrecarga simulada no soporta mezclarlos (en Java/C# no harías un método que combine esas firmas; serían exclusivas).
Sobrecarga en Java/C# (ejemplo AndroideMovil)
En Java:"""

"""
class AndroideMovil {
    public void mover() {
        System.out.println("El androide da un paso hacia adelante.");
    }
    public void mover(int pasos) {
        System.out.println("El androide avanza " + pasos + " pasos.");
    }
    public void mover(int x, int y) {
        System.out.println("El androide se desplaza a la posicion (" + x + ", " + y + ").");
    }
}
Uso:
AndroideMovil bot = new AndroideMovil();
bot.mover();
bot.mover(3);
bot.mover(10, 5);
El compilador determinará que:
bot.mover() llama al primero.
bot.mover(3) coincide con la firma de un entero (no confundible con (int,int) porque solo hay uno).
bot.mover(10,5) llama al de dos enteros.
"""
"""En C# sería similar:
csharp
Copiar
Editar
class AndroideMovil {
    public void Mover() {
        Console.WriteLine("El androide da un paso hacia adelante.");
    }
    public void Mover(int pasos) {
        Console.WriteLine($"El androide avanza {pasos} pasos.");
    }
    public void Mover(int x, int y) {
        Console.WriteLine($"El androide se desplaza a la posición ({x}, {y}).");
    }
}
Nota: La sobrecarga se resuelve en tiempo de compilación generalmente, por el número/tipos de argumentos. No tiene relación con la herencia ni polimorfismo dinámico, es más una conveniencia para no usar nombres distintos para funciones similares.
Otro ejemplo: funciones matemáticas
Sobrecargar constructores es común también (varias formas de crear objeto). Por ejemplo, en Java:"""

"""public class Punto {
    private int x, y;
    public Punto() { x=0; y=0; }
    public Punto(int x, int y) { this.x=x; this.y=y; }
    public Punto(int valor) { this.x = this.y = valor; } // inicializa ambos con el mismo valor
}
Aquí tres constructores: sin args, dos ints, y uno int (que setea ambos). En Python, esto se haría con default values or classmethods.
Ejercicios de Sobrecarga
Ejercicio 1: Simular sobrecarga en Python: Crea una clase Conversor con un método convertir. Quieres que convertir pueda usarse de dos formas:
convertir(valor) -> convierta de Celsius a Fahrenheit (por ejemplo, si es un conversor de temperaturas).
convertir(valor, unidad) -> si unidad es "F" convierta de Fahrenheit a Celsius, si es "C" de Celsius a Fahrenheit. Implementa esto en un único método usando parámetros opcionales. Demuestra su uso.
<details> <summary><strong>Solución en Python</strong></summary>"""


class Conversor:
    def convertir(self, valor, unidad=None):
        if unidad is None or unidad.upper() == "C":
            # interpreta valor en Celsius, convierte a Fahrenheit
            fahr = valor * 9.0/5.0 + 32
            print(f"{valor}°C = {fahr:.2f}°F")
            return fahr
        elif unidad.upper() == "F":
            # interpreta valor en Fahrenheit, convierte a Celsius
            cels = (valor - 32) * 5.0/9.0
            print(f"{valor}°F = {cels:.2f}°C")
            return cels
        else:
            print("Unidad no reconocida. Use 'C' o 'F'.")
            return None
"""Pruebas:"""

conv = Conversor()
conv.convertir(100)         # asume Celsius a F
conv.convertir(212, "F")    # F a C (212F deberian ser 100C)
conv.convertir(0, "C")      # explicitamente C a F (0C -> 32F)
conv.convertir(32, "F")     # 32F -> 0C
"""Salida:"""
"""
100°C = 212.00°F
212°F = 100.00°C
0°C = 32.00°F
32°F = 0.00°C"""

"""Aquí, convertir actúa diferente según reciba unidad o no. En Java/C#, se podría tener convertir(double valor) y convertir(double valor, char unidad) separados. </details> Ejercicio 2: (Para lenguajes con sobrecarga nativa, conceptual) Describe cómo podrías tener múltiples constructores en una clase Libro en Java o C#: uno que tome título y autor, otro que tome título, autor y año, y otro que tome título solamente (asumiendo autor desconocido). Escribe el código de los constructores sobrecargados. Luego explica cómo decidiría el lenguaje cuál constructor usar en una llamada new Libro("1984", "George Orwell") versus new Libro("El Quijote"). <details> <summary><strong>Respuesta esperada (en texto, con código ejemplo Java/C#)</strong></summary> En Java:
public class Libro {
    private String titulo;
    private String autor;
    private int anio;
    
    // Constructor 1: Título y autor
    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
        this.anio = 0; // 0 indica que no se especificó el a\u00f1o
    }
    // Constructor 2: Título, autor, a\u00f1o
    public Libro(String titulo, String autor, int anio) {
        this.titulo = titulo;
        this.autor = autor;
        this.anio = anio;
    }
    // Constructor 3: solo título
    public Libro(String titulo) {
        this.titulo = titulo;
        this.autor = "Desconocido";
        this.anio = 0;
    }
    // ... (métodos getters, etc.)
}
En C# similar:
csharp
Copiar
Editar
public class Libro {
    public string Titulo;
    public string Autor;
    public int Anio;
    // Constructor 1
    public Libro(string titulo, string autor) {
        Titulo = titulo;
        Autor = autor;
        Anio = 0;
    }
    // Constructor 2
    public Libro(string titulo, string autor, int anio) {
        Titulo = titulo;
        Autor = autor;
        Anio = anio;
    }
    // Constructor 3
    public Libro(string titulo) {
        Titulo = titulo;
        Autor = "Desconocido";
        Anio = 0;
    }
}
"""