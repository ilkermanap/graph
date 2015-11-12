class Dugum:
    def __init__(self, adi):
        self.adi = adi
        self.ozellikler = {}

    def ozellik_ekle(self, adi, degeri):
        self.ozellikler[adi] = degeri

    def ozellik(self,adi):
        if adi in self.ozellikler.keys():
            return self.ozellikler[adi]
        else:
            return None

class Yol:
    def __init__(self, baslangic, bitis):
        self.baslangic = baslangic
        if bitis is not None:
            self.bitis = [bitis]
        else:
            self.bitis = []
        self.ozellikler = {}

    def bitis_ekle(self, bitis_nokta):
        if bitis_nokta not in self.bitis:
            self.bitis.append(bitis_nokta)

    def ozellik_ekle(self, adi, degeri):
        self.ozellikler[adi] = degeri

    def ozellik(self,adi):
        if adi in self.ozellikler.keys():
            return self.ozellikler[adi]
        else:
            return None

class Kat:
    def __init__(self, adi, seviye , ust = None, alt = None):
        self.adi = adi
        self.seviye = seviye
        self.ust = ust
        self.alt = alt
        self.giris = {}

class Bina:
    def __init__(self, adi):
        self.adi = adi
        self.katlar = {}

    def kat_ekle(self, yenikat):
        self.katlar[yenikat.adi] = yenikat

class Harita:
    def __init__(self, adi, hml=None):
        self.adi = adi
        self.yollar = []
        self.dugumler = {}
        self.binalar = {}
        if hml is not None:
            self.yukle(hml)

    def yukle(self, hml):
        print hml
        for satir in (open(hml,"r").readlines()):
            nesne, deger = satir.split(":")
            if nesne == "dugum":
                d = self.dugum_yap(deger)
                if d.adi not in self.d.keys():
                    self.dugumler[d.adi] = d
            if nesne == "yol":
                y = self.yol_yap(deger)


    def yol_yap(self,satir):
        p = satir.split(",")
        d1 = p[0]
        d2 = p[1]
        if yol_
        if len(p) > 2:
            for parca in p[2:]:
                ad, deger = parca.split("=")

    def yol_kontrol(self,baslangic, bitis):
        for yol in self.yollar:
            if yol.baslangic == baslangic:
                if yol.bitis == bitis:
                    return yol
        return None

    def dugum_yap(self, satir):
        p = satir.split(",")
        adi = p[0]
        d = Dugum(adi)
        if len(p) > 1:
            for parca in p[1:]:
                if parca.find("=") > -1:
                    ad, deger = parca.split("=")
                    try:
                        deger = float(deger)
                    except:
                        deger = int(deger)
                    finally:
                        pass
                    print ad, deger, type(deger)
                    d.ozellik_ekle(ad, deger)
        return d

    def yol_ekle(self, yeni_yol):
        if yeni_yol not in self.yollar:
            self.yollar.append(yeni_yol)

    def dugum_ekle(self, yeni_dugum):
        if yeni_dugum.adi not in self.dugumler.keys():
            self.dugumler[yeni_dugum.adi]  = yeni_dugum

    def bina_ekle(self, yeni_bina):
        if yeni_bina.adi not in self.binalar.keys():
            self.binalar[yeni_bina.adi] = yeni_bina

if __name__ == "__main__":
    harita = Harita("test","harita.hml")
