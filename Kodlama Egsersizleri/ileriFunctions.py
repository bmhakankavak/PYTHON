# #args
# def fonksiyon(*args):
#     for i in args:
#         print(i)
#
#
# fonksiyon(1,2,3,4)
#
# #
# def fonk(**kwargs):
#     for i,y in kwargs.items():
#         print(i,y)
#
#
# fonk(z=1,x=3,y=5)
#
# def selam(ad):
#     print("selam ",ad)
#
# sabah = selam
#
# sabah("deneme")

def fonksiyon(islem):
    def topla(*args):
        toplam = 0
        for i in args:
            toplam +=i

        return  toplam
    def carp(*args):
        carp = 1
        for i in args:
            carp *=i
        return carp
    if (islem=="Topla"):
        return topla
    elif(islem=="carp"):
        return  carp

#fonksiyon(1,2,3,3,3,4)

f1 = fonksiyon("carp")

print(f1(1,2,3,3,4))

def f1(pad):
    print("Adınız =",pad)
def f2(soyad):
    print("Soyad =",soyad)

def caller(fnc,p1):
    print(fnc(p1))


caller(f1,"HAKAN")
caller(f2,"KAVAK")



