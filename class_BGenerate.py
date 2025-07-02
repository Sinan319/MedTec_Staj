import random
from class_Manager import manager
class bGenerate:
    def __init__(self):
        self.b=[]
        self.symbols= manager().sembol
        self.states=  manager().durum
        self.sayi_uret_b()
    def oran(self,line):
        toplam= sum(line)
        for i in range(len(line)):
            line[i]= round(line[i]/toplam,2)
    def sayi_uret_b(self): 
        for i in range(len(self.states)):
            subMatrix=[]
            for j in range(len(self.symbols)):
                subMatrix.append(round(random.random(),2))
            self.oran(subMatrix)
            self.b.append(subMatrix)

# obje= bGenerate()
# print(obje.b)