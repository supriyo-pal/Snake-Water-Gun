# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:46:37 2020

@author: Supriyo
"""

import random

#counter to check how many times the incidents happends
you_win=0
comp_win=0
draw=0
b=1

    
while b:
    you=input("Choose Snake(s) / Water(w) / Gun(g) ")
    
    # Funtion to implement the strategy
    def win(comp,you):
        print("Compuer Choose ",comp)
        print("You Choose ",you)
        if comp==you:
            return None
        
        elif comp=='w':
            if you=='g':
                return False
            elif you=='s':
                return True
        
        
        elif comp=='g':
            if you=='w':
                return True
            elif you=='s':
                return False
        
        elif comp=='s':
            if you=='g':
                return True
            elif you=='w':
                return False
            
    comp=random.randint(1,3) #Coputer will generate a random number between from 1 to 3
    if comp==1:
        comp='s'
    elif comp==2:
        comp='w'
    elif comp==3:
        comp='g'
    a_win=win(comp,you)#calling of the defined function
    
    print("Game Result \n")
    if a_win==True:
        print("You win ")
        you_win+=1#incrementing the counter
    elif a_win==None:
        print("Match Draw ")
        draw+=1
    elif a_win==False:
        print("Computer win")
        comp_win+=1
    
    again=input("Do you want to play again ? y/n ")#asking the user to continue or not
    if again=='y':
        b=1
    else:
        b=0

#printing the result 
print("You Wins :",you_win, " times")
print("Computer wins :",comp_win," times")
print("Match draw :",draw," times")


