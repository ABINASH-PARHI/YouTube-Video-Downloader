# This is a sample Python script.
import pyttsx3

sound = pyttsx3.init()
import tkinter as tk
from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    download_status_label.config(text="Downloading... {:.1f}%".format(percent))
    root.update()


def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()
        sound.say("Download Started. Please Wait.")
        sound.runAndWait()
        video_title.set("Title: " + ytobject.title)
        video_channel.set("Channel: " + ytobject.author)
        video.download()
        download_status_label.config(text="Download Complete!")
        sound.say("Download Complete!")
        sound.runAndWait()
    except:
        sound.say("Invalid link. Check link again.")
        sound.runAndWait()
        download_status_label.config(text="Invalid link. Check link again")


root = tk.Tk()
root.geometry("1366x768")
root.title("YouTube Video Downloader")

title = tk.Label(root, text="Insert a YouTube link", font=("Roboto", 26))
title.pack(padx=10, pady=10)

url = tk.StringVar()
link = tk.Entry(root, width=400, textvariable=url)
link.pack()

video_title = tk.StringVar()
video_channel = tk.StringVar()

title_label = tk.Label(root, textvariable=video_title, font=("Roboto", 18, "bold"))
title_label.pack()

channel_label = tk.Label(root, textvariable=video_channel, font=("Roboto", 18, "bold"))
channel_label.pack()

note = tk.Label(root, text="Note:- The downloaded YouTube video will be saved in the same directory as the program.",
                font=("Roboto", 18))
note.pack(padx=10, pady=10)
note = tk.Label(root, text="Note:- Please make sure that you are connected to the internet.", font=("Roboto", 18))
note.pack(padx=10, pady=10)

button = tk.Button(root, text="Download Video", command=startDownload)
button.pack(padx=12, pady=10)

download_status_label = tk.Label(root, text="", font=("Roboto", 16))
download_status_label.pack()

root.mainloop()