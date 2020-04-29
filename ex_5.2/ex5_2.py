#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#Invalid input, Maximum is 10, Minimum is 2




#print a number that the user types.
while True:
    num = input("Enter a number: ")

    if num == "done" : break
    break

    fnum = float(num)
    print(fnum)

    num = num + 1
    tot = tot + num

#Try to get a proper number from the user.
    try:
        num = float(num)

    except :
        print("Invalid entry")
        continue


#compare to previous number, including the first, None
#    if fnum == None:
#        largest = fnum

#    elif fnum > largest:
#        largest = fnum

#    if fnum == None:
#        smallest = fnum

#    elif fnum < smallest:
#        smallest = fnum

#print("Maximum", largest)
#print("Minimum", smallest)
#print(fnum)
