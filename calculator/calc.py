#Interactive calculator with ratings stored in a seperate file
#wip


userIn = int(input('Enter your first number: '))
userIn2 = int(input('Enter your second number: '))

print('What operation you want to do on this numbers?')
print('[+] for addition')
print('[-] for subtraction')
print('[*] for multiplication')
print('[/] for division')
print('[//] for floor')
userOp = str(input('Specify here: '))

#operations
add = userIn + userIn2
sub = userIn - userIn2
mul = userIn * userIn2
div = userIn / userIn2
floor = userIn // userIn2


if (userOp == '+'):
    print(userIn, userOp, userIn2, '=', add)
elif (userOp == '-'):
    print(userIn, userOp, userIn2, '=', sub)
elif(userOp == '*'):
    print(userIn, userOp, userIn2, '=', mul)
elif(userOp == '/'):
    print(userIn, userOp, userIn2, '=', div)
elif(userOp == '//'):
    print(userIn, userOp, userIn2, '=', floor)
else:
    print('Please input correct keyword!')

#ratings

rating = open("ratings.txt", "a")
userRate = str(input("Please leave a rating below \n"))

rating.write(userRate)
rating.close()

input('Press ENTER to exit')


