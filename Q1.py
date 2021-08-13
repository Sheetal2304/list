pat=[1,3,2,1,2,3,1,0,1,3]
p = 0
while p<=len(pat):
    pass
    if (pat[p] == 0):
        current = pat[p]
        break
    elif (pat[p] % 2 == 0):
        continue
    print("pat[p]",pat[p]) 
    p=p+1
print("current",current)  
