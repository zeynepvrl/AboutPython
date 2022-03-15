a = 9
x = 4
y = x+(a/x)/2
print(y)

x = 9
a = 4
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x=y



n = int(input("Enter a number: "))
flag = True

for i in range(3, n):
    if (n%i==0):
        print("divided by", str(i))
        flag = False
        break                           # or i = n
if not flag:
    print("The number is not prime")
else:
    print("The number is prime")









