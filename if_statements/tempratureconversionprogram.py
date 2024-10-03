unit=input("Is it Celsius or Fahrenheit? (C/F) ")
temp=float(input("Enter the temperature: "))

if(unit=="C" or unit=="c"):
    converted_temp=(temp*9/5)+32
    print(converted_temp)
elif(unit=="F" or unit=="f"):
    converted_temp=(temp-32)*5/9
    print(converted_temp)
else:
    print("Invalid unit")