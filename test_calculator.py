import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    
    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_substract1(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_substract2(self):
        self.assertEqual(self.calc.subtract(1, 3), -2)
    
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(2, -7), -14)
    
    def test_divide1(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(7, 5), 2)
    
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(3, -5), 3)
    

if __name__ == '__main__':
    unittest.main()