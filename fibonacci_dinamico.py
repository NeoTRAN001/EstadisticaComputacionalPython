import sys
import time

def fibonacci_r(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_r(n - 1) + fibonacci_r(n - 2)

def fibonacci_d(n, memo = {}):
    result = None

    if n == 0 or n == 1:
        return 1

    try:
        result = memo[n]
    except KeyError:
        result = fibonacci_d(n - 1, memo) + fibonacci_d(n - 2, memo)
        memo[n] = result
    
    return result

if __name__ == '__main__':

    sys.setrecursionlimit(10002)

    n = int(input('Write a number: '))

    first_time = time.time()
    print(f'Result: { fibonacci_d(n) }')
    last_time = time.time()

    print(f'\n{last_time - first_time}')