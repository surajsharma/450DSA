A = [-1, -2, -3, 0, -2, 1, -4, 5, -9, 8]


def sortNegative(A, i):
    print(A, i)
    if i <= 0:
        return A
    if A[i] < 0:
        A[i], A[0] = A[0], A[i]

    return sortNegative(A[:i], i-1)


B = sortNegative(A, len(A)-1)
print(B)
