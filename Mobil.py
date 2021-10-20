class Mobil():
                                                                                     #nama: Bibin aripin
    def __init__(self, jumlah_roda, transmisi, merk):                                #kelas : TI20C
        self.jumlah_roda = jumlah_roda                                               #NIM : 20200040002
        self.transmisi = transmisi                                                   #TUGAS OOP : inheritance(pewarisan)
        self.merk = merk  

    def jalankan(self):                                          #method jalankan class parent 
        print("ayo jalan "+self.merk)
class Mobiltruck(Mobil):                                                                
     
    def __init__(self, jumlah_roda, transmisi, merk, muatan_max):

        super().__init__(jumlah_roda, transmisi, merk)
        self.muatan = muatan_max

    def maxMuatan(self, muatan):
        print("max muatan "+self.muatan)  

    def jalankan(self):                                            #method jalankan class child
        print("ayo jalan "+self.merk)                              #overide method jalankan pada class Mobiltruck
                                 
sedan = Mobil(4, "auto", "mazda")
sedan.jalankan()
truck = Mobiltruck(8, "manual", "hino", 1000)
truck.jalankan()

print(sedan.__dict__)
print(truck.__dict__)
  
 