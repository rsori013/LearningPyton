#rather than the progam not working 
#we want to be able to run this script
# using try block

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError  as err:
    print(err)

