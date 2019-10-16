from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd


# naive approach
def naive_factorization(n):
    l = []
    # calculate prime numbers until n/2
    sieve = sieve_of_eratosthenes(n//2+1)
    sieve = [[i, sieve[i]] for i in range(len(sieve))][2:]
    sieve = filter(lambda x: x[1], sieve)
    for i, _ in sieve:
        # test for integer division
        if n % i == 0:
            l.append(i)

    return l


def g(x, n):
    return (x**2 + 1) % n


# not finitw yet.
def polland_rho(n):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)

    if d == n:
        return False
    return d


if __name__ == "__main__":
    while True:
        alg = input(
            "Do you want to use my naive approach (n) or the Polland Rho algorithm (p)? ")
        while True:
            n = input(
                "Enter exit to choose algorithm. Otherwise enter a number: ")
            if n.isnumeric():
                n = int(n)

                print(naive_factorization(n))
