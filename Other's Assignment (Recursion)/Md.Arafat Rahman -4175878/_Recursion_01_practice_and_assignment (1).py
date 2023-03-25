def add_numbers(Num_list):
    # Base case
    if len(Num_list) == 0:
        return 0
    else:
        return Num_list[0] + add_numbers(Num_list[1:])
num_list_str=input("Enter a list of numbers, seperatad by commas:")

num_list=[int(num) for num in num_list_str.split(",")]
sum_of_Numbers = add_numbers(num_list)
print("The sum of the first 10 numbers is: {}".format(sum_of_Numbers))
