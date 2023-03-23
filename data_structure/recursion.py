# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))

def check_if_obtacles(x, y, obstacles):
    return True if [x, y] in obstacles else False

obstacles = [[5, 5], [4, 2], [2, 3]]
print(check_if_obtacles(2, 3, obstacles))
