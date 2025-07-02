import random
from class_Manager import manager

class aGenerate:
    def __init__(self):
        self.a=[]
        self.states= manager().durum
        self.sayi_uret_a()
    def oran(self,line):
        toplam= sum(line)
        for i in range(len(line)):
            line[i]= round(line[i]/toplam,2)
    def sayi_uret_a(self): 
        for i in range(len(self.states)):
            subMatrix=[]
            for j in range(len(self.states)):
                subMatrix.append(round(random.random(),2))
            self.oran(subMatrix)
            self.a.append(subMatrix)

obje=aGenerate()
print(obje.a)
#yukarıdaki kısım a'yı test etmek için 