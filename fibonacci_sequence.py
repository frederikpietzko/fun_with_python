

# intuitive recusion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    while True:
        n = int(input("Calculate Fibonacci for n=?"))
        print(fibonacci(n))
