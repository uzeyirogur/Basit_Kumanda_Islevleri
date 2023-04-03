import random
import time

class Kumanda() :

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT") :

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self) :

        if (self.tv_durum == "Açık") :
            print("Televizyon zaten açık...")

        else :
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self) :

        if (self.tv_durum == "Kapalı") :
            print("Televizyon zaten kapalı...")

        else :
            print("Televizyon kapatılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self) :

        while True :
            cevap = input("Sesi azalt: '-'\nSesi arttır: '+'\nÇıkış : exit\nSecim:")

            if(cevap == "+") :
                self.tv_ses += 10

                if(self.tv_ses == 100) :
                    print("Ses en yüksek düzeyde...")
                    break
                else :
                    print("Ses arttırılıyor...")
                    print(f"Ses {self.tv_ses}")

            elif(cevap == "-") :
                self.tv_ses -= 10
                if(self.tv_ses <= 0) :
                    print("Ses tamamen kapalı")
                    break
                else :
                    print("Ses kısılıyor...")
                    print(f"Ses : {self.tv_ses}")

            elif(cevap == "exit") :
                print("Ses ayarlarından çıkılıyor...")
                break

            else :
                print("Geçersiz Giriş...")

    def kanal_ekle(self,kanal_ismi) :

        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")

    def rastgele_kanal(self) :

        rastgele = random.randint(0,len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print(f"Şu anki kanal : {self.kanal}")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self) :

        return  f"KANAL LİSTESİ\nTv Durumu : {self.tv_durum}\nSes Derecesi : {self.tv_ses}\nKanal Listesi : {self.kanal_listesi}\nŞu anki Kanal : {self.kanal}"


print("TELEVİZYON UYGULAMASI")
print("""
1. TV AÇ
2. TV KAPAT
3. SES AYARLARI
4. KANAL EKLE
5. KANAL SAYISINI ÖĞRENME
6. RASTGELE KANALA GEÇME
7. TELEVİZYON BİLGİLERİ
8. EXİT
""")

kullanici = Kumanda()
while True :
    islem = input("Yapmak istediğiniz işlemi yukarıdaki menüden seçerek giriniz : ")

    if (islem == "8") :
        print("Menü kapatılıyor...")
        break

    elif (islem == "1") :
        kullanici.tv_ac()

    elif (islem == "2") :
        kullanici.tv_kapat()

    elif (islem == "3") :
        kullanici.ses_ayarları()

    elif (islem == "4") :
        Kanal_adı = input("EKlemek İstediğiniz kanalı giriniz : (KANALLARI - İLE AYIR) : ")
        kanal_listesi = Kanal_adı.split("-")

        for eklenecekler in kanal_listesi :
            kullanici.kanal_ekle(eklenecekler)

    elif (islem == "5") :
        print("Kanal Sayısı: ",len(kullanici))

    elif (islem == "6") :
        kullanici.rastgele_kanal()

    elif (islem == "7") :
        print(kullanici)

    else :
        print("Geçersiz giriş...")
