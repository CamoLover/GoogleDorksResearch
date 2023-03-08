import webbrowser

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
            webbrowser.open("https://www.google.fr/search?q="+dorks[linknumber]+":"+name_accurate+" site="+site) #search name with dorks and on specific website
            linknumber+=1 
        webbrowser.open("https://www.google.fr/search?q="+name_accurate+" site="+site) #search name without dorks, on specific website



dorks("name","example.com")