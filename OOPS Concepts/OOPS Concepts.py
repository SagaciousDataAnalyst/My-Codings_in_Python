#!/usr/bin/env python
# coding: utf-8

# # OOPS(bject Orianted Programming System)

# ## class, object,inheritance,abstraction,polymorphism
# 

# ### Class and object

# In[1]:


# program to create a class

class Myclass:  #Creating the class
    print("Myclass")


# In[2]:


# program to create an object/instance of the class

class Myclass:  #Creating the class
    print("Myclass")
    
Myclass()  # creating the object/instance(The process of creating the object/instance is known as "Instantation")


# In[3]:


# program to understand the constructor

class Myclass:
    def __init__(self):   # it is the constructor to construct the objects,it invokes automatically when we creat an object/instance. 
        print("hi.......")          #(if you did not create object/instance constructor doesn't invokes)
        
        
        


# In[ ]:


# program to understand that, a constructor can only called/invoked when object/instance is created

class Myclass:
    def __init__(self):   # it is the constructor to construct the objects,it invokes automatically when we creat an object/instance. 
        print("hi.......")          #(if you did not create object/instance constructor doesn't invokes)
        
Myclass()  # creating the object/instance       
        


# In[5]:


# program to pass arguments to the parameters of the constructor

class Myclass:
    def __init__(self,a,b):  # constructor with the parameters. we have to pass arguments to this parameter when we create an object/instance
        print(a,b)  # in this case " a " and " b " are the local variables
        
Myclass(10,20)  #craeting the object/instance and passing arguments to the constructor
        


# In[9]:




class Myclass:
    def __init__(self,a,b):  # constructor with the parameters. we have to pass arguments to this parameter when we create an object/instance
        self.a=a  # creating the instance variable "a"
        self.b=b  # creating the instance variable "b"
        print(self.a,self.b)
        
m=Myclass(20,30)  #craeting the object/instance and passing arguments to the constructor

        


# In[12]:


class Myclass:
    def __init__(self,a,b,c):  # constructor with the parameters. we have to pass arguments to this parameter when we create an object/instance
        self.a=a  # creating the instance variable "a"
        self.b=b  # creating the instance variable "b"
        print(a,b,c) # were, "a" and "b" are local variables
        print(self.a,self.b)
        
m=Myclass(20,30,40)  #craeting the object/instance and passing arguments to the constructor

       


# In[7]:


class A:
    x=20 #static/class variable
    print(x)
    def __init__(self):
        self.a=1 #instance variables
        self.b=2
        print("1) ",self.a,self.b)
        
    def f(self):
#         self.c=5
#         print(self.c)
        print("2) ",self.a,self.b)
        print(A.x)
        
a=A() #creating instance 
a.f()
print(a.b)
a.b=3
print(a.b)

c=A()
d=A()



# In[48]:


class A:
    def __init__(abc,x,y):
        abc.x=x
        abc.y=y
        print(x)
        print(y)
        
a=A(1,2) 
print("***********************")
b=A(3,4)


# In[1]:


class A:
    def __init__(self,a):
    
        print ("hi")


class B(A):
    def __init__(self,a):
        self.a=a
        print(a)
B(2)

# class C(B):
#     pass
# B()


# In[28]:


class A:
    x=10
    def a():
        y=20
        print(y)
    a()
    
    def f(self,a):
        self.a=a
        print(a)
        print(A.x)

A()
A().f(1729)
print(A.x)


# In[33]:


class Person:
    def __init__(self):
        self.name = "JK"
        self.age = 26
    def f(self):
        print("hi Mr.",self.name)
        print("so, your ",self.age,",right?")
   

p1 = Person()
p1.f()


# In[22]:


class Class_srinu:
    def __init__(self,a,c):
        self.a=a
        self.c=c
        print(self.a ,self.c)
    def function(self):
        print("srinivas")
        
    
        
        
a=Class_srinu(2,5)    
print(a.a)
a.function()


# In[ ]:





# In[ ]:





# In[12]:


#Modifing the value of the asttrible by using the obect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("math", 1729)

print(p1.name)
print(p1.age)
p1.name="stats"
print(p1.name)


# In[1]:


"""
restricting the changes in the modifications in the instance var

"""

class Person:
    def __init__(self, __name, age):
        self.__nme = __name
        self.age = age

p1 = Person("math", 1729)
print(p1.age)

print(p1.__name) # gives error


# In[37]:


"""
It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:

"""

class Person:
  def __init__(py, name, age):
    py.name = name
    py.age = age

p1 = Person("math", 1729)

print(p1.name)
print(p1.age)
p1.name="stats"
print(p1.name)


# In[5]:


"""
understanding the instance variables
instance variable:whose seperate copy is created in every object/instance

""""

class A:
    def __init__(self):
        self.x=1729 #instance var
        
    def f(self):
        self.x+=1

a1=A()
a2=A()
print(a1.x)
print(a2.x)

a1.f()
print(a1.x)
print(a2.x)


# In[31]:



"""
understanding the class variables
class variable:whose single copy is available in every object/instance

"""

class A:
    x=1729
    
    #class method 
    @classmethod   
    def f(cls):
        cls.x+=1

a1=A()
a2=A()
print(a1.x)
print(a2.x)

a1.f()
print(a1.x)
print(a2.x)


# In[29]:


# class variables, accessing the out side

class A:
    x=10
    print(x)
print(A.x)
A.x+=1
print(A.x)
print(A.x)


# In[25]:


# class variables, accessing the out side

class A:
    x=10
    print(x)
print(A.x)
A.x+=1
print(A.x)

a1=A()
print(a1.x)
a1.x+=1
print(a1.x)
a2=A()
print(a2.x)


# # Abstruction 

# In[11]:


class A():
    def __init__(self):
        self.x=3
        print(self.x)        
a=A()
print(a.x)


# In[4]:


#abstruction
class A():
    def __init__(self):
        self.__x=3 #private variable
        print(self.__x)        
a=A()
print(a._A__x)  # name namgling


# In[3]:


class A:
    def __init__(self):
        self.x=2
        self.__y=3
    def f(self):
        print(self.x)
        print(self.__y)
    
a=A()
a.f()
print(a._A__y) # name namgling


# In[15]:




class A:
    def __init__(self):
        self.x=2  #public var
        self.__y=3  # private var
    def f(self):
        print(self.x) 
    
    
a=A()
a.f()

print(a.x)
print(a._A__y) 


# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class. 
# 
# 
# Why use Abstract Base Classes : 
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes in your mind is difficult or not possible. 
# 
# 
# How Abstract Base classes work : 
# By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

# In[2]:


from abc import ABC,abstractmethod

class A(ABC):
    
    @abstractmethod
    def x(self,a,b):
        pass
    
class B1(A):
    def x(self,a,b):
        print("sum is : ",a+b)
        

class B2(A):
    def x(self,a,b):
        print("difference is : ",a-b)
        
class B3(A):
    def x(self,a,b):
        print("sum is : ",a*b)
        

B1().x(1,2)
B2().x(1,2)
B3().x(1,2)


# In[9]:


class A:
    def f(self):
        x=13
        print(x)
       
class B(A):
    def f(self):
        x=1
        print(x)
B().f()


# In[13]:


class A:
    def f(self):
        x=10
        print(x)
        
    def f(self,x):
        self.x=20
        print(self.x)
        
    def f(self,x,y):
        self.x=x
        self.y=y
        print(self.x,self.y)
        
        
A().f(1,2)
       
       
       


# In[ ]:





# In[2]:


from abc import *

class Car(ABC):
    def __init__(self,rno):
        self.rno=rno
        
    def display(self):
        print("my car number is : ",self.rno)
        
    @abstractmethod
    def steering(self):
        pass 
    
    @abstractmethod
    def breaking(self):
        pass 
    
class Maruthi(Car):
    def steering(self):
        print("maruthi uses usual steering")
        
    def breaking(self):
        print("maruthi uses hydraulic breacking system")
        
m=Maruthi(11)
m.display()
m.steering()
m.breaking()
    


# In[16]:


class A:
    def __init__(self):
        print("A class")
        
class B(A):
    def __init__(self):
        super().__init__()

B()


# # Types of methods in class(instance,class,static methods)

# In[3]:


# instance method

"""
instance methods are the methods which acts upon the instance variables

"""

class A:
    
    #this is constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    #this is an instance method 
    def display(self):
        print("hi ",self.name)
        print("your marks are ",self.marks)
        
        
num=int(input("enter the no of students : "))
while(i<num):
    name=input("enter the student name : ")
    marks=int(input("enter the student marks : "))

    #creating instance of the class 
    a=A(name,marks)
    a.display()
    i+=1
    print("************************************************")


# In[3]:


#instance methods
#accessor and mutator

"""

"""

class A:
    
    #mutator method
    def setName(self,name):
        self.name=name
    
    #accessor method
    def getName(self):
        return self.name
    
    #mutator method
    def setMarks(self,marks):
        self.marks=marks
        
    #accessor method
    def getMarks(self):
        return self.marks
    
    
n=int(input("how many students : "))
i=0
while(i<n):
    #creating instance
    a=A()
    name=input("Enter name : ")
    a.setName(name)
    marks=int(input("Enter marks : "))
    a.setMarks(marks)
    i+=1
    
    print("hi",a.getName())
    print("your marks ",a.getMarks())    
        


# In[72]:


#class methods

"""
class methods are the methods whose work on the class/static variables
they work on class level
writen using the "@classmethod" decorator
first parameter is the "cls"
calling formate is "class_name.method()"
"""
class A:
    x=10
    @classmethod
    def f(cls):
        print(cls.x)

A().f()
A.f()
    
    
print("********************************")

class A:
    x=10
    @classmethod
    def f(cls,y):
        print(y)
        print(cls.x)

A().f(1) # this argument is taken by "y"
A.f(1)    


# In[2]:


#static method

"""
static methods are used when some processing is related to the class,
but,does not need the  class or its instaces to perform any work

"""

import math
class A:
    #creating thr static method
    @staticmethod
    def f(x):
        return math.sqrt(x)
    
num=int(input('enter the number to find the squareroot :'))
print("suareroot of {} is {}".format(num,A.f(num)))


# In[16]:


class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print(self.id,self.name,self,salary)
class Myclass:
    @staticmethod
    def getvalues(e):
        e.salary+=1000
        e.display()
        
e=Emp(11,"Jk",1000)
Myclass.getvalues(e)


# # inner class and outter class

# In[12]:


#inner class 

class Outterclass:
    def __init__(self,Id,name):
        self.Id=Id
        self.name=name
        self.ic=self.Innerclass()
    def display(self):
        print(self.Id,self.name)
        
    class Innerclass:
        def __init__(self):
            self.dd=22
            self.mm=12
            self.yyyy=2000
        def display(self):
            print("my dob is : {}/{}/{} ".format(self.dd,self.mm,self.yyyy))
            
o=Outterclass(11,"shailaja")
o.display()

i=o.ic
i.display()


# In[21]:


#inner class

class A:
    def display(self):
        print("this is outter class")
    
    class B:
        def display(self):
            print("this is inner class")
            
a=A()
a.display()
#A().B().display()

b=A().B() #creating the B class obeject as a sub object to the A class
b.display()
A().B().display()
        


# # inheritance

# In[ ]:





# In[26]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("Mr", "X")
# x.printname()

class Student(Person):
  pass
y = Student("Mr", "Y")
y.printname()


# In[9]:


class A:
    def __init__(self,x):
        self.x=x
        
    def f(self):
        print(self.x) 
        
    def g():
        print("I am g method")
    g()
        
        
a=A(23)
a.f()


# In[7]:


class A:
    def __init__(self):
        print("hi")
A()


# In[28]:


class A:
    def __init__(self):
        self.Id=11
        self.name='SHAILAJA'
        self.Marks=11
    def getDetails(self):
        print("hi {} , your Id is {}, and you got {} in this exam".format(self.Name,self.Id,self.Marks))
        
class B(A):
#     def __init__(self):
#         super().__init__()
#         self.age=21
    pass
        

B().getDetails()

"""
getting error...., WHY?????????????????

"""


# In[11]:


"""
CASE(1): If a sub_class does not have the constructor, then when we create a object to the sub_class,
then the super_class constructor automatically invocked.

CASE(2): but, if you have constructor in the sub_class , then when we ctreate object to the sub_class,
then it invock the sub_class constructor only but not super class.

CASE(3): In this case to access the super_class constructor when we have sub_class constructor too, we 
have to use "super()" method.

"""

print("CASE(1)")

class A:
    def __init__(self):
        print("hi")
    
class B(A):
    pass
B()

print("*************************************")

print("CASE(2)")
class A:
    def __init__(self):
        print("hi")
    
class B(A):
    def __init__(self):
        print("hello")
        
B()

print("*************************************")

print("CASE(3)")
class A:
    def __init__(self):
        print("hi")
    
class B(A):
    def __init__(self):
        super().__init__()
        print("hello")
        
B()


# In[5]:


#the super method

class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self,a,b): # "b" is sub_class constructor parameter,"a" is super_class constructor parameter
        super().__init__(a) #calling super class constructor
        self.b=b #initializing the sub_class constructor parameter
        
    def f(self):
        print(self.a,self.b)
        
b=B(1,2)
b.f()


# In[3]:


class A:
    def __init__(self):
        print("A class")
        super().__init__()

class B:
    def __init__(self):
        print("B class")
    
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C class")
        
C()


# In[16]:


class A:
    def __init__(self):
        print("A class")
        super().__init__()

class B:
    def __init__(self):
        super().__init__()
        print("B class")
        
    
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C class")
        
C()


# In[3]:


class car():
    def wheel(self):
        self.run()
    def run(self):
        print("done")
        pass
    def milege(self):
        return str(120/0)
c = car()
c.wheel()


# In[17]:


class A:
    def __init__(self):
        print("A class ")
        super().__init__()
        
class B:
    def __init__(self):
        print("B class ")
        super().__init__()
    
        
class C:
    def __init__(self):
        print("C class ")

        
class D(A,B,C):
    def __init__(self):
        print("D class ")
        super().__init__()
        
        
        
D()


# In[21]:


class A:
    def __init__(self):
        print("A class")


class B(A):
    def __init__(self):
        print("B class")
        
    
class C(B):
#     def __init__(self):
#         print("C class")
            pass
        
C()
B()


# In[15]:


class Car:   
    def __init__(self):    
        self.x=10                
        print("Car object")       
        
class BMW(Car):                  
    def __init__(self):
        self.x=20
        print("BMW object")
        
class BMW_3_series(BMW):      
    pass

class BMW_7_series(BMW):        
    def __init__(self):
        self.x=30
        super().__init__()      
        print("BMW_7_series object")
        
class Benz(Car):
    def __init__(self):
        print("Benz objec")
        self.x=40
        super().__init__()
        
class Test(Benz,BMW_7_series,BMW_3_series):
    def __init__(self):
        self.x=50
        super().__init__()
        print("Test objec")
        
        
t=Test()
print(t.x)


# # Polymorphism
# 
# we have two types of concepts in polymorphism : 
# 1) Method overloading ( does not supported by the python).
# 2) Method overriding  ( does not supported by the python) 

# """
# Method Overriding : -
# 
# Method overriding is a concept of object oriented programming that allows us to change the implementation of a function in the child class that is defined in the parent class. It is the ability of a child class to change the implementation of any method which is already provided by one of its parent class
# 
# """

# In[29]:


# program to understand Method overriding

class Parent:
    def display(self): # overrided
        print(" I am in parent class....")
        
class Child:
    def display(self):  #overriding
        print(" I am in child class....")
        
Child().display()


# In[ ]:





# # Class

# In[ ]:





# In[27]:


class Myclass:             # defining the class
    x=20                   # class/static variable
    print("1) ",x)
    def f():               # defining the metho(class/static method)
        x=30               # local variable
        print("2) ",x)
        print("3) ",Myclass.x)  # accessing the class variable inside the method
    print("4) ",x)
    f()                    # function  calling
    
    
    def g(self):         # instance method
        self.x=40        # instance variable
        print("5) ",self.x)
    
    
Myclass() # creating an object or instance(instatation)
m=Myclass()
m.g()
m.x=41
print("6) ",m.x)

m1=Myclass()
m2=Myclass()
m3=Myclass()


# In[30]:


print("hi")


# In[28]:





# In[20]:


# constructor

class A:

    def __init__(self,name,age):   # constructor(used to construct the objects OR to initialize the variables)
        self.name=name  
        self.age=age
        print("I had initialized my variables")
        
    def f(self,x): 
        self.x=x
        print(self.x)
        print(self.name,"is ",self.age," years old.")
        
    def g(self):
        print("hi",self.name)
        
        
a=A("Mr.X",21)
a.g()
a.f(23)



# In[18]:


class A:
    def __init__(self):
        self.x=1
        self.y=2
        
    def f(self):
        print(self.x,self.y)
        
    
a=A()
a.f()


# In[22]:


"""
Inheritance: acquiring the propertice of the one class to another class

"""

class A:
     def __init__(self):   # constructor(used to construct the objects OR to initialize the variables)
        self.name="Mr.X"  
        self.age=21
        print("I had initialized my variables")
        
    
class B(A):
    print(self.name)
    
B()
    

    
    


# In[24]:


x=10
print("x")
print(x)


# In[15]:


class A:    # parent/super/base class
    def __init__(self):
        print("A class")
        
class B(A):  # child/sub/derived class
    def __init__(self):
        print("B class")
        super().__init__()

B()


# In[1]:


class A:
    def __init__(self):
        print("hi")
        
A(A(A()))


# In[2]:


class A:
    def __init__(self,a):
        print("hi")
        
A(A(A(1)))


# In[3]:


class A:
    def __init__(self,a):
        print(a)
A(A(A(12)))


# In[4]:


class A:
    def __init__(self,a):
        print(a)
        print("hhi")
A(A(A(12)))


# In[5]:


class A:
    def __init__(self,a):
        print(a)
        
    def __str__(self):
        return "hi"
    
A(A(A(12)))


# In[6]:


class A:
    def __init__(self,a):
        print(a)
        
    def __str__(self):
        return "hi"
    
print(A(A(A(12))))


# In[7]:


class A:
    def __init__(self):
        print("hi")
        
    def __str__(self):
        return "hello"
        
print(A())


# In[ ]:





# In[3]:


class A:
    def __init__(self):
        self.f()
        
    def f(self):
        print("hello")

        
A()


# In[14]:


class A:
    def f(self):
        self.g()
        self.h()
        
    def g(self):
        print("I am g() method")
        
    def h(self):
        print("I am h() method")
        
class B(A):
    A().f()


# In[16]:


class A:
    def __init__(self):
        print("@".join("Data"))
        
A()


# In[19]:


def gen():
    yield 0
    yield i
    yield 3
        
for i in gen():
    print(next())


# In[ ]:




