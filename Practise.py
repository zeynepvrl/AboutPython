def is_prime(num):
    flag = True
    for i in range(3, num):
        if(num%i)==0:
            flag = False
            break
    return flag



n = int(input("Enter a number: "))
while True:
    n+=1
    if is_prime(n):
        print("next prime number is:", str(n))
        break                                         # YENİ KODA GEÇİŞ



def areaRect(side1, side2):
    return(1)
def dist(x1, y1, x2, y2):
    return(1)
def areaRectCorner(x1, y1, x2, y2):
    side1 = dist(x1, y1, x1, y2)
    side2 = dist(x1, y1, x2, y1)
    area = areaRect(side1, side2)
    return area

x1 = 5
y1 = 1
x2 = 19
y2 = 12
print(areaRectCorner(x1, y1, x2, y2))                     # YENİ KODA GEÇİŞ





def areaRect(side1, side2):
    return(side1, side2)
def dist(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d
def areaRectCorner(x1,y1,x2,y2):
    side1 = dist(x1,y1,x2,y2)
    side2 = dist(x1,y1,x2,y1)
    area = areaRect(side1, side2)
    return area

x1 = 1
y1 = 1
x2 = 12
y2 = 12
print(areaRectCorner(x1,y1,x2,y2))

if sayi %3==0:
     print("A")
else:
     print("B")


def alku(x):
    return x % 2 == 0


toplam = 0
sayac = 0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range(int(baslangic), int(bitis) + 1):
    if (alku(int(sayi))):
        toplam = toplam + sayi
        sayac = sayac + 1
print((toplam / sayac))


a = input("Birinci sayıyı giriniz")
b = input("İkinci sayıyı giriniz")
c =input("Üçüncü sayısı giriniz")
if(a>=b)