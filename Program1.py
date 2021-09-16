class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def addition(self):
        res=0
        res=self.a+self.b
        print (res)
    
    def substraction(self):
        res=0
        res=self.a-self.b
        print (res)
        
    
    def multiplication(self):
        res=0
        res=self.a*self.b
        print (res)
    
    def division(self):
        res=0
        res=self.a/self.b
        print (res)
    
    def default(self):
        print("Invalid Operation")
        

print("Enter 2 numbers")
a=float(input())
b=float(input())
c=calculator(a,b)

print("If you want to perform Addition operation then type 'Addition'")
print("If you want to perform Substraction operation then type 'Substraction'")
print("If you want to perform Multiplication operation then type 'Multiplication'")
print("If you want to perform Division operation then type 'Division'")
print("Enter Arthimatic Operation")
operation=input()

if(operation=='Addtion'):
    c.addition()

elif(operation=='Substraction'):
    c.substraction()

elif(operation=='Multiplication'):
    c.multiplication()

elif(operation=='Division'):
    c.division()

else:
    c.default()
    


        


    
    
