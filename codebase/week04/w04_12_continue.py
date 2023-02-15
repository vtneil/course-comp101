def add5(lst):
    sums = 0

    for elem in lst:
        if elem % 5 == 0:
            continue
        sums += elem

    return sums
