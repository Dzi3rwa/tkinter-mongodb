from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import json
from pymongo import MongoClient
from operator import attrgetter

root = tk.Tk()
root.title("database-viewer")
root.geometry("1100x600")


Imie = tk.StringVar()
Nazwisko = tk.StringVar()
Wiek = tk.StringVar()
Miasto = tk.StringVar()
Nowa = tk.StringVar()
Szukaj = tk.StringVar()
Szukaj2 = tk.StringVar()
Aktualizuj1 = tk.StringVar()
Aktualizuj2 = tk.StringVar()
Adres = tk.StringVar()
Port = tk.StringVar()
Baza = tk.StringVar()
Kolekcja = tk.StringVar()
Dodajklucz1 = tk.StringVar()
Dodajklucz2 = tk.StringVar()
db = tk.StringVar()
coll = tk.StringVar()

client = MongoClient()
trv = Treeview()


def kolekcja():
    baza = db.get()
    mydb = client[baza]
    collection = mydb.list_collection_names()
    tab = []
    j = 0
    for i in collection:
        tab.insert(j, i)
        j += 1
    sub_window = tk.Toplevel(root)
    sub_window.geometry("400x200")
    sub_window.title("Kolekcje")
    wrapper = LabelFrame(sub_window, text="Kolekcje")
    wrapper.pack(fill="both", expand="yes", padx=20, pady=10)
    k = ttk.Combobox(wrapper, width=27, textvariable=coll)
    k['values'] = (tab)
    k.current(0)
    k.pack(side=LEFT, padx=30)

    buttonDodaj = Button(wrapper,  text="POŁĄCZ",
                         command=lambda: polacz(baza))
    buttonDodaj.pack(side=LEFT, padx=15)


def pokazBazy():
    tab = []
    j = 0
    for i in client.list_database_names():
        tab.insert(j, i)
        j += 1
    sub_window = tk.Toplevel(root)
    sub_window.geometry("400x200")
    sub_window.title("Bazy danych")
    wrapper = LabelFrame(sub_window, text="Bazy danych")
    wrapper.pack(fill="both", expand="yes", padx=20, pady=10)
    k = ttk.Combobox(wrapper, width=27, textvariable=db)
    k['values'] = (tab)
    k.current(0)
    k.pack(side=LEFT, padx=30)
    buttonDodaj = Button(wrapper,  text="DODAJ", command=kolekcja)
    buttonDodaj.pack(side=LEFT, padx=15)


def polacz(baza):
    adres = Adres.get()
    port = Port.get()
    kolekcja = coll.get()
    try:
        string = str("mongodb://" + adres + ":" + port + "/")
        global client
        client = MongoClient(string)
        global trv
        global mycol
        global mydb
        mydb = client[baza]
        mycol = mydb[kolekcja]

        obj = mycol.find_one()

        if obj != None:

            if len(obj) == 5:
                trv = Treeview(wrapper1, columns=(1, 2, 3, 4),
                               show="headings", height="18")
                trv.pack(side=LEFT)
                Scrollbar2 = Scrollbar(
                    wrapper1, orient=HORIZONTAL, command=trv.xview)
                Scrollbar2.pack(side=TOP, fill=X)
                trv.configure(xscrollcommand=Scrollbar2.set)
                tab = []
                if obj != None:
                    j = 0
                    for i in obj:
                        if i != "_id":
                            tab.insert(j, i)
                            j += 1
                t = ""
                lableImie = Label(wrapper3, text=tab[0])
                lableImie.pack(side=LEFT, padx=5)
                entryImie = Entry(wrapper3, textvariable=Imie,  width=20)
                entryImie.pack(side=LEFT, padx=15)
                lableNazwisko = Label(wrapper3, text=tab[1])
                lableNazwisko.pack(side=LEFT, padx=5)
                entryNazwisko = Entry(
                    wrapper3, textvariable=Nazwisko, width=20)
                entryNazwisko.pack(side=LEFT, padx=15)
                labelWiek = Label(wrapper3, text=tab[2])
                labelWiek.pack(side=LEFT, padx=5)
                entryWiek = Entry(wrapper3, textvariable=Wiek, width=20)
                entryWiek.pack(side=LEFT, padx=15)
                labelMiasto = Label(wrapper3, text=tab[3])
                labelMiasto.pack(side=LEFT, padx=5)
                entryMiasto = Entry(wrapper3, textvariable=Miasto,  width=20)
                entryMiasto.pack(side=LEFT, padx=15)
                buttonDodaj = Button(wrapper3,  text="DODAJ", command=dodaj)
                buttonDodaj.pack(side=LEFT, padx=15)

            elif len(obj) == 6:
                trv = Treeview(wrapper1, columns=(1, 2, 3, 4, 5),
                               show="headings", height="18")
                trv.pack(side=TOP)
                Scrollbar2 = Scrollbar(
                    wrapper1, orient=HORIZONTAL, command=trv.xview)
                Scrollbar2.pack(side=TOP, fill=X)
                trv.configure(xscrollcommand=Scrollbar2.set)
                tab = []
                if obj != None:
                    j = 0
                    for i in obj:
                        if i != "_id":
                            tab.insert(j, i)
                            j += 1
                t = ""
                lableImie = Label(wrapper3, text=tab[0])
                lableImie.pack(side=LEFT, padx=5)
                entryImie = Entry(wrapper3, textvariable=Imie,  width=20)
                entryImie.pack(side=LEFT, padx=15)
                lableNazwisko = Label(wrapper3, text=tab[1])
                lableNazwisko.pack(side=LEFT, padx=5)
                entryNazwisko = Entry(
                    wrapper3, textvariable=Nazwisko, width=20)
                entryNazwisko.pack(side=LEFT, padx=15)
                labelWiek = Label(wrapper3, text=tab[2])
                labelWiek.pack(side=LEFT, padx=5)
                entryWiek = Entry(wrapper3, textvariable=Wiek, width=20)
                entryWiek.pack(side=LEFT, padx=15)
                labelMiasto = Label(wrapper3, text=tab[3])
                labelMiasto.pack(side=LEFT, padx=5)
                entryMiasto = Entry(wrapper3, textvariable=Miasto,  width=20)
                entryMiasto.pack(side=LEFT, padx=15)
                labelNowa = Label(wrapper3, text=tab[4])
                labelNowa.pack(side=LEFT, padx=5)
                entryNowa = Entry(wrapper3, textvariable=Nowa,  width=20)
                entryNowa.pack(side=LEFT, padx=15)
                buttonDodaj = Button(wrapper3,  text="DODAJ", command=dodaj)
                buttonDodaj.pack(side=LEFT, padx=15)
            elif len(obj) == 7:
                trv = Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6),
                               show="headings", height="18")
                trv.pack()
        else:
            trv = Treeview(wrapper1, columns=(1, 2, 3, 4),
                           show="headings", height="18")
            trv.pack()
            trv.heading(1, text="imie")
            trv.heading(2, text="nazwisko")
            trv.heading(3, text="wiek")
            trv.heading(4, text="miasto")
            t = ""
            lableImie = Label(wrapper3, text="imie")
            lableImie.pack(side=LEFT, padx=5)
            entryImie = Entry(wrapper3, textvariable=Imie,  width=20)
            entryImie.pack(side=LEFT, padx=15)
            lableNazwisko = Label(wrapper3, text="nazwisko")
            lableNazwisko.pack(side=LEFT, padx=5)
            entryNazwisko = Entry(wrapper3, textvariable=Nazwisko, width=20)
            entryNazwisko.pack(side=LEFT, padx=15)
            labelWiek = Label(wrapper3, text="wiek")
            labelWiek.pack(side=LEFT, padx=5)
            entryWiek = Entry(wrapper3, textvariable=Wiek, width=20)
            entryWiek.pack(side=LEFT, padx=15)
            labelMiasto = Label(wrapper3, text="miasto")
            labelMiasto.pack(side=LEFT, padx=5)
            entryMiasto = Entry(wrapper3, textvariable=Miasto,  width=20)
            entryMiasto.pack(side=LEFT, padx=15)
            buttonDodaj = Button(wrapper3,  text="DODAJ", command=dodaj)
            buttonDodaj.pack(side=LEFT, padx=15)

        j = 1
        for i in obj:
            if i != "_id":
                trv.heading(j, text=i)
                j += 1
        pokaz()

    except:
        t = ""

    tab = []
    if obj != None:
        j = 0
        for i in obj:
            if i != "_id":
                tab.insert(j, i)
                j += 1
    else:
        tab.insert(0, "imie")
        tab.insert(1, "nazwisko")
        tab.insert(2, "wiek")
        tab.insert(3, "miasto")

    global lableAktualizuj1
    lableAktualizuj1 = Label(wrapper5, text="KOLUMNA DO AKUTUALIZACJI:")
    lableAktualizuj1.pack(side=LEFT, padx=30)
    k = ttk.Combobox(wrapper5, width=27, textvariable=Aktualizuj1)
    k['values'] = (tab)
    k.current(0)
    k.pack(side=LEFT, padx=30)
    lableAktualizuj2 = Label(wrapper5, text="NOWA WARTOŚĆ:")
    lableAktualizuj2.pack(side=LEFT, padx=30)
    entryAktualizuj2 = Entry(wrapper5, textvariable=Aktualizuj2, width=20)
    entryAktualizuj2.pack(side=LEFT, padx=30)
    buttonAktualizuj = Button(wrapper5,  text="AKUTALIZUJ", command=akt)
    buttonAktualizuj.pack(side=LEFT, padx=30)


def dodaj():
    b = True
    imie = Imie.get()
    nazwisko = Nazwisko.get()
    wiek = Wiek.get()
    miasto = Miasto.get()
    nowa = Nowa.get()

    obj = mycol.find_one()

    if obj != None and len(obj) > 5:
        tab = []
        j = 0
        for i in obj:
            if i != "_id":
                tab.insert(j, i)
                j += 1

        user = {tab[0]: imie, tab[1]: nazwisko,
                tab[2]: wiek, tab[3]: miasto, tab[4]: nowa}
        for i in obj:
            for i in mycol.find():
                if i[tab[0]] == user[tab[0]] and i[tab[1]] == user[tab[1]] and i[tab[2]] == user[tab[2]] and i[tab[3]] == user[tab[3]] and i[tab[4]] == user[tab[4]]:
                    b = False
    elif obj != None:
        tab = []
        j = 0
        for i in obj:
            if i != "_id":
                tab.insert(j, i)
                j += 1
        user = {tab[0]: imie, tab[1]: nazwisko,
                tab[2]: wiek, tab[3]: miasto}
        for i in obj:
            for i in mycol.find():
                if i[tab[0]] == user[tab[0]] and i[tab[1]] == user[tab[1]] and i[tab[2]] == user[tab[2]] and i[tab[3]] == user[tab[3]]:
                    b = False
    else:
        user = {"imie": imie, "nazwisko": nazwisko,
                "wiek": wiek, "miasto": miasto}
    print(b)
    if b == True:
        mycol.insert_one(user)

    for i in trv.get_children():
        trv.delete(i)

    for i in mycol.find():
        j = 1
        string = ""
        for k in i:
            if k != "_id":
                string += i[k] + " "
                j += 1
        aktualizuj([string])


def szukaj():
    a = Szukaj.get()
    tab = []
    for i in trv.get_children():
        trv.delete(i)
    for i in mycol.find():
        print(i)
        for k in i:
            if i[k] == a:
                tab.append(i)
                break

    for i in tab:
        j = 1
        string = ""
        for k in i:
            if k != "_id":
                string += i[k] + " "
                j += 1
        aktualizuj([string])


def usun():
    w = trv.selection()[0]
    index = 1
    j = 1
    for i in trv.get_children():
        if w == i:
            w = index
        trv.delete(i)
        index += 1
    for i in mycol.find():
        if j == w:
            mycol.delete_one(i)
        j += 1

    for i in mycol.find():
        j = 1
        string = ""
        for k in i:
            if k != "_id":
                string += i[k] + " "
                j += 1
        aktualizuj([string])


def akt():
    j = 1
    kol = Aktualizuj1.get()
    wartosc = Aktualizuj2.get()
    kolumna = kol.lower()
    w = trv.selection()[0]
    index = 1
    for i in trv.get_children():
        if w == i:
            w = index
        trv.delete(i)
        index += 1

    for i in mycol.find():
        if j == w:
            try:
                t = "KOLUMNA DO AKUTUALIZACJI:"
                lableAktualizuj1.config(text=t)
                myquery = {"_id": i["_id"]}
                newvalues = {"$set": {kolumna: wartosc}}
                mycol.update_one(myquery, newvalues)
            except:
                t = "NIE MA TAKIEJ KOLUMNY!"
                lableAktualizuj1.config(text=t)
        j += 1

    for i in mycol.find():
        j = 1
        string = ""
        for k in i:
            if k != "_id":
                string += i[k] + " "
                j += 1
        aktualizuj([string])


def dodajKlucz():

    def aktualizuj2(rows):
        for i in rows:
            trv2.insert('', 'end', values=i)

    kol = Dodajklucz1.get()
    wartosc = Dodajklucz2.get()
    kolumna = kol.lower()
    w = trv.selection()[0]
    index = 1

    for i in trv.get_children():
        if w == i:
            w = index
        index += 1
    trv.destroy()

    obj = mycol.find_one()
    tab = []
    j = 0
    for i in obj:
        if i != "_id":
            tab.insert(j, i)
            j += 1

    j = 1
    for i in mycol.find():
        if j == w:
            myquery = {tab[0]: i[tab[0]], tab[1]: i[tab[1]],
                       tab[2]: i[tab[2]], tab[3]: i[tab[3]]}
            newvalues = {"$set": {kolumna: wartosc}}
            mycol.update_one(myquery, newvalues)
        else:
            myquery = {"_id": i["_id"]}
            newvalues = {"$set": {kolumna: ""}}
            mycol.update_one(myquery, newvalues)

        j += 1

    obj = mycol.find_one()

    if len(obj) == 5:
        trv2 = Treeview(wrapper1, columns=(1, 2, 3, 4),
                        show="headings", height="18")
        trv2.pack()
    elif len(obj) == 6:
        trv2 = Treeview(wrapper1, columns=(1, 2, 3, 4, 5),
                        show="headings", height="18")
        trv2.pack()

    j = 1
    for i in obj:
        if i != "_id":
            trv2.heading(j, text=i)
            j += 1
    trv2.heading(5, text=kolumna)
    j = 1
    for i in mycol.find():
        if j == w:
            aktualizuj2([i[tab[0]] + " " + i[tab[1]] +
                         " " + i[tab[2]] + " " + i[tab[3]] + " " + wartosc])
        else:
            aktualizuj2([i[tab[0]] + " " + i[tab[1]] +
                         " " + i[tab[2]] + " " + i[tab[3]]])
        j += 1


def pokaz():
    for i in trv.get_children():
        trv.delete(i)

    for i in mycol.find():
        j = 1
        string = ""
        for k in i:
            if k != "_id":
                string += i[k] + " "
                j += 1
        aktualizuj([string])


def plikJson():
    jsonArray = []
    obj = mycol.find_one()
    tab = []
    j = 0
    for i in obj:
        if i != "_id":
            tab.insert(j, i)
            j += 1

    for i in mycol.find():
        jsonArray.append({tab[0]: i[tab[0]], tab[1]: i[tab[1]],
                         tab[2]: i[tab[2]], tab[3]: i[tab[3]], tab[4]: i[tab[4]]})
    jsonFilePath = "mongo.json"

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray, indent=4))


def aktualizuj(rows):
    for i in rows:
        trv.insert('', 'end', values=i)


global wrapper1
wrapper1 = LabelFrame(root, text="Użytkownicy")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)


def fun1():
    new = tk.Toplevel()


def fun2():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("650x200")
    sub_window.title("Połącz")
    wrapper0 = LabelFrame(sub_window, text="Połącz")
    wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
    lableBlad = Label(wrapper0)
    lableBlad.pack(side=LEFT, padx=10)
    lableAdres = Label(wrapper0, text="ADRES:")
    lableAdres.pack(side=LEFT, padx=10)
    entryAdres = Entry(wrapper0, textvariable=Adres,
                       width=20, text="localhost")
    entryAdres.insert(0, "")
    entryAdres.insert(0, "localhost")
    entryAdres.pack(side=LEFT, padx=10)
    lablePort = Label(wrapper0, text="PORT:")
    lablePort.pack(side=LEFT, padx=10)
    entryPort = Entry(wrapper0, textvariable=Port,  width=20)
    entryPort.insert(0, "")
    entryPort.insert(0, "27017")
    entryPort.pack(side=LEFT, padx=10)
    buttonPokaz = Button(
        wrapper0,  text="POKAZ dostepne bazy", command=pokazBazy)
    buttonPokaz.pack(side=LEFT, padx=10)


global sub_window2
sub_window2 = tk.Toplevel(root)
sub_window2.geometry("1150x200")
sub_window2.title("Dodaj")
sub_window2.withdraw()
wrapper3 = LabelFrame(sub_window2, text="Dodaj")
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)


def fun3():
    sub_window2.deiconify()


def fun4():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("200x200")
    sub_window.title("Usuń")
    wrapper4 = LabelFrame(sub_window, text="Usuń")
    wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)
    buttonUsun = Button(wrapper4, text="USUN WYBRANY ELEMENT", command=usun)
    buttonUsun.pack()


global sub_window3
sub_window3 = tk.Toplevel(root)
sub_window3.geometry("1050x200")
sub_window3.title("Aktualizuj")
sub_window3.withdraw()
wrapper5 = LabelFrame(sub_window3, text="Aktualizuj")
wrapper5.pack(fill="both", expand="yes", padx=20, pady=10)


def fun5():
    sub_window3.deiconify()


def fun6():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("1050x200")
    sub_window.title("Aktualizuj")
    wrapper6 = LabelFrame(sub_window, text="Dodaj klucz")
    wrapper6.pack(fill="both", expand="yes", padx=20, pady=10)
    lableDodajKlucz = Label(wrapper6, text="NOWY KLUCZ:")
    lableDodajKlucz.pack(side=LEFT, padx=30)
    entryDodajKlucz = Entry(wrapper6, textvariable=Dodajklucz1,  width=20)
    entryDodajKlucz.pack(side=LEFT, padx=30)
    lableDodajKlucz2 = Label(wrapper6, text="NOWA WARTOŚĆ:")
    lableDodajKlucz2.pack(side=LEFT, padx=30)
    entryDodajKlucz2 = Entry(wrapper6, textvariable=Dodajklucz2, width=20)
    entryDodajKlucz2.pack(side=LEFT, padx=30)
    buttonDodajKlucz = Button(
        wrapper6,  text="DODAJ KLUCZ", command=dodajKlucz)
    buttonDodajKlucz.pack(side=LEFT, padx=30)


def fun7():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("1050x200")
    sub_window.title("Szukaj")
    wrapper2 = LabelFrame(sub_window, text="Szukaj")
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    entrySzukaj = Entry(wrapper2, textvariable=Szukaj,  width=30)
    entrySzukaj.pack(side=LEFT, padx=60)
    buttonSzukaj = Button(wrapper2,  text="SZUKAJ", command=szukaj)
    buttonSzukaj.pack(side=LEFT, padx=60)
    buttonPokaz = Button(wrapper2,  text="POKAŻ WSZYSTKO", command=pokaz)
    buttonPokaz.pack(side=LEFT, padx=60)


def fun8():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("1050x200")
    sub_window.title("JSON")
    wrapper = LabelFrame(sub_window, text="JSON")
    wrapper.pack(fill="both", expand="yes", padx=20, pady=10)
    buttonJson = Button(wrapper,  text="NOWY PLIK JSON", command=plikJson)
    buttonJson.pack(side=LEFT, padx=60)


menubar = tk.Menu(root)
menu_connection = tk.Menu(menubar, tearoff=0)
menu_action = tk.Menu(menubar, tearoff=0)
menu_view = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="connection", menu=menu_connection)
menubar.add_cascade(label="action", menu=menu_action)
menubar.add_cascade(label="view", menu=menu_view)

menu_connection.add_command(label="Connect", command=fun2)

menu_db_type = tk.Menu(menu_connection, tearoff=0)
menu_connection.add_cascade(label="db type", menu=menu_db_type)
menu_db_type.add_command(label="NoSQL", command=fun1)
menu_db_type.add_command(label="SQL", command=fun1)


menu_connection.add_separator()
menu_connection.add_command(label="exit", command=root.destroy)

menu_action.add_command(label="add", command=fun3)
menu_action.add_command(label="remove", command=fun4)
menu_action.add_command(label="update", command=fun5)
menu_action.add_command(label="new key", command=fun6)
menu_action.add_command(label="filter", command=fun7)
menu_action.add_separator()
menu_action.add_command(label="JSON file", command=fun8)


def color():
    sub_window = tk.Toplevel(root)
    sub_window.geometry("400x200")
    sub_window.title("Color")
    wrapper = LabelFrame(sub_window, text="Color")
    wrapper.pack(fill="both", expand="yes", padx=20, pady=10)


def sizeS():
    root.geometry("300x300")


def sizeM():
    root.geometry("700x450")


def sizeL():
    root.geometry("1100x700")


def red():
    root.config(bg="red")
    menubar.config(bg="red", fg="#FA9F88")
    menu_connection.config(bg="red", fg="#FA9F88")
    menu_action.config(bg="red", fg="#FA9F88")
    menu_color.config(bg="red", fg="#FA9F88")
    menu_size.config(bg="red", fg="#FA9F88")
    menu_view.config(bg="red", fg="#FA9F88")
    menu_db_type.config(bg="red", fg="#FA9F88")


def green():
    root.config(bg="green")
    menubar.config(bg="green", fg="#93D68D")
    menu_connection.config(bg="green", fg="#93D68D")
    menu_action.config(bg="green", fg="#93D68D")
    menu_color.config(bg="green", fg="#93D68D")
    menu_size.config(bg="green", fg="#93D68D")
    menu_view.config(bg="green", fg="#93D68D")
    menu_db_type.config(bg="green", fg="#93D68D")


def blue():
    root.config(bg="blue")
    menubar.config(bg="blue", fg="#92CDF5")
    menu_connection.config(bg="blue", fg="#92CDF5")
    menu_action.config(bg="blue", fg="#92CDF5")
    menu_color.config(bg="blue", fg="#92CDF5")
    menu_size.config(bg="blue", fg="#92CDF5")
    menu_view.config(bg="blue", fg="#92CDF5")
    menu_db_type.config(bg="blue", fg="#92CDF5")


menu_color = tk.Menu(menu_view, tearoff=0)
menu_view.add_cascade(label="color", menu=menu_color)
menu_color.add_command(label="red", command=red)
menu_color.add_command(label="green", command=green)
menu_color.add_command(label="blue", command=blue)

menu_size = tk.Menu(menu_view, tearoff=0)
menu_view.add_cascade(label="size", menu=menu_size)
menu_size.add_command(label="small", command=sizeS)
menu_size.add_command(label="medium", command=sizeM)
menu_size.add_command(label="large", command=sizeL)

root.config(menu=menubar)
root.mainloop()
