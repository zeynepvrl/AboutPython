n = 10
sum = 1
for i in range(n):
    if((i%2)==0):
        print("value of i:" ,i)
        sum+=i
print("The sum of even values from 0 to" + str(n-1) + "is" + str(sum))
txt = "the sum of even values from 0 to {0} is {1}"       # as a second method
print(txt.format(n, sum))

n = 10
sum = 0
i = 0
while(i<n):
    if((i%2)==0):
        print(i)
        sum += i
    i+=1           # if this line did'nt exist, this situation is created a infinie loop
print("the sum of even values from 0 to"+str(n-1)+"is"+str(sum))

choice = 0
while(True):
    choice = int(input("pick a number from 1-10: "))
    if(choice==6):
        print("Right!")
        break
    else:
        print("wrong!")

