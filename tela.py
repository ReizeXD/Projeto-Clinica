import customtkinter 

import tkinter as tk
from tkinter import *
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import DateEntry

from fila import *


co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10= "#146C94"   # azul
co11="#36699B"
co12="#224160"
co14="#B97A5A"
co15="#1182AF"



root=customtkinter.CTk()
customtkinter.set_appearance_mode("Light")
class sistema():
    def __init__(self):
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.mostrar_fila()
        self.logo()
        self.agendar()
        root.mainloop()
    def tela(self):
        self.root.title("sistema")
        self.root.configure(background="white")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
    def frames_da_tela(self):
        self.frame1=customtkinter.CTkFrame(self.root,bg_color=co11,fg_color=co11)
        self.frame1.place(relx=0, rely=0.15, relwidth=0.43, relheight=1)

        self.frame2=customtkinter.CTkFrame(self.root,bg_color=co11,fg_color=co11)
        self.frame2.place(relx=0.43, rely=0.15, relwidth=0.57, relheight=1)

        self.frame3=customtkinter.CTkFrame(self.root,bg_color=co15,fg_color=co15)
        self.frame3.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        self.frame4=customtkinter.CTkFrame(self.frame1,bg_color=co6,fg_color=co6)
        self.frame4.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.55)
    def widgets_frame1(self):

        self.label2=customtkinter.CTkLabel(self.frame1,text="Consultar",font=('Castellar',35,'bold' ))
        self.label2.place(relx=0.18,rely=0.02)

        combobox_var = customtkinter.StringVar(value="Serviço")
        self.box=customtkinter.CTkComboBox(self.frame1,values=["1","2"],variable=combobox_var)
        self.box.place(relx=0.1,rely=0.14)

        self.buttom2=customtkinter.CTkButton(self.frame1, width=120, text="Próximo")
        self.buttom2.place(relx=0.6,rely=0.14)

    def widgets_frame2(self):
        self.label1=customtkinter.CTkLabel(self.frame2,text="Agendar",font=('Castellar',35,'bold' ))
        self.label1.place(relx=0.3,rely=0.02)
        
        self.entry1=customtkinter.CTkEntry(self.frame2,width=370,placeholder_text="Nome",placeholder_text_color=co0)
        self.entry1.place(relx=0.1,rely=0.12)

        self.entry2=customtkinter.CTkEntry(self.frame2,placeholder_text="CPF",placeholder_text_color=co0)
        self.entry2.place(relx=0.6,rely=0.22)

        self.entry3=customtkinter.CTkEntry(self.frame2,placeholder_text="RG",placeholder_text_color=co0)
        self.entry3.place(relx=0.1,rely=0.22)

        self.entry4=customtkinter.CTkEntry(self.frame2,width=370,placeholder_text="Endereço",placeholder_text_color=co0)
        self.entry4 .place(relx=0.1,rely=0.39)

        self.entry5=customtkinter.CTkEntry(self.frame2,placeholder_text="Celular",placeholder_text_color=co0)
        self.entry5.place(relx=0.1,rely=0.49)

        self.entry6=customtkinter.CTkEntry(self.frame2,placeholder_text="Email",placeholder_text_color=co0)
        self.entry6.place(relx=0.6,rely=0.49)

        self.buttom=customtkinter.CTkButton(self.frame2,height=40,width=130, text="Agendar", command=self.agendar())
        self.buttom.place(relx=0.35,rely=0.67)

    def mostrar_fila(self):
    # creating a treeview with dual scrollbars
        list_header = ["Pacientes"]

        self.tree_pacientes = ttk.Treeview(self.frame4, selectmode="extended",columns=list_header, show="headings",height=18)
     
        # vertical scrollbar
        vsb = ttk.Scrollbar(self.frame4, orient="vertical", command=self.tree_pacientes.yview)   
        # horizontal scrollbar
        hsb = ttk.Scrollbar(self.frame4, orient="horizontal", command=self.tree_pacientes.xview)
        vsb.place(relx=0.95, rely=0, relheight=1)
        hsb.place(relx=0, rely=0.95, relwidth=0.95)

        self.tree_pacientes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_pacientes.grid(column=1, row=1, sticky='nsew')
        self.frame4.grid_rowconfigure(0, weight=12)

        hd=["center"]
        h=[570]
        n=0

        for col in list_header:
            self.tree_pacientes.heading(col, text=col.title(), anchor=NW)
            
            self.tree_pacientes.column(col, width=h[n],anchor=hd[n])

            n+=1 
        """ 
        for item in df_list:
            self.tree_pacientes.insert('', 'end', values=item) 
            """
    def logo(self):
        self.app_logo=Image.open("imagem\ccc.png")
        self.app_logo=self.app_logo.resize((72,72))
        self.app_logo=ImageTk.PhotoImage(self.app_logo)

        self.l_app_logo = Label(self.frame3,image=self.app_logo, text=" Computer Med Center", width=850, compound=LEFT, anchor=NW, font=('Castellar 30 bold'), bg=co0, fg=co15,)
        self.l_app_logo.place(x=10, y=0)


    def agendar(self):
        self.p_nome=self.entry1.get()
        print(self.p_nome)

sistema()