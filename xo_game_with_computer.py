import random as r
a11 = "-"
a12 = "-"
a13 = "-"
a21 = "-"
a22 = "-"
a23 = "-"
a31 = "-"
a32 = "-"
a33 = "-"
loop = True
played = []
def printxo():
    print(a11,a12,a13)
    print(a21,a22,a23)
    print(a31,a32,a33)

def refresh():
    global a11,a12,a13,a21,a22,a23,a31,a32,a33,loop,played
    a11 = "-"
    a12 = "-"
    a13 = "-"
    a21 = "-"
    a22 = "-"
    a23 = "-"
    a31 = "-"
    a32 = "-"
    a33 = "-"
    loop = True
    played = []
def player1():
    global played
    playing = int(input("Player1   : Enter the row and colomn number => "))
    while(1):
        if(playing not in [11,12,13,21,22,23,31,32,33]):
            playing = int(input("Player1   : Enter the row and colomn number => "))
        else:
            break
    playing = str(playing)
    playing = 'a'+playing[:]
    while(playing in played):
        print(playing," already exits")
        playing = int(input("Player1   : Enter the row and colomn number => "))
        playing = str(playing)
        playing = 'a'+playing[:]
    played.append(playing)
    if(playing == 'a11'):
        global a11
        a11 = "X"
    elif(playing == 'a12'):
        global a12
        a12 = "X"
    elif(playing == 'a13'):
        global a13
        a13 = "X"
    elif(playing == 'a21'):
        global a21
        a21 = "X"
    elif(playing == 'a22'):
        global a22
        a22 = "X"
    elif(playing == 'a23'):
        global a23
        a23 = "X"
    elif(playing == 'a31'):
        global a31
        a31 = "X"
    elif(playing == 'a32'):
        global a32
        a32 = "X"
    elif(playing == 'a33'):
        global a33
        a33 = "X"
    printxo()
    print("\n")

def defence():
    if(((a11==a12=='X') and (a13 != 'X')) or ((a31==a22=='X') and (a13 != 'X')) or ((a33==a23=='X') and (a13 != 'X'))):
        return 'a13'
    elif(((a11==a13=='X') and (a12 != 'X')) or ((a22==a32=='X') and (a12 != 'X'))):
        return 'a12'
    elif(((a13==a12=='X') and (a11 != 'X')) or ((a33==a22=='X') and (a11 != 'X')) or ((a31==a21=='X') and (a11 != 'X'))):
        return 'a11'
    elif(((a21==a22=='X') and (a23 != 'X')) or ((a13==a33=='X') and (a23 != 'X'))):
        return 'a23'
    elif(((a21==a23=='X') and (a22 != 'X')) or ((a11==a33=='X') and (a22 != 'X')) or ((a12==a32=='X') and (a22 != 'X')) or ((a13==a31=='X') and (a22 != 'X'))):
        return 'a22'
    elif(((a23==a22=='X') and (a21 != 'X')) or ((a11==a31=='X') and (a21 != 'X'))):
        return 'a21'
    elif(((a31==a32=='X') and (a33 != 'X')) or ((a11==a22=='X') and (a33 != 'X')) or ((a13==a23=='X') and (a33 != 'X'))):
        return 'a33'
    elif(((a31==a33=='X') and (a32 != 'X')) or ((a12==a22=='X') and (a32 != 'X'))):
        return 'a32'
    elif(((a33==a32=='X') and (a31 != 'X')) or ((a13==a22=='X') and (a31 != 'X')) or ((a11==a21=='X') and (a31 != 'X'))):
        return 'a31'
def attack():
    if(((a11==a12=='O') and (a13 != 'O')) or ((a31==a22=='O') and (a13 != 'O')) or ((a33==a23=='O') and (a13 != 'O'))):
        return 'a13'
    elif(((a11==a13=='O') and (a12 != 'O')) or ((a22==a32=='O') and (a12 != 'O'))):
        return 'a12'
    elif(((a13==a12=='O') and (a11 != 'O')) or ((a33==a22=='O') and (a11 != 'O')) or ((a31==a21=='O') and (a11 != 'O'))):
        return 'a11'
    elif(((a21==a22=='O') and (a23 != 'O')) or ((a13==a33=='O') and (a23 != 'O'))):
        return 'a23'
    elif(((a21==a23=='O') and (a22 != 'O')) or ((a11==a33=='O') and (a22 != 'O')) or ((a12==a32=='O') and (a22 != 'O')) or ((a13==a31=='O') and (a22 != 'O'))):
        return 'a22'
    elif(((a23==a22=='O') and (a21 != 'O')) or ((a11==a31=='O') and (a21 != 'O'))):
        return 'a21'
    elif(((a31==a32=='O') and (a33 != 'O')) or ((a11==a22=='O') and (a33 != 'O')) or ((a13==a23=='O') and (a33 != 'O'))):
        return 'a33'
    elif(((a31==a33=='O') and (a32 != 'O')) or ((a12==a22=='O') and (a32 != 'O'))):
        return 'a32'
    elif(((a33==a32=='O') and (a31 != 'O')) or ((a13==a22=='O') and (a31 != 'O')) or ((a11==a21=='O') and (a31 != 'O'))):
        return 'a31'
def player2():
    global played
    options = ['a11','a12','a13','a21','a22','a23','a31','a32','a33']
    playing = attack()
    if(playing == None):
        playing = defence()
        if(playing == None):
            playing = r.choice(options)
    while(playing in played):
        playing = r.choice(options)
    played.append(playing)
    if(playing == 'a11'):
        global a11
        a11 = "O"
    elif(playing == 'a12'):
        global a12
        a12 = "O"
    elif(playing == 'a13'):
        global a13
        a13 = "O"
    elif(playing == 'a21'):
        global a21
        a21 = "O"
    elif(playing == 'a22'):
        global a22
        a22 = "O"
    elif(playing == 'a23'):
        global a23
        a23 = "O"
    elif(playing == 'a31'):
        global a31
        a31 = "O"
    elif(playing == 'a32'):
        global a32
        a32 = "O"
    elif(playing == 'a33'):
        global a33
        a33 = "O"
    print("\nPlayer 2")
    printxo()
    print("\n")

def checking():
    global loop
    #print("checking loop is being executed")
    #print(a11!="-" and a22!="-" and a33!="-")
    if(a11!="-" and a12!="-" and a13!="-"):
        if(a11==a12==a13):
            
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a21!="-" and a22!="-" and a23!="-"):
        if(a21==a22==a23):
            
            print("\n-------------------------------------------")
            print(a21," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a31!="-" and a32!="-" and a33!="-"):
        if(a31==a32==a33):
            
            print("\n-------------------------------------------")
            print(a31," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a11!="-" and a21!="-" and a31!="-"):
        if(a11==a21==a31):
            
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a12!="-" and a22!="-" and a32!="-"):
        if(a12==a22==a32):
            
            print("\n-------------------------------------------")
            print(a12," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a13!="-" and a23!="-" and a33!="-"):
        if(a13==a23==a33):
            
            print("\n-------------------------------------------")
            print(a13," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a11!="-" and a22!="-" and a33!="-"):
        if(a11==a22==a33):
            
            
            print("\n-------------------------------------------")
            print(a11," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    if(a13!="-" and a22!="-" and a31!="-"):
        if(a13==a22==a31):
            
            print("\n-------------------------------------------")
            print(a13," wins")
            print("------------------------------------------- \n\n")
            loop = False
            
    
    #print(a11==a12==a13 or a21==a22==a23 or a31==a32==a33 or a11==a21==a31 or a12==a22==a32 or a13==a23==a33 or a11==a22==a33 or a13==a22==a31)

#checking()



 

while(1):
    printxo()
    flag = 0
    while(loop):
        player1()
        flag+=1
        checking()
        if(loop == False):
            break
        if(flag == 9):
            print("\n-------------------------------------------")
            print("Match Draw")
            print("------------------------------------------- \n\n")
            break
        player2()
        flag+=1
        checking()
        if(loop == False):
            break
        if(flag == 9):
            break
    choice = input("Do u want to play again(y/n)?! ").lower()
    if(choice != 'y'):
        break
    refresh()
