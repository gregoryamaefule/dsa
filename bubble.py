def bubble_sort(A):
    passes = len(A)
    for i in range(passes):
        for j in range(0, passes-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [5,3,2,1,1]

print(bubble_sort(A))