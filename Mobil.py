class Mobil():
                                                                                     #nama: Bibin aripin
    def __init__(self, jumlah_roda, transmisi, merk):                                #kelas : TI20C
        self._jumlah_roda = jumlah_roda             #protected                                  #NIM : 20200040002
        self.transmisi = transmisi                  #public                                 #TUGAS OOP : inheritance(pewarisan)
        self.merk = merk  

    def jalankan(self):
        print("ayo jalan "+self.merk)   

class Mobiltruck(Mobil):                                                                
     
    def __init__(self, jumlah_roda, transmisi, merk, muatan_max):

        super().__init__(jumlah_roda, transmisi, merk)
        self.__muatan = muatan_max

    def maxMuatan(self, muatan):   #tapi method ini bisa di akses di luar class namanya setter getter
        return self.__muatan  #private hanya bisa di akses oleh class itu sendiri 
                                              #contoh di sini class Mobiltruck
sedan = Mobil(4, "auto", "mazda")
sedan.jalankan()
truck = Mobiltruck(8, "manual", "hino", 1000)

print("truck mampu menampung beban ",truck.maxMuatan(1000));  #mencoba akses method visibility public dengan property
#private

print(sedan.__dict__)
print(truck.__dict__)
print("truck mampu menampung beban ",truck.maxMuatan(1000));  #mencoba akses method visibility public dengan property
#private
