# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
# e.g input: s = "abc" k = 1
# output: "bcd"

def caesarCipher(s, k):
    result = ""
    for i in s:
        if "A" <= i <= "Z":
            result += chr((ord(i) + k - ord("A")) % 26 + ord("A"))
        elif "a" <= i <= "z":
            result += chr((ord(i) + k - ord("a")) % 26 + ord("a"))
        else:
            result += i

    return result
