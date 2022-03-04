import math
import datetime
import random
# List
lis = [1,2,3,5,6]
lenth = len(lis)
sum = 0
for i in lis:
  sum += i

print(random.random())
print(datetime.datetime.now())
print(lenth)
lis.pop()
print("After pop",lis)
lis.append(10)
print("After append",lis)
lis.extend([4,5,6])
print("after extend",lis)

print("Squreroot of 4", math.sqrt(4))

A = "anish"
print("Capital all",A.capitalize())