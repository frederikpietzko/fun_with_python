from tabulate import tabulate


def sieve_of_eratosthenes(n):
    is_prime = [True for i in range(n+1)]

    number = 2
    while (number**2 <= n):
        if is_prime[number]:
            i = number * 2
            while i <= n:
                is_prime[i] = False
                i += number
        number += 1

    return is_prime


if __name__ == "__main__":
    while True:
        n = int(input("Calculate sieve of eratosthenes until n: "))
        sieve = sieve_of_eratosthenes(n)
        table = tabulate(
            [[is_prime] for is_prime in sieve], showindex="always")
        print(table)
