z=[10,40,30,20,50]
print(z)
z[2]=99
print(z)
p=[100,123.123,True]
print(p)
print(z[2])
q=[100,200,100,200,300]
print(q)
x=[10,20,30,40,50,60]
print(x)
while True:
    i=int(input("enter the search element"))
    if i in x:
        print("element is found")
        break
    else:
        print("element is not found")