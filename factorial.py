def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
