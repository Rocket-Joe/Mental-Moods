import os
import tkinter as tk
from tkinter.constants import BOTTOM
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Danger import scanFile
from tkinter.messagebox import showinfo

class MainPage:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        font = 'oswald'

        def openEditor():
            self.window = tk.Toplevel(self.master)
            self.app = Editor(self.window)

        def openDescription():
            self.window = tk.Toplevel(self.master)
            self.app = txtDisplay(self.window, '\description.txt')

        def openInfo():
            self.window = tk.Toplevel(self.master)
            self.app = txtDisplay(self.window, '\info.txt')

        def openEntries():
            self.window = tk.Toplevel(self.master)
            self.app = Viewer(self.window)

        editor = tk.Button(master, 
                        text='editor', 
                        command=openEditor,
                        height = 3,
                        width = 12,
                        font = font)
        editor.place(x=480+15, y=100)

        description = tk.Button(master, 
                        text='Description', 
                        command=openDescription,
                        height = 3,
                        width = 12,
                        font = font)
        description.place(x=160+15, y=100)

        info = tk.Button(master, 
                        text='info', 
                        command=openInfo,
                        height = 3,
                        width = 12,
                        font = font)
        info.place(x=0+15, y=100)

        Files = tk.Button(master, 
                        text='View previous\nentires', 
                        command=openEntries,
                        height = 3,
                        width = 12,
                        font = font)
        Files.place(x=320+15, y=100)

        Title = tk.Label(master,
                        text = 'Mental Mooods',
                        font = font)
        Title.pack()

        master.geometry('640x360')
        self.frame.pack()

class Editor:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        file = os.getcwd().replace('\Program Code', '\Journal Entries')
        os.chdir(file)

        def open_file():
            filepath= askopenfilename(
                initialdir=os.getcwd(),
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not filepath:
                return
            with open(filepath, "r") as input_file:
                text = input_file.read()
                txt_edit.insert(tk.END, text)
            app.title(f"Text Editor Application - {filepath}")

        def save_file():
            num = len([name for name in os.listdir('.') if os.path.isfile(name)])
            file = open('Entry '+str(num+1)+'.txt', 'w+')
            with file as output_file:
                text = txt_edit.get(1.0, tk.END)
                output_file.write(text)
                print(file.read())
                checkDanger(master, text)

        master.title("Text Editor Application")
        master.rowconfigure(0, minsize=800, weight=1)
        master.columnconfigure(1, minsize=800, weight=1)

        txt_edit = tk.Text(master)
        fr_buttons = tk.Frame(master, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(fr_buttons, text="Open", command= open_file)
        btn_save = tk.Button(fr_buttons, text="Save as...", command= save_file)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky="ew", padx=5)

        fr_buttons.grid(row=0, column=0, sticky="ns")
        txt_edit.grid(row=0, column=1, sticky="nsew")

class txtDisplay:
    def __init__(self, master, File):
        self.master = master
        self.frame = tk.Frame(self.master)

        filename = os.getcwd().replace('\Program Code', File)
        print('FileName',filename)
        if not os.path.isdir(filename):
            file = open(filename)


            thig = tk.Label(master, 
                            text = file.read())
            thig.pack()
            file.close()
            master.geometry('640x360')
            self.frame.pack()
        else:
            print('given dir')

class Viewer:
    def __init__(self, master):
        self.master = master
        frames = []
        currentFrame = 0

        def openEditor(input):
            print('INPUT', input)
            self.window = tk.Toplevel(self.master)
            fileChange = '\Journal Entries'+input
            print('FILE CHANGE',fileChange)
            self.app = txtDisplay(self.window, fileChange)

        filesList = os.listdir('..\Journal Entries')

        b = []
        entry = []
        for i in range(len(filesList)):
            if (i) % 10 == 0:
                frames.append(tk.Frame(self.master))
            entry.append('\Entry '+str(i+1)+'.txt')

        for i in range(len(filesList)):
            if (i+1) % 10 == 0:
                currentFrame += 1
            print('Entry#', entry[i])
            thig = entry[i]
            
            b.append(tk.Button(frames[currentFrame],
                            text = i+1,
                            width = 5,
                            command = lambda: openEditor(thig)))
            b[i].pack(side='left')

        for frame in frames:
            frame.pack(side = 'top')

def checkDanger(master, txt):
    if scanFile(txt):
        print('AHH')
        showinfo('SelfHarm alert','We noticed that your last entry contained self harm \n words. Consider looking at our info page for help')
    else:
        print('ahh...')

root = tk.Tk()
app = MainPage(root)
root.mainloop()