size = int(input("Masukkan size: "))
rumus = int(size/2) 


# angka 1
for i in range(1, size+1):
    print(" " * size+"x")
print ()

# # angka 5
print("x" * size)
for i in range(1, rumus):
    print("x") 
print("x" * size)
for i in range(1, rumus):
    print(" " * (size-1) +"x") 
print("x" * size)
print ()

# angka 1
for i in range(1, size+1):
    print(" " * size+"x")