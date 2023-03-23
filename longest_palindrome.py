def palindromeAt(s, left, r):
    while left >= 0 and r < len(s) and s[left] == s[r]:
        left -= 1
        r += 1
    return s[left+1:r]


def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        odd = palindromeAt(s, i, i)
        even = palindromeAt(s, i, i+1)

        res = max(res, odd, even, key=len)
    return res


def palindromeIndex(s: str) -> int:
    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            if is_palindrome(s[:len(s)-i-1] + s[len(s)-i:]):
                return len(s)-i-1
    return -1


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    ans = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(ans):
                    ans = s[i:j]
    return ans


print(palindromeIndex("cacddcda"))
