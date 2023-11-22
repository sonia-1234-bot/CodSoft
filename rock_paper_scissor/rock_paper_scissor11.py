from tkinter import *
from PIL import Image,ImageTk
import random

root=Tk()
root.title("Rock Papper Scissor")
root.geometry("600x600")


def game():
    top = Toplevel()
    top.title("Game")
    top.geometry("600x600")
    global user_score
    global system_score

    user_score=0
    system_score=0

    label1 = Label(top, text="Choose One",font=20)
    label1.grid(row=0, column=1, padx=150, pady=40)
    
    rock_button = Button(top, text="✊", command=lambda: play_game("✊"),width=5,height=2,font=14)
    rock_button.grid(row=1, column=0, padx=10)
    
    paper_button = Button(top, text="🖐", command=lambda: play_game("🖐"),width=5,height=2,font=14)
    paper_button.grid(row=1, column=1, padx=10)
    
    scissor_button = Button(top, text="✌️", command=lambda: play_game("✌️"),width=5,height=2,font=14)
    scissor_button.grid(row=1, column=2, padx=10)


def play_game(choice):    
    top1=Toplevel()
    system = ["✊", "🖐", "✌️"]
    sys_choice=random.choice(system)
    system_choice=Label(top1,text="System output"+ sys_choice,font=20)
    system_choice.grid(row=1,column=0,padx=200)
    if choice=="✊":
        if sys_choice=="🖐":
            result=Label(top1,text="You Lost",font=24)
            result.grid(row=2,column=0,padx=150)
            system_score=system_score+1
        else:
            result=Label(top1,text="You won",font=24) 
            result.grid(row=2,column=0,padx=150) 
            user_score=user_score+1  

    elif choice=="🖐":
        if sys_choice=="✌️":
            result=Label(top1,text="You Lost",font=24)
            result.grid(row=2,column=0,padx=150)
            system_score=system_score+1
        else:
            result=Label(top1,text="You won",font=24) 
            result.grid(row=2,column=0,padx=150) 
            user_score=user_score+1  

    elif choice=="✌️": 
        if sys_choice=="✊":
            result=Label(top1,text="You Lost",font=24)
            result.grid(row=2,column=0,padx=150)
            system_score=system_score+1
        else:
            result=Label(top1,text="You won",font=24) 
            result.grid(row=2,column=0,padx=150) 
            user_score=user_score+1  
    top1.destroy        
         
    

img=ImageTk.PhotoImage(Image.open("rock paper scissor.jpeg"))
my_label=Label(image=img)
my_label.grid(row=0,column=0,columnspan=3,padx=160,pady=60)
instructions=Label(root,text='''INSTRUCTIONS:''')
instructions.grid(row=1,column=0)

instruction=Label(root,text=''' Rock beats Scissors 
Scissor beats Paper 
Paper beats Rock  ''')
instruction.grid(row=2,column=0)

btn=Button(root,text="Start the Game", borderwidth=5,command=game)
btn.grid(row=3,column=0,padx=250,pady=40)


root.mainloop()