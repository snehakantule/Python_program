n1=0
n2=1
count=10
print(n1,n2,end=" ")
for i in range(2,count):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()