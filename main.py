from tkinter import *
from pytube import YouTube

root=Tk()
root.geometry('500x300')
root.title('Youtube downloder')
Label(root,text='Youtube downloader').pack()    

link=StringVar()
#place(x=160,y=60)
Label(root,text="paste link here:").place(x=190,y=60)
link_en=Entry(root,width=60,textvariable=link).place(x=10,y=90)
print(link.get())

def Download(link):
    print(str(link))
    url=YouTube(link)
    video=url.streams.first()
    video.download()
    Label(root,text='Downloaded').place(x=200,y=160)

Button(root,text='Download',bg='blue',command=lambda: Download(link.get())).place(x=200,y=130)
#command=lambda: send_message(email_body.get(),address.get())
root.mainloop()