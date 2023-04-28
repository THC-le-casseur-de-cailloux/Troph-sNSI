import tkinter as tk    
import gui_components.banner as bn
import gui_components.stats as st
import gui_components.actions as a
import graphs.actualisation as act
import graphs.SEIR_graphs_tk as grph

mainapp = tk.Tk()  # Crée une instance de la classe Tk
l = 1000#mainapp.winfo_screenwidth()#
h =820 #mainapp.winfo_screenheight()# 
print(l,h)

mainapp.geometry(f"{1280}x{695}+0+0") # Configure la géométrie de la fenêtre # Bloque le redimensionnement de la fenêtre
mainapp.title("SEIR model simulation") # Configure le titre de la fenêtre
mainapp['bg']="#303030" # Configure la couleur de fond de la fenêtre

frame=bn.banner(mainapp,l)
U=st.stats(mainapp,l)
a.action(mainapp,l)

# Fonction pour actualiser l'affichage toutes les secondes

g=grph.graphs_gui(mainapp,l,h)

def actualisation(n=0):
    global g
    if n >= 400:
        return
    if bn.redem == "finish":
        n=0
        g=grph.graphs_gui(mainapp,l,h)
    act.updategraph(n,mainapp,l,h,g)
    st.updatestats(n,l,U)
    bn.compteur(frame,n,l)
    while bn.redem == False:
        mainapp.update()
    while bn.lecture == False:
            mainapp.update() 
    mainapp.after(int(100/bn.sp), actualisation, n+1)


actualisation()
# Boucle principale
mainapp.mainloop()
