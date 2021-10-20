class Mobil():

    def __init__(self, jumlah_roda, transmisi, merk):  
        self.jumlah_roda = jumlah_roda                        
        self.transmisi = transmisi                            
        self.merk = merk  

    def jalankan(self):
        print("ayo jalan "+self.merk)	

class Mobiltruck(Mobil):                                                                
     pass                                 
   
sedan = Mobil(4, "auto", "mazda")
truck = Mobiltruck(8, "manual", "volvo")
sedan.jalankan()
truck.jalankan()
 
    	
