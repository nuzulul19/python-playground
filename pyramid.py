def pyramid(n):
    space = n
    val = 1

    for _ in range(n):
        print_value = ""
        print_value += " " * space
        print_value += "*" * val
        space -= 1
        val += 2
        print(print_value)


pyramid(20)
