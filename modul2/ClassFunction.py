class Titik (object) :
  # Constructor
  def __init__(self, x = 0, y = 0) :
    self.x = x
    self.y = y

  def pindah(self, x, y) :
    self.x = x
    self.y = y
  
  def cetak(self) : 
    print(f'{self.x}, {self.y}')


titik = Titik()
titik.cetak()
titik.pindah(5,10)
titik.cetak()