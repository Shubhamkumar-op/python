print('Hello world')
# python mathematical function

print(abs(-45))
print(abs(100))

#ceil()
import math
print(math.ceil(-45.12))
print(math.ceil(100.12))
print(math.ceil(math.pi))

#exp(x)

print(math.exp(100))

#floor(x)
print(math.floor(-45.12))
print(math.floor(100.12))

#log(x)
print(math.log(math.pi))
print(math.log(100.12))

#max(x)
print(max(80,100,10,120))

#min()
print(min(100,10,12,0))

#pow()
print(math.pow(100,2))
print(math.pow(2,100))

#round()
print(round(20.36566))
print(round(-50.232323))

#sqrt()
print(math.sqrt(100))
print(math.sqrt(55))


#Python Random Number Functions
import random
#choice() function
list1 = [1, 5, 9, 4, 5, 6]
print(random.choice(list1))

string = "shubham"
print(random.choice(string))

#randrange()
print(random.randrange(20, 50, 3))

#uniform() 
print(random.uniform(5, 10))

#shuffle() function

li = ['S', 'H', 'U', 'B', 'H','A','M']
random.shuffle(li)
print(li)

random.shuffle(li)
print(li)


