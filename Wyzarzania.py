# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:40:47 2020

@author: LENOVO
"""
import math
import random

#temperatura początkowa
T=1
#współczynnik stygnięcia
a=0.9
#liczba epok
e=100
#liczba prób
pr=10

wymiar=2

#funkcja dla wymiaru 2
def fun(x):
    return x*x

# funkcja która decyduje czy daną wartosc zamienic z x czy nie
def decyzja(x,xp,temp):
    prawd=math.exp((fun(xp)-fun(x))/temp)
    liczba = random.uniform(0,1)
    if(liczba<prawd):
        return True
    else:
        return False


def Annealing(p,k,e,pr,a,T):
    # losujemy wartosc początkową
    x=random.uniform(-10,10)
   
    for j in range(e):
        for i in range(pr):
            #ustawiamy wartosci początku i końca przedziału( są one zależne od temperatury)
            k=x+2*T
            if(k>10):
                k=10
            p=x-2*T
            if(p<-10):
                p=-10
            
            xprim=random.uniform(p,k)
            if(fun(xprim)>fun(x)):
                x=xprim
                
            else:
                if(decyzja(x,xprim,T)==True):
                    x=xprim
        T=T*a
        if(j==e-1)and(i==pr-1):
            print("maksimum funkcji: ",x,"wartosc: ",fun(x))
            

Annealing(-10,10,100,15,0.9,1)
        



    
