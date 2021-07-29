import cassiopeia as cass
from tkinter import *
from tkinter import ttk

cass.set_riot_api_key("") #insert your api key here

app = Tk()
app.title('Check your stats')
app.geometry('400x500')

#wyswietlanie gier jako lista
def wyswietl_gry():
    tree.delete(*tree.get_children())
    text = napis1.get()
    summoner = cass.get_summoner(name=text,region=wybor_region.get())
    global mecze
    mecze = cass.get_match_history(summoner,None,int(liczbagier.get()))
    
    label4 = Label(app,text='Kliknij dwukrotnie na mecz aby zobaczyc szczegoly',font=('bold',11), pady=13,padx=15)
    label4.grid(row=4, columnspan=4, sticky=W,padx=10)
    

    
    for x in range(int(liczbagier.get())):
        for gamer in mecze[x].participants:
            if gamer.summoner.name == text:
                tree.insert(parent='', index='end', iid=x, text='', values=(x,czy_wygrany(gamer),gamer.champion.name))


#sprawdza czy dany mecz jest wygrany
def czy_wygrany(gamer):
    if gamer.stats.win == False:
        return 'Lose'
    else:
        return 'Win'


#dwukrotne klikniecie jakiegos meczu
def clicker(event):
    app2 = Toplevel(app)
    
    selected = tree.focus()

    label_1 = Label(app2,text=f'Mapa: {mecze[int(selected)].map.name}')
    label_1.grid(row=0, column=0)

    #BLUE TEAM

    #summoners name
    Label(app2,text=f"Blue team ({czy_wygrany(mecze[int(selected)].blue_team.participants[0])}):").grid(row=1,column=0,sticky=W,padx=20,pady=15)

    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].blue_team.participants[x].summoner.name}").grid(row=x+2,column=0,sticky=W,padx=20)
    

    #kda
    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].blue_team.participants[x].stats.kills}-{mecze[int(selected)].blue_team.participants[x].stats.deaths}-{mecze[int(selected)].blue_team.participants[x].stats.assists}").grid(row=x+2,column=2,sticky=W,padx=20)


    #champions
    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].blue_team.participants[x].champion.name}").grid(row=x+2,column=1,sticky=W,padx=20)

    

    #RED TEAM

    #summoners name
    Label(app2,text=f"\nRed team ({czy_wygrany(mecze[int(selected)].red_team.participants[0])}):").grid(row=7,column=0,sticky=W,padx=20,pady=15)
    
    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].red_team.participants[x].summoner.name}").grid(row=x+8,column=0,sticky=W,padx=20)


    #kda
    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].red_team.participants[x].stats.kills}-{mecze[int(selected)].red_team.participants[x].stats.deaths}-{mecze[int(selected)].red_team.participants[x].stats.assists}").grid(row=x+8,column=2,sticky=W,padx=20)


    #champ
    for x in range(5):
        Label(app2,text=f"{mecze[int(selected)].red_team.participants[x].champion.name}").grid(row=x+8,column=1,sticky=W,padx=20)
 
    
    app2.geometry('350x400')



napis1 = StringVar()

label1 = Label(app,text='Nick:', font=('bold',11), pady=13,padx=15)
label1.grid(row=0, column=0, sticky=W)

label2 = Label(app,text='Liczba gier:',font=('bold',11), pady=13,padx=15)
label2.grid(row=1, column=0, sticky=W)

label3 = Label(app,text='Region:',font=('bold',11), pady=13,padx=15)
label3.grid(row=2, column=0, sticky=W)

wpisanie1 = Entry(app, textvariable=napis1)
wpisanie1.grid(row=0,column=1)

opcje1 = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]

opcje2 = [
    'EUNE',
    'EUW',
    'NA'
]

liczbagier = StringVar()
liczbagier.set(opcje1[4])

wybor_region = StringVar()
wybor_region.set(opcje2[0])

drop1 = ttk.Combobox(app,value=opcje1,textvariable=liczbagier,width=4)
drop1.current(0)
drop1.grid(row=1,column=1,padx=15)

drop2 = ttk.Combobox(app,value=opcje2,textvariable=wybor_region,width=6)
drop2.current(0)
drop2.grid(row=2,column=1,padx=15)

button = Button(app, text='Zatwierdz', width=12, command=wyswietl_gry)
button.grid(row=1,column=3, padx=38)

tree = ttk.Treeview(app)

tree['columns'] = ('id','champion','win/lose')

tree.column('#0',width=0, stretch=NO)
tree.column('id', anchor=CENTER, width=30)
tree.column('champion', anchor=CENTER, width=150)
tree.column('win/lose', anchor=CENTER, width=150)

tree.heading('id',text="id",anchor=CENTER)
tree.heading('champion',text="champion",anchor=CENTER)
tree.heading('win/lose',text="win/lose",anchor=CENTER)

tree.grid(row=3,column=0,columnspan=10,pady=30,padx=10)

tree.bind('<Double-1>', clicker)

mainloop()