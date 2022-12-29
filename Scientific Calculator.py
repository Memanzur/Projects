import math

def scientific_calculator(operation, num1, num2=None):
  if operation == '+':
    return num1 + num2
  elif operation == '-':
    return num1 - num2
  elif operation == '*':
    return num1 * num2
  elif operation == '/':
    return num1 / num2
  elif operation == 'sqrt':
    return math.sqrt(num1)
  elif operation == 'sin':
    return math.sin(num1)
  elif operation == 'cos':
    return math.cos(num1)
  elif operation == 'tan':
    return math.tan(num1)
  else:
    return "Invalid operator"

print(scientific_calculator('+', 1, 2))  # 3
print(scientific_calculator('-', 4, 2))  # 2
print(scientific_calculator('*', 3, 5))  # 15
print(scientific_calculator('/', 6, 2))  # 3
print(scientific_calculator('sqrt', 9))  # 3
print(scientific_calculator('sin', 90))  # 1.0
print(scientific_calculator('cos', 0))  # 1.0
print(scientific_calculator('tan', 45))  # 1.0
print(scientific_calculator('^', 2, 3))  # Invalid operator
