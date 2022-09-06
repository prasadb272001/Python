#print("hello Boy")
 # Variables
#x=str(3)
#y=int(3)
#z=float(3)
#print(x)    # x will be '3' , "3"
#print(y)    # x will be 3
#print(z)    # x will be 3.0
#print(type(x)) 
#print(type(y))
#print(type(z))

#Defining Variables
#num=10
#my_name="Micheal"
#print(num)
#print(my_name)

#Undefined variables
#2my="Jhon"
#my-var="Jhon"
#my var="John"

#CAMEL CASE ---> myVariableName
#Pascal Case--->MyVariableName
#Snake Case--->my_variable_name

#mutiple values to a variavles
#x,y,z="abs","bbb","ccc"
#print(x)
#print(y)
#print(z)

#x=y=z="aaa"
#print(x)
#print(y)
#print(z)

#fruits=["Apples","bananas","mango"]
#x,y,z,=fruits
#print(x)
#print(y)
#print(z)

#x="python"
#y="abx"
#print(x,y)
#print(x+y)


#x=99
#y=88
#print(x+y)
#print(x*y)
#print(x-y)
#print(x/y)

#global aiable
#x="pyton"
#def fun):
#    prit("I" +x)
#fun()

#Data types

#a="Hello"
#b=20
#c=20.5
#d=1j
#e=["apple","mango"]    
#f=("apple","mango")
#g=range(6)
#h={"name":"M","Post":"g"}
#print(type(a))    
#print(type(b))
#print(type(c))
#print(type(d))
#print(type(e))
#print(type(f))
#print(type(g))
#print(type(h))


#Conditional Statements
#a=1
#b=1
#if a==b:
#    print("the given values are equal")
#elif a>=b:
#    print("a is grater than b")
#else:
#    print("they are not equal")


#Loops
#i=1
#while i<6:
#    print(i)
#    if i==2:
#        break
#    i+=1

#For Loops
#Fruits =["apple","mango"] 
#for x in Fruits :
#   print(x)

#for x in Fruits :
#   print(x)

#Fruits =["apple","mango"] 
#for x in Fruits :
#   if x=="mango":
#        continue
#   print(x)

#for x in range(8):
#    print(x)
#else:
#    print("range is completed")

    #Nested loops

#color=["Yellow","green","red"]    
#fruits=["mango","apple","watermelon"]
#for x in color:
#    for y in fruits:
#        print(x,y)


#Tuples
#mytuple=("apple","cherry","mango","orange")
#print(len(mytuple))
#tuple1=("apple",)  #--> mention , to show tuple without , it will show string
#print(type(tuple1))

#tuple1=("apple","mango","cherry")  #str
#tuple2=(1,2,3) #int
#tuple3=(True,False,True) #bool
#my_tuple=("apple",1,"orange",2)
#print(type(my_tuple))

# Lists

#my=["apple","mango"]
#print(type(my))
#print(my)

#list1=["apple","mango","cherry"]  #str
#list2=[1,2,3] #int
#list3=[True,False,True] #bool

#mylist=list(("apple","orange","cherry"))

#list1=["apple","mango","cherry"] 
#print(list1[0])
#print(list1[-2])
#print(list1[1:2])
    
#list1=["apple","mango","cherry"] 
#list3=[1,2,3]
#list1.append("banans")
#list1.insert(0,"zero")
#list1.extend(list3) #---> here we can use tuples also
#list1.remove("mango")
#list1.pop(1)
#del list1[1]
#list1.clear()
#print(list1)

#list1=["apple","mango","cherry"] 
#for i in range(len(list1)):
#    print(list1[i])

#i=0
#while i<len(list1):
#   print(list1[i])
#   i=i+1

#list1.sort()
#list1.sort(reverse=True)
#list1.reverse()
#print(list1)
#list2=list1.copy()
#print(list2)

#list1=["apple","mango","cherry"] 
#list2=[1,2,3]

#list1.append(list2)
#for x in list2:
#    list1.append(x)
#print(list1)

#Dictionaries

#dict1={
#    "brand":"ford",
#    "model":"mu",
#    "year":1964
    
#}

#for x in dict1:
#    print(x)
#    print(dict1[x])

#for x in dict1.values():
#    print(dict1)
    



#print(dict1)
#print(dict1["model"]) #output for single item
#print(len(dict1))
#print(type(dict1['year']))
#x=dict1.keys()
#print(x)
#y=dict1.values()
#print(y)
#z=dict1.items()

#dict1["color"]="blue"
#print(z)


#dict1.update({"year":2021})
#print(dict1)

#del dict1['year']
#print(dict1)
#dict1.clear()
#print(dict1)

#Functions

#def main():
#    print("hello")
#main()

#def fun(fname):
#    print(fname+"re")
#fun("ab")


#Decoraters

#def print_mes(message):
#    greeting="hello"


#    def print_it():
#        print(greeting, message)
#    print_it()
#print_mes("Python")

# def decorater_1(fun1):
#     def execute():
#         print("executing it now")
#         fun1()
#         print("excuted the function")
#     return execute
# def who_are_we():
#     print("we are the coolest living being")
# who_are_we = decorater_1()
# who_are_we()

# def printer():
#     print("Heyy every one")
# def disply_this(function):
#     def inside():
#         print("executing",function.__name__,"function")
#         function()
#         print("finshed execution")
#     return inside
# decorated_function=disply_this(printer)
# decorated_function()


# def disply_this(function):
#     def inside():
#         print("executing",function.__name__,"function")
#         function()
#         print("finshed execution")
#     return 
# #@display_this
# def printer():
#     print("Heyy every one")
# printer()

#Positional Arguements

# def number(n1,n2):
#     sum=n1+n2
#     return sum
# marks=number(5.7,7.1)
# print("result" ,marks)

#Default Arguements

# def marks(n1=20,n2=300):
#     sum=n1+n2
#     return sum
# result=marks(10) 
# print(result)

#Keyword Arguements

# def greeting(name,message):
#     print("Hello",name)
#     print(message)

# greeting("Man","How are you")

# *args 

# def fun(*kids):
#     print("smallest kid "+kids[1])
# fun("aaa","bbb","ccc") 

# kwargs - keyward arguements

# def func(child1,child2,child3,child4):
#     print("cutest child is "+child1)
# func("aaa","ddd","qqq","ccc")

# **Kwargs-->Arbitary keyword arguements

# def my_fun(**kids):
#     print("height of "+kids["fname"]+" is the smallest among all "+kids["lname"])
# my_fun(fname="aa",lname="bb")



