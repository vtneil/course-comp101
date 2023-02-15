def f1():
    A = []
    for i in range(0, 10):
        A.append(i)
    return A


def main1():
    a = f1()
    print(a)
    b = a
    print(b)
    a[2] = 88
    print(b)


def main2():
    a = f1()
    print(a)
    b = list(a)
    print(b)
    a[2] = 99
    print(b)


main2()
