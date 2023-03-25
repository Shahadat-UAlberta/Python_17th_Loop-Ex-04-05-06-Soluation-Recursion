def summation(sm):
    if sm == 0:
        return 0
    else:
        return sm + summation(sm-1)

sum = summation(10)

print(sum)
