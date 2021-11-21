class Mobil_overidding():
                                                                                     #nama: Bibin aripin
    def __init__(self, jumlah_roda, transmisi, merk):                                #kelas : TI20C
        self.jumlah_roda = jumlah_roda                                               #NIM : 20200040002
        self.transmisi = transmisi                                                   #TUGAS OOP : inheritance(pewarisan)
        self.merk = merk
       

    def __add__(self,pabrikan):
        return pabrikan.merk

    def jalankan(self):                                          #method jalankan class parent 
        print("ayo jalan "+self.merk)
class Mobiltruck(Mobil_overidding):                                                                
     
    def __init__(self, jumlah_roda, transmisi, merk, muatan_max):

        super().__init__(jumlah_roda, transmisi, merk)
        self.muatan = muatan_max

    def maxMuatan(self, muatan):
        print("max muatan "+self.muatan)  

    def jalankan(self):                                            #method jalankan class child
        print("ayo jalan "+self.merk)                              #overide method jalankan pada class Mobiltruck
                                 
#class ini juga akan di import ke file main.py