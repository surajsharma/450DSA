A = [44, 33, 22, 11, 00]


def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)
        return [m] + select_sort_rec(b)


sorted = select_sort_rec(A)
print(sorted)
