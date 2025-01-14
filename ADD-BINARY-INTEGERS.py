def add_binary(a, b):
    n = len(a)
    c = [0] * (n + 1)

    carry = 0

    for i in range(n, 0, -1):
        a_bit = a[i-1]
        b_bit = b[i-1]
        c_bit = a_bit + b_bit + carry

        c[i] = c_bit % 2
        carry = c_bit // 2

    c[0] = carry
    return c

print(add_binary([1,0,1,1], [1,1,0,1]))