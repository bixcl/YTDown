import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def HighRes():
    try:
        ytlink = link.get()
        YTobject = YouTube(ytlink,on_progress_callback = progress)
        video = YTobject.streams.get_highest_resolution()
        dolabel.configure(text=YTobject.title)
        video.download(output_path=os.getcwd())  # Save the video to the current directory
        finish.configure(text="")
        finish.configure(text="Done")
    except:
        finish.configure(text="youtube link invalid/ or the content creator make it for kid")


def audio():
    try:
        ytlink = link.get()
        YTobject = YouTube(ytlink,on_progress_callback = progress)
        video = YTobject.streams.get_audio_only()
        dolabel.configure(text=YTobject.title)
        video.download(output_path=os.getcwd())  # Save the video to the current directory
        finish.configure(text="")
        finish.configure(text="Done")
    except:
        finish.configure(text="youtube link invalid/ or the content creator make it for kid")

def LowRes():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink,on_progress_callback = progress)
        video = ytobject.streams.get_lowest_resolution()
        dolabel.configure(text=ytobject.title)
        video.download(output_path=os.getcwd())  # Save the video to the current directory
        finish.configure(text="")
        finish.configure(text="Done")
    except:
        finish.configure(text="youtube link invalid/ or the content creator make it for kid")
        
def progress(stream,chunk,bytes_remaining):
    total_size= stream.filesize
    byDown = total_size - bytes_remaining
    perComp = byDown / total_size * 100 
    per = str(int(perComp))
    percnt.configure(text=per)
    percnt.update()

    bar.set(float(perComp)/100)


app = ctk.CTk()
app.geometry("420x420")
app.title("VideoDownloader")

dolabel = ctk.CTkLabel(app, text="download video")
dolabel.pack(pady=5)


urlvar = tk.StringVar()
link = ctk.CTkEntry(app,width=420,textvariable=urlvar)
link.pack()



percnt = ctk.CTkLabel(app,text="0")
percnt.pack()

bar=ctk.CTkProgressBar(app,width=400)
bar.set(0)
bar.pack(padx=10, pady=10)

finish = ctk.CTkLabel(app,text="")
finish.pack()

btn = ctk.CTkButton(app,text="High Resulotion", command = HighRes)
btn.pack(pady=5,fill=tk.BOTH)

btn = ctk.CTkButton(app,text="get audio only", command = audio)
btn.pack(pady=5,fill=tk.BOTH)

btn = ctk.CTkButton(app,text="Low Resulotion", command = LowRes)
btn.pack(pady=5,fill=tk.BOTH)

app.mainloop()
