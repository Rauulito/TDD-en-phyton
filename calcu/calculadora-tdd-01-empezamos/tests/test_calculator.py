

# Cargamos el módulo unittest
import unittest

# Importamos la clase calculadora
import sys
sys.path.insert(0,'/Users/rauln/Documents/Desarrolo orientado a objetos/TDD-en-phyton/calcu/calculadora-tdd-01-empezamos/src')
from calculator import Calculator


# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
# Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)

