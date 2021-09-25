<?php 
   
   class Tugas2 {

      private $warna;
      private $transmisi = "manual";
      private $jumlahRoda;


      public function jalankan($warna,$jumlahRoda)
      {
      	$this->warna;
      	$this->jumlahRoda;
      	$this->transmisi;
        
        $message = "Mobil berwarna ".$this->warna." dengan jumlah roda ".$this->jumlahRoda." dengan transmisi ".$this->transmisi;
      	return $message;
      }

   }

   $mobil = new Tugas2();
   echo $mobil->jalankan("Merah",4);




 ?>