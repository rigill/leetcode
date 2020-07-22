# https://leetcode.com/problems/reverse-integer/
# TODO:
# Look into using [::-] to reverse list 

def reverse(x: int) -> int:
    min_limit = -0x80000001
    max_limit = 0x7fffffff

    neg = '-' if bool(x < 0) else ''
    x = str(x).replace('-', '')

    rev = [i for i in reversed(str(x))]
    rev.insert(0, neg)
    rev = int(''.join(rev))
    if rev < min_limit or rev > max_limit:
        return 0
    else:
        return rev

print(reverse(123) == 321)
print(reverse(-123) == -321)
print(reverse(120) == 21)
print(reverse(1534236469) == 0)

