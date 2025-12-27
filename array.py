x=list(map(int,input().split(",")))  #[2,5,7,1,9]
min1=max1=x[0] #2
for i in range(1,len(x)):
    if x[i]<min1:
        min1=x[i]
        if x[i]>max1:
            max1=x[i]
print(min1,max1)