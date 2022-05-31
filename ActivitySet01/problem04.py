hrs = float(input("Enter Hours: "))
rate = float(input("enter rate: "))

if (hrs>40):
    h = hrs-40
    print(40*rate + h*rate*1.5)
else :
    print(hrs*rate)