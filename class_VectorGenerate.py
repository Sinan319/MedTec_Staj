import random
from class_Manager import manager

class vectorGenerate:
    def __init__(self):
        self.vector=[]
        self.states= manager().durum
        self.sayi_uret_PI()
    def oran(self,line):
        toplam= sum(line)
        for i in range(len(line)):
            line[i]= round(line[i]/toplam,2)
    def sayi_uret_PI(self): 
        for i in range(len(self.states)):
            self.vector.append(round(random.random(),2))
        self.oran(self.vector)

# obje= vectorGenerate()
# print(obje.vector)