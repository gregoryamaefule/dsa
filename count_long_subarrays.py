def count_long_subarrays(A: tuple) -> int:
    x = 1
    y = 1
    for i in range(len(A)):
        hold = 0
        l = 0
        for j in range(i, len(A)):
            if A[j] > hold:
                l += 1
                hold = A[j]
                continue
            break
        if l > x:
            x = l
            continue
        if l == x:
            y += 1
            continue
    if x == 1:
        y = len(A)
    return y

print(count_long_subarrays((1,3,4,5,2,7,5,6,9,10,8)))