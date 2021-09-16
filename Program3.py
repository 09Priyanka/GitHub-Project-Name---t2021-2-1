
print("Enter 'a' value:")
n=int(input())
i=0
j=0
a=[]


for i in range(n*2):
    if(i%2!=0):
        a.append(i)
    i=i+1
    
print("Odd number series:")

if(n%2==0):
    a=a[:-1]
    for j in a:
        print(j)
else:
    for j in a:
        print(j)
    
   