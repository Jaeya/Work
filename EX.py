Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print("Hello python")
Hello python
>>> 2 *3
6
>>> 2**10
1024
>>> print 김유림?
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(김유림?)?
>>> print ("김유림")
김유림
>>> 
>>> strA = "phyton"
>>> strA
'phyton'
>>> type(strA)
<class 'str'>
>>> len(strA)
6
>>> 
>>> strB ="""
다중으로
문자열ㅇㄹ
저장하기"""
>>> strB
'\n다중으로\n문자열ㅇㄹ\n저장하기'
>>> 
>>> 
>>> print(strB)

다중으로
문자열ㅇㄹ
저장하기
>>> 
>>> strA[0]
'p'
>>> strA[1]
'h'
>>> strA[:3]
'phy'
>>> strA[-1]
'n'
>>> strA[-2:]
'on'
>>> strA[-2]
'o'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'strA', 'strB']
>>> abs()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    abs()
TypeError: abs() takes exactly one argument (0 given)
>>> 
>>> 
>>> 
>>> x = 100
>>> y = 3.14
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'strA', 'strB', 'x', 'y']
>>> 
>>> 
>>> 
>>> colors = ["Red","Blue","Green"]
>>> colors.append("Black")
>>> print colors
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(colors)?
>>> print(colors)
['Red', 'Blue', 'Green', 'Black']
>>> colors.insert(1,"White")
>>> print(colors)
['Red', 'White', 'Blue', 'Green', 'Black']
>>> colors.index("red")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    colors.index("red")
ValueError: 'red' is not in list
>>> print (colors.index("Red"))
0
>>> colors.index("Red")
0
>>> colors.remove("Red")
>>> print(colors)
['White', 'Blue', 'Green', 'Black']
>>> colors.sort()
>>> print(colors)
['Black', 'Blue', 'Green', 'White']
>>> colors.reverse()
>>> print(colors)
['White', 'Green', 'Blue', 'Black']
>>> 
>>> 
>>> 
>>> 
>>> colors = ["red","blue","green"]
>>> colors
['red', 'blue', 'green']
>>> len(colors)
3
>>> colors[0]
'red'
>>> colors[1]
'blue'
>>> colors
['red', 'blue', 'green']
>>> colors.ap
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    colors.ap
AttributeError: 'list' object has no attribute 'ap'
>>> colors.append("white")
>>> colors
['red', 'blue', 'green', 'white']
>>> colors.append("black")
>>> colors
['red', 'blue', 'green', 'white', 'black']
>>> colors.insert(1,"pink")
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'black']
>>> colors.
SyntaxError: invalid syntax
>>> colors.extend(["blue","pink","white"])
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'black', 'blue', 'pink', 'white']
>>> colors += ["red]
	   
SyntaxError: EOL while scanning string literal
>>> colors += ["red"]
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'black', 'blue', 'pink', 'white', 'red']
>>> colors += "red"
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'black', 'blue', 'pink', 'white', 'red', 'r', 'e', 'd']
>>> colors.pop()
'd'
>>> colors.pop()
'e'
>>> colors.pop()
'r'
>>> colors.pop()
'red'
>>> colors.pop(1)
'pink'
>>> colors
['red', 'blue', 'green', 'white', 'black', 'blue', 'pink', 'white']
>>> colors.remove("green")
>>> colors.
SyntaxError: invalid syntax
>>> colors
['red', 'blue', 'white', 'black', 'blue', 'pink', 'white']
>>> colors.index("red")
0
>>> colors.count()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    colors.count()
TypeError: count() takes exactly one argument (0 given)
>>> colors.count("red")
1
>>> colors.reverse()
>>> colors
['white', 'pink', 'blue', 'black', 'white', 'blue', 'red']
>>> colors.sort()
>>> colors
['black', 'blue', 'blue', 'pink', 'red', 'white', 'white']
>>> a ={1,2,3,4}
b
>>> b = {3,4,4,5}
>>> a
{1, 2, 3, 4}
>>> b
{3, 4, 5}
>>> type(a)
<class 'set'>
>>> a.union(b)
{1, 2, 3, 4, 5}
>>> a.intersection(b)
{3, 4}
>>> a.difference(b)
{1, 2}
>>> a | b
{1, 2, 3, 4, 5}
>>> a & b
{3, 4}
>>>   a - b
  
SyntaxError: unexpected indent
>>> a - b
{1, 2}
>>> type()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> tuple()
()
>>> tp = (1,2,3)
>>> len(tp)
3
>>> tp
(1, 2, 3)
>>> type(tp)
<class 'tuple'>
>>> tp[0]
1
>>> tp[1]
2
>>> tp[2]
3
>>> def calc(a,b):
	return a+b , a*b

>>> 
>>> result = calc(3,4)
>>> result
(7, 12)
>>> result[0]
7
>>> result[1`]
SyntaxError: invalid syntax
>>> result[1]
12
>>> d = dict(a=1,b=2,c=3)
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>> type(d)
<class 'dict'>
>>> color = {"apple":"red","banana":"yellow"}
>>> color
{'apple': 'red', 'banana': 'yellow'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dict[1]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    dict[1]
TypeError: 'type' object is not subscriptable
>>> print(d['a'])
1
>>> print(color['apple'])
red
>>> for item in color.items()
SyntaxError: invalid syntax
>>> for item in  color.items()
SyntaxError: invalid syntax
>>> print(item)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print(item)
NameError: name 'item' is not defined
>>> for item in color.items():
	print(item)

	
('apple', 'red')
('banana', 'yellow')
>>> 
>>> 
>>> 
>>> print("id : %s, name : %s" % ("kim", "김유신"))
id : kim, name : 김유신
>>> 
>>> def add(a,b)
SyntaxError: invalid syntax
>>> def add(a,b):
	return a+b

>>> 
>>> 
>>> a+b
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> args = (3,4)
>>> add(*args)
7
>>> 
>>> 
>>> 
>>> phone = {"kim" : }
SyntaxError: invalid syntax
>>> phone = {"kim " : "1111", "lee" : "2222" , "park" : "3333"}
>>> phone.keys()
dict_keys(['kim ', 'lee', 'park'])
>>> phone.value()
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    phone.value()
AttributeError: 'dict' object has no attribute 'value'
>>> phone.values()
dict_values(['1111', '2222', '3333'])
>>> for k in phone.keys():
	print(k)

	
kim 
lee
park
>>> "park" in phone
True
>>> "moon" in phone
False
>>> "moon" not in phone
True
>>> 
>>> p = phone
>>> p
{'kim ': '1111', 'lee': '2222', 'park': '3333'}
>>> p["moon"] = "1234"
>>> p
{'kim ': '1111', 'lee': '2222', 'park': '3333', 'moon': '1234'}
>>> phone
{'kim ': '1111', 'lee': '2222', 'park': '3333', 'moon': '1234'}
>>> id(phone), id(p)
(2183407796544, 2183407796544)
>>> 
>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> isRight = True
>>> type(isRight)
<class 'bool'>
>>> 1<2
True
>>> 1 !=2
True
>>> 1==2
False
>>> True and True and True
True
>>> True or False or False
True
>>> True or False or False
True
>>> bool(0)
False
>>> bool(3)
True
>>> bool("")
False
>>> bool(None)
False
>>> bool([1,2,3])
True
>>> bool(-1)
True
>>> bool(Null)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    bool(Null)
NameError: name 'Null' is not defined
>>> a = [1,2,3]
>>> b = a
>>> a[0] = 38
>>> a
[38, 2, 3]
>>> b
[38, 2, 3]
>>> id(a),id(b)
(2183407782592, 2183407782592)
>>> a= [100,200,300]
>>> b  = a[:]
>>> a[0] = 101
>>> a
[101, 200, 300]
>>> b
[100, 200, 300]
>>> id(a), id(b)
(2183407712128, 2183407412608)
>>> 
>>> import copy
>>> a = [10,20,30]
>>> b = copy.deepcompy(A)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    b = copy.deepcompy(A)
AttributeError: module 'copy' has no attribute 'deepcompy'
>>> b = copy.deepcopy(a)
>>> a[0] = 11
>>> a
[11, 20, 30]
>>> b
[10, 20, 30]
>>> id(a),id(b)
(2183407689472, 2183407782592)
>>> 
>>> 
>>> 
>>> 5/2
2.5
>>> 5//2
2
>>> 2 ** 5
32
>>> 5 % 2
1
>>> 4 % 2
0
>>> 5 == 5
True
>>> 5 == 2
False
>>> 1.5 == (3/2)
True
>>> 
============================================================================= RESTART: D:/Lecture/Work/ifelse.py ============================================================================
Input Score:99
Grade Is : A
>>> 
============================================================================= RESTART: D:/Lecture/Work/ifelse.py ============================================================================
Input Score:30
Grade Is : D
>>> 
>>> 
>>> value = 5
>>> while value > 0:
	print(value)
	value -= 1

	
5
4
3
2
1
>>> 
>>> lst = ["apple", 100, 3.14]
>>> for item in lst:
	print(item, type(item))

	
apple <class 'str'>
100 <class 'int'>
3.14 <class 'float'>
>>> print lst
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(lst)?
>>> print item
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(item)?
>>> print (item)
3.14
>>> for x in [2,3,4,5,6]
SyntaxError: invalid syntax
>>> for x in [2,3,4,5,6]:
	print("---{0}단---".format(x))
	for y in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(x,y,x*y))

		
---2단---
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
---3단---
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
---4단---
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
---5단---
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
---6단---
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
>>> for x in [2,3,4,5,6,7,8,9]:
	print("---{0}단---".format(x))
	for y in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(x,y,x*y))

		
---2단---
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
---3단---
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
---4단---
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
---5단---
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
---6단---
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
---7단---
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
---8단---
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
---9단---
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
>>> 
>>> 
>>> for i in [1,2,3,4,5,6,7,8,9,10]:
	print("*" * i)

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> for i in[10,9,8,7,6,5,4,3,2,1]
SyntaxError: invalid syntax
>>> for i in[10,9,8,7,6,5,4,3,2,1]:
	print("*" *i)

	
**********
*********
********
*******
******
*****
****
***
**
*
>>> 
>>> 
>>> lst= [1,2,3,4,5,6,7,8,9,10]
>>> for item in lst:
	if item > 5:
		break
	print("item:{0}".format(item))

	
item:1
item:2
item:3
item:4
item:5
>>> 
>>> lst = [1,2,3,4,5,6,7,8,9,10]
>>> for item in lst:
	if item %2 == 0:
		continue
	print("item : {0}".format(item))

	
item : 1
item : 3
item : 5
item : 7
item : 9
>>> 
>>> lst = [1,2,3,4,5,6,7,8,9,10]
>>> for item in lst:
	if item %2 == 0:
		break
	print("item : {0}".format(item))

	
item : 1
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(range(10,20,2))
[10, 12, 14, 16, 18]
>>> 
>>> 