month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if((month==2) and (year%4==0)):
    print("Number of days is 29")
elif(month==2):
    print("Number of days is 28");
elif month in range(1,12,2):
    print("Number of days is 31")
else:
    print("No of days=30")
          
