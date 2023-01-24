from tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return

    global expression
    expression += str(touche)
    equation.set("")


def calculer():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression=""

def effacer():
    global expression
    expression = ""
    equation.set("")

def pourcentage():
    try:
        a=expression
        return
        b=expression
        return
        c=expression
        return
        d=expression
        return
        e=expression
        tota=a+b+c+d+e
        
        per=float(tota)*(100/500)
        
     
        
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("erreur")
        expression=""

def racine_carrée():
    try:
        x=expression
        x**(0.5)
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("erreur")
        expression=""

if __name__ == "main":
    gui = Tk()

    # couleur de fond
    gui.configure(background="#101419")

    # titre de l'application
    gui.title("Calculatrice")

    # taille de la fenetre
    gui.geometry("235x385")

    # variable pour stocker le contenu actuel
    equation = StringVar()

    # boite de resultats
    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height="2")
    resultat.grid(columnspan=4)

    #boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "_", 1, 2, 3, "+", 0, ".", "/", "=", "V", "%"]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B", fg="#FFF", height=4, width=6)
        #rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grind(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    b = Label(gui, text="Effacer", bg="#984447", fg="#FFF", height=4, width=26)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4)
    gui.mainloop()
