list1=[2,1,3,4,5,6,3,2,3,1,4,2,4]
list2=[]
i=0
while i<len(list1):
    count=0
    j=0
    while j<len(list1):
        if list1[j]==list1[i]:
            count+=1
        j+=1
    if list1[i]in list2:
        i+=1
        continue
    list2.append(list1[i])
    if count%2==0:
        print(list1[i],"",count//2,"pair")
    i+=1