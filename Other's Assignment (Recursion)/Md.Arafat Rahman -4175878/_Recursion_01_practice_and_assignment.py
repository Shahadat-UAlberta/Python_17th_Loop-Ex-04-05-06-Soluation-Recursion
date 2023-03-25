def add_numbers(Num_list):
    # Base case
    if len(Num_list) == 0:
        return 0
    else:
        return Num_list[0] + add_numbers(Num_list[1:])


##>>>>>>>Testing_the_function<<<<<<<
numbers = [1,1,1,1,1,1,1,1,1,1]
sum_of_Numbers = add_numbers(numbers)
print("The sum of the first 10 numbers is: {}".format(sum_of_Numbers))
