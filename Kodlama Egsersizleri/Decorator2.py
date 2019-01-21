def duzelt(fonksiyon):
    def wrapper(sayilar):
        tekler  = []
        ciftler = []
        for i in sayilar:
            if(i%2==1):
                tekler.append(i)
            else:
                ciftler.append(i)

        x = fonksiyon(ciftler)
        print(ciftler)
        return  x
    return  wrapper

@duzelt
def topla(sayilar):
    toplam = 0
    for i in sayilar:
        toplam +=i
    return toplam

print(topla(range(1,10)))
