#store info, key value pairs like maps in c++? 
#we will see as it goes 
# jan -> january 
#disctionary always a {} 
monthConvesions={
    #key : value !! Gotta be unique
    0 : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "June" : "June",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
#print(monthConvesions.keys())
#print(monthConvesions.values())
#print(monthConvesions["April"]) #can only have the key and will print the value
print(monthConvesions["Mar"]) # will print the value march
print(monthConvesions.get("Luv","None of the options")) # if none of the options are present, will print None
print(monthConvesions.get(0)) # will print January


