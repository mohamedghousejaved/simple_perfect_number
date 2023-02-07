a=int(input("enter value"))
sum = 0
for i in range(1,a):
  if a % i == 0:
    sum=sum+i
    i=i+1
    if sum == a:
        print(a,"is a perfect number")
    else:
        print(end="")