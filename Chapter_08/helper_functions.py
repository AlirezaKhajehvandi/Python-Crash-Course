###############################################################
def print_odd_numbers(n: int):
    """
    Prints all odd numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit.
    """
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)

# Example usage:
# print_odd_numbers(10)
# print(20*"-")

###############################################################
def print_even_numbers(n: int):
    """
    Prints all even numbers from 0 to n.
    
    Parameters:
    n (int): The upper limit.
    """
    for i in range(n + 1):
        if i % 2 == 0:
            print(i)

def add_any_number(a, b):
    return a + b

###############################################################
def add_integers(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of a and b.
    """
    return int(a) + int(b)

# Example usage:
# result = add_integers(3, 5)
# print(result) 
# print(20*"-")

###############################################################
def add_floats(a: float, b: float) -> float:
    """
    Adds two floats and returns the result.
    
    Parameters:
    a (float): The first float.
    b (float): The second float.
    
    Returns:
    float: The sum of a and b.
    """
    return float(a) + float(b)

# Example usage:
# result = add_floats(3.5, 2.5)
# print(result)  
# print(20*"-")

###############################################################
def factorial(n: int) -> int:
    """
    Calculates the factorial of a number.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    """
    fact = 1

    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            fact *= i # fact = fact * i
        return fact

# Example usage:
# result = factorial(10)
# print(result)
# print(20*"-")  

###############################################################
def print_fibonacci_series(n: int):
    """
    Prints the Fibonacci series up to n terms.
    
    Parameters:
    n (int): The number of terms in the Fibonacci series.
    """
    a, b = 0, 1
    for _ in range(n):
        print(f"{a},", end=" ")
        a, b = b, a + b
    print(end="\n")
# Example usage:
# print_fibonacci_series(10)
# print(20*"-")

###############################################################
# Example of Recursive Function
def factorial_recursive_func(n: int) -> int:
    """
    Calculates the factorial of a number.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
# result = factorial_recursive(10)
# print(result)
# print(20*"-")  
