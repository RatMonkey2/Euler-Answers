num=1
sum=0
while num<1000:
	if num%3==0:
		sum+=num
	if num%5==0:
		sum+=num
	if num%15==0:
		sum-=num
	num+=1
print(sum)