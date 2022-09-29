

# Cargamos el módulo unittest
import unittest

# Importamos la clase calculadora
import sys
sys.path.insert(0,'/Users/rauln/Documents/Desarrolo orientado a objetos/TDD-en-phyton/calcu/calculadora-tdd-01-empezamos/src')
from calculator import Calculator


# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
# Creamos una prueba para probar un valor inicial
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)
    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        # Ejecutamos el método
        self.calc.add(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    # Creamos un nuevo test para comprobar la resta
    def test_resta_method(self):
        # Ejecutamos el método
        self.calc.resta(3, 1)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    # Creamos un nuevo test para comprobar la multiplicacion
    def test_multi_method(self):
        # Ejecutamos el método
        self.calc.multi(2, 4)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(8, self.calc.value)

    # Creamos un nuevo test para comprobar la division
    def test_division_method(self):
        # Ejecutamos el método
        self.calc.division(9, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(3, self.calc.value)

    # Creamos un nuevo test para comprobar la potencia
    def test_potencia_method(self):
        # Ejecutamos el método
        self.calc.potencia(2, 4)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(16, self.calc.value)

