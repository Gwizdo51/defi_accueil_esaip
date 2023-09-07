from tkinter import *
import tkinter
from convertisseur import *
 
root = Tk()
root.geometry('1200x500')
btn1 =  Menubutton ( root, text = "unité de mesure de base", relief = RAISED )
btn1.menu  =  Menu ( btn1, tearoff = 1 )
btn1["menu"]  =  btn1.menu

val_saisie = Label(root, text='Entrez votre valeur')
val_saisie.place()

val = Entry(root, width=10)
val.place(x = 130, y = 104)
    
val_init = IntVar()
val_init1 = IntVar()
val_init2 = IntVar()
val_init3 = IntVar()
val_init4 = IntVar()
val_init5 = IntVar()
val_init6 = IntVar()
val_init7 = IntVar()
val_init8 = IntVar()
val_init9 = IntVar()
val_init10 = IntVar()

 
btn1.menu.add_checkbutton ( label = "kg",
                          variable = val_init )
btn1.menu.add_checkbutton ( label = "km/h",
                          variable = val_init1 )
btn1.menu.add_checkbutton ( label = "Francs",
                          variable = val_init2 )
btn1.menu.add_checkbutton ( label = "€",
                          variable = val_init3 )
btn1.menu.add_checkbutton ( label = "$",
                          variable = val_init4 )
btn1.menu.add_checkbutton ( label = "mp/h",
                          variable = val_init5 )
btn1.menu.add_checkbutton ( label = "livres",
                          variable = val_init6 )
btn1.menu.add_checkbutton ( label = "m/s",
                          variable = val_init7 )
btn1.menu.add_checkbutton ( label = "pente (%)",
                          variable = val_init8 )
btn1.menu.add_checkbutton ( label = "pente (°)",
                          variable = val_init9 )
btn1.menu.add_checkbutton ( label = "écartement des enceintes",
                          variable = val_init10 )

btn1.place(x = 200, y = 100)
unit_base = Entry()

btn2 =  Menubutton ( root, text = "unité de mesure de conversion", relief = RAISED )
btn2.menu  =  Menu ( btn2, tearoff = 0 )
btn2["menu"]  =  btn2.menu
    
val_init11 = IntVar()
val_init12 = IntVar()
val_init13 = IntVar()
val_init14 = IntVar()
val_init15 = IntVar()
val_init16 = IntVar()
val_init17 = IntVar()
val_init18 = IntVar()
val_init19 = IntVar()
val_init20 = IntVar()
val_init21 = IntVar()
 
btn2.menu.add_checkbutton ( label = "kg",
                          variable = val_init11 )
btn2.menu.add_checkbutton ( label = "km/h",
                          variable = val_init12 )
btn2.menu.add_checkbutton ( label = "Francs",
                          variable = val_init13 )
btn2.menu.add_checkbutton ( label = "€",
                          variable = val_init14 )
btn2.menu.add_checkbutton ( label = "$",
                          variable = val_init15 )
btn2.menu.add_checkbutton ( label = "mp/h",
                          variable = val_init16 )
btn2.menu.add_checkbutton ( label = "livres",
                          variable = val_init17 )
btn2.menu.add_checkbutton ( label = "m/s",
                          variable = val_init18 )
btn2.menu.add_checkbutton ( label = "pente (%)",
                          variable = val_init19 )
btn2.menu.add_checkbutton ( label = "pente (°)",
                          variable = val_init20 )
btn2.menu.add_checkbutton ( label = "écartement des enceintes",
                          variable = val_init21 )

btn2.place(x = 500, y = 100)
unit_convert = Entry()

btn3 =  tkinter.Button (text = "convertir", relief = RAISED )
unit_result = Entry()

val_res = Label(root)
val_res.place()

val1 = Entry(root, width=10)
val1.place(x = 970, y = 104)

btn3.place(x = 900, y = 100)
root.mainloop()