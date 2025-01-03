'''fibonacci number'''
from typing import Generator
def fibonacci_generator(n:int)->Generator[int, None, None]:
    """Generate the first n Fibonacci numbers using a generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
num = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci sequence:", list(fibonacci_generator(num)))
