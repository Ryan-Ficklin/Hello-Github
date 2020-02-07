import random

roll = random.randint(1,6)

print(roll)

i = 0
while(i < 10):
    roll = random.randint(1,6)
    print(roll)
    i += 1

print("Next!")
