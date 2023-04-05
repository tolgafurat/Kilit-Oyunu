def KarakterKontrol(degisken):
  if len(degisken) != 1:
    return False
  else:
    return True

def RakamKontrol(degisken):
  try:
    degisken = int(degisken)
  except ValueError:
    return False
  else:
    return True

def BaslangicAralikKontrol(degisken):
  if not 4 <= int(degisken) <= 8:
    return False
  else:
    return True


def HamleAralikKontrol(degisken, boyut):
  if not 1 <= int(degisken) <= boyut:
    return False
  else:
    return True

  
def HamleSutunKontrol(hamle, sutunlar):
  sutunKontrol = False

  sutunKontrol1, sutunKontrol2 = False, False
  while not sutunKontrol1 and not sutunKontrol2:
    for key in sutunlar.keys():
      if hamle[1].upper() == key:
        sutunKontrol1 = True
        break
    for key in sutunlar.keys():
      if hamle[4].upper() == key:
        sutunKontrol2 = True
        break
    if sutunKontrol1 and sutunKontrol2:
      sutunKontrol = True

  return sutunKontrol


def TabloDoldur(liste, boyut, tasSayisi, oyuncu1, oyuncu2):
    satir1, sutun1, satir2, sutun2, yerlestirilen = boyut - 1, 0, 0, 0, 0
    while True:
      liste[satir1][sutun1] = oyuncu1
      liste[satir2][sutun2] = oyuncu2
      yerlestirilen += 1
      sutun1 += 1
      sutun2 += 1
      if yerlestirilen == tasSayisi:
        break
      elif sutun1 == boyut:
        sutun1, sutun2 = 0, 0
        satir1 -= 1
        satir2 += 1
    return liste



def OyunBaslat():

    while True:
      oyuncu1 = input("1. Oyuncuyu temsil etmek için bir karakter giriniz: ")
      if KarakterKontrol(oyuncu1):
        break
      else:
        print("Lütfen sadece tek karakter girin!")

    while True:
      oyuncu2 = input("2. Oyuncuyu temsil etmek için bir karakter giriniz: ")
      if KarakterKontrol(oyuncu2):
        break
      else:
        print("Lütfen sadece tek karakter girin!")

    while True:
      boyut = input("Oyun alanının satır/sütun sayısını giriniz(4-8): ")
      if RakamKontrol(boyut) and BaslangicAralikKontrol(boyut):
        break
      else:
        print("Lütfen 4 ile 8 arasında bir rakam girin!")

    while True:
      tasSayisi = input("Oyuncuların sahip olacağı taş sayısını giriniz(4-8): ")
      if RakamKontrol(boyut) and BaslangicAralikKontrol(boyut):
        break
      else:
        print("Lütfen 4 ile 8 arasında bir rakam girin!")

    boyut, tasSayisi = int(boyut), int(tasSayisi)

    liste = [ [ " " for i in range(boyut) ] for j in range(boyut) ]
    liste = TabloDoldur(liste, boyut, tasSayisi, oyuncu1, oyuncu2)
    sira = False

    while True:
      sira = TabloYazdir(liste, boyut, sira)
      kazanan = KazananVarMi(liste, boyut, oyuncu1, oyuncu2)
      if kazanan != -1:
        print(f"\n\nOyuncu {kazanan} kazandı.")
        while True:
          tekrar = input("Tekrar oynamak ister misiniz(E/H)?:").upper()
          if tekrar == "E":
            main()
          elif tekrar != "H":
            print("Lütfen e veya h girin(büyük-küçük harf önemsiz)")
          else:
            break
        break
      if sira:
        oyuncu = oyuncu1
      else:
        oyuncu = oyuncu2
      liste = HamleYap(liste, boyut, oyuncu, oyuncu1, oyuncu2)
      


def TabloYazdir(liste, boyut, oyuncuSirasi):
  alfabe = ["A", "B", "C", "D", "E", "F", "G", "H"]
  print()
  for i in range(boyut):
    print(f"     {alfabe[i]}", end="")
  cizgi = "------" * boyut

  print()
  for i in range(boyut):
    print("   " + cizgi)
    for j in range(boyut):
      if j == boyut - 1:
        print(f" {liste[i][j]:^3}", end=f" | {i+1}\n")
      elif j == 0:
        print(f"{i+1} | {liste[i][j]:^3}", end=" |")
      else:
        print(f" {liste[i][j]:^3}", end=" |")
  
  print("   " + cizgi)

  for i in range(boyut):
    print(f"     {alfabe[i]}", end="")
  print()
  oyuncuSirasi = not oyuncuSirasi #sıranın hangi oyuncuda olduğu burada değiştiriliyor, KazananVarMi fonksiyonu her çağrıldığında önce bu fonksiyon çalıştığından sırası gelen oyuncu da burada belirleniyor
  return oyuncuSirasi

def HamleYap(liste, boyut, oyuncuSirasi, oyuncu1, oyuncu2):
  
  kontrol1, kontrol2, kontrol3, kontrol4, kontrol5, kontrol6, kontrol7, kontrol8, kontrol9, kontrol10, kontrol11=False, False, False, False, False, False, False, False, False, False, False
  if boyut == 4:
    sutunlar = {"A": 1, "B": 2, "C": 3, "D": 4}
  elif boyut == 5:
    sutunlar = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
  elif boyut == 6:
    sutunlar = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
  elif boyut == 7:
    sutunlar = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}
  else:
    sutunlar = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

  
  if oyuncuSirasi == oyuncu1:
    pasifOyuncu = oyuncu2
  else:
    pasifOyuncu = oyuncu1

  while not kontrol1 or not kontrol2 or not kontrol3 or not kontrol4 or not kontrol5 or not kontrol6 or not kontrol7 or not kontrol8 or not kontrol9 or not kontrol10 or not kontrol11:
    hamle = input(f"\nOyuncu {oyuncuSirasi}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz:")
    if RakamKontrol(hamle[0]) and HamleAralikKontrol(hamle[0], boyut) and RakamKontrol(hamle[3]) and HamleAralikKontrol(hamle[3], boyut):
      kontrol1 = True
    else:
      kontrol1 = False
      print(f"Lütfen satır numarasına 1 ile {boyut} arasında bir rakam girin!")
      continue
    if not HamleSutunKontrol(hamle, sutunlar):
      kontrol2 = False
      print("Lütfen oyun alanında mevcut olan sütunlardan birini giriniz!")
      continue
    else:
      kontrol2 = True
    if liste[int(hamle[3]) - 1][sutunlar[hamle[4].upper()] - 1] == " ":
      kontrol3 = True
    else:
      kontrol3 = False
      print("Taşı hareket ettirmek istediğiniz alan doludur. Lütfen başka bir yer girin.")
      continue
    if liste[int(hamle[0]) - 1][sutunlar[hamle[1].upper()] - 1] == " ":
      kontrol4 = False
      print("Girdiğiniz karede bir taş bulunamadı. Lütfen başka bir yer girin.")
      continue
    else:
      kontrol4 = True
    if liste[int(hamle[0]) - 1][sutunlar[hamle[1].upper()] - 1] == pasifOyuncu:
      kontrol5 = False
      print("Rakip oyuncunun taşını hareket ettiremezsiniz. Lütfen başka bir yer girin.")
      continue
    else:
      kontrol5 = True
    if int(hamle[0]) != int(hamle[3]) and sutunlar[hamle[1].upper()] != sutunlar[hamle[4].upper()]:
      print("Sadece dikey veya yatay hareket yapabilirsiniz!")
      kontrol6 = False
      continue
    else:
      kontrol6 = True
    if int(hamle[0]) == int(hamle[3]) and sutunlar[hamle[1].upper()] == sutunlar[hamle[4].upper()]:
      print("Hedef ve varış karelerini aynı girdiniz. Lütfen tekrar giriş yapın.")
      kontrol7 = False
      continue
    else:
      kontrol7 = True
    if int(hamle[0]) == int(hamle[3]): #aynı satırda gidilecekse
      sutunFarki = sutunlar[hamle[1].upper()] - sutunlar[hamle[4].upper()]
      kontrol8v2 = False
      if sutunFarki > 0: #sütunda azalmaya doğru gidiliyorsa(büyükten küçüğe gidiş)
        for i in range(1, sutunFarki + 1):
          if liste[int(hamle[0]) - 1][sutunlar[hamle[1].upper()] - 1 - i] != " ": #bir alt sütun boş değilse
            print("Taşı taşımak istediğiniz sütunda başka bir taş bulunduğundan hamle geçersizdir!")
            kontrol8 = False
            kontrol8v2 = True
            break
      if kontrol8v2:
        continue
      else:
        kontrol8 = True
    else:
      kontrol8 = True
    if int(hamle[0]) == int(hamle[3]): #aynı satırda gidilecekse
      sutunFarki = sutunlar[hamle[1].upper()] - sutunlar[hamle[4].upper()]
      kontrol9v2 = False
      if sutunFarki < 0: #sütunda artmaya doğru gidiliyorsa(küçükten büyüğe gidiş)
        sutunFarki = abs(sutunFarki) #sütun farkını döngüde kullanmak için mutlak değerini alıyoruz
        for i in range(1, sutunFarki + 1):
          if liste[int(hamle[0]) - 1][sutunlar[hamle[1].upper()] - 1 + i] != " ": #bir üst sütun boş değilse
            print("Taşı taşımak istediğiniz sütunda başka bir taş bulunduğundan hamle geçersizdir!")
            kontrol9 = False
            kontrol9v2 = True
            break
      if kontrol9v2:
        continue
      else:
        kontrol9 = True
    else:
      kontrol9 = True
    if sutunlar[hamle[1].upper()] == sutunlar[hamle[4].upper()]: #aynı sütunda gidilecekse
      kontrol10v2 = False
      satirFarki = int(hamle[0]) - int(hamle[3])
      if satirFarki > 0:
        for i in range(1, satirFarki + 1):
          if liste[int(hamle[0]) - 1 - i][sutunlar[hamle[1].upper()] - 1] != " ": 
            kontrol10v2 = True
            kontrol10 = False
            print("Taşı taşımak istediğiniz satırda başka bir taş bulunduğundan hamle geçersizdir!")
            break
      if kontrol10v2:
        continue
      else:
        kontrol10 = True
    else:
      kontrol10 = True
    if sutunlar[hamle[1].upper()] == sutunlar[hamle[4].upper()]: #aynı sütunda gidilecekse
      kontrol11v2 = False
      satirFarki = int(hamle[0]) - int(hamle[3])
      if satirFarki < 0:
        satirFarki = abs(satirFarki) #satır farkını döngüde kullanmak için mutlak değerini alıyoruz
        for i in range(1, satirFarki + 1):
          if liste[int(hamle[0]) - 1 + i][sutunlar[hamle[1].upper()] - 1] != " ": 
            print("Taşı taşımak istediğiniz satırda başka bir taş bulunduğundan hamle geçersizdir!")
            kontrol11v2 = True
            kontrol11 = False
            break
      if kontrol11v2:
        continue
      else:
        kontrol11 = True
    else:
      kontrol11 = True
            
  
  liste[int(hamle[0]) - 1][sutunlar[hamle[1].upper()] - 1] = " " #hareket ettirilen taşın yeri boşaltıldı
  liste[int(hamle[3]) - 1][sutunlar[hamle[4].upper()] - 1] = oyuncuSirasi

  liste = TasKilitle(liste, hamle, boyut, oyuncu1, oyuncu2)

  return liste

def KomsulukKontrol(hamleSatiri, hamleSutunu, hedefSatir, hedefSutun):
  if abs(hamleSatiri - hedefSatir) == 1 and abs(hamleSutunu - hedefSutun) != 1: #eğer dikey komşuluk varsa
    return 1
  
  if abs(hamleSatiri - hedefSatir) != 1 and abs(hamleSutunu - hedefSutun) == 1: #eğer yatay komşuluk varsa
    return 2

  return 0 #herhangi bir komşuluk yoksa

def TasKilitle(liste, hamle, boyut, oyuncu1, oyuncu2):
  sutunlar = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
  sutunlarTers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
  kilitSayaci = 0 #bu sayaç 2 olursa yani en az 2 tarafında rakip taş varsa taş kilitlenecek
  

  #önce durumları farklı olduğu için 4 köşenin kontrolünü yapıyoruz, aşağıdaki döngüde köşeler gelince continue diyerek atlayacağız kontrollerini
  if KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, 0, 0) != 0 and liste[0][0] != " ": #sol üst köşe ile son hamledeki taş komşu ise ve sol üst boş değilse
    if liste[0][0] == oyuncu1 or liste[0][0] == oyuncu2: #sol üst köşe
      if liste[0][1] != liste[0][0] and liste[0][1] != " ":
        kilitSayaci += 1
      if liste[1][0] != liste[0][0] and liste[1][0] != " ":
        kilitSayaci += 1
      if kilitSayaci == 2: #2 tarafında da rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
            liste[0][0] = " "
            print(f"\n**************************************************\n1a konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")
      kilitSayaci = 0

  if KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, boyut - 1, 0) != 0 and liste[boyut - 1][0] != " ": #sol alt köşe ile son hamledeki taş komşu ise ve sol alt boş değilse
    if liste[boyut - 1][0] == oyuncu1 or liste[boyut - 1][0] == oyuncu2: #sol alt köşe
      if liste[boyut - 1][1] != liste[boyut - 1][0] and liste[boyut - 1][1] != " ":
        kilitSayaci += 1
      if liste[boyut - 2][0] != liste[boyut - 1][0] and liste[boyut - 2][0] != " ":
        kilitSayaci += 1
      if kilitSayaci == 2: #2 tarafında da rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
            liste[boyut - 1][0] = " "
            print(f"\n**************************************************\n{boyut}a konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")
      kilitSayaci = 0

  if KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, 0, boyut - 1) != 0 and liste[0][boyut - 1] != " ": #sağ üst köşe ile son hamledeki taş komşu ise ve sağ üst boş değilse
    if liste[0][boyut - 1] == oyuncu1 or liste[0][boyut - 1] == oyuncu2: #sağ üst köşe
      if liste[0][boyut - 2] != liste[0][boyut - 1] and liste[0][boyut - 2] != " ":
        kilitSayaci += 1
      if liste[1][boyut - 1] != liste[0][boyut - 1] and liste[1][boyut - 1] != " ":
        kilitSayaci += 1
      if kilitSayaci == 2: #2 tarafında da rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
            liste[0][boyut - 1] = " "
            print(f"\n**************************************************\n1{sutunlar[boyut].lower()} konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")
      kilitSayaci = 0

  if KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, boyut - 1, boyut - 1) != 0 and liste[boyut - 1][boyut - 1] != " ": #sağ alt köşe ile son hamledeki taş komşu ise ve sağ alt boş değilse
    if liste[boyut - 1][boyut - 1] == oyuncu1 or liste[boyut - 1][boyut - 1] == oyuncu2: #sağ alt köşe
      if liste[boyut - 2][boyut - 1] != liste[boyut - 1][boyut - 1] and liste[boyut - 2][boyut - 1] != " ":
        kilitSayaci += 1
      if liste[boyut - 1][boyut - 2] != liste[boyut - 1][boyut - 1] and liste[boyut - 1][boyut - 2] != " ":
        kilitSayaci += 1
      if kilitSayaci == 2: #2 tarafında da rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
            liste[boyut - 1][boyut - 1] = " "
            print(f"\n**************************************************\n{boyut}{sutunlar[boyut].lower()} konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")
      kilitSayaci = 0

  
  for i in range(boyut):
    for j in range(boyut):
      if (i == 0 and j == 0) or (i == boyut - 1 and j == 0) or (i == 0 and j == boyut - 1) or (i == boyut -1 and j == boyut - 1): #herhangi bir köşe noktayı kontrol etmeden atlıyoruz
        continue
      if i == int(hamle[3]) - 1 and j == sutunlarTers[hamle[4].upper()] - 1: #son hamlede oynattığımız taşı da atlıyoruz çünkü intihar etmesine izin vermiyoruz
        continue
      if liste[i][j] == " ": #boş kareler için kontrol etmeye gerek yok
        continue
      kilitSayaci = 0

      if KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, i, j) == 1: #eğer döngüde sırası gelen kare ile son hamlede oynatılan kare dikey komşu ise sadece dikeye bakılacak
        kilitSayaci = 0
        if liste[i][j] == oyuncu1 or liste[i][j] == oyuncu2: #tabloda oyuncu1'e ait bir taş bulduk, etrafındaki karelere bakacağız
          if i != 0: #indis 0 değilse bir öncesine bakılabilir
            if liste[i-1][j] != liste[i][j] and liste[i-1][j] != " ": #bir gerisinde rakip oyuncu varsa
              kilitSayaci += 1
            if kilitSayaci == 1:
              if i != boyut - 1: #indis sonda değilse bir sonrasına bakılabilir
                if liste[i+1][j] != liste[i][j] and liste[i+1][j] != " ": #bir ilerisinde rakip oyuncu varsa
                  kilitSayaci += 1
        if kilitSayaci == 2: #en az 2 tarafında rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
          liste[i][j] = " "
          print(f"\n**************************************************\n{i+1}{sutunlar[j+1].lower()} konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")

      elif KomsulukKontrol(int(hamle[3]) - 1, sutunlarTers[hamle[4].upper()] - 1, i, j) == 2: #komşuluk yataydaysa sadece yatayda kilitlenme var mı diye bakılacak
        kilitSayaci = 0
        if j != 0: #şimdi de sütununa göre bakılacak
          if liste[i][j-1] != liste[i][j] and liste[i][j-1] != " ":
            kilitSayaci += 1
        if j != boyut - 1:
          if liste[i][j+1] != liste[i][j] and liste[i][j+1] != " ":
            kilitSayaci += 1
        
        if kilitSayaci == 2: #en az 2 tarafında rakip taş tespit edildiğinden taş kilitlenecek(silinecek)
          liste[i][j] = " "
          print(f"\n**************************************************\n{i+1}{sutunlar[j+1].lower()} konumundaki taş kilitlendi ve dışarı çıkarıldı.\n**************************************************")

  return liste
      


def KazananVarMi(liste, boyut, oyuncu1, oyuncu2):
  oyuncu1TasSayaci, oyuncu2TasSayaci = 0, 0
  for i in range(boyut):
    for j in range(boyut):
      if liste[i][j] == oyuncu1:
        oyuncu1TasSayaci += 1
      elif liste[i][j] == oyuncu2:
        oyuncu2TasSayaci += 1
  if oyuncu1TasSayaci < 2:
    return oyuncu2
  elif oyuncu2TasSayaci < 2:
    return oyuncu1
  else:
    return -1


def main():

  OyunBaslat()


main()