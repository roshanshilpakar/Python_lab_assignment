import calendar as cal
month = int(input("Enter Month:"))
year = int(input("Enter Year:"))
if(year>999 and year<10000):
    if(month>=1 and month<=12):
        print(cal.month(year,month))
    else:
        print("Invalid Input")
else:
    print("Invalid Input")