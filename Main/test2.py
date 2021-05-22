#nahodne cislo
import random
y = 0
for i in range(20):
    x = random.randint(1,10)
    if x % 2 == 0:
        y += 1
    print(x)
print('Cislo bolo párne',y,'krát')
