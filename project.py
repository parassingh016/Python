import re
hand = open("x.txt")
sum = 0
str1=""
for line in hand:
    line.rstrip()
    y = re.findall('[0-9]+',line)
    for z in y:
        z = z + str1
        z = int(z)
        sum = sum + z
print(sum)


  