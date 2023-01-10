#python string

b = "shubham kumar singh"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

#Upper Case
print(b.upper())

#Lower Case
print(b.lower())


#Replace String

print(b.replace("s", "S"))

#split()
print(b.split(" "))


#list
li = ["shubham", "saumya", "shub"]
print(li)
print(len(li))
print(type(li))
print(li[1:])

li.append("kumar")
print(li)
li.insert(2, "verma")
print(li)

#w3school
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Tuple
tup = ("shuaham", "saumya", "kumar")
print(tup)
print(type(tup))


tp = ("apple", "banana", "cherry")
y = list(tp)
y.append("orange")
tp= tuple(y)
print(tp)
y.remove("apple")
tp = tuple(y)
print(tp)

del tp
print(tp) #will get error


#set
ms = {"shubham", "saumya", "kumar"}
print(ms)
for x in ms:
  print(x)

ms.add("verma")
print(ms)

ms.remove("verma")
print(ms)
