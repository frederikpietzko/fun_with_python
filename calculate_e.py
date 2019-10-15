from math import factorial
from decimal import Decimal, getcontext

# calculate e via brothers's formula


def calc_summands(k):
    for i in range(k):
        q1 = 2*i + 2
        q2 = factorial(2*i + 1)
        yield Decimal(q1/q2)


def calc_e(k, precision):
    getcontext().prec = precision
    summands = calc_summands(k)
    e = sum(summands)
    return str(e)


if __name__ == "__main__":
    while True:
        n = int(input(
            "How many steps of Brothers' Formulae do you want execute to calculate e?"))
        p = int(input("What shall be the precision of the calculation?"))
        print(calc_e(n, p))
