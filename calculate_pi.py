from math import factorial, sqrt
from decimal import Decimal, getcontext


def cal_summand(k):
    q1 = factorial(6*k)*(545140134*k + 13591409)
    q2 = factorial(3*k)*(factorial(k) ** 3)*((-262537412640768000)**k)
    return Decimal(q1 / q2)


def calc_pi(k):
    getcontext().prec = k
    summands = (cal_summand(i) for i in range(k))
    q1 = Decimal(426880 * sqrt(10005))
    q2 = Decimal(0)
    for summand in summands:
        q2 += summand

    return str(Decimal(q1/q2))[:k+2]


if __name__ == "__main__":
    while True:
        n = input("How many numbers need to be calulated?")
        n = int(n)
        print(calc_pi(n))
