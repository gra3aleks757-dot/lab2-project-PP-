def add(a, b):
    """Combined version with logging"""
    result = a + b
    print(f"Adding: {a} + {b} = {result}")
    return result
  
def subtract(a, b):
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a * b

print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
