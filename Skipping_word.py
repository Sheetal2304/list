a="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b=a.split()
i=0
while i<len(b):
	if b[i]=="over":
		i+=1
		continue
	print(b[i],end=" ")
	i=i+1