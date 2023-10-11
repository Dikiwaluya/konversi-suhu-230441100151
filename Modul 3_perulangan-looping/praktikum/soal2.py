awal = int(input("Masukkan batas awal: "))
akhir = int(input("Masukkan batas akhir: "))

print(f"Bilangan prima antara {awal} dan {akhir} adalah:")

for i in range(awal, akhir+1):
  if i > 1:
    for n in range(2, i):
      if (i % n) == 0:
        break
    else:
      print(i)