#CLASE ATOMO
class Atom:
    atomo=""
    posicionX=0
    posicionY=0
    posicionZ=0
    def __init__(self, atomo, posicionX,posicionY,posicionZ):
        self.atomo=atomo
        self.posicionX=posicionX
        self.posicionY=posicionY
        self.posicionZ=posicionZ
    def info(self):
        print(self.atomo,self.posicionX,self.posicionY,self.posicionZ)
    def distancia(self,atomo2):
        self.atomo2 = atomo2
        num1 = float(self.atomo2.posicionX) - float(self.posicionX)
        num1 = num1**2
        
        num2 = float(self.atomo2.posicionY) - float(self.posicionY)
        num2 = num2**2
        
        num3 = float(self.atomo2.posicionZ) - float(self.posicionZ)
        num3 = num3**2
        
        resul = num1+num2+num3
        resul = resul**0.5
        
        print('{:,.6f}'.format(resul))
#         print(resul)