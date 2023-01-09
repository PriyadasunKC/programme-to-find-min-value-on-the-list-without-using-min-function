# programme to find min value on the list without using min() function

# initializing min value
min_value = 0

my_list3 = [5,3,8,-1,-2,0]
for number in my_list3:

# check the value in list is less than the initilized value to min_value by us
    if (min_value > number):
    
    # if it true it assign to the min_value
        min_value = number
print("{} is the min number".format(min_value))
