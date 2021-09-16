print("Enter 'a' value:")
n=int(input())
i=0
a=[]


for i in range(n*2):
    if(i%2!=0):
        a.append(i)
    i=i+1
    
print("Odd number series:")

for i in a:
    print(i)
    