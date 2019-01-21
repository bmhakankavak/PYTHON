import time
def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        baslama = time.time()
        sonuç = fonksiyon(sayılar)
        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuç

    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç


(kareleri_hesapla(range(100000)))


"""

Çıktı

kareleri_hesapla 0.1340925693511963 saniye sürdü.
küpleri_hesapla 0.13509273529052734 saniye sürdü.

"""
