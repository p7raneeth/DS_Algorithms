def fibonacci(n):
    """
    using recursion the time complexity is 2**n which is highly inefficient
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(7))


def fibo_dp(n):
    """
    using Dynamic Programming the time complexity is brought down to O(n)
    """
    result = {}
    result[0], result[1] = 0, 1
    for i in range(2, n+1):
        result[i] = result[i-2] + result[i-1]
    return result[i]

print(fibo_dp(7))
