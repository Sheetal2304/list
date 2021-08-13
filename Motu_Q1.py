# user=int(input("enter the number"))
user=145
# sum=0
# while user>0:
#     a=user%10
#     j=0
#     b=1
#     while j>0:
#         b=b*j
#         j-=1
#     user=user//10
# print(b)


# num=int(input("enter the number"))
# sum=0
# yn=num
# while num>0:
#     i=1
#     f=1
#     y=num%10
#     while i<=y:
#         f=f*i
#         i+=1
#     sum+=f
#     num=num//10
# if sum==yn:
#     print(sum,"yes")
# else:
#     print(sum,"no")

list1=["a","b","c","d"]
user=int(input("enter the number"))
i=0
b=[]
while i<len(list1):
    # user=int(input("enter the number"))
    j=1
    while j<=user:
        print(list1[i],end="")
        print(j,end=" ")
        j+=1
    i+=1

# list1=["a","b","c","d"]
# user=int(input("enter the number"))
# i=0
# b=[]
# while i<len(list1):
#     print(list1[i],end="")
#     # i+=1
# j=1
# while j<=user:
#     print(j,end="")
#     j+=1
#     i+=1