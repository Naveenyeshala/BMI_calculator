print("<<<<<<<<<<   welcome to BMI Calculator   >>>>>>>>>>>>>")
Name=input("Enter your name:\n")
weight= float(input("enter your weight in kg:  "))
height_cm=float(input("Enter your height in cm :  "))  
height=height_cm/100
BMI=weight/(height**2)

BMI=weight/(height*height)       

print("BMI is:",BMI)

if BMI>0:
    if(BMI<18.5):
        print(Name+",you are under weight.")
    elif(BMI<=24.9):
        print(Name+",you are Normal weight.")
    elif(BMI<=29.9):
        print(Name+",you are over obese.")
    elif(BMI<=34.9):
        print(Name+",you are severely obese.")
    else:
        print(Name+",you are morbidly obese. ")
else:
    print("ENTER VAID DETAILS")