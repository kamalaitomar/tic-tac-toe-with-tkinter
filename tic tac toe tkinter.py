from tkinter import *

game =Tk()
game.title("KML Tic-Tac-Toe")

player = "X"
counter = 0


roles = Label(game, text= player +" you have the role" , font="times 14")
roles.grid(row =5, column=2)

conter = Label(game, text= counter, font="times 14")
# conter.grid(row=6,column=2)

winner = Label(game, text="....", font="times 14")
winner.grid(row=7,column=2)

def check():
    if b1["text"] == b2["text"] == b3["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b4["text"] == b5["text"] == b6["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b7["text"] == b8["text"] == b9["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b1["text"] == b4["text"] == b7["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b2["text"] == b5["text"] == b8["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b3["text"] == b6["text"] == b9["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b1["text"] == b5["text"] == b9["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b3["text"] == b5["text"] == b7["text"] != " ":
        winner["text"]="**congratulation** \n -- "+ player+" -- \n **you win**"
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    elif b1["state"]==b2["state"]==b3["state"]==b4["state"]==b5["state"]==b6["state"]==b7["state"]==b8["state"]==b9["state"]== DISABLED:
        winner["text"]="*-no one wine-*\n*-the game ended-*\n*-in draw-*"


def play_again():
    global player
    global counter
    b1["state"]=NORMAL
    b1["text"]=" "
    b2["state"]=NORMAL
    b2["text"]=" "
    b3["state"]=NORMAL
    b3["text"]=" "
    b4["state"]=NORMAL
    b4["text"]=" "
    b5["state"]=NORMAL
    b5["text"]=" "
    b6["state"]=NORMAL
    b6["text"]=" "
    b7["state"]=NORMAL
    b7["text"]=" "
    b8["state"]=NORMAL
    b8["text"]=" "
    b9["state"]=NORMAL
    b9["text"]=" "
    winner["text"]="...."
    player = "X"
    counter = 0
    
again = Button(game, text="click here \n if you want play again", bg="green",fg="white", font=("times 13"), command=play_again)
again.grid(row=8,column=2)


def click1():
    global counter 
    global player
    b1["text"] = player
    b1["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter
       
b1=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"), command=click1)
b1.grid(row=1,column=1)


def click2():
    global counter 
    global player
    b2["text"] = player
    b2["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b2=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"), command=click2)
b2.grid(row=1,column=2)


def click3():
    global counter 
    global player
    b3["text"] = player
    b3["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b3=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"), command = click3)
b3.grid(row=1,column=4)


def click4():
    global counter 
    global player
    b4["text"] = player
    b4["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b4=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"), command=click4)
b4.grid(row=2,column=1)


def click5():
    global counter 
    global player
    b5["text"] = player
    b5["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b5=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"),command=click5)
b5.grid(row=2,column=2)


def click6():
    global counter 
    global player
    b6["text"] = player
    b6["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b6=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"),command=click6)
b6.grid(row=2,column=4)


def click7():
    global counter 
    global player
    b7["text"] = player
    b7["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter


b7=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"),command=click7)
b7.grid(row=4,column=1)


def click8():
    global counter 
    global player
    b8["text"] = player
    b8["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b8=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"),command=click8)
b8.grid(row=4,column=2)


def click9():
    global counter 
    global player
    b9["text"] = player
    b9["state"] = DISABLED
    if counter >= 4:
        check()
    if player == "X":
        player = "O"
    else:
        player = "X"
    counter += 1
    roles["text"] = "it's " + player + " role"
    conter["text"] = counter

b9=Button(game, bg="#48dbfb",width=4,height=1, text=" ",font=("arial", 50,"bold"),command= click9)
b9.grid(row=4,column=4)
   


game.mainloop()