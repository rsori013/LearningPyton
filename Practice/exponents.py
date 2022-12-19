
def raise_to_power(base_number, power):
    #return (base_number**power)
    result = 1
    for index in range (power):
        result = result *base_number
    return result




base = input("Enter the base number: ")
exponent = input("Enter the exponent: ")


print (raise_to_power(int(base),int(exponent)))