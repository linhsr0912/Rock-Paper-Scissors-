from tkinter import *
from random import randint

win = Tk()

select = {
    1 : "Rock" ,
    2 : "Scissor" ,
    3 : "Paper" ,
}

# function for ston
def Rock():
    sys_random = randint(1,3)
    lbl["text"] = "opponent : " + select[sys_random]
    if sys_random == 2 :
        lblresultUser["text"] =int(lblresultUser["text"]) +1
    elif sys_random == 3 :
        lblresultSystem["text"] =int(lblresultSystem["text"]) +1


# function for paper
def Paper():
    sys_random = randint(1,3)
    lbl["text"] = "opponent : " + select[sys_random]
    if sys_random == 2 :
        lblresultSystem["text"] =int(lblresultSystem["text"]) +1
    elif sys_random == 1 :
        lblresultUser["text"] =int(lblresultUser["text"]) +1

# function for scissor
def Scissor():
    sys_random = randint(1,3)
    lbl["text"] = "opponent : " + select[sys_random]
    if sys_random == 1 :
        lblresultSystem["text"] =int(lblresultSystem["text"]) +1
    elif sys_random == 3 :
        lblresultUser["text"] =int(lblresultUser["text"]) +1

# For reset the game
def Reset():
    lblresultUser["text"] = 0
    lblresultSystem["text"] = 0
    lbl["text"]= "Select"



# *************************************  App appearance design  **************************************#
#  title at the head of win
win.title("* Made By Irealmatin *")

# minimom size that you can change
win.minsize(300,400)

# Lable of select
win.rowconfigure([0,1] , weight= 1)
win.columnconfigure(0 , weight= 1)
lbl = Label(master = win  , text = " Select " , bg = "powder blue" , height = 2 ,
font =("arial" , 18 , "bold"))
lbl.grid(row = 0 ,column = 0 , sticky = "nwe" )

# 3 Button for Rock Paper Scissors !
frmbtn = Frame(master= win , height= 100 , bg= "red")
frmbtn.columnconfigure([0,1,2] , weight=1)

# this is for Rock
rockbtn = Button(master= frmbtn , text= "Rock" , height= 3 , 
                 font = ("None" , 16 , "bold"), command=Rock ).grid(row = 0 , column= 0 ,sticky= "nwes" , padx=2 , pady=3)

# this is for Paper
paperkbtn = Button(master= frmbtn , text= "Paper" , height= 3 , 
                 font = ("None" , 16 , "bold"),command=Paper).grid(row = 0 , column= 1 ,sticky= "nwes" , padx=2 , pady=3)

# this is for Scissor
scissorbtn = Button(master= frmbtn , text= "Scissor" , height= 3 , 
                 font = ("None" , 16 , "bold"),command=Scissor).grid(row = 0 , column= 2 ,sticky= "nwes" , padx=2 , pady=3)

frmbtn.grid(row = 1 , column= 0 , sticky= "wen" )


# result labale 
frmresult = Frame(master= win , height= 200)
frmresult.rowconfigure([0,1] , weight= 1)
frmresult.columnconfigure([0,1] , weight= 1)

lblresultnameUser = Label(master= frmresult , text= " Your points" , relief= "ridge").grid(row=0 , column=0 , sticky="nswe")
lblresultnameSystem = Label(master= frmresult , text= "Opponent points" , relief= "ridge").grid(row=0 , column=1 , sticky="nswe")

lblresultUser = Label(master= frmresult , text= "0" ,height=3, bg= "blue" , fg="#fff" , font=("None" , 40 , "bold")) 
lblresultUser.grid(row=1 , column=0 , sticky= "nswe")

lblresultSystem = Label(master= frmresult , text= "0" ,height=3, bg= "red", fg="#fff" , font=("None" , 40 , "bold"))
lblresultSystem.grid(row=1 , column=1 , sticky= "nswe")
frmresult.grid(row=2 , column=0 , sticky= "nswe")

# Lable Reset 
btnReset = Button(master=win , text="Reset" , bg="powder blue", font=("None" ,18 , "bold"), relief="ridge" , command=Reset).grid(row=3 , column=0 , sticky="nswe")

win.mainloop()
