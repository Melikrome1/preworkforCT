
#Question1
def hello_name(user_name):
    print(f"Hello_{user_name}!")
hello_name("cynthia")

#Question2
def first_odds():
    for i in range(1, 101, 2):
        print(i)
first_odds()

#Question3
def max_num_in_list(a_list):
    max_num = None
    for num in a_list:
        if max_num is None or num > max_num:
            max_num = num
    return max_num
my_list = [1, 5, 2, 8, 3]
print(max_num_in_list(my_list))

#Question4
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2000))
print(is_leap_year(2001))


#Question5
def is_consecutive(a_list):
    if len(a_list) < 2:
        return True
    sorted_list = sorted(a_list)
    for i in range(len(sorted_list) - 1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return False
    return True
print(is_consecutive([2, 3, 4, 5, 6, 7])) 
print(is_consecutive([1, 2, 4, 5])) 

