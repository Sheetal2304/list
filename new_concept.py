a=["123","456","678b","12@","234y","544"]
# a =["123","678",]
x=[]
for i in a:
    try:
        b = int(i)
        x.append(b)
    except:
        # print("error")
        continue
print(x)
# print("----")
