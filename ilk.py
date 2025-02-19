try:
    sayi = int(input("Bir sayı giriniz: "))
    sonuc = 10 / sayi 
    print("Sonuç:", sonuc)
except ValueError:
    print("Hata: Lütfen bir sayı giriniz!")
except ZeroDivisionError:
    print("Hata: Bir sayıyı sıfıra bölemezsiniz!")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:",e)            