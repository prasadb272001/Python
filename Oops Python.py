#Arrays --> Like Functions

# cars=["BMW","Honda"]
# x=len(cars)
# cars.append("Volvo")
# print(cars)

# cars.pop(1)
# print(cars)

#Class & Objects

# class Myclass:
#     x=5
# p1=Myclass()
# print(p1.x)

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=People("Amogh","19")

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def myFunc(self):
#         print("Hello my name is "+self.name)
#         print("Hello my age is "+self.age)
# p1=Person("Munny","19")
# p1.myFunc()
  

# #Parametrized Constructor
# class vinni:
#     def __init__(self,name,id):
#         self.name= name
#         self.id= id
#     def display(self):
#         print("name&id",self.name,self.id)
# s1=vinni(1,"xyz")
# s1.display()


#Default Constructor or Non Parametrized constructor

# class vinni:
#     def __init__(self):
#         print("Non parametrized")
#     def display(self,name):
#         print("name",name)
# s1=vinni()
# s1.display("xyz")

#Encapsulation and abstraction

# class vinni():
#     def __init__(self):
#         self.__id=100
#     def display(self):
#         print("ID",self.__id)
# s1=vinni()
# s2=vinni()
# s2.__id=101
# s1.display()
# s2.display()

# class vinni():
#     def __init__(self):
#         self.__id=100
#     def display(self):
#         print("ID",self.__id)
#     def setID(self,id):
#         self.__id=id
# s1=vinni()
# s2=vinni()
# s2.setID(101)
# s1.display()
# s2.display()

#single inheritance

# class Parent:
#     def fun1(self):
#         print("This is the parent class")
# class Child(Parent):
#     def fun2(self):
#         print("This is the child class")

# s1=Child()
# s1.fun1()
# s1.fun2()

#Multilevel inheritances

# class Parent:
#     def fun1(self):
#         print("This is the parent class")
# class Child(Parent):
#     def fun2(self):
#         print("This is the child class")
# class Child2(Child):
#     def fun3(self):
#         print("this is the 2nd child")

# s1=Child2()
# s1.fun1()
# s1.fun2()
# s1.fun3()

#Multiple inheritance

# class Parent:
#      def fun1(self):
#          print("This is the parent class")
# class Child:
#      def fun2(self):
#          print("This is the child class")
# class Child1(Parent,Child):
#      def fun3(self):
#          print("this is the 2nd child")

# d=Child1()
# d.fun1()
# d.fun2()
# d.fun3()

#Hybrid Inheritance

# class Parent:
#      def fun1(self):
#          print("This is the parent class")
# class Child(Parent):
#      def fun2(self):
#          print("This is the child class")
# class Child1(Parent):
#      def fun3(self):
#          print("this is the 2nd child")

# d=Child()
# d1=Child1()
# d.fun1()
# d.fun2()
# d1.fun1()
# d1.fun3()




