import unittest
from calc import Calculator

class Test(unittest.TestCase):  
    
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4,7), 11)
        
    def test_div(self):
        self.assertEqual(self.calc.sub(2,2), 0)
        
    def test_mult(self):
        self.assertEqual(self.calc.mult(5,10), 50)
        
    def test_div(self):
        self.assertEqual(self.calc.div(12,12), 1)
        
if __name__ == "__main__":
    unittest.main()