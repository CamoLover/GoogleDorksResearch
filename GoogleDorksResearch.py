import webbrowser
from  tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
window=Tk()

def dorks(name, site, filetype):
    dorks = ["intitle","intext","inurl"]#dorks list
    name_accurate = '"'+name+'"' #Remake name in correct format
    if site == "" : #if no website to search
        for i in range(len(dorks)) :
            if filetype == "" :
                webbrowser.open("https://www.google.fr/search?q="+dorks[i]+":"+name_accurate) #search name with dorks
            else :
                webbrowser.open("https://www.google.fr/search?q="+dorks[i]+":"+name_accurate+" filetype:"+filetype) #search name with dorks
    else : #if there is a specific website
        for i in range(len(dorks)) :
            if filetype == "" :
                webbrowser.open("https://www.google.fr/search?q="+dorks[i]+":"+name_accurate+" site:"+site) #search name with dorks and on specific website
            else :
                webbrowser.open("https://www.google.fr/search?q="+dorks[i]+":"+name_accurate+" site:"+site+" filetype:"+filetype) #search name with dorks and on specific website
        webbrowser.open("https://www.google.fr/search?q="+name_accurate+" site:"+site) #search name without dorks, on specific website

#----------------------------------------------------------
#tkinter part

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("background.png")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
e = Example(window)
e.pack(fill=BOTH, expand=YES)

lbl=Label(window, text="Google Dorks Research", background="#1F052C", foreground="white")
lbl.place(relx=.5, rely=.05,anchor= CENTER)
lbl=Label(window, text="Name :", background="#1F052C", foreground="white")
lbl.place(relx=.2, rely=.3,anchor= CENTER)
txtfldname=Entry(window, bd=5)
txtfldname.place(relx=.5, rely=.3,anchor= CENTER)
lbl=Label(window, text="Website :", background="#1F052C", foreground="white")
lbl.place(relx=.2, rely=.4,anchor= CENTER)
txtfldsite=Entry(window, bd=5)
txtfldsite.place(relx=.5, rely=.4,anchor= CENTER)
lbl=Label(window, text="Filetype :", background="#1F052C", foreground="white")
lbl.place(relx=.2, rely=.5,anchor= CENTER)
txtfldfile=Entry(window, bd=5)
txtfldfile.place(relx=.5, rely=.5,anchor= CENTER)
btn=Button(window, text="research", command=lambda : dorks(txtfldname.get(), txtfldsite.get(), txtfldfile.get()))
btn.place(relx=.5, rely=.6,anchor= CENTER)


window.tk.call('wm', 'iconphoto', window._w, ImageTk.PhotoImage(file='logo.png'))
window.title('Google dorks research')
window.geometry("300x300")
window.mainloop()