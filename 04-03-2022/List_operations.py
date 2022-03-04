lis = [1,2,3,4,5,6,7,8,9,10]

# Append
lis.append(10)
print("Append 10",lis)
# pop
lis.pop()
lis.pop(0)
print('Pop',lis)
# remove
lis.remove(4)
print('remove 4',lis)
# Extend
lis.extend([11,12,13])
print('extend',lis)

# List comprehension

even = [i for i in lis if i%2 == 0]
print('even',even)

odd = [i for i in lis if i%2 != 0]
print('odd',odd)

sqr = [i**2 for i in lis]
print('Square')

# Clear 

lis.clear()
print('clear',lis)