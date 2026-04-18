class MultiFunctions():
    def SubFields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
            print(temp)

    def OddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="Female"):
            if(age>18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("INVALID INPUT DATA")

    def Percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        Total=S1+S2+S3+S4+S5
        print("Total:",Total)
        Percentage=(Total/500)*100
        print("Percentage:",Percentage)

    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        AreaFormula=(Height*Breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",AreaFormula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        PerimeterFormula=Height1+Height2+Breadth
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",PerimeterFormula)