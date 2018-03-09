#x = int(input("x = "))

#if 0 < x < 7:
#    print("{} in raneg of 0 to 7, lets continue".format(x))
#    y = 2 * x -5
#    if y < 0:
#        print("y is negative")
#    else:
#        if y > 0:
#            print("y is positive")
#        else:
#            print("y = 0")

#x = int(input("x = "))

#if 0 < x < 7:
#    print("{} in raneg of 0 to 7, lets continue".format(x))
#    y = 2 * x -5
#    if y < 0:
#        print("y is negative")
#    elif y > 0:
#        print("y is positive")
#    else:
#        print("y = 0")

## switch case analogy

#print(''' Menu:
#1. File
#2. View
#3. Exit
#''')

#choice = input("Enter your choice")

#if choice == "1":
#    print('You have selected file')
#elif choice == "2":
#    print('You have selected View')
#elif choice == "3":
#    print('Stopping')
#else:
#    print('Incorrect choice')
                
is_ready = True

if is_ready:
    msg = "Ready"
else:
    msg = "Not ready"

print(msg)

is_ready = False

msg = is_ready and "Ready" or "Not ready yet"

print(msg)

# ternar operator in python
is_ready = True

msg = "Ready" if is_ready else "Not ready yet"

print(msg)
