from tkinter import *
import random
from tkinter import messagebox
score=0
timeleft=60
answers=["alka","phone","java","mumbai","peacock","laptop","curtain","chair","potato","tomato","watch","clock","mirror","mobile","hyderabad","patna","bihar","jharkhand","chennai","bokaro"]
words=["aalk","oneph","avja","bmumai","ccokeap","ptloap","iantruc","raich","ottaop","mattoo","atwhc","ocklc","rrroim","bileom","erabadyhd","natpa","hiarb","rkhandjha","nnaiehc","ooarkb"]
word=random.randrange(0,20,1)
def start():
   global answers,words,word
   l3.config(text=words[word])
   countdown()
def check():
   global answers,words,word,score
   ans=e1.get()
   if ans==answers[word]:
      #messagebox.showinfo("sucess","your answer is correct")
      score+=1
      l4.config(text="score:  "+str(score))
      reset()
   else:
      messagebox.showwarning("warning","your answer is wrong")  
      e1.delete(0,END)      
def reset():
    global answers,words,word
    e1.delete(0,END) 
    word=random.randrange(0,20,1)
    l3.config(text=words[word])
def countdown():
    global timeleft
    if timeleft>0:
      timeleft = timeleft-1
      l5.config(text="Timeleft: "+str(timeleft))
      l5.after(1000,countdown) 
      if timeleft==0:
         messagebox.showwarning("Game over","Times up")         
         messagebox.showinfo("congragulations","your score is "+str(score))         
         root.quit()
root=Tk()
root.geometry("400x500+100+100")
root.title("puzzled words")
root.config(background="black")
l1=Label(root,text="write the correct word......",font=("Girassol",18),bg="black",fg="white")
l1.pack()
l2=Label(root,text="press start to start the game",font=("Girassol",16),bg="black",fg="white")
l2.pack(pady=20)
b1=Button(root,text="start",font=("Baloo Bhai",14),bg="red",width=15,command=start)
b1.pack()
l3=Label(root,text="    ",font=("Baloo Bhai",18),bg="black",fg="white")
l3.pack(pady=20)
e1=Entry(root,width=15,font=("Baloo Bhai",16))
e1.pack()
b2=Button(root,text="check",font=("Baloo Bhai",13),bg="pink",width=18,command=check)
b3=Button(root,text="change word",font=("Baloo Bhai",13),bg="pink",width=18,command=reset)
b2.pack(pady=20)
b3.pack()
l4=Label(root,text="score: "+str(score),font=("Baloo Bhai",14),bg="black",fg="white")
l5=Label(root,text="Timeleft: "+str(timeleft),font=("Baloo Bhai",14),bg="black",fg="white")
l4.pack(pady=20)
l5.pack()
root.mainloop()