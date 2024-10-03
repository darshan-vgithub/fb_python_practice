weight=input("Enter the weight:")
unit=input("Enter the unit (K or L):")

if(unit=="K" or unit=="k"):
    converted_weight=float(weight)*2.20462  
    print(converted_weight)
elif(unit=="L" or unit=="l"):
    converted_weight=float(weight)/2.20462
    print(converted_weight)
else:
    print("Invalid unit")