# functions questions:

# 1.) to calculate square of a number:
'''def square(n):
    print("ans is: ",n**2)

square(5)'''

# 2.) sum of two numbers:
'''def sum(a,b):
    return a+b

ans=sum(2,3)
print(ans)'''

# 3.) polymorphism in functions:
'''def multiply(p1, p2):
    return p1*p2

print(multiply(2,4))
print(multiply(2,'a'))'''

# 4.) function returning multiple values:
'''import math
def circle(r):
    area=math.pi* r**2
    circumference=2*math.pi*r
    return area, circumference

# print(circle(2))
a,c=circle(4)
print("area: ",a, "circumference: ",c)'''

# 5.) default parameter functions:
'''def greet(name="simran"):
    print("good morning ",name)

greet("sneha")
greet()'''

# 6.) lamda function:
'''cube=lambda x: x**3
print(cube(3))'''

# 7.) function with *args:
'''def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3))'''

# 8.) function using kwargs:
'''def P_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

P_kwargs(name="simran")
P_kwargs(name="abc",color="red")'''

# 9.) even number generator using yield function
'''def even_gen(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even_gen(10):
    print(num)'''

# 10.) factorial using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
ans=fact(5)
print(ans)



