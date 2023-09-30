from tkinter import *
import pyshorteners
import pyperclip

root1 = Tk()
root1.title("URL Shortener")
root1.geometry("400x350")  
root1.configure(bg="thistle")
root1.resizable(False, False)

url = StringVar()
sortUrl = StringVar()

def urlshort():
    sort_Url = url.get()
    if sort_Url:
        generateurl = pyshorteners.Shortener().tinyurl.short(sort_Url)
        sortUrl.set(generateurl)
        # Updating  the outcome label
        outcome_label.config(text=f"Shortened URL: {generateurl}")
    else:
        sortUrl.set("")
    
        outcome_label.config(text="")

def copy():
    generateurl = sortUrl.get()
    if generateurl:
        pyperclip.copy(generateurl)

Label(root1, text="URL Shortener App", font=("Arial", 16, "bold"), fg="indigo", bg="thistle").pack(pady=15)
Entry(root1, textvariable=url, width=30, font=("Arial", 12)).pack(pady=10)
Button(root1, text="Shorten URL", command=urlshort, font=("Arial", 12)).pack(pady=10)
Entry(root1, textvariable=sortUrl, width=30, font=("Arial", 12)).pack(pady=10)
Button(root1, text="Copy URL", command=copy, font=("Arial", 12)).pack(pady=10)

# Outcome label
outcome_label = Label(root1, text="", font=("Arial", 12), fg="green", bg="thistle")
outcome_label.pack(pady=10)

root1.mainloop()
