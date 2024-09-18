
import random
secenekler = ["rock","paper","scissors"]
a = random.choice(secenekler)

b = input("rock, paper , scissors ")

if a==b : 
    print(a)
    print("draw")
elif a=="rock" and b=="paper" : 
    print(a)
    print("lose")
elif a=="rock" and b=="scissors" : 
    print(a)
    print("win")
    
elif a=="paper" and b=="rock" : 
    print(a)
    print("win")
elif a=="paper" and b=="scissors" : 
    print(a)
    print("lose")
elif a=="scissors" and b=="rock" : 
    print(a)
    print("lose")
elif a=="scissors" and b=="paper" : 
    print(a)
    print("win")
else : 
    print( "hata")
    



   