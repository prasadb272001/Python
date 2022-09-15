n=int(input("enter the fibnocci number "))
def fibnocii(a,b,n):
    if n==0:
        return
    c=a+b
    print(c)
    fibnocii(b,c,n-1)
a=0
b=1
print(a)
print(b)
fibnocii(a,b,n-2)
