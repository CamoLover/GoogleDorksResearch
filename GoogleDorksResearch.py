import webbrowser
from  tkinter import *
from tkinter import ttk
window=Tk()


def dorks(name, site):
    dorks = ["intitle","intext","inurl"]#dorks list
    linknumber = 0 #current number in dorks array
    name_accurate = '"'+name+'"' #Remake name in correct format
    if site == "" : #if no website to search
        for i in range(len(dorks)) :
            webbrowser.open("https://www.google.fr/search?q="+dorks[linknumber]+":"+name_accurate) #search name with dorks
            linknumber+=1
    else : #if there is a specific website
        for i in range(len(dorks)) :
            webbrowser.open("https://www.google.fr/search?q="+dorks[linknumber]+":"+name_accurate+" site:"+site) #search name with dorks and on specific website
            linknumber+=1 
        webbrowser.open("https://www.google.fr/search?q="+name_accurate+" site:"+site) #search name without dorks, on specific website

#----------------------------------------------------------
#tkinter part


lbl=Label(window, text="Google Dorks Research")
lbl.place(x=80, y=50)
lbl=Label(window, text="Name :")
lbl.place(x=20, y=100)
txtfldname=Entry(window, text="Name", bd=5)
txtfldname.place(x=80, y=100)
lbl=Label(window, text="Website :")
lbl.place(x=20, y=125)
txtfldsite=Entry(window, text="Website", bd=5)
txtfldsite.place(x=80, y=125)
btn=Button(window, text="research", command=lambda : dorks(txtfldname.get(), txtfldsite.get()))
btn.place(x=120, y=175)



window.title('Google dorks research')
window.geometry("300x300")
window.mainloop()