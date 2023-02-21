class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if tipo in ['gasolina', 'electrico']:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, marca, motor, registro, asientos):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos
        Auto.cantidadCreados += 1
        
    def cantidadAsientos(self):
        c = 0
        for num in self.asientos:
            if num is not None:
                c += 1
        return c
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for num in self.asientos:
                if num is not None:
                    if num.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"

