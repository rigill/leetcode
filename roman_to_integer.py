# TODO
# redo this with a single loop and loop from left to right and add the following
# if the number is larger otherwise subtract the number ( something like that )
# https://leetcode.com/problems/roman-to-integer/
def romanToInt(s: str) -> int:
    cloneString = s
    count = 0

    while(cloneString):
        if 'IV' in cloneString:
            count = count + 4
            cloneString = cloneString.replace('IV', '')
        elif 'IX' in cloneString:
            count = count + 9
            cloneString = cloneString.replace('IX', '')
        elif 'XL' in cloneString:
            count = count + 40
            cloneString = cloneString.replace('XL', '')
        elif 'XC' in cloneString:
            count = count + 90
            cloneString = cloneString.replace('XC', '')
        elif 'CD' in cloneString:
            count = count + 400
            cloneString = cloneString.replace('CD', '')
        elif 'CM' in cloneString:
            count = count + 900
            cloneString = cloneString.replace('CM', '')
        else:
            if 'I' in cloneString:
                count = count + 1
                cloneString = cloneString.replace('I', '', 1)
            elif 'V' in cloneString:
                count = count + 5
                cloneString = cloneString.replace('V', '', 1)
            elif 'X' in cloneString:
                count = count + 10
                cloneString = cloneString.replace('X', '', 1)
            elif 'L' in cloneString:
                count = count + 50
                cloneString = cloneString.replace('L', '', 1)
            elif 'C' in cloneString:
                count = count + 100
                cloneString = cloneString.replace('C', '', 1)
            elif 'D' in cloneString:
                count = count + 500
                cloneString = cloneString.replace('D', '', 1)
            elif 'M' in cloneString:
                count = count + 1000
                cloneString = cloneString.replace('M', '', 1)

    return count


print(romanToInt('III') == 3)
print(romanToInt('IVIV') == 4)
print(romanToInt('IX') == 9)
print(romanToInt('LVIII') == 58)
print(romanToInt('MCMXCIV') == 1994)
print(romanToInt('MCMXCVI') == 1996)
