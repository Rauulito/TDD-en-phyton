# Importamos la clase calculadora
import sys
sys.path.insert(0, '/Users/rauln/Documents/Desarrolo orientado a objetos/TDD-en-phyton/calcu/calculadora-tdd-01-empezamos/src' )
from calculator import Calculator

#Prueba de la suma
a = 1
b = 3
c = Calculator()
c.add(a, b)
print("Prueba suma: {} + {} = {}".format(a, b, c.value))

# Prueba de resta
a = 3
b = 1
c = Calculator()
c.resta(a, b)
print("Prueba resta: {} - {} = {}".format(a, b, c.value))

# Prueba de multiplicacion
a = 3
b = 2
c = Calculator()
c.multi(a, b)
print("Prueba multiplicación: {} * {} = {}".format(a, b, c.value))

# Prueba de division
a = 6
b = 2
c = Calculator()
c.division(a, b)
print("Prueba división: {} / {} = {}".format(a, b, c.value))

# Prueba de potencia
a = 2
b = 3
c = Calculator()
c.potencia(a, b)
print("Prueba potencia: {} ^ {} = {}".format(a, b, c.value))

# Prueba de factorial
a = 3
c = Calculator()
c.factorial(a)
print("Prueba factorial: {}! = {}".format(a, c.value))