{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "72e072a5",
   "metadata": {},
   "source": [
    "# class and object"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63e3ba26",
   "metadata": {},
   "source": [
    "# class,methods,constructor,self,variables,\n",
    "#"
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
       "<__main__.B at 0x2a934a0130>"
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
    "        se\n",
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
   "execution_count": 30,
   "id": "a0318294",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi\n"
     ]
    }
   ],
   "source": [
    "class Myclass:\n",
    "    print(\"hi\")"
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
   "execution_count": 13,
   "id": "91b90fe1",
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
    "    def __init__(self, name, age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "    def f(self):\n",
    "        print(\"hi Mr.\",self.name)\n",
    "        print(\"so, your \",self.age,\",right?\")\n",
    "   \n",
    "\n",
    "p1 = Person(\"JK\", 26)\n",
    "p1.f()\n",
    "\n"
   ]
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
   "execution_count": 36,
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
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_6776/1619797905.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[0mp1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPerson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"math\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1729\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 13\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mp1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     14\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mp1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mage\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[0mp1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"stats\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
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
    "print(p1.__name)\n",
    "print(p1.age)\n",
    "p1.__name=\"stats\"\n",
    "print(p1.__name)"
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
   "id": "80149ba2",
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
   "execution_count": 19,
   "id": "e8bbbe01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
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
    "print(A.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b948d05d",
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
    "        self.__x=3\n",
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
    "print(a.__A__y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6ea4a036",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sum is :  3\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "operations() missing 1 required positional argument: 'b'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\SHAILA~1\\AppData\\Local\\Temp/ipykernel_3000/1536635568.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mB\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m \u001b[0mB\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moperations\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     28\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     29\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mC\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: operations() missing 1 required positional argument: 'b'"
     ]
    }
   ],
   "source": [
    "from abc import ABC,abstractmethod\n",
    "class Math(ABC):\n",
    "    @abstractmethod\n",
    "    def operations(self,a,b):\n",
    "        pass\n",
    "    \n",
    "class A(Math):\n",
    "    def operations(self,a,b):\n",
    "        print(\"sum is : \",a+b)\n",
    "        \n",
    "class B(Math):\n",
    "    def operations(self,a,b):\n",
    "        print(\"difference is : \",a-b)\n",
    "        \n",
    "class C(Math):\n",
    "    def operations(self,a,b):\n",
    "        print(\"multiplication is : \",a*b)\n",
    "        \n",
    "class D(Math):\n",
    "    def operations(self,a,b):\n",
    "        print(\"division is : \",a/b)\n",
    "        \n",
    "a=A()\n",
    "a.operations(1,2)\n",
    "    \n",
    "b=B()\n",
    "B.operations(1,2)\n",
    "\n",
    "c=C()\n",
    "c.operations(1,2)\n",
    "\n",
    "d=D()\n",
    "d.operations(1,2)\n"
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
