age=100
if(age>=18):
    print("you are an adult")
elif age<=0:
    print("you haven't been born yet")
elif(age>=1 and age<=17):
    print("you are a kid")  
elif(age==100):
    print("you are too old to sign up")
else:
    print("you are a baby")



response=input("Do you want to continue? (Y/N)")

if response=="y" or response=="Y":
    print("continue")
elif response=="n" or response=="N":
    print("stop")

def hello(name):
    if name == "":
        print("you haven't entered the name")
        name = input("Please enter your name: ")
        hello(name)
    else:
        print(f"hello {name}")

hello("")