# https://leetcode.com/problems/longest-common-prefix/
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) <= 0:
        return ''

    strs.sort()

    prefix = strs[0]

    for i, char in enumerate(prefix):
        for word in strs[1:]:
            if i + 1 > len(word):
                break
            if char != word[i]:
                prefix = prefix[:i]

    return prefix

print(longestCommonPrefix(["flower","flow","flight"]) == "fl")
print(longestCommonPrefix(["dog","racecar","car"]) == "")
print(longestCommonPrefix(["cb","cbb","a"]) == "")
print(longestCommonPrefix(["abab","aba","abc"]) == "ab")
print(longestCommonPrefix(["abab","aba", ""]) == "")
