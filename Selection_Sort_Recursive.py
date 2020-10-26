A = [44, 33, 22, 11, 00]

# def sortAnArray(A):
#     # Traverse through all array elements
#     for i in range(len(A)):
#         # Find the minimum element in remaining
#         min_idx = i
#         for j in range(i+1, len(A)):
#             if A[min_idx] > A[j]:
#                 min_idx = j
#         # Swap the found minimum element with
#         A[i], A[min_idx] = A[min_idx], A[i]
#     return A


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
