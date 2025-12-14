def nilai():
  print("\n=======================")
  print("CODE HITUNG NILAI BY ZIDANE")
  print("\n=======================")
  
  
  
  nilai_mtk = float(input("Masukan nilai MTK: "))
  nilai_bindo = float(input("Masukan nilai B.Indo: "))
  nilai_pkn = float(input("Masukan nilai Pkn: "))
  nilai_tik = float(input("Masukan nilai TIK: "))
  nilai_binggris = float(input("Masukan nilai B.Inggris: "))
  nilai_agama = float(input("Masukan nilai Agama: "))
  nilai_ipa = float(input("Masukan nilai IPA: "))
  nilai_ips = float(input("Masukan nilai IPS: "))
  
  total_nilai = (nilai_mtk + nilai_bindo + nilai_pkn + nilai_tik + nilai_binggris + nilai_agama + nilai_ipa + nilai_ips)/ 8
  if total_nilai >= 100:
    print(total_nilai)
    print("SELAMAT KAMU LULUS DENGAN NILAI SEMPURNA ")
  if total_nilai <= 99:
    print(total_nilai)
    print("SELAMAT KAMU LULUS DENGAN NILAI YANG BAGUS")
  if total_nilai <= 82:
    print(total_nilai)
    print("SELAMAT KAMU LULUS DENGAN NILAI CUKUP BAGUS ")
  if total_nilai <= 78:
    print(total_nilai)
    print("SELAMAT KAMU LULUS DENGAN NILAI KKM")
  if total_nilai <= 70:
    print(total_nilai)
    print("MAAF KAMU TIDAK LULUS,COBA LAGI DI SEMESTER DEPAN")
   