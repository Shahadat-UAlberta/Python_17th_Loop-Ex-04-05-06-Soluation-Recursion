def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n+1)

print_numbers(2)
