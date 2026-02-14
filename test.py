import unittest
from calc import Calculator

class Test(unittest.TestCase):  
    
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4,7), 11)
        self.assertEqual(self.calc.add(8,9), 17)
        
    def test_div(self):
        self.assertEqual(self.calc.sub(2,2), 0)
        self.assertEqual(self.calc.sub(9,5), 4)
        
    def test_mult(self):
        self.assertEqual(self.calc.mult(5,10), 50)
        self.assertEqual(self.calc.mult(5,5), 25)
        
    def test_div(self):
        self.assertEqual(self.calc.div(18,2), 9)
        self.assertEqual(self.calc.div(12,12), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(1, 0)
    
        
if __name__ == "__main__":
    unittest.main()