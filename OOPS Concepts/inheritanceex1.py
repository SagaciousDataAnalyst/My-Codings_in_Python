{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "72e072a5",
   "metadata": {},
   "source": [
    "# OOPS"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "425e8cf8",
   "metadata": {},
   "source": [
    "# class,methods,constructor,self,variables,\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac0dcca2",
   "metadata": {},
   "source": [
    "# Class and object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0176da7e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1)  10\n",
      "hi\n",
      "2)  1\n",
      "3)  10\n",
      "4)  1\n",
      "5)  2\n",
      "6)  10\n",
      "7)  1\n",
      "8)  2\n",
      "9)  2\n",
      "10)  10\n",
      "11)  1\n",
      "12)  2\n",
      "13)  3\n"
     ]
    }
   ],
   "source": [
    "class Myclass:\n",
    "    a=10 #{class/static variable}\n",
    "    print(\"1) \",a)\n",
    "    \n",
    "    #{special method called constructor}\n",
    "    def __init__(self):\n",
    "        self.x=1 #{instance variable}\n",
    "        print(\"2) \",self.x)\n",
    "        print(\"3) \",Myclass.a) #{accessing the class/static variable}\n",
    "    \n",
    "    \n",
    "    def f():\n",
    "        print(\"hi\")\n",
    "    f()\n",
    "    #{instance method}\n",
    "    def f1(self):\n",
    "        self.y=2 #{instance variable}\n",
    "        print(\"4) \",self.x)\n",
    "        print(\"5) \",self.y)\n",
    "        print(\"6) \",Myclass.a) #{accessing the class/static variable}\n",
    "        \n",
    "    \n",
    "    #instance method\n",
    "    def f2(self):\n",
    "        self.z=3 #instance variable\n",
    "        print(\"7) \",self.x)\n",
    "        print(\"8) \",self.y)\n",
    "        print(\"9) \",self.y)\n",
    "        print(\"10) \",Myclass.a) #accessing the class/static variable\n",
    "    \n",
    "    \n",
    "\n",
    "#{creating the instance/object to the \"Myclass\"}\n",
    "m=Myclass() #{when you create an instance constructor in automatically invocked(called)}\n",
    "\n",
    "#{calling the methods using instance(only instance methods can be called by instance/object)}\n",
    "m.f1()\n",
    "m.f2()\n",
    "\n",
    "#{accessing the instance variable by using the instance/object}\n",
    "print(\"11) \",m.x)\n",
    "print(\"12) \",m.y)\n",
    "print(\"13) \",m.z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdc84f3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#instance method\n",
    "    def f2(self):\n",
    "        self.z=3 #instance variable\n",
    "        print(\"7) \",self.x)\n",
    "        print(\"8) \",self.y)\n",
    "        print(\"9) \",self.y)\n",
    "        print(\"10) \",Myclass.a) #accessing the class/static variable\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6ed8ea21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "1)  1 2\n",
      "2)  1 2\n",
      "20\n",
      "2\n",
      "3\n",
      "1)  1 2\n",
      "1)  1 2\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    x=20 #static/class variable\n",
    "    print(x)\n",
    "    def __init__(self):\n",
    "        self.a=1 #instance variables\n",
    "        self.b=2\n",
    "        print(\"1) \",self.a,self.b)\n",
    "        \n",
    "    def f(self):\n",
    "#         self.c=5\n",
    "#         print(self.c)\n",
    "        print(\"2) \",self.a,self.b)\n",
    "        print(A.x)\n",
    "        \n",
    "a=A() #creating instance \n",
    "a.f()\n",
    "print(a.b)\n",
    "a.b=3\n",
    "print(a.b)\n",
    "\n",
    "c=A()\n",
    "d=A()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "40896fac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "***********************\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    def __init__(abc,x,y):\n",
    "        abc.x=x\n",
    "        abc.y=y\n",
    "        print(x)\n",
    "        print(y)\n",
    "        \n",
    "a=A(1,2) \n",
    "print(\"***********************\")\n",
    "b=A(3,4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8c5e552",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<__main__.B at 0xdf772b96a0>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class A:\n",
    "    def __init__(self,a):\n",
    "    \n",
    "        print (\"hi\")\n",
    "\n",
    "\n",
    "class B(A):\n",
    "    def __init__(self,a):\n",
    "        self.a=a\n",
    "        print(a)\n",
    "B(2)\n",
    "\n",
    "# class C(B):\n",
    "#     pass\n",
    "# B()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "bfff62a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "1729\n",
      "10\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    x=10\n",
    "    def a():\n",
    "        y=20\n",
    "        print(y)\n",
    "    a()\n",
    "    \n",
    "    def f(self,a):\n",
    "        self.a=a\n",
    "        print(a)\n",
    "        print(A.x)\n",
    "\n",
    "A()\n",
    "A().f(1729)\n",
    "print(A.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4e4f8baf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi Mr. JK\n",
      "so, your  26 ,right?\n"
     ]
    }
   ],
   "source": [
    "class Person:\n",
    "    def __init__(self):\n",
    "        self.name = \"JK\"\n",
    "        self.age = 26\n",
    "    def f(self):\n",
    "        print(\"hi Mr.\",self.name)\n",
    "        print(\"so, your \",self.age,\",right?\")\n",
    "   \n",
    "\n",
    "p1 = Person()\n",
    "p1.f()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "218b0a76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 5\n",
      "2\n",
      "srinivas\n"
     ]
    }
   ],
   "source": [
    "class Class_srinu:\n",
    "    def __init__(self,a,c):\n",
    "        self.a=a\n",
    "        self.c=c\n",
    "        print(self.a ,self.c)\n",
    "    def function(self):\n",
    "        print(\"srinivas\")\n",
    "        \n",
    "    \n",
    "        \n",
    "        \n",
    "a=Class_srinu(2,5)    \n",
    "print(a.a)\n",
    "a.function()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f3c4fc7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "baf22d86",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "368ebb38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "math\n",
      "1729\n",
      "stats\n"
     ]
    }
   ],
   "source": [
    "#Modifing the value of the asttrible by using the obect\n",
    "\n",
    "class Person:\n",
    "  def __init__(self, name, age):\n",
    "    self.name = name\n",
    "    self.age = age\n",
    "\n",
    "p1 = Person(\"math\", 1729)\n",
    "\n",
    "print(p1.name)\n",
    "print(p1.age)\n",
    "p1.name=\"stats\"\n",
    "print(p1.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "cd9ad383",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Person' object has no attribute '__name'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_4812/2696374223.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[0mp1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPerson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"math\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1729\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 13\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mp1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'Person' object has no attribute '__name'"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "restricting the changes in the modifications in the instance var\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "class Person:\n",
    "  def __init__(self, __name, age):\n",
    "    self.__nme = __name\n",
    "    self.age = age\n",
    "\n",
    "p1 = Person(\"math\", 1729)\n",
    "\n",
    "print(p1.__name) # gives erroe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f3d1ea37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "math\n",
      "1729\n",
      "stats\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "It does not have to be named self , you can call it whatever you like,\n",
    "but it has to be the first parameter of any function in the class:\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "class Person:\n",
    "  def __init__(py, name, age):\n",
    "    py.name = name\n",
    "    py.age = age\n",
    "\n",
    "p1 = Person(\"math\", 1729)\n",
    "\n",
    "print(p1.name)\n",
    "print(p1.age)\n",
    "p1.name=\"stats\"\n",
    "print(p1.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7617b1a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1729\n",
      "1729\n",
      "1730\n",
      "1729\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "understanding the instance variables\n",
    "instance variable:whose seperate copy is created in every object/instance\n",
    "\n",
    "\"\"\"\"\n",
    "\n",
    "class A:\n",
    "    def __init__(self):\n",
    "        self.x=1729 #instance var\n",
    "        \n",
    "    def f(self):\n",
    "        self.x+=1\n",
    "\n",
    "a1=A()\n",
    "a2=A()\n",
    "print(a1.x)\n",
    "print(a2.x)\n",
    "\n",
    "a1.f()\n",
    "print(a1.x)\n",
    "print(a2.x)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "683cb708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1729\n",
      "1729\n",
      "1730\n",
      "1730\n",
      "1731\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\"\"\"\n",
    "understanding the class variables\n",
    "class variable:whose single copy is available in every object/instance\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "class A:\n",
    "    x=1729\n",
    "    \n",
    "    #class method \n",
    "    @classmethod   \n",
    "    def f(cls):\n",
    "        cls.x+=1\n",
    "\n",
    "a1=A()\n",
    "a2=A()\n",
    "print(a1.x)\n",
    "print(a2.x)\n",
    "\n",
    "a1.f()\n",
    "print(a1.x)\n",
    "print(a2.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "82a5f4f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
      "11\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "# class variables, accessing the out side\n",
    "\n",
    "class A:\n",
    "    x=10\n",
    "    print(x)\n",
    "print(A.x)\n",
    "A.x+=1\n",
    "print(A.x)\n",
    "print(A.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "615afb44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
      "11\n",
      "11\n",
      "12\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "# class variables, accessing the out side\n",
    "\n",
    "class A:\n",
    "    x=10\n",
    "    print(x)\n",
    "print(A.x)\n",
    "A.x+=1\n",
    "print(A.x)\n",
    "\n",
    "a1=A()\n",
    "print(a1.x)\n",
    "a1.x+=1\n",
    "print(a1.x)\n",
    "a2=A()\n",
    "print(a2.x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dca938c6",
   "metadata": {},
   "source": [
    "# Abstruction "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d2a33544",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "class A():\n",
    "    def __init__(self):\n",
    "        self.x=3\n",
    "        print(self.x)        \n",
    "a=A()\n",
    "print(a.x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e39f1727",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'A' object has no attribute '__x'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_3632/732060014.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__x\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__x\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'A' object has no attribute '__x'"
     ]
    }
   ],
   "source": [
    "#abstruction\n",
    "class A():\n",
    "    def __init__(self):\n",
    "        self.__x=3 #private variable\n",
    "        print(self.__x)        \n",
    "a=A()\n",
    "print(a.__x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4ec66e38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    def __init__(self):\n",
    "        self.x=2\n",
    "        self.__y=3\n",
    "    def f(self):\n",
    "        print(self.x)\n",
    "        print(self.__y)\n",
    "    \n",
    "a=A()\n",
    "a.f()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "798e7da9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'A' object has no attribute '_A__A__y'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_3632/3668017462.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_3632/3668017462.py\u001b[0m in \u001b[0;36mf\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__A__y\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'A' object has no attribute '_A__A__y'"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "class A:\n",
    "    def __init__(self):\n",
    "        self.x=2  #public var\n",
    "        self.__y=3  # private var\n",
    "    def f(self):\n",
    "        print(self.x) \n",
    "        print(self.__A__y)\n",
    "    \n",
    "a=A()\n",
    "a.f()\n",
    "\n",
    "print(a.x)\n",
    "print(a.__A__y) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0a87895e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum is :  3\n",
      "difference is :  -1\n",
      "sum is :  2\n"
     ]
    }
   ],
   "source": [
    "from abc import ABC,abstractmethod\n",
    "\n",
    "class A(ABC):\n",
    "    \n",
    "    @abstractmethod\n",
    "    def x(self,a,b):\n",
    "        pass\n",
    "    \n",
    "class B1(A):\n",
    "    def x(self,a,b):\n",
    "        print(\"sum is : \",a+b)\n",
    "        \n",
    "class B2(A):\n",
    "    def x(self,a,b):\n",
    "        print(\"difference is : \",a-b)\n",
    "        \n",
    "class B3(A):\n",
    "    def x(self,a,b):\n",
    "        print(\"sum is : \",a*b)\n",
    "        \n",
    "\n",
    "B1().x(1,2)\n",
    "B2().x(1,2)\n",
    "B3().x(1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "97b43f88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my car number is :  11\n",
      "maruthi uses usual steering\n",
      "maruthi uses hydraulic breacking system\n"
     ]
    }
   ],
   "source": [
    "from abc import *\n",
    "\n",
    "class Car(ABC):\n",
    "    def __init__(self,rno):\n",
    "        self.rno=rno\n",
    "        \n",
    "    def display(self):\n",
    "        print(\"my car number is : \",self.rno)\n",
    "        \n",
    "    @abstractmethod\n",
    "    def steering(self):\n",
    "        pass \n",
    "    \n",
    "    @abstractmethod\n",
    "    def breacking(self):\n",
    "        pass \n",
    "    \n",
    "class Maruthi(Car):\n",
    "    def steering(self):\n",
    "        print(\"maruthi uses usual steering\")\n",
    "        \n",
    "    def breacking(self):\n",
    "        print(\"maruthi uses hydraulic breacking system\")\n",
    "        \n",
    "m=Maruthi(11)\n",
    "m.display()\n",
    "m.steering()\n",
    "m.breacking()\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c725af53",
   "metadata": {},
   "source": [
    "# Types of methods in class(instance,class,static methods)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "919417b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no of students : 3\n",
      "enter the student name : aaa\n",
      "enter the student marks : 123\n",
      "hi  aaa\n",
      "your marks are  123\n",
      "************************************************\n",
      "enter the student name : bbb\n",
      "enter the student marks : 2324\n",
      "hi  bbb\n",
      "your marks are  2324\n",
      "************************************************\n",
      "enter the student name : cccc\n",
      "enter the student marks : 789\n",
      "hi  cccc\n",
      "your marks are  789\n",
      "************************************************\n"
     ]
    }
   ],
   "source": [
    "# instance method\n",
    "\n",
    "\"\"\"\n",
    "instance methods are the methods which acts upon the instance variables\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "class A:\n",
    "    \n",
    "    #this is constructor\n",
    "    def __init__(self,name,marks):\n",
    "        self.name=name\n",
    "        self.marks=marks\n",
    "        \n",
    "    #this is an instance method \n",
    "    def display(self):\n",
    "        print(\"hi \",self.name)\n",
    "        print(\"your marks are \",self.marks)\n",
    "        \n",
    "        \n",
    "num=int(input(\"enter the no of students : \"))\n",
    "while(i<num):\n",
    "    name=input(\"enter the student name : \")\n",
    "    marks=int(input(\"enter the student marks : \"))\n",
    "\n",
    "    #creating instance of the class \n",
    "    a=A(name,marks)\n",
    "    a.display()\n",
    "    i+=1\n",
    "    print(\"************************************************\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "13d28d43",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/2013575966.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m \u001b[0mn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"how many students : \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     28\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     29\u001b[0m \u001b[1;32mwhile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m<\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1004\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1005\u001b[0m             )\n\u001b[1;32m-> 1006\u001b[1;33m         return self._input_request(\n\u001b[0m\u001b[0;32m   1007\u001b[0m             \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1008\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"shell\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1049\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1050\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1051\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1052\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1053\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#instance methods\n",
    "#accessor and mutator\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "class A:\n",
    "    \n",
    "    #mutator method\n",
    "    def setName(self,name):\n",
    "        self.name=name\n",
    "    \n",
    "    #accessor method\n",
    "    def getName(self):\n",
    "        return self.name\n",
    "    \n",
    "    #mutator method\n",
    "    def setMarks(self,marks):\n",
    "        self.marks=marks\n",
    "        \n",
    "    #accessor method\n",
    "    def getMarks(self):\n",
    "        return self.marks\n",
    "    \n",
    "    \n",
    "n=int(input(\"how many students : \"))\n",
    "i=0\n",
    "while(i<n):\n",
    "    #creating instance\n",
    "    a=A()\n",
    "    name=input(\"Enter name : \")\n",
    "    a.setName(name)\n",
    "    marks=int(input(\"Enter marks : \"))\n",
    "    a.setMarks(marks)\n",
    "    i+=1\n",
    "    \n",
    "    print(\"hi\",a.getName())\n",
    "    print(\"your marks \",a.getMarks())    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "c1c11c76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
      "********************************\n",
      "1\n",
      "10\n",
      "1\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "#class methods\n",
    "\n",
    "\"\"\"\n",
    "class methods are the methods whose work on the class/static variables\n",
    "they work on class level\n",
    "writen using the \"@classmethod\" decorator\n",
    "first parameter is the \"cls\"\n",
    "calling formate is \"class_name.method()\"\n",
    "\"\"\"\n",
    "class A:\n",
    "    x=10\n",
    "    @classmethod\n",
    "    def f(cls):\n",
    "        print(cls.x)\n",
    "\n",
    "A().f()\n",
    "A.f()\n",
    "    \n",
    "    \n",
    "print(\"********************************\")\n",
    "\n",
    "class A:\n",
    "    x=10\n",
    "    @classmethod\n",
    "    def f(cls,y):\n",
    "        print(y)\n",
    "        print(cls.x)\n",
    "\n",
    "A().f(1) # this argument is taken by \"y\"\n",
    "A.f(1)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "636f69d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number to find the squareroot :625\n",
      "suareroot of 625 is 25.0\n"
     ]
    }
   ],
   "source": [
    "#static method\n",
    "\n",
    "\"\"\"\n",
    "static methods are used when some processing is related to the class,\n",
    "but,does not need the  class or its instaces to perform any work\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "import math\n",
    "class A:\n",
    "    #creating thr static method\n",
    "    @staticmethod\n",
    "    def f(x):\n",
    "        return math.sqrt(x)\n",
    "    \n",
    "num=int(input('enter the number to find the squareroot :'))\n",
    "print(\"suareroot of {} is {}\".format(num,A.f(num)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c72018ed",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'salary' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/109612885.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mEmp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"shailaja\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0mMyclass\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/109612885.py\u001b[0m in \u001b[0;36mgetvalues\u001b[1;34m(e)\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mgetvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m         \u001b[0me\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msalary\u001b[0m\u001b[1;33m+=\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m         \u001b[0me\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mEmp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"shailaja\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/109612885.py\u001b[0m in \u001b[0;36mdisplay\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msalary\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msalary\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdisplay\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mid\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0msalary\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mMyclass\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mstaticmethod\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'salary' is not defined"
     ]
    }
   ],
   "source": [
    "class Emp:\n",
    "    def __init__(self,id,name,salary):\n",
    "        self.id=id\n",
    "        self.name=name\n",
    "        self.salary=salary\n",
    "    def display(self):\n",
    "        print(self.id,self.name,self,salary)\n",
    "class Myclass:\n",
    "    @staticmethod\n",
    "    def getvalues(e):\n",
    "        e.salary+=1000\n",
    "        e.display()\n",
    "        \n",
    "e=Emp(11,\"shailaja\",1000)\n",
    "Myclass.getvalues(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15101c7c",
   "metadata": {},
   "source": [
    "# inner class and outter class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "040874b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11 shailaja\n",
      "my dob is : 22/12/2000 \n"
     ]
    }
   ],
   "source": [
    "#inner class \n",
    "\n",
    "class Outterclass:\n",
    "    def __init__(self,Id,name):\n",
    "        self.Id=Id\n",
    "        self.name=name\n",
    "        self.ic=self.Innerclass()\n",
    "    def display(self):\n",
    "        print(self.Id,self.name)\n",
    "        \n",
    "    class Innerclass:\n",
    "        def __init__(self):\n",
    "            self.dd=22\n",
    "            self.mm=12\n",
    "            self.yyyy=2000\n",
    "        def display(self):\n",
    "            print(\"my dob is : {}/{}/{} \".format(self.dd,self.mm,self.yyyy))\n",
    "            \n",
    "o=Outterclass(11,\"shailaja\")\n",
    "o.display()\n",
    "\n",
    "i=o.ic\n",
    "i.display()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4992cbaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is outter class\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'B' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/2328592327.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 13\u001b[1;33m \u001b[0mb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mB\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     14\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'B' is not defined"
     ]
    }
   ],
   "source": [
    "#inner class\n",
    "\n",
    "class A:\n",
    "    def display(self):\n",
    "        print(\"this is outter class\")\n",
    "    \n",
    "    class B:\n",
    "        def display(self):\n",
    "            print(\"this is inner class\")\n",
    "            \n",
    "a=A()\n",
    "a.display()\n",
    "b=A().B() #creating the B class obeject as a sub object to the A class\n",
    "b.display()\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c969172",
   "metadata": {},
   "source": [
    "# inheritance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03beb7a5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d7982de8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John Doe\n",
      "Mike Olsen\n"
     ]
    }
   ],
   "source": [
    "class Person:\n",
    "  def __init__(self, fname, lname):\n",
    "    self.firstname = fname\n",
    "    self.lastname = lname\n",
    "\n",
    "  def printname(self):\n",
    "    print(self.firstname, self.lastname)\n",
    "\n",
    "#Use the Person class to create an object, and then execute the printname method:\n",
    "\n",
    "x = Person(\"John\", \"Doe\")\n",
    "x.printname()\n",
    "\n",
    "class Student(Person):\n",
    "  pass\n",
    "x = Student(\"Mike\", \"Olsen\")\n",
    "x.printname()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "400bcc0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "class A:\n",
    "    def setDetails(self,Id,Name,Marks):\n",
    "        self.Id=Id\n",
    "        self.name=Name\n",
    "        self.Marks=Marks\n",
    "    def getDetails(self):\n",
    "        print(\"hi {} , your Id is {}, and you got {} in this exam\".format(self.Id,self.Name,self.Marks))\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "88e706e7",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'true' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_2960/478566532.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0minheritanceex1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mA\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msetDetails\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"shailaja\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetDetails\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\My Files\\inheritanceex1.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     30\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"0176da7e\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m    \"metadata\": {\n\u001b[1;32m---> 32\u001b[1;33m     \u001b[1;34m\"scrolled\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mtrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     33\u001b[0m    },\n\u001b[0;32m     34\u001b[0m    \"outputs\": [\n",
      "\u001b[1;31mNameError\u001b[0m: name 'true' is not defined"
     ]
    }
   ],
   "source": [
    "import inheritanceex1\n",
    "a=A()\n",
    "a.setDetails(11,\"shailaja\",11)\n",
    "a.getDetails()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c5735712",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi\n",
      "hi\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    def f(self):\n",
    "        print(\"hi\")\n",
    "        \n",
    "class B:\n",
    "    def f(self):\n",
    "        print(\"hello\")\n",
    "        \n",
    "class C(A,B):\n",
    "    pass\n",
    "c=C()\n",
    "c.f()\n",
    "c.f()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6db17e3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.B at 0x14fa285310>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class A:\n",
    "    def __init__(self):\n",
    "        print(\"hi\")\n",
    "class B:\n",
    "    pass\n",
    "\n",
    "B()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6df15223",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "hello hello\n"
     ]
    }
   ],
   "source": [
    "#overriding\n",
    "\n",
    "class A:\n",
    "    def __init__(self):\n",
    "        print(\"hi\")\n",
    "        \n",
    "    def f(self):\n",
    "        print(\"hi hi\")\n",
    "        \n",
    "class B(A):\n",
    "    def __init__(self):\n",
    "        print(\"hello\")\n",
    "        \n",
    "    def f(self):\n",
    "        print(\"hello hello\")\n",
    "\n",
    "B().f()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1aa6dc81",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
