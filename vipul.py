name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line  = line.strip()
    if line.startswith('from'):
        word = line.split()
        word = word[0:2]
        d[word] = d.get(word,0)+1
        
lst = list()
for k,v in d.items():
    tup = (k,v)
    lst.append(tup)

lst.sort()
for k,v in lst:
    print(k,v)