
def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input("Enter limit: "))

print_numbers(n)

my_list = [1,2]

def add_to_list(some_list):
    some_list.append(8)

add_to_list(my_list)

print(my_list)