def loginnih():
  password = "0857"
  
  print ("\n===========FORM LOGIN===========")
  nama_user = input("Masukan nama: ")
  print (f"Selamat datang {nama_user}")
  pass_user = input("Masukan password: ")
  if pass_user == password:
    print ("Password benar,selamat datang")
  else:
    print ("Password kamu salah")
    input("Masukan password: ")
   