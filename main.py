from tkinter import *
from ttkthemes import themed_tk as tk
from pytube import YouTube
import tkinter.messagebox as tmsg

#--------------GUI--------------

root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.resizable(0,0)
root.geometry("600x300")
root.title("Youtube Video Downloader - Lokesh Vyas")

#--------------Function for downloader--------------

def downloader():
    yt_url = YouTube(str(link.get()))
    yt_video = yt_url.streams.first()
    yt_video.download()
    tmsg.showinfo("Successful Download", "Your video has been downloaded successfully.")

#--------------Labels--------------
l1 = Label(root,text="Youtube Video Downloader", font="arial 20 bold", fg="red")
l1.pack()

l2 = Label(root,text="Paste Your Link Here:", font="arial 15 bold")
l2.place(x=190,y=60)

#--------------Entry widgets and Button--------------
link = StringVar()

yt_link = Entry(root, width=70, textvariable=link)
yt_link.place(x=90,y=100)

submit_button = Button(root,text="Download Video", bg="red", fg="white",command=downloader)
submit_button.place(x=250,y=150)

root.mainloop()