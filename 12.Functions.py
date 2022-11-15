#suppose
a=10
b=20
sum=a+b
#print(sum)

a=30
b=30
sum=a+b
#print(sum)

# now we usw function
def add(x,y):
    sum=x+y
    print(x+y)
add(10,20)
add(30,30)
add(50000,3333)

def addition(x,y,z):
    sum=x+y+z
    print(x+y+z)
addition(10,20,30)

def sub(x,y):
    result=x-y
    print(x-y)

sub(30,20)

def message():
    print("no parameter")
add(20,30)
sub(30,20)
message()

def say_hi(name,age):
    print("Hello "+name + ", you are " +age)

say_hi("Saeed","34")
say_hi("Focasting","54")

def say_hi(name,age):
    print("Hello "+name + ", you are " +str(age))

say_hi("Saeed",34)
say_hi("Focasting",54)








