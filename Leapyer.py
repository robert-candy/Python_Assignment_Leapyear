
num = int(input("please enter a year  :"))

if (num % 4) == 0:
    if (num % 100) == 0:
        print(num, "is not a leap year")
    else:
       print(num, "is a leap year")
else:
  print(num, "is not a leap year")
