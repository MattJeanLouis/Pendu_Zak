from library import *
import streamlit as st

def main():
    # Afficher les données JSON avant le reset du bouton
    with st.expander("avant le reset du bouton"):
        st.json(get_json())

    # Bouton pour changer le mot et réinitialiser les vies
    with st.expander("Bouton"):
        if st.button("changer_mot", type="primary"):
            changer_mot(choisir_mot(), changer_vie(10))

    # Titre de l'application
    st.title("Bienvenue dans le jeu du pendu by Raphalious !")
    # Afficher le nombre de lettres du mot à deviner
    st.write("Le mot à deviner contient", len(mot_actuel()), "lettres.")

    # Input pour la proposition de lettre
    proposition = st.text_input("Proposition de lettre :", "", max_chars=1)

    # Si une proposition a été faite
    if proposition != "" :
        # Tant qu'il reste des vies et que la proposition est valide
        while vie_actuel() > 0 and proposition:
            # Afficher le mot à deviner et les lettres trouvées
            st.write("\nMot à deviner :", afficher_mot_cache(mot_actuel(), afficher_lettres_trouvees()))
            # Afficher le nombre de vies restantes
            st.write("Vies restantes :", vie_actuel())

            # Si la proposition est une lettre
            if len(proposition) == 1:
                lettre = proposition.lower()
                
                # Si la lettre a déjà été devinée
                if lettre in afficher_lettres_trouvees():
                    st.write("Vous avez déjà deviné cette lettre !")
                
                # Si la lettre est dans le mot
                elif lettre in mot_actuel():
                    
                    # Ajouter la lettre aux lettres trouvées
                    ajoute_lettre_trouvees(lettre)
                    
                    # Si toutes les lettres ont été trouvées
                    if set(afficher_lettres_trouvees()) == set(mot_actuel()):
                        st.write("\nFélicitations ! Vous avez deviné le mot", mot_actuel(), "!")
                        break
                    else:
                        st.write("La lettre", lettre, "se trouve dans le mot.")
                else:
                    st.write("La lettre", lettre, "ne se trouve pas dans le mot.")
                    # Enlever une vie
                    changer_vie((vie_actuel()-1))

            else:
                # Si la proposition est un mot
                mot_propose = proposition.lower()
                # Si le mot proposé est le bon
                if mot_propose == mot_actuel():
                    st.write("\nFélicitations ! Vous avez deviné le mot", mot, "!")
                    break
                else:
                    st.write("Le mot", mot_propose, "n'est pas le bon.")
                    # Enlever une vie
                    changer_vie((vie_actuel()-1))
            # Réinitialiser la proposition
            proposition = ""

    # Si toutes les vies sont perdues
    if vie_actuel() == 0:
        st.write("\nDésolé, vous avez perdu... Le mot à deviner était :", mot)

    # Afficher les données JSON après le traitement du bouton
    with st.expander("apres le traitement du bouton"):
            st.json(get_json())

if __name__ == "__main__":
    # Exécuter la fonction principale
    main()