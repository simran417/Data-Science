# conditional questions

# 1.) age group categorization
x=int(input("enter your age: "))

if x<13:
    print("child")
elif x<20:
    print("teenager")
elif x<60:
    print("adult")
else:
    print("senior")

# 2.) movie ticket pricing
age=int(input("enter your age: "))
day=input("enter day: ")
price=12 if age>=18 else 8
if day=="wednessday":
    price -=2
print(price)    

# 3.) grade calculator
score=int(input("enter score: "))
if score>=90 and score<=100:
    print("a grade")
elif score<=80 and score>90:
    print("b grade")
elif score>=70 and score<80:
    print("c grade")
else:
    print("poor")    

# 4.) fruit ripeness checker
color=input("enter colour: ")

if color=="green":
    print("unripe")
elif color== "yellow":
    print("ripe")
elif color== "brown":
    print("over ripe")

# 5.) wheather activity suggestion
weather=input("enter weather: ")
if weather=="sunny":
    print("go for a walk")
elif weather== "rainy":
    print("read a book")
elif weather=="snowy":
    print("make a snowman")

# 6.) transportation mode
distance=int(input("enter distance: "))
if distance <3:
    print("walk")
elif distance >=3:
    print("bike")
elif distance>15:
    print("car")

# 7.) coffee customization
size=input("enter coffee size")
extra_shot=True
if extra_shot==True:
    print("coffee with extrashot")
else:
    print("coffee")

# 8.) password strength checker:
password = input("enter password")
cnt=len(password)
if cnt<6:
    print("weak")
elif cnt>6 and cnt<10:
    print("medium")
elif cnt>15:
    print("strong")

# 9.) leap year checker
year=int(input("enter year: "))
if(year%400==0) or (year%4==0 and year%100 !=0):
    print("leap year")
else:
    print("not a leap year")

# 10.) pet food recommendation system:
pet=input("enter pet: ")
age=int(input("enter pet age: "))
if pet=="dog":
    if(age<2):
        print("puppy food")
elif pet=="cat":
    if(age<3):
        print("kitty food")



