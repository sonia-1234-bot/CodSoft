from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import font 

root=Tk()
root.title("Rock Papper Scissor")
root.geometry("600x600")

#Global variables initialization
count=0
user_score=0
system_score=0

#Initializing font size and font family
const_font=font.Font(family="Cascadia Mono SemiBold",size=20)
font2=font.Font(family="Cascadia Mono SemiBold",size=10)
btn_font=font.Font(family="Sitka Display",size=16)
font3=font.Font(family="Rockwell Extra Bold",size=24)

#Displaying the result and continue to play the game
def game():
    global count
    global user_score
    global system_score
    #clearing the window
    for widget in root.winfo_children():
        widget.destroy()

    #Checking if the match is complete with 5 rounds limit       
    if count==5:
        result=Toplevel()
        result.title("Result")
        result.geometry("600x600")
        #Checking the result of the match based on the user_score and system score
        if user_score>system_score:
            count=0
            result_label=Label(result,text="You Won The Match",font=font3) 
            result_label.grid(row=0,column=0,padx=150,pady=50)   
            user_result_label=Label(result,text="User Score : " +str(user_score),font=20)
            user_result_label.grid(row=1,column=0,padx=150,pady=(50,10))
            sys_result_label=Label(result,text="System Score : " +str(system_score),font=20)
            sys_result_label.grid(row=2,column=0,padx=150,pady=(10,50))
            user_score=0
            system_score=0
            another_round_button=Button(result,text="Play Again",command=game,font=btn_font,width=10)
            another_round_button.grid(row=3,column=0,padx=150,pady=10)   
            end_button=Button(result,text="End Game",font=btn_font,command=result.quit)
            end_button.grid(row=4,column=0,padx=150,pady=10)
        elif user_score==system_score:
            count=0
            result_label=Label(result,text="Match is Tie",font=font3) 
            result_label.grid(row=0,column=0,padx=150,pady=50)   
            user_result_label=Label(result,text="User Score : " +str(user_score),font=20)
            user_result_label.grid(row=1,column=0,padx=150,pady=(50,10))
            sys_result_label=Label(result,text="System Score : " +str(system_score),font=20)
            sys_result_label.grid(row=2,column=0,padx=150,pady=(10,50))
            user_score=0
            system_score=0
            another_round_button=Button(result,text="Play Again",command=game,font=btn_font,width=10)
            another_round_button.grid(row=3,column=0,padx=150,pady=10)   
            end_button=Button(result,text="End Game",font=btn_font,command=result.quit)
            end_button.grid(row=4,column=0,padx=150,pady=10)

        else:
            count=0
            result_label=Label(result,text="You Lost The Match",font=font3) 
            result_label.grid(row=0,column=0,padx=150,pady=50)   
            user_result_label=Label(result,text="User Score : " +str(user_score),font=20)
            user_result_label.grid(row=1,column=0,padx=150,pady=(50,10))
            sys_result_label=Label(result,text="System Score : " +str(system_score),font=20)
            sys_result_label.grid(row=2,column=0,padx=150,pady=(10,50))
            user_score=0
            system_score=0
            another_round_button=Button(result,text="Play Again",command=game,font=btn_font,width=10)
            another_round_button.grid(row=3,column=0,padx=150,pady=10)
            end_button=Button(result,font=btn_font,text="End Game",command=result.quit)
            end_button.grid(row=4,column=0,padx=150,pady=10)   
    
    label1 = Label(text="Choose One",font=const_font)
    label1.grid(row=0, column=1, padx=130, pady=100)
    
    rock_button = Button(text="✊",borderwidth=5, command=lambda: play_game("✊"),width=5,height=2,font=btn_font)
    rock_button.grid(row=1, column=0,padx=10)
    
    paper_button = Button(text="🖐",borderwidth=5, command=lambda: play_game("🖐"),width=5,height=2,font=btn_font)
    paper_button.grid(row=1, column=1)
    
    scissor_button = Button(text="✌️",borderwidth=5, command=lambda: play_game("✌️"),width=5,height=2,font=btn_font)
    scissor_button.grid(row=1, column=2)

#Function to check who has won the round
def play_game(choice):
    global count   
    global user_score
    global system_score
    count=count+1
    for widget in root.winfo_children():
        widget.destroy() 
    system = ["✊", "🖐", "✌️"]
    sys_choice=random.choice(system)
    system_choice=Label(text="System output"+ sys_choice,font=30)
    system_choice.pack(pady=(100,10))
    if choice=="✊": 
        if sys_choice=="🖐":
            result=Label(text="You Lost",font=font3)
            result.pack()
            system_score=system_score+1
        elif sys_choice=="✊":
            result=Label(text="Tie",font=font3)
            result.pack()
            result1=Label(text="Each one point",font=font2)
            result1.pack()
            system_score=system_score+1 
            user_score=user_score+1   
        else:
            result=Label(text="You won",font=font3) 
            result.pack() 
            user_score=user_score+1  

    elif choice=="🖐":
        if sys_choice=="✌️":
            result=Label(text="You Lost",font=font3)
            result.pack()
            system_score=system_score+1
        elif sys_choice=="🖐":
            result=Label(text="Tie",font=font3)
            result.pack()
            result1=Label(text="Each one point",font=font2)
            result1.pack()
            system_score=system_score+1 
            user_score=user_score+1     
        else:
            result=Label(text="You won",font=font3) 
            result.pack() 
            user_score=user_score+1  

    elif choice=="✌️": 
        if sys_choice=="✊":
            result=Label(text="You Lost",font=font3)
            result.pack()
            system_score=system_score+1
        elif sys_choice=="✌️":
            result=Label(text="Tie",font=font3)
            result.pack()
            result1=Label(text="Each one point",font=font2)
            result1.pack()
            system_score=system_score+1 
            user_score=user_score+1     
        else:
            result=Label(text="You won",font=font3) 
            result.pack()
            user_score=user_score+1  
    back_button=Button(text="Back",command=game,font=btn_font)
    back_button.pack(pady=50)        
         
    
#Initial page of the game 
img=ImageTk.PhotoImage(Image.open("rock_paper_scissor/rock paper scissor.jpeg"))
my_label=Label(image=img)
my_label.grid(row=0,column=0,columnspan=3,padx=160,pady=60)
instructions=Label(root,text='''INSTRUCTIONS:''',font=const_font)
instructions.grid(row=1,column=0)

instruction=Label(root,text=''' Rock beats Scissors 
 Scissor beats Paper 
  Paper beats Rock  
                 Each match contains 5 rounds                  ''',font=font2)
instruction.grid(row=2,column=0)

btn=Button(root,text="Start Game",font=btn_font, borderwidth=5,command=game)
btn.grid(row=3,column=0,padx=250,pady=40)


root.mainloop()