dict = {'Nama':'Rahma Anggana Rarastyasa', 'Hobi 1': 'Jalan-Jalan', 'Hobi 2':'Menonton Film','Hobi 3':'Membaca', 'Sosial Media 1':'Instagram @rarastyasa_ra', 'Sosial Media 2':'Twitter @rarastyasa', 'Sosial Media 3':'Email rararastyasa@student.uns.ac.id',
        'Lagu Kesukaan 1':'Lose-Niki Zefanya','Lagu Kesukaan 2':'Blue Jeans-Gangga','Lagu Kesukaan 3':'Driver Licence-Olivia Rodrigo', 'Makanan Favorit 1':'Nasi Goreng','Makanan Favorit 2':'Sate','Makanan Favorit 3':'Bakso'}

print(dict)
dict['Hobi 3'] = "Bulu Tangkis"
dict['Sosial Media 2'] = "ID Line rarastyasa_ra"

del dict['Makanan Favorit 2']
del dict['Makanan Favorit 3']

dict['Hobi 4'] = "Bersepeda"
print(dict)