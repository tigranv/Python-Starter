
for i in range(2, 20, 3):
    if i > 15:
        break
    print("i = ", i)
    
for i in range(3): 
    response = input('enter stop to crash progr: ')
    if response == 'stop':
        break
else:
    print('finished loop')
print('finished app')