from tkinter import *

root=Tk()
root.title("Calculator")
e=Entry(root,width=35,borderwidth=5,font=16,bg="beige")
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)

#Function to consider the numbers entered
def button_insert(num):
    current=e.get()
    e.delete(0,END) 
    e.insert(0,str(current)+str(num))

#Function to clear the entered data    
def button_clr():
    e.delete(0,END)    

#Funtion to get the first number entered and the operator entered
def button_func(operator):
    first_number=e.get()
    global f_num
    global op
    op=operator
    f_num=float(first_number)
    e.insert(0,str(first_number)+op) 
    e.delete(0,END) 
 
#Funtion for permormimg operation based on the operator selected 
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if op=="+":
        e.insert(0,f_num+float(second_number))
    elif op=="-":
        e.insert(0,f_num-float(second_number))    
    elif op=="*":
        e.insert(0,f_num*float(second_number))    
    elif op=="/":
        e.insert(0,f_num/float(second_number))    
    elif op=="%":
        e.insert(0,f_num%float(second_number))                

#Buttons for the numbers, operators, equating and clearing the data
button1=Button(root,font=14,text="1",padx=40,pady=40,bg="beige",command=lambda:button_insert(1))
button2=Button(root,font=14,text="2",padx=40,pady=40,bg="beige",command=lambda:button_insert(2))
button3=Button(root,font=14,text="3",padx=40,pady=40,bg="beige",command=lambda:button_insert(3))
button4=Button(root,font=14,text="4",padx=40,pady=40,bg="beige",command=lambda:button_insert(4))
button5=Button(root,font=14,text="5",padx=40,pady=40,bg="beige",command=lambda:button_insert(5))
button6=Button(root,font=14,text="6",padx=40,pady=40,bg="beige",command=lambda:button_insert(6))
button7=Button(root,font=14,text="7",padx=40,pady=40,bg="beige",command=lambda:button_insert(7))
button8=Button(root,font=14,text="8",padx=40,pady=40,bg="beige",command=lambda:button_insert(8))
button9=Button(root,font=14,text="9",padx=40,pady=40,bg="beige",command=lambda:button_insert(9))
button0=Button(root,font=14,text="0",padx=40,pady=40,bg="beige",command=lambda:button_insert(0))
button_dec=Button(root,font=20,text=".",padx=42,pady=40,bg="beige",command=lambda:button_insert("."))
button_add=Button(root,font=16,text="+",padx=40,pady=40,bg="lightgreen",command=lambda:button_func("+"))
button_sub=Button(root,font=16,text="-",padx=42,pady=40,bg="lightgreen",command=lambda:button_func("-"))
button_mul=Button(root,font=16,text="*",padx=44,pady=40,bg="lightgreen",command=lambda:button_func("*"))
button_div=Button(root,font=16,text="/",padx=45,pady=40,bg="lightgreen",command=lambda:button_func("/"))
button_mod=Button(root,font=16,text="%",padx=40,pady=40,bg="lightgreen",command=lambda:button_func("%"))
button_eql=Button(root,font=20,text="=", padx=100,pady=40,bg="lightblue",command=button_equal)
button_clear=Button(root,font=20,text="CLR",padx=32,pady=40,bg="lightblue",command=button_clr)

#Adjusting the position of the buttons
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button_dec.grid(row=5,column=0)

button_add.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_mul.grid(row=2,column=3)
button_div.grid(row=3,column=3)
button_mod.grid(row=4,column=3)
button_clear.grid(row=1,column=3)
button_eql.grid(row=5,column=1,columnspan=80)


root.mainloop()