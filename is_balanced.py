def isBalanced(s):
    map_bracket = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    tmp = []
    for i in s:
        if i in "([{":
            tmp.append(i)
        else:
            if len(tmp) == 0:
                return "NO"
            if map_bracket[tmp[-1]] != i:
                return "NO"
            tmp.pop()

    return "YES" if len(tmp) == 0 else "NO"
