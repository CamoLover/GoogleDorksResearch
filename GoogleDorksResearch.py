import webbrowser
dorks = ["intitle","intext","inurl"]#dorks list
linknumber = 0 #current number in dorks array
name = input("Rentrée le nom de la personne : ") #name of the researched person
name_accurate = '"'+name+'"' #Remake name in correct format
site = input("Un site specifique a recherchée ? (rajoutée l'extension ex = .com) (Si vous n'avez pas de site passer) :") #Specific website to research
if site == "" : #if no website to search
    for i in range(len(dorks)) :
        webbrowser.open("https://www.google.fr/search?q="+dorks[linknumber]+":"+name_accurate) #search name with dorks
        linknumber+=1
else : #if there is a specific website
    for i in range(len(dorks)) :
        webbrowser.open("https://www.google.fr/search?q="+dorks[linknumber]+":"+name_accurate+" site="+site) #search name with dorks and on specific website
        linknumber+=1 
    webbrowser.open("https://www.google.fr/search?q="+name_accurate+" site="+site) #search name without dorks, on specific website