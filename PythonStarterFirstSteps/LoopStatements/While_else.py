counter = 5

while counter:
    print(counter)
    counter -= 1
else:
    print("loop is complete")
    print("counter = ", counter)


print("----------------------------")
print()

attempts_left = 3

while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter your password: (You have {} attempts) - ".format(attempts_left +1))
    if password == "98eaxc":
        print("Acces granted")
        break
else:
    print("Access denied")