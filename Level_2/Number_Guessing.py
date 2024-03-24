import random as rd

def find(n,key):

    if n == key :
        return True
    
    if n > key :
        n = int(input("Your number is too high, enter small number : "))
        return find(n,key)
    
    if n < key :
        n = int(input("Your number is too low, enter greater number : "))
        return find(n, key)

while True :

    print("\n!!!---------------Game Started---------------!!!")
    
    key = rd.randint(0,100)
    
    n = int(input("Enter a number b/w 1 to 100 : "))
    ans = find(n, key)
    
    print()
    print("Wow!, You Entered Correct Number.....!!!")
    print()
    
    print("!!!~~~~~~~~~~~~~~YOU WON THE GAME~~~~~~~~~~~~~~!!!")
    print()
    
    print("!!!................Game Over...................!!!\n")
    
    if ans:
        s = input("Do you want to Play Again Y / n ? : ")
        
        if s == 'Y':
            continue
        
        elif s == 'n':
            print()
            print("!!!............Thank You For Playing............!!!")
            print()
            break