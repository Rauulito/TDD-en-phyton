class Calculator:
    def __init__(self):
        self.value = 0

    #creamos funcion para que funcione la suma
    def add(self, a, b):
        self.value = a + b

    #creamos una funcion para la resta
    def resta(self, a, b):
        self.value = a - b

    #creamos una funcion para la multiplicacion
    def multi(self, a, b):
        self.value = a * b

    #creamos una funcion para la division
    def division(self, a, b):
        self.value = a / b

    #creamos una funcion para la potencia(siendo a la base y b el exponente)
    def potencia(self, a, b):
        self.value = a ** b