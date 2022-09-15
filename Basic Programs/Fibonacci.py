num=int(input("enter number to print fibonacci "))
starting_value=0
sec_value=1
sum=0
if num<=0:
    print("Entered invalid number")
else:
    print("Fibonacci Sequence")
    for i in range(num):
        print(sum,end=' ')
        starting_value=sec_value
        sec_value=sum
        sum=starting_value +sec_value

