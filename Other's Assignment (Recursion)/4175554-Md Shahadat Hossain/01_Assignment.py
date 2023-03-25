def print_sum(n, total):
    if n <= 10:
        total += n
        print(total)
        print_sum(n+1, total)

print_sum(1, 0)
