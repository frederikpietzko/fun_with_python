

def classic_euclid_recursive(a, b):
    if b == 0:
        return a
    if a == 0:
        return b

    if a > b:
        return classic_euclid_recursive(a-b, b)
    else:
        return classic_euclid_recursive(a, b-a)


def modern_euclic_recursive(a, b):
    if b == 0:
        return a
    else:
        return modern_euclic_recursive(b, a % b)


# the iterative algorithm is trivial

if __name__ == "__main__":
    while True:
        alg = input("Classic (c) or modern euclid (e) algorithm?")

        while True:
            n = input(
                "Enter exit to choose algorithm. Otherwise enter a number: ")
            if n.isnumeric():
                a = int(n)
                b = int(input("Enter second number: "))

                gdc = classic_euclid_recursive(
                    a, b) if alg == "c" else modern_euclic_recursive(a, b)
                print(gdc)
            else:
                break
