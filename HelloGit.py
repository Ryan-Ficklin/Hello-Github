# comment 
a = 6
b = 5
print("Hello, World!")
print(a+b)

# how to make a list
myList = [1, 2, 3, 4, 3, 2, 1]

# how to access elements of a list
myList[3]

# how to stride
print(myList[0:6:2]) # from index 0 to 6, skipping by 2

#strings are just lists
phrase = "Catch the dog"
phrase[2]
phrase[4]
phrase[-1: 0: -3]
#strides work backwards, -1 is right, 0 is left, down by 3

# how to write a function
def sumFunction(a, b):
	return a + b

# how to call a function
print(sumFunction(2,20))

x = 10
y = -10

# blocks of code
if(x == 10):
	x = 5
elif(y == -10):
	y = 5
else:
	x = y - x

# loop
myList = [1, 3, 8, 412, 43, 2, 20]

# length of list 
len(myList)

# while
x = 0
while(x < 5):
        x+=1
        print("x = " + str(x))
# for loop
for i in range(len(myList)):
	print(i)

#for each loop
for val in myList:
	print(val)

#dictionaries
lookup = {}
lookup['kc'] = 'chiefs'
lookup['ne'] = 'patriots'
lookup['la'] = 'chargers'
lookup['suck'] = 'raiders'
print(lookup['kc'])
