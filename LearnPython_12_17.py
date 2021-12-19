import time
i=1
sum=0
while i<=100:
    if(i%2==0):
        sum+=i
#        time.sleep(0.5)
    i=i+1
print(sum)

for item in 'Python':
    print(item)

#水仙花数字
for item in range(100,1000):
    L=int(item/100)
    M=int(item%100/10)
    N=int(item%10)
    if(item==pow(L,3)+pow(M,3)+pow(N,3)):
        print(item)
 #   time.sleep(0.2)
 #   print(item)



l=list(['1','21','21','hello'])
print



