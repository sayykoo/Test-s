class Calculator:   
    def __init__(self):
        self.ans = []
    
    def add(self, a, b):
        result = a + b
        return result
    
    def sub(self, a, b):
        result = a - b
        return result
    
    def mult(self, a, b):
        result = a * b
        return result
    
    def div(self, a, b):
        if b == 0:
            none = "деление на 0))"
            return none
        result = a / b
        return round(result, 2)
    

calc = Calculator()
result = calc.sub(2, -1)
print(f"Ответ: {result}")