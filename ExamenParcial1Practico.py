#A01197677
#Erasmo Villarreal Sánchez
from random import *
from string import *
abecedario = ascii_lowercase
letraRandom= choice(ascii_lowercase)
letra = input("Ingresa la letra: ")
letraR= 0 #posicion de la letra random
letraIn= 0 #posicion de la letra que inputeo
count = 1
intentos= 0
for i in range(0,len(abecedario)):
    if letraRandom==abecedario[i]:
        letraR =  i
        #print(letraR, letraRandom, "random")
    if letra == abecedario[i]:
        letraIn = i  
        #print(letraIn,letra, "letra inputeada")
while letra != letraRandom:
    if letraR == letraIn:
            print("ganaste")
    if letraR < letraIn:
            print("menos")
            letra = input("ingresa la letra: ") 
            count+=1        
    elif letraR > letraIn:   
            print("mas")
            letra = input("ingresa la letra: ")
            count+=1 

print(count, "le atinaste despues de estos intentos")



    



