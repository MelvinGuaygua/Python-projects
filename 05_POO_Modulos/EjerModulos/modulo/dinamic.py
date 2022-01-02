from modulo.step import *
   
archivo = "C60.xyz"
text = open(archivo).readlines()
atomos = obtenerAtomos() #lista de todos los atomos
def obtenerDinamic():
    dinamic=[]    
    a=0
    b=60
    for i in range(188): #porque hay 188 steps
        step=[]
        for i in range(a,b):
            step.append(atomos[i])
        dinamic.append(step)
        a+=60
        b+=60
    return dinamic
