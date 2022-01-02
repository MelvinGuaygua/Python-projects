from modulo.dinamic import *
import sys


dinamic = obtenerDinamic()

# for i in range(188):
#     dinamic[i][4].distancia(dinamic[i][41])

# print(sys.argv)

a=int(sys.argv[1])
b=int(sys.argv[2])

def ejecutar(a,b):
    for i in range(188):
        dinamic[i][a].distancia(dinamic[i][b])
    
ejecutar(a,b)
  