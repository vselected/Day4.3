# Given an int n, return the absolute difference between
# n and 21, except return double the absolute difference if n is over 21.
#
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0
# diff21(22) → 2
# diff21(25) → 8
# diff21(30) → 18
# diff21(0) → 21
# diff21(1) → 20
# diff21(2) → 19
# diff21(-1) → 22
# diff21(-2) → 23
# diff21(50) → 58

def diff21(n):
    if n > 21:
        n = n-21
        n = n*2
        return n
    else:
        return 21-n

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(22))
print(diff21(25))
print(diff21(30))
print(diff21(0))
print(diff21(1))
print(diff21(2))
print(diff21(-1))
print(diff21(-2))
print(diff21(50))