class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))        # Output: 5
print(calc.add(5, 10))    # Output: 15
print(calc.add(5, 10, 15)) # Output: 30
