class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def divide(self,a,b):
        if(b==0):
            return "can't divide by 0"
        else:
            return a/b

o=Calculator()
v=True
while(v):
    try:
        n1,n2=int(input("Enter first number ")),int(input("Enter second number "))
    except:
        print("invalid value ")
        continue
    sign=input("Enter +,-,*,/ ,s for stop")
    if(sign.lower()=="s"):
        break
    if(sign=="+"):
        print("Addition ",o.add(n1,n2))
    elif(sign=="-"):
        print("Subtract ",o.sub(n1,n2))
    elif(sign=="*"):
        print("Multiply ",o.multi(n1,n2))
    elif(sign=="/"):
        print("Divide ",o.divide(n1,n2))
    else:
        print("Invalid selection")