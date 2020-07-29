# https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
    if not s:
        return True
    if len(s) <= 1:
        return False

    stack = []

    for i, char in enumerate(s):
        last_stack = stack[len(stack) - 1] if stack else ''

        if char == "(":
            stack.append(char)
        elif char == ")" and last_stack == "(":
            stack.pop()

        elif char == "[":
            stack.append(char)
        elif char == "]" and last_stack == "[":
            stack.pop()

        elif char == "{":
            stack.append(char)
        elif char == "}" and last_stack == "{":
            stack.pop()
        else:
            stack.append(char)

    return bool(len(stack) == 0)

print(isValid("([)]") == False)
print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)
print(isValid("{[]}") == True)
print(isValid("]") == False)
print(isValid("") == True)
print(isValid("(])") == False)
