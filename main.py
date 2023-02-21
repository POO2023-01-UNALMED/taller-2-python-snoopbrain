class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
            self.color = color

class Motor:
    def __init__(self):
        self.numeroCilindros = 0
        self.tipo = ""
        self.registro = 0
        
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
        
    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if asiento is not None:
                cantidad += 1
        return cantidad
        
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento is not None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"

