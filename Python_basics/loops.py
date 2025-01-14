# conditional loops statements:

# 1.) count positive numbers:
'''nums=[1,-2,3,-4,5,6,-7,-8,9,10]
cnt_positive_num=0
for x in nums:
    if(x>0):
        cnt_positive_num +=1
print(cnt_positive_num)'''

# 2.) count even numbers:
'''x=10
cnt=0
for a in range(x+1):
    if a%2==0:
        cnt +=1
        # print(a)
print(cnt)'''

# 3.) multiplication table printer:
'''num=int(input("enter no.: "))
for x in range(1,11):
    if x==5:
        continue
    print(num*x)'''

# 4.) reverse a string:
'''name="simran"
rev_name=" "
for x in name:
    rev_name=x+rev_name
print(rev_name)'''

# 5.) find the first non repeated character:
'''input_str="aabbc"
for x in input_str:
    if input_str.count(x)==1:
        print(x)'''

# 6.) factorial counter using while loop:
'''numb=5
fact=1
while numb>0:
    fact *= numb
    numb -= 1
print(fact)'''

# 7.) keep asking the user for input until they enter a no. between 1 and 10

'''while True:
    num=int(input("enter a number between 0 and 10: "))
    if 1<=num<=10:
        print("thanks")
        break
    else:
        print("enter a valid number")'''

# 8.) prime number checker:
'''num=int(input("enter number: "))
is_prime= True
if num>1:
    for i in range(2,num):
        if(num%i)==0:
             is_prime=False
             break
        
print(is_prime)'''

# 9.) list uniquness checker:
'''items = ["apple", "banana", "orange", "apple", "mango"]
unique=set()  # set contain all unique values
for i in items:
    if i in unique:
        print("duplicate", i)
        break
    else:
        unique.add(i)'''

# 10.) exponential backoff:
import time
wait_time=1
max_retries=5
attempts=0
while attempts< max_retries:
    print(attempts, wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1