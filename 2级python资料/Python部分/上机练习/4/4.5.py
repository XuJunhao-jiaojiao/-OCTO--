import random
total = random.randint(1, 10000)
change = 0
nochange = 0
for i in range(1, total+1):
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    if a == b:
        nochange += 1
    else:
        change += 1
print('不换的概率：{},换的概率：{}'.format(nochange/total,change/total))
