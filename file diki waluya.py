nama_saya = str("Nama = Diki Waluya")
print(nama_saya, type(nama_saya))

NIM = str("NIM = 230441100151")
print (NIM, type(NIM))

print()

#meengonversi suhu derajat celcius menjadi derajat fahrenheit
celsius = int(input("masukkan suhu dalam derajat celcius : "))
fahrenheit = int((celsius*(9/5))+32)

print ("jika celcius =",celsius,"derajat celcius","maka farenheit =",fahrenheit,"derajat fahrenheit")

print()

#mengonversi suhu derajat fahrenheit menjadi derajat celcius
fahrenheit = int(input("masukkan suhu dalam derajat fahrenheit : "))
celsius = int(((5*fahrenheit)-(5*32))/9)

print ("jika fahrenheit =",fahrenheit,"derajat fahrenheit","maka celsius =",celsius,"derajat celcius")
