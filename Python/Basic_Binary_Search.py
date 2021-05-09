def BinarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst)-1

    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1



print(BinarySearch(11,[1,2,3,4,5,11,19,22,90]))
