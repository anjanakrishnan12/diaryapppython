from tkinter import*
import webbrowser

def openfilep():
    webbrowser.open("DIARYDIARY.txt")
def readfilep():
    textfilep= open("DIALYDIARY.txt")
    print (textfile.read())
    textfilep.close()


def writefilep():
    diaryEntry = textbox.get()
    diaryEntry = diaryEntry+"\n"
    textbox.delete(0,1000)
    textfilep=open("DIALYDIARY.txt", "a")
    textfilep.write(diaryEntry)
    textfilep.close()
    


def close():
    mGui.destroy()

mGui= Tk()

mGui.geometry("750x345")


mGui.title ("HELLO MY DIARY!!!!!")

menubar= Menu (mGui)
menu1= Menu (menubar, tearoff=0)
menu1.add_command (label="python Idle", command = readfilep)
menu1.add_command (label="Notepad", command= openfilep)
menu1.add_command (label="exit", command=close)



menubar.add_cascade (label="open", menu=menu1)

mGui.config (menu=menubar )



diary= Label (mGui, text="MY MEMORIES IN DIARY", bg= "yellow", fg="black", width=45, bd= 1)
diary.pack(pady=10)
textbox=Text(mGui, width=50, bg="orange", bd=45 )


save=Button(text="SAVE", command=writefilep , bg="yellow", fg= "BLACK")
textbox.pack(pady= 15)
save.pack(pady=45)
mGui.mainloop()
