def total(num):
    if num == 1:
        return 1
    else:
        result = num + total(num -1)
        return result

print(total(6))