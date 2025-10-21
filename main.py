from tkinter import SINGLE, Text, Tk, Label, Entry, Button, StringVar, Toplevel, messagebox

from user import User
from book import BOOKS_FILE_NAME, Book
from borrow import Borrow
import re
from tkinter import Tk, Label, Entry, Button, StringVar
import user_manage
from tkinter import *


window= Tk()

window = Canvas(window,width=450, height= 450)
window.pack()
image = PhotoImage(file='C:\\Users\\PCHPI5\\Desktop\\application biblio\\ab\python interface graphique\\logo.png')
window.create_image(0,0, anchor = NW , image = image)
class LibraryApp:
    def __init__(self):
        self.APPL = Tk()
        self.APPL.geometry("400x300")
        self.APPL.title("Bibliothèque UIR")

        self.logged_in_user_id = None
        self.is_admin = False
        self.ADMIN_PASSWORD = "admin"
        self.ADMIN_LOGIN = "admin"
        self.ADMIN = "__ID__ADMIN__"
        self.MAX_BOOKS_PER_STUDENT = 3

        self.user_login_var = StringVar()
        self.user_password_var = StringVar()

        Label(self.APPL, text="Bienvenue dans la bibliothèque UIR!",fg='white', bg='blue', font=('tajawal', 17, 'bold')).pack(pady=10)

        Label(self.APPL, text="Login:",fg='black', bg='cyan').pack()
        Entry(self.APPL, textvariable=self.user_login_var).pack(pady=5)

        Label(self.APPL, text="Mot de passe:",fg='black', bg='cyan').pack()
        Entry(self.APPL, textvariable=self.user_password_var, show="*").pack(pady=5)

        user_button = Button(self.APPL, text='Utilisateur (U)', command=self.connect_as_user,bg='lime')
        user_button.pack(pady=5)

        admin_button = Button(self.APPL, text='Administrateur (A)', command=self.connect_as_admin,bg='lime')
        admin_button.pack(pady=5)

        self.APPL.mainloop()
    #ayayayayay
    def connect_as_user(self):
        user_login = self.user_login_var.get()
        user_password = self.user_password_var.get()

        if user_login and user_password:
            if self.log_in(user_login, user_password) and not self.is_admin_login(user_login, user_password):
                messagebox.showinfo("Connexion", f"Connecté en tant qu'utilisateur avec succès. ID: {self.logged_in_user_id}")
                self.show_user_menu()
            else:
                messagebox.showerror("Erreur de connexion", "Login ou mot de passe incorrect.")
        else:
            messagebox.showwarning("Champ vide", "Veuillez remplir tous les champs.")

    def connect_as_admin(self):
        admin_login = self.user_login_var.get()
        admin_password = self.user_password_var.get()

        if admin_login == self.ADMIN_LOGIN and admin_password == self.ADMIN_PASSWORD:
            self.logged_in_user_id = self.ADMIN
            self.is_admin = True
            messagebox.showinfo("Connexion", "Connecté en tant qu'administrateur avec succès.")
            self.show_admin_menu()
        else:
            messagebox.showerror("Erreur de connexion", "Identifiant ou mot de passe administrateur incorrect.")

            #user menu
    def show_user_menu(self):
        user_menu_window = Toplevel(self.APPL)
        user_menu_window.title("Menu Utilisateur")
        user_menu_label = Label(user_menu_window, text="Bienvenue dans le menu utilisateur!")
        user_menu_label.pack()

        user_menu_button_1 = Button(user_menu_window, text="Afficher les livres disponible", command=self.handle_user_option_1)
        user_menu_button_1.pack()

        user_menu_button_2 = Button(user_menu_window, text="Emprunter un livre", command=self.handle_user_option_2)
        user_menu_button_2.pack()

        user_menu_button_3 = Button(user_menu_window, text="Retourner un livre", command=self.handle_user_option_3)
        user_menu_button_3.pack()

        user_menu_button_4 = Button(user_menu_window, text="Afficher les livres vous ayant empruntés", command=self.handle_user_option_4)
        user_menu_button_4.pack()

        user_menu_button_0 = Button(user_menu_window, text="Se déconnecter", command=self.handle_user_option_0)
        user_menu_button_0.pack()


          
         
       

    def handle_user_option_1(self):
       
        print("Option 2 du menu utilisateur")
    
    def handle_user_option_2(self):
     
        print("Option 3 du menu utilisateur")

    def handle_user_option_3(self):
       
        print("Option 3 du menu utilisateur")

    def handle_user_option_4(self):
      
        print("Option 4 du menu utilisateur")

    def handle_user_option_5(self):
       
        print("Option 5 du menu utilisateur")

    def handle_user_option_0(self):
       
        print("Option 0 du menu utilisateur")

     #admin menu
     


    def show_admin_menu(self):
        admin_menu_window = Toplevel(self.APPL)
        admin_menu_window.title("Menu Administrateur")
        admin_menu_label = Label(admin_menu_window, text="Bienvenue dans le menu administrateur!")
        admin_menu_label.pack()
        def open_add_user_window():
          add_user_window = Toplevel()  
          AddUserWindow(add_user_window)


        admin_menu_button_1 = Button(admin_menu_window, text="Ajouter un utilisateur", command=open_add_user_window)
        admin_menu_button_1.pack()


        admin_menu_button_2 = Button(admin_menu_window, text="Afficher les utilisateurs", command=self.handle_admin_option_2)
        admin_menu_button_2.pack()

        admin_menu_button_3 = Button(admin_menu_window, text="Ajouter un livre", command=self.handle_admin_option_3)
        admin_menu_button_3.pack()

        admin_menu_button_4 = Button(admin_menu_window, text="Afficher les livres", command=self.handle_admin_option_4)
        admin_menu_button_4.pack()

        admin_menu_button_5 = Button(admin_menu_window, text="Afficher les livres empruntés", command=self.handle_admin_option_5)
        admin_menu_button_5.pack()

        admin_menu_button_6 = Button(admin_menu_window, text="Gérer les comptes utilisateurs", command=self.handle_admin_option_6)
        admin_menu_button_6.pack()



        admin_menu_button_8 = Button(admin_menu_window, text="Afficher les livre disponibles", command=self.handle_admin_option_8)
        admin_menu_button_8.pack()



        admin_menu_button_0 = Button(admin_menu_window, text="Se déconnecter", command=lambda :self.handle_admin_option_0(admin_menu_window))
        admin_menu_button_0.pack()

      

   

        
       

    def open_add_user_window():
        AddUserWindow()
        print("utilisateur avec succés")
        messagebox.showinfo("-", " Utilisateur ajouté avec succes ")
    def handle_admin_option_2(self):
     DisplayUsersWindow()
    print("Option 2 du menu administrateur")

    def handle_admin_option_3(self):

     AddBookWindow()

    def handle_admin_option_4(self):
     DisplayBooksWindow()
    print("Option 4 du menu administrateur")

    def handle_admin_option_5(self):
       BorrowedBooksWindow()
    print("Option 5 du menu administrateur")

    def handle_admin_option_6(self):
      UserManageWindow()
    print("Option 6 du menu administrateur")


    def handle_admin_option_8(self):
        
   
        print("Option 8 du menu administrateur")




 
    def handle_admin_option_0(self,admin_menu_window):
        def log_out():
            global logged_in_user_id, is_admin
            logged_in_user_id = None
            is_admin = False
            admin_menu_window.destroy()

        log_out()
        print("Au revoir !")
        messagebox.showinfo("Aurevoir", " Merci d'avoir utiliser notre Application ")



    def log_in(self, login, password):
        users = User.get_users()
        for user in users:
            if user["login"] == login and user["password"] == password:
                self.logged_in_user_id = user["user_id"]
                self.is_admin = self.is_admin_login(login, password)
                return True
        return False

    def is_admin_login(self, login, password):
        return (login == self.ADMIN_LOGIN and password == self.ADMIN_PASSWORD)
from tkinter import Tk, Toplevel, Label, Listbox, Scrollbar, END, Button


class AddUserWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ajouter un utilisateur")

        self.user_id_var = StringVar()
        self.name_var = StringVar()
        self.nickname_var = StringVar()
        self.mail_var = StringVar()
        self.login_var = StringVar()
        self.password_var = StringVar()

        Label(master, text="ID utilisateur:").grid(row=0, column=0)
        Entry(master, textvariable=self.user_id_var).grid(row=0, column=1)

        Label(master, text="Nom:").grid(row=1, column=0)
        Entry(master, textvariable=self.name_var).grid(row=1, column=1)

        Label(master, text="Prénom:").grid(row=2, column=0)
        Entry(master, textvariable=self.nickname_var).grid(row=2, column=1)

        Label(master, text="Email:").grid(row=3, column=0)
        Entry(master, textvariable=self.mail_var).grid(row=3, column=1)

        Label(master, text="Login:").grid(row=4, column=0)
        Entry(master, textvariable=self.login_var).grid(row=4, column=1)

        Label(master, text="Mot de passe:").grid(row=5, column=0)
        Entry(master, textvariable=self.password_var, show="*").grid(row=5, column=1)

        Button(master, text="Ajouter utilisateur", command=self.add_user).grid(row=6, columnspan=2)

    def add_user(self):
        user_id = self.user_id_var.get()
        name = self.name_var.get()
        nickname = self.nickname_var.get()
        mail = self.mail_var.get()
        login = self.login_var.get()
        password = self.password_var.get()

        if user_id and name and nickname and mail and login and password:
           
            User(user_id, name, nickname, mail, login, password).create_user()
            print("Utilisateur ajouté avec succès.")
        else:
            print("Veuillez renseigner tous les champs.")
class DisplayUsersWindow:
    def __init__(self):
        self.user_window = Tk()
        self.user_window.title("Liste des Utilisateurs")

       
        self.user_listbox = Listbox(self.user_window, width=50, height=20)
        self.user_listbox.pack(padx=10, pady=10)

        scrollbar = Scrollbar(self.user_window, orient="vertical", command=self.user_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.user_listbox.config(yscrollcommand=scrollbar.set)

        
        self.display_users()

        
        close_button = Button(self.user_window, text="Fermer", command=self.user_window.destroy)
        close_button.pack(pady=10)

    def display_users(self):
        
        users = User.get_users()

       
        for user in users:
            user_info = f"ID: {user['user_id']}, Nom: {user['name']}, Prénom: {user['nickname']}"
            self.user_listbox.insert("end", user_info)


class DisplayBooksWindow:
    def __init__(self):
        self.books_window = Tk()
        self.books_window.title("Liste des Livres")

      
        self.books_listbox = Listbox(self.books_window, width=50, height=20)
        self.books_listbox.pack(padx=10, pady=10)

        scrollbar = Scrollbar(self.books_window, orient="vertical", command=self.books_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.books_listbox.config(yscrollcommand=scrollbar.set)

       
        self.display_books()

        
        close_button = Button(self.books_window, text="Fermer", command=self.books_window.destroy)
        close_button.pack(pady=10)

    def display_books(self):
      
        books = Book.get_books()

       
        for book in books:
            book_info = f"ID: {book['book_id']}, Titre: {book['title']}, Auteur: {book['author']}"
            self.books_listbox.insert("end", book_info)

class AddBookWindow:
    BOOKS_FILE_NAME = "books.txt"

    def __init__(self):
        self.add_book_window = Toplevel()
        self.add_book_window.title("Ajouter un livre")

        self.book_id_var = StringVar()
        self.title_var = StringVar()
        self.author_var = StringVar()
        self.editor_var = StringVar()
        self.isbn_var = StringVar()
        self.num_copies_var = StringVar()
        self.year_var = StringVar()

        Label(self.add_book_window, text="ID du livre:").grid(row=0, column=0)
        Entry(self.add_book_window, textvariable=self.book_id_var).grid(row=0, column=1)

        Label(self.add_book_window, text="Titre:").grid(row=1, column=0)
        Entry(self.add_book_window, textvariable=self.title_var).grid(row=1, column=1)

        Label(self.add_book_window, text="Auteur:").grid(row=2, column=0)
        Entry(self.add_book_window, textvariable=self.author_var).grid(row=2, column=1)

        Label(self.add_book_window, text="Éditeur:").grid(row=3, column=0)
        Entry(self.add_book_window, textvariable=self.editor_var).grid(row=3, column=1)

        Label(self.add_book_window, text="ISBN:").grid(row=4, column=0)
        Entry(self.add_book_window, textvariable=self.isbn_var).grid(row=4, column=1)

        Label(self.add_book_window, text="Nombre de copies:").grid(row=5, column=0)
        Entry(self.add_book_window, textvariable=self.num_copies_var).grid(row=5, column=1)

        Label(self.add_book_window, text="Année:").grid(row=6, column=0)
        Entry(self.add_book_window, textvariable=self.year_var).grid(row=6, column=1)

        Button(self.add_book_window, text="Ajouter livre", command=self.add_book).grid(row=7, columnspan=2)

    def add_book(self):
        book_id = self.book_id_var.get()
        title = self.title_var.get()
        author = self.author_var.get()
        editor = self.editor_var.get()
        isbn = self.isbn_var.get()
        num_copies = self.num_copies_var.get()
        year = self.year_var.get()

        if book_id and title and author and editor and isbn and num_copies and year:
           
            new_book_data = f"{book_id},{title},{author},{editor},{isbn},{num_copies},{year}\n"

            
            with open(self.BOOKS_FILE_NAME, "a") as file:
                file.write(new_book_data)

            print(f"Livre ajouté avec succès. ID du livre: {book_id}, Titre: {title}, Auteur: {author}")
            self.add_book_window.destroy()  
        else:
            print("Veuillez remplir tous les champs.")

class BorrowedBooksWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Livres empruntés")

       
        self.borrowed_books_text = Text(self.window, wrap="word", width=80, height=20)
        self.borrowed_books_text.pack()

       
        refresh_button = Button(self.window, text="Actualiser", command=self.refresh_borrowed_books)
        refresh_button.pack()

        self.refresh_borrowed_books()

    def refresh_borrowed_books(self):
        
        self.borrowed_books_text.delete(1.0, END)

       
        borrowed_books = self.read_borrowed_books_from_file()

       
        for entry in borrowed_books:
            user_id = entry["user_id"]
            book_id = entry["book_id"]
            due_date = entry["due_date"]

            user = User.get_user(user_id)
            book = Book.get_book_by_id(book_id)

            if user and book:
                book_info = f"{user['name']} {user['nickname']} - Livre : {book['title']} - Date de retour : {due_date}\n"
                self.borrowed_books_text.insert(END, book_info)
            else:
                print("Données utilisateur ou livre manquantes.")

    def read_borrowed_books_from_file(self):
        try:
            with open("borrowed_books.txt", "r") as file:
                content = []
                for line in file:
                    values = line.strip().split(",")
                    if len(values) == 3:
                        user_id, book_id, due_date = values
                        content.append({"user_id": user_id, "book_id": book_id, "due_date": due_date})

                return content
        except FileNotFoundError:
            messagebox.showinfo("Erreur", "Fichier borrowed_books.txt introuvable.")
            return []

    def run(self):
        self.window.mainloop()











# Lancement de l'application



app = LibraryApp()
addUserWindow = AddUserWindow()
display_users_window = DisplayUsersWindow()
display_users_window.user_window.mainloop()
display_books_window = DisplayBooksWindow(Tk())
root = Tk()
add_book_window = AddBookWindow(root)
root.mainloop()
borrowed_books_window = BorrowedBooksWindow()
borrowed_books_window.run()
window.mainloop()



