def sort_dictionary(d):
    return dict(sorted(d.items()))

print("Enter array size:")
n=int(input())
i=0
a=[]

print("Enter array elements")
for i in range(n):
    x=int(input())
    a.append(x)
    i=i+1

print("Array elements")
for i in a:
    print(i)
    
print("Count of each element")

count={}

for i in a:
    element_count=0
    element_count=a.count(i)
    count[i]=element_count

print(sort_dictionary(count))
#for key in sorted(count):
    #print(key,count[key])


