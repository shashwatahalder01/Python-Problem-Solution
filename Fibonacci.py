n=int(input())
l=[0,1]
i=2
while i < n+2:
    l.append(l[i-1]+l[i-2])
    i+=1

print(*l, sep = ", ") 


