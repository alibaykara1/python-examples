def hesap_makinesi():
    print("🔢 Hesap Makinesi Programı")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Üs alma (^)")
    print("6. Mod alma (%)")
    print("7. Çıkış (q)")

    while True:
        # Kullanıcıdan işlem seçimi 
        secim = input("\nBir işlem seçin (1/2/3/4/5/6 veya q):")

        # Çıkış için kontrol 
        if secim == 'q' or secim == '7' :
            print("Hesap makinesi kapanıyor... Görüşürüz!")
            break #Döngü sonlanır 

        # Sayıları kullanıcıdan al
        try:
            sayi1 = float(input("Birinci sayıyı girin:"))
            sayi2 = float(input("İkinci sayıyı giriniz:"))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")
            continue

        # İşlemleri kontrol et ve sonucu yazdır

        if secim == '1':
            print(f"Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == '2':
            print(f"Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif secim == '3':
            print(f"Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif secim == '4':
            if sayi2 != 0:
                print(f"Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez!")
        elif secim == '5':
            print(f"Sonuç: {sayi1} ^ {sayi2} = {sayi1 ** sayi2}") # ÜS alma işlemi
        elif secim == '6':
            print(f"Sonuç: {sayi1} % {sayi2} = {sayi1 % sayi2}")# Mod alma işlemi
        else:
            print("Hata: Geçersiz işlem seçimi, lütfen 1, 2, 3, 4, 5, 6 veya q seçin." )

# Fonksiyonu çalıştır 
hesap_makinesi() 