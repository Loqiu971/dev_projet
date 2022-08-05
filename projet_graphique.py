#!/bin/usr/env python3
# -*- coding : utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import random
import time

###### TOUTES les fonctions #####

def lancer():
    ### Menu
    choix = ''
    #Creation d'un frame pour le texte principale
    frame1 = Frame(ui, bg = "white", borderwidth = 2, relief = GROOVE)
    frame1.pack(padx = 10, pady = 10)

    texte = "1 Lire les règles de la simulation \n" +\
           "2 Choix des différents mode de la simulation \n" +\
           "3 Lancer la partie\n" +\
           "4 Quitter la simulation"
    label1 = Label(frame1, text = "Bienvenue sur Tri Ex, un simulateur de tri de carte !    \n  ", font = ("Purisa", 22), bg ="#1B94C2")
    label1.pack()
    label2 = Label(frame1, text = " Créateurs : LAFONT Lucas et VERGEROLLE Loïcq  .                                                                                               ", font = ("Purisa", 10), bg = "#1B94C2")
    label2.pack(side = LEFT)
    #label2 = Label(frame2, text = texte, font = ("Purisa", 18), bg = "#1B94C2")
    #label2.pack()
    BoutonLancer = Button(ui, text = " CONTINUER", font = ("Purisa", 17), borderwidth = 2, bg = "#1792CB", width = 12, height = 1, command = menu)   
    BoutonLancer.pack()
    ui.mainloop()

def menu():
    global uk, ui, fond, Bouton1, Bouton2, Bouton3, Bouton4
    ui.destroy()
    uk = Tk()
    uk.title("Le Tri Ex")
    uk.configure(bg = "#1B94C2")
    uk.resizable(width = False, height = False)
    # Image de fond

    fond = Canvas(uk, width = 740, height = 400, bg = "#1792CB")
    fond.pack()
    # Frame et boutons...
    frame1 = Frame(uk, bg = "#1B94C2", borderwidth = 2, relief = GROOVE)
    frame1.pack(side = BOTTOM, padx = 10, pady = 10)

    def fond_bleu():
        global fond
        global Bouton1, Bouton2, Bouton3, Bouton4
        fond.destroy()
        Bouton1.destroy()
        Bouton2.destroy()
        Bouton3.destroy()
        Bouton4.destroy()
        buttons()
        fond = Canvas(uk, width = 740, height = 400, bg = "#2AA9BF")
        fond.pack(side = TOP)
    
        
    def fond_rouge():
        global Bouton1, Bouton2, Bouton3, Bouton4
        global fond
        fond.destroy()
        Bouton1.destroy()
        Bouton2.destroy()
        Bouton3.destroy()
        Bouton4.destroy()
        fond = Canvas(uk, width = 740, height = 400, bg = "#E7524B")
        fond.pack(side = TOP)
        buttons()
        
    def fond_vert():
        global fond
        global Bouton1, Bouton2, Bouton3, Bouton4
        fond.destroy()
        Bouton1.destroy()
        Bouton2.destroy()
        Bouton3.destroy()
        Bouton4.destroy()
        fond = Canvas(uk, width = 740, height = 400, bg = "#38AA21")
        fond.pack(side = TOP)
        buttons()
        
        
    #Menu bar..
    menubar = Menu(uk)
    menufichier = Menu(uk,tearoff=0)
    menufichier.add_command(label = "Fond bleu", command  = fond_bleu)
    menufichier.add_command(label = "Fond rouge", command = fond_rouge)
    menufichier.add_command(label = "Fond vert", command = fond_vert)
    menubar.add_cascade(label="Font d'écran", menu= menufichier)


    menubar.add_cascade(label = "Quitter", command = uk.destroy)

    uk.config(menu = menubar)

    def buttons():
        global Bouton1, Bouton2, Bouton3, Bouton4
        Bouton1 = Button(frame1, text = "Règles de la simulation", font = ("Purisa", 10), borderwidth = 2, bg = "#1792CB", width = 20, height = 2, command = règle_du_jeu)
        Bouton1.pack(side = LEFT, padx = 10, pady = 10)
        Bouton2 = Button(frame1, text = "Modes de simulation", font = ("Purisa", 10), borderwidth = 2, bg = "#1792CB", width = 20, height = 2, command = mode_simulation)
        Bouton2.pack(side = LEFT, padx = 10, pady = 10)
        Bouton3 = Button(frame1, text = "Lancer la simulation", font = ("Purisa", 10), borderwidth = 2, bg = "#1792CB", width = 20, height = 2, command = jouer)
        Bouton3.pack(side = LEFT, padx = 10, pady = 10)
        Bouton4 = Button(frame1, text = "Quitter la simulation", font = ("Purisa", 10), borderwidth = 2, bg = "#1792CB", width = 20, height = 2, command = quitter )
        Bouton4.pack(side = LEFT, padx = 10, pady = 10)

    buttons()
    uk.mainloop()
    
def quitter():
    global uk
    sur = Tk()
    sur.title("Le Tri Ex")
    sur.configure(bg = "#1B94C2")
    sur.resizable(width = False, height = False)
    label = Label(sur, text = "Etês vous sûr de vouloir quitter la simluation ?", font = ("Purisa", 15), bg = "#1B94C2")
    label.pack()

    def quitt():
        global uk
        uk.destroy()
        sur.destroy()

    def reste():
        sur.destroy()
        
    bouton1 = Button(sur, text = "OUI", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 2, width = 5, height = 1, command = quitt)
    bouton2 = Button(sur, text = "NON", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 2, width = 5, height =1, command = reste)
    bouton2.pack(side = RIGHT)
    bouton1.pack(side = RIGHT)
    sur.mainloop()


def mode_simulation():
    global mode

    ib = Tk()
    ib.title("Le Tri Ex")
    ib.configure(bg = "#1B94C2")
    ib.resizable(width = False, height = False)

    frame1 = Frame(ib, bg = "#1B94C2", borderwidth = 2, relief = GROOVE)
    frame2 = Frame(frame1, bg = "#1B94C2", borderwidth = 2, relief = GROOVE)
    frame1.pack()
    frame2.pack(side = BOTTOM)

    label1 = Label(frame1, text = "Choisissez le mode de simulation :\n", font = ("Purisa", 20), bg = "#1B94C2")
    label1.pack()

    # Button

    def Button1():
        print("Vous avez choisi : le tri croissant !")
        choix = "tri croissant"
        recuperation_du_choix(choix)

    def Button2():
        print("Vous avez choisi : le tri décroissant !")
        choix = "tri décroissant"
        recuperation_du_choix(choix)

    def Button3():
        print("Vous avez choisi : le tri à bulle !")
        choix = "tri bulle"
        recuperation_du_choix(choix)

    def Button4():
        print("Vous avez choisi : le tri par insertion !")
        choix = "tri insertion"
        recuperation_du_choix(choix)

    def recuperation_du_choix(choix):
        global mode

        mode = choix
        print("le mode est : ",mode)
        ib.destroy()

    bouton1 = Button(frame2, text = "Tri croissant", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 0.5, width = 12, height = 1, command = Button1)
    bouton2 = Button(frame2, text = "Tri décroisant", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 0.5, width = 12, height = 1, command = Button2)
    bouton3 = Button(frame2, text = "Tri à bulle", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 0.5, width = 12, height = 1, command = Button3)
    bouton4 = Button(frame2, text = "Tri par insertion", font = ("Purisa", 10), bg = "#1B94C2", borderwidth = 0.5, width = 12, height = 1, command = Button4)
    bouton1.pack(side = LEFT)
    bouton2.pack(side = LEFT)
    bouton3.pack(side = LEFT)
    bouton4.pack(side = LEFT)
    
    print("Ultime test : {}".format(mode))

    ib.mainloop()
    
def règle_du_jeu():
    uk = Tk()
    uk.title("Le Tri Ex")
    uk.configure(bg = "#1B94C2")
    uk.resizable(width = False, height = False)
    frame1 = Frame(uk, bg = "#1B94C2", borderwidth = 2, relief = GROOVE)
    frame1.pack(padx = 10, pady = 10)

    frame2 = Frame(frame1, bg = "#1B94C2", borderwidth = 1, relief = GROOVE)
    frame2.pack(side = BOTTOM, padx = 10, pady = 10)
    
    texte1 = ("Les règles de la simulation sont :")
    texte2 = ("\nLorsque vous lancez la simulation, le programme va générer un jeu de carte.")
    texte3 = ("Pour les placer aléatoirement avant la simulation.")
    texte4 = ("Ceci pour ensuite les trier dans le mode voulu.")
    texte5 = ("C'est l'utilisateur qui choisi le mode de tri  que va effectuer l'ordinateur.")
    
    label1 = Label(frame1, text = texte1, font = ("Purisa", 20, 'bold'), bg = "#1B94C2")
    label2 = Label(frame2, text = texte2, font = ("Purisa", 17), bg = "#1B94C2")
    label3 = Label(frame2, text = texte3, font = ("Purisa", 17), bg = "#1B94C2")
    label4 = Label(frame2, text = texte4, font = ("Purisa", 17), bg = "#1B94C2")
    label5 = Label(frame2, text = texte5, font = ("Purisa", 17), bg = "#1B94C2")
    label1.pack(side = TOP)
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    

    uk.mainloop()



def jouer():
    global mode, ui, fond
    
    # Initialisation des coordonnées
    
    x1 = 100
    x2 = 190
    x3 = 280
    x4 = 370
    x5 = 460
    x6 = 550
    x7 = 640
    y = 330

    #Met aléatoirement les images dans le cadre...
    i = 7
    l  = [x1, x2, x3, x4, x5, x6, x7]
    while i <= 13:

        x = random.choice(l)
        print("la variable choisi est : {} ".format(x))
        print("La valeur de la variable que l'on supprime : {}".format(l.index(x)))
        del l[l.index(x)]

        
   
        ##### Affiche les cartes : 7, 8, 9, 10, valet, Dame, roi . En fonction de la valeur de x choisit aléatoirement.
        if i == 7:
            img1 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\{}.gif'.format(i))
            image1 = fond.create_image(x, y, image = img1)

        elif i == 8:
            img2 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\{}.gif'.format(i))
            image2 = fond.create_image(x, y, image = img2)

        elif i == 9:
            img3 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\{}.gif'.format(i))
            image3 = fond.create_image(x, y, image = img3)

        elif i == 10:
            img4 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\{}.gif'.format(i))
            image4 = fond.create_image(x, y, image = img4)
            
        elif i == 11:
            img5 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\valet.gif')
            image5 = fond.create_image(x, y, image = img5)

        elif i == 12:
            img6 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\dame.gif')
            image6 = fond.create_image(x, y, image = img6)

        elif i == 13:
            img7 = PhotoImage(file = r'D:\Users\lycée-loicq\Desktop\Cours_ISN\Projet_Le_Trie_Ex\roi.gif')
            image7 = fond.create_image(x, y, image = img7)

        print("La liste est : {}".format(l))
        i += 1

    ###
    rang = x1, x2, x3, x4, x5, x6, x7
    

    ###### Fontion test     
    def deplacement_souris(evt):
        print("X = {} : Y = {}".format(evt.x, evt.y))

    fond.bind('<Motion>', deplacement_souris)

    # Créer la fenêtre 
    ui.mainloop()

def wait():
    import time
    time.sleep(5)
    
def principal():
    lancer()
   

############# Fonction test
def deplacement_souris(evt):
    print("X = {} : Y = {}".format(evt.x, evt.y))


def gestionnaire(event):
    global x_inity
    if event.keysym == 'Left':
        x -= 10
    elif event.keysym == 'Right':
        x += 10
    else:
        x += 0
    jardin.coords(f_window, x, y)

#jardin.bind('<Key>', gestionnaire)

#############


if __name__ == "__main__":
    mode = 0
    var = ''
    mode_default = True
    ################################           
    #Initialisation du module tkinter

    ui = Tk()
    ui.title('Le Tri Ex')
    ui.configure( bg = "#1B94C2" )
    ui.resizable(width = False, height = False)
    '''a = ui.winfo_screenwidth()
    b = ui.winfo_screenheight()
    jardin = Canvas(ui, width = a, height= b, bg='palegreen')
    jardin.pack()'''

    ###### Deplacement de la souris 
    ui.bind('<Motion>', deplacement_souris)

    ####Lancement des fonctions
    principal()
   