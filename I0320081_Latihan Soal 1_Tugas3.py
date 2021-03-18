print ("***Daftar Nama***")
Teman_kelasB = ['Alam', 'Ojat', 'Hani', 'Mira', 'Rafli', 'Ilham', 'Ivan', 'Memed', 'Hilmy', 'Hasan']
print (Teman_kelasB)
#Menampilkan List Index
print ("Nama index ke [4] adalah", Teman_kelasB[4])
print ("Nama index ke [6] adalah", Teman_kelasB[6])
print ("Nama index ke [7] adalah", Teman_kelasB[7])
#Mengganti Nama Teman
Teman_kelasB[3] = 'Hafiz'
Teman_kelasB[5] = 'Iffa'
Teman_kelasB[9] = 'Nadiya'
#Menambah Nama Teman
Teman_kelasB.append("Vika")
Teman_kelasB.append("Issa")
#Menampilkan Perulangan Nama Teman
f = 0
for j in range(0,12):
    print(Teman_kelasB[f])
    f = f+1
print(len(Teman_kelasB))