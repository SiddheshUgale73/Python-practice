Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: C:\Users\hp\Desktop\python\operators.py ===============
25 >> 4
1
47 >> 2
11
~ 9
-10
~6
-7
15 << 4
240
15 << 3
120
x=5
print(id(x))
2533621498224
y=5
print(id(y))
2533621498224
z=5.0
print(id(z))
2533660811920
x is y
True
x is z
False
x==z
True
x is not z
True
z is not x
True
x="Ritika"
a in x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a in x
NameError: name 'a' is not defined
'a'in x
True
'p'in x
False
ord('A')
65
ord('a')
97
d1=[11,33,22,44,55,67,678]
44 in d1
True
32 in d1
False
44 not in d1
False
4 and 6
6
4 & 6
4
