import random
from class_AGenerate import aGenerate
from class_BGenerate import bGenerate
from class_VectorGenerate import vectorGenerate

class SequenceGenerate():
    def __init__(self): # aşağıda olanlar def'ler içinde kullanılmalı ama nasıl?
        self.states= aGenerate().states
        self.symbols= bGenerate().symbols
        self.init= vectorGenerate().vector        
        self.A= aGenerate().a
        self.B= bGenerate().b   
        self.sequence_dizisi= []  # sequence dizisini [a,b,a] şeklinde
        self.state_dizisi=[] # S2,S1,S2
        self.generateSequence()


    def generateSequence(self):
        n=int(input("kaç kez çalişsin? : "))
        self.initialState()
        self.generateSymbol(1) # (1), sayiOkuyucuyu bozar mı? !!
        for i in range(n):
            self.generateSymbol(1)
            self.nextState(1)
        for j in range(len(self.state_dizisi)):
            sequence={"t" : f"{j}","state": f"{self.state_dizisi[j]}","symbol": f"{self.sequence_dizisi[j]}"} # key_value
            print("sequence böyle olur: ",sequence)
        # for döngüsü içinde t0,t1=S1,S2.. bunları sırayla t'lere eşitle (list içinde list olur, diğer kısımlarda kullanılacaktır!!) 
    def initialState(self):
        total=0
        sayac=0
        sayi= round(random.random(),2)
        for i in range(len(self.states)): # states i için kullanıldığında: random sayısı, en sonuncunun da sağında olursa problem olmaz çünkü total mantığı
            if(sayi<=self.init[i]+total): 
                self.state_dizisi.append(self.states[sayac])
                break
            else:
                total+= self.init[i]
                sayac+=1

    def generateSymbol(self,sayiOkuyucu): 
        total= 0
        sayac=0
        sayi=round(random.random(),2)
        for i in self.B[self.sayiOkuyucu()]: 
            if(sayi<=i+total): 
                self.sequence_dizisi.append(self.symbols[sayac])
                break
            else:
                total+= i 
                sayac+=1
       
    def sayiOkuyucu(self):
        okuyucu_state=self.state_dizisi[-1]
        okuyucu_state=int(okuyucu_state.replace("S",""))-1 # burası, üretilen olasılık değerler listesinde doğru tuple bloğunun alınmasını sağlıyor
        return okuyucu_state
    
    def nextState(self,sayiOkuyucu): # her S için farklı çıktı değerleri oluşmalı
        total= 0
        sayac=0
        sayi=round(random.random(),2)
        for i in self.A[self.sayiOkuyucu()]:
            if(sayi<=i+total): 
                self.state_dizisi.append(self.states[sayac])
                break
            else:
                total+=i
                sayac+=1
                
obje= SequenceGenerate()
