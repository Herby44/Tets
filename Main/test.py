#nahodne cislo
import random
y = 0
for i in range(5):
    x = random.randint(1,6)
    if x == 6:
        y += 1
    print(x)
print('Cislo 6 bolo vypisane',y,'krát')
