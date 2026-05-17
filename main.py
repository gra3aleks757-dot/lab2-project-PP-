def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    
    Args:
        a (int/float): First multiplier
        b (int/float): Second multiplier
    
    Returns:
        int/float: Product of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a * b

print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
