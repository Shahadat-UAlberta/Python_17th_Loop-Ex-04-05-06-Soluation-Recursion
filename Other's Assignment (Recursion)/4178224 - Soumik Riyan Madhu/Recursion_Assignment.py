num = int(input())


def sum(n):
    if n == 0:
        return n
    else:
        return n + sum(n - 1)


if num == 0:
    print("ENTER A POSITIVE NUMBER PLEASE!")
else:
    print("The sum of", "(", 1, "-", num, ")", "is", sum(num))
