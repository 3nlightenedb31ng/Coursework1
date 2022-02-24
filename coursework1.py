from tkinter import *
from PIL import Image, ImageTk, ImageSequence
window = Tk()
window.title("walking GIF")
window.minsize(width=800, height=700)
msg = Message(window, text="Tap play button to watch GIF", bg='blue', padx=400, pady=300)
msg.pack()


def gif():
    img = Image.open("walk.gif")
    lbl = Label(window)
    lbl.place(x=50, y=50)
    for img in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        window.update()
    window.after(0, gif)


Button(window, text="Play", bg="red", fg='blue', command=gif).place(x=750, y=650)
Button(window, text="Exit", bg='red', fg='blue', command=exit).place(x=700, y=650)

window.mainloop()
