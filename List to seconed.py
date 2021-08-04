print ("Please enter the list of time in order of 1.hour 2.minute 3.second")

hour= int (input("hour:"))
minute = int (input("minute:"))
second = int(input("second:"))


result= hour*3600+ minute*60 +second

print("total seconds we have in this period of time:",result)
