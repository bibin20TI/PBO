class Mobil():
	    
    def __init__(self, jumlah_roda, transmisi, warna, merk):  # Nama  : Bibin aripin
    	self.jumlah_roda = jumlah_roda                        # Kelas : TI20C
    	self.transmisi = transmisi                            # NIM   : 20200040002
    	self.warna = warna                                    # Mata Kuliah : Pemograman Berorientasi Objek
    	self.merk = merk
    	
    def jalankan(self):
        print("ayo jalan "+self.merk)	

sedan = Mobil(4, 'auto', 'putih', 'mazda')
print(sedan.__dict__)
sedan.jalankan()
