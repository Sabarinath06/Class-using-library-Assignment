class everything():
    def Subfields():
        print("Sub-fields in AI are:")
        Lists=["Machine Learning","Neutral Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for List in Lists:
            print(List)
    def oddeven():
        enter=int(input("Enter a number: "))
        if(enter%2==0):
            print(enter,"is Even number")
        else:
            print(enter,"is Odd number")   
    def Elegible():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(Gender=="Male",age=="18"):
            print("NOT ELIGIBLE")
    def percentage():
        m1=int(input("Subject1= "))
        m2=int(input("Subject2= "))
        m3=int(input("Subject3= "))
        m4=int(input("Subject4= "))
        m5=int(input("Subject5= "))
        Total=[m1+m2+m3+m4+m5]
        for total in Total:
            print("Total: ",total)
            percentage=[(total/500)*100]  
            for Percentage in percentage:
                print("Percentage: ",Percentage)
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        Areaformula= [height*breadth/2]
        for area in Areaformula:
            print("Area of Traingle:",area)
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            Breadth=int(input("Breadth:"))
            perimeter=[Height1+Height2+Breadth]
            print("Perimeter formula: Height1+Height2+Breadth")
            for peri in perimeter:
                print("Perimeter of traiangle:",peri)         
          