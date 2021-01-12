A = [99, 0, 23, 3, 45, 4, 56, 4, 5, 6, 5, 6, 7, 8]

def sortAnArray(A):
    # Traverse through all array elements
    for i in range(len(A)):
        # Find the minimum element in remaining
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        # Swap the found minimum element with
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

sorted = sortAnArray(A)
print(sorted)
