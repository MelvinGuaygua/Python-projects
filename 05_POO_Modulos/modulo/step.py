from modulo.atom import *

archivo = "C60.xyz"
text = open(archivo).readlines()

#ESTA FUNCION DEVUELVE UNA LISTA CON TODOS LOS ATOMOS
n=60
def obtenerAtomos():
    dinamic=[]    
    a=2
    b=62
    step=[]
    for i in range(188): 
        for i in range(a,b):
            step.append(Atom(text[i].split()[0],text[i].split()[1],text[i].split()[2],text[i].split()[3]))
        a+=62
        b+=62
    return step
   