class Calculator:
    def add(self,a,b):
        print("Addition ",(a+b))
    def sub(self,a,b):
        print("Subtract ",(a-b))
    def multi(self,a,b):
        print("Multiply ",(a*b))
    def divide(self,a,b):
        print("Divide ",(a/b))

o=Calculator()
n1,n2=int(input("Enter first number ")),int(input("Enter second number "))
sign=input("Enter +,-,*,/ ")
if(sign=="+"):
    o.add(n1,n2)
elif(sign=="-"):
    o.sub(n1,n2)
elif(sign=="*"):
    o.multi(n1,n2)
elif(sign=="/"):
    o.divide(n1,n2)
else:
    print("Invalid selection")