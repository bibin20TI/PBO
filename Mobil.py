
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
        self.__muatan = muatan_max #private property maksudnya property ini
        #hanya bisa di akses oleh class itu sendiri
        #dan kita akan akses property ini dengan menggunakan 
        #method yang visibiliy public 

    def maxMuatan(self, muatan):   #ini dia method yang bisa di akses di luar class atau biasa di sebut dengan setter & getter
        return self.__muatan  #private hanya bisa di akses oleh class itu sendiri 
                                              
# sedan =  Mobil(4, "auto", "mazda")
# truck = Mobiltruck(8, "manual", "hino", 1000)
#kita akan import dan inisiasikan class ini di file main.pyatan(1000));  #mencoba akses method visibility public dengan property
#private
