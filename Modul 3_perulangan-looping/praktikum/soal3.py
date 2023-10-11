while True:
  lamaPinjam = int(input("lama peminjaman buku : "))

  dendaPerhari = 2000
  dendaPerminggu = 5000
  totalDenda = 0
  
  for i in range(1, lamaPinjam+1):
    if i > 7:
      totalDenda += dendaPerhari
      if i % 7 == 0:
        totalDenda += dendaPerminggu

  if totalDenda == 0:
    print(f"terima kasih telah meminjam buku")
  else:
    print(f"Anda telah melewati batas peminjaman selama {lamaPinjam-7} dan anda terkena denda sebesar Rp.{totalDenda}")
  while True:
    ulang = input("hitung lagi? (ya/tidak):")
    if ulang.lower() == "tidak":
      break
    elif ulang.lower() == "ya":
      break
    else:
      print("masukkan yang bener bang")

  if ulang.lower() == "tidak":
      print("selesai")
      break