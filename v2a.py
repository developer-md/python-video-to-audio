import moviepy
from moviepy import editor
import tkinter 
from tkinter import *
from tkinter import messagebox

def v2a():
    vid=location.get()
    x=0
    try:
        v=moviepy.editor.VideoFileClip(vid)
        audio=v.audio
        aud=location1.get()
        audio.write_audiofile(aud)
    except Exception as e:
        messagebox.showerror("Error",e)
        x=x+1
    if (x==1):
        print("something wrong")
    else:
        messagebox.showinfo('success','Successfully convert')


root=tkinter.Tk()
root.geometry("600x500")
root.title("V2A convertor")
root.config(bg='skyblue')
root.resizable(0,0)

heading=Label(text="Video to Audio convertor",font=("Times",18,"bold")
             ,width=100,bg="skyblue",fg="red")
heading.pack(pady=(10,50))

label=Label(text="paste here your video location",font=("consalis",18,"bold")
            ,width=100,bg="skyblue",fg="black")
label.pack()

note=Label(text="Note: like this (D:\\song\\abc.mp4)",font=("Times",12)
           ,bg="skyblue")
note.pack()

location=Entry(font=("consalis",15),width=30)
location.pack(pady=(10,50))


label1=Label(text="where you want to save",font=("consalis",18,"bold")
             ,width=100,bg="skyblue",fg="black")
label1.pack()

note1=Label(text="Note: like this (D:\\save here\\abc.mp3)"
            ,font=("Times",12),bg="skyblue")
note1.pack()

location1=Entry(font=("consalis",15),width=30)
location1.pack()


button=Button(text="convert",command=v2a,font=("consalis",12,"bold")
              ,bg="white",border="2")
button.pack(pady=(20,10))

#put a Label
footer=Label(root,text="developed by developer md:",width=100
            ,font=("consalis",20),bg="black",fg="gold")
footer.pack(pady=(70,10))



root.mainloop()

