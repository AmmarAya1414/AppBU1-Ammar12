from tkinter import*
import main
def login():
    global logged_in_user_id, is_admin
    user_or_admin = user_or_admin_entry.get().lower()


    if user_or_admin == "u":
        user_login = user_login_entry.get()
        user_password = user_password_entry.get()

        if user_login and user_password:
            # Ajoutez votre logique de connexion pour l'utilisateur ici
            messagebox.showinfo("Connexion réussie", "Connecté en tant qu'utilisateur avec succès.")
            logged_in_user_id = "123"  # Remplacez par l'ID réel de l'utilisateur
            is_admin = False
        else:
            messagebox.showerror("Erreur", "Veuillez remplir votre login et votre mot de passe.")
    elif user_or_admin == "a":
        admin_login = admin_login_entry.get()
        admin_password = admin_password_entry.get()

        if admin_login and admin_password:
            # Ajoutez votre logique de connexion pour l'administrateur ici
            messagebox.showinfo("Connexion réussie", "Connecté en tant qu'administrateur avec succès.")
            logged_in_user_id = "__ID__ADMIN__"
            is_admin = True
        else:
            messagebox.showerror("Erreur", "Veuillez remplir votre login et votre mot de passe.")
    else:
        messagebox.showerror("Erreur", "Choix invalide. Veuillez sélectionner une option valide (U ou A).")

def display_user_menu():
    result_label.config(text="\nMenu utilisateur:\n1 - Afficher les livres\n2 - Emprunter un livre\n3 - Afficher les livres empruntés\n4 - Retourner un livre\n5 - Afficher les livres disponibles\n6 - Afficher les livres vous ayant empruntés\n0 - Se déconnecter")

def display_admin_menu():
    result_label.config(text="\nMenu administrateur:\n1 - Ajouter un utilisateur\n2 - Afficher les utilisateurs\n3 - Ajouter un livre\n4 - Afficher les livres\n5 - Emprunter un livre\n6 - Afficher les livres empruntés\n7 - Gérer les comptes utilisateurs\n8 - Gérer les emprunts de livres\n9 - Afficher les livres en retard\n10 - Marquer un livre comme rendu\n11 - Afficher les livres disponibles\n12 - Afficher les utilisateurs ayant empruntés un livre\n0 - Se déconnecter")

def display_menu():
    if is_admin:
        display_admin_menu()
    else:
        display_user_menu()

# Création de la fenêtre principale
APL = Tk()
APL.geometry("600x400+100+50")
APL.title('Bibliothèque UIR')

# Création des widgets
welcome_label = Label(APL, text='Bienvenue dans la bibliothèque UIR!', fg='black', bg='turquoise', font=('tajawal', 17, 'bold'))
welcome_label.pack(fill='x', pady=10)

user_or_admin_label = Label(APL, text='Voulez-vous vous connecter en tant qu\'utilisateur (U) ou administrateur (A)?',
                             font=('tajawal', 14), fg='turquoise', bg='black')
user_or_admin_label.pack(pady=10)



user_login_label = Label(APL, text="Login utilisateur:")
user_login_label.pack()
user_login_entry = Entry(APL)
user_login_entry.pack()

user_password_label = Label(APL, text="Mot de passe utilisateur:")
user_password_label.pack()
user_password_entry = Entry(APL, show="*")
user_password_entry.pack()

admin_login_label = Label(APL, text="Login administrateur:")
admin_login_label.pack()
admin_login_entry = Entry(APL)
admin_login_entry.pack()

admin_password_label = Label(APL, text="Mot de passe administrateur:")
admin_password_label.pack()
admin_password_entry = Entry(APL, show="*")
admin_password_entry.pack()

result_label = Label(APL, text="")
result_label.pack(pady=10)
login_button = Button(APL, text="Se connecter", command=login)
login_button.pack(pady=5)

# Affichage de la fenêtre principale
APL.mainloop()