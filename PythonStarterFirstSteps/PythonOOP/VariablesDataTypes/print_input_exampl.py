# print

print(2, 3, 4, 5, sep = ', ')
print('he', 'llo', sep = '')

print(1, end = ' ')
print(2, end = "\n\n\n\n")
print("he", end = "")
print("llo", )

# input
st = input("Enter a string: ")
print('you entered "{0}"'.format(st))
input("Press key to continue")

n = int(input("first number -"))
m = int(input("second number -"))
print('{} + {} = {}'.format(n, m, n + m))
