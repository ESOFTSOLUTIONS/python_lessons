#Found the hour when the email was sent
name = input("Enter file:")
fh = open(name)
counts = dict()
f=list()
for line in fh:
    if not line.startswith('From '):
        continue
    words=line.split()
    d=words[5].split(':')
    l=d[:1]
    for hou in l:
        counts[hou] = counts.get(hou,0)+1
for k,v in counts.items():
    newtup=(k,v)
    f.append(newtup)
f=sorted(f,reverse=False)
for k,v in f:
    print(k,v)