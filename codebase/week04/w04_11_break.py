def search(lst, k):
    found = False

    for elem in lst:
        if elem == k:
            found = True
            break

    return found
