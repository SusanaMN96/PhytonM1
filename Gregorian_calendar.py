year = int(input("Enter a year: "))

if year < 1582:
    type_of_year = "Not within the Gregorian calendar period"
elif year%4 != 0:
    type_of_year = "Common year"
elif year%400 != 0:
    type_of_year = "Common year"
elif year%100 != 0:
    type_of_year = "Leap year"
else:
    type_of_year = "Leap year"
    
print(type_of_year)
