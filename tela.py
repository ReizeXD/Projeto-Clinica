import customtkinter 

import tkinter as tk
from tkinter import *
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image


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
        self.df_list=""
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.mostrar_fila()
        self.logo()
        self.areas()
        root.mainloop()
    def tela(self):
        self.root.title("Computer Med Center")
        self.root.configure(background="white")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
    def tela_proximo(self):
        self.tela_p=customtkinter.CTk()
        self.tela_p.title("eiii") 
        self.tela_p.configure(background="white")
        self.tela_p.geometry("450x300")
        self.tela_p.resizable(False,False)
        self.frames_da_tela2()
        self.widgets_frame5()
        self.tela_p.mainloop()
    def frames_da_tela(self):
        self.frame1=customtkinter.CTkFrame(self.root,bg_color=co11,fg_color=co11)
        self.frame1.place(relx=0, rely=0.15, relwidth=0.43, relheight=1)

        self.frame2=customtkinter.CTkFrame(self.root,bg_color=co11,fg_color=co11)
        self.frame2.place(relx=0.43, rely=0.15, relwidth=0.57, relheight=1)

        self.frame3=customtkinter.CTkFrame(self.root,bg_color=co15,fg_color=co15)
        self.frame3.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        self.frame4=customtkinter.CTkFrame(self.frame1,bg_color=co6,fg_color=co6)
        self.frame4.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.55)

        self.tree_frame = tk.Frame(self.frame4)
        self.tree_frame.pack(fill="both", expand=True)
    def frames_da_tela2(self):
        self.frame5=customtkinter.CTkFrame(self.tela_p,bg_color=co1,fg_color=co1)
        self.frame5.place(relx=0 ,rely=0, relwidth=1, relheight=1)
    def widgets_frame1(self):

        self.label2=customtkinter.CTkLabel(self.frame1,text="Consultar",font=('Castellar',35,'bold' ))
        self.label2.place(relx=0.18,rely=0.02),

        self.combobox_var = customtkinter.StringVar(value="Serviço")
        self.box=customtkinter.CTkComboBox(self.frame1,values=["Fisioterapia","Psicologo",'Oftalmologista','Cardiologista','Oncologista'],variable=self.combobox_var,command=self.atualizar)
        self.box.place(relx=0.1,rely=0.14)

        self.buttom2=customtkinter.CTkButton(self.frame1, width=120, text="Próximo",command=self.proximo,hover_color=co0)
        self.buttom2.place(relx=0.6,rely=0.14)

        self.label_linha=customtkinter.CTkLabel(self.frame1, text="h", width=1, height=350,bg_color=co0)
        self.label_linha.place(relx=0.99,rely=0.12)

    def widgets_frame2(self):
        self.label1=customtkinter.CTkLabel(self.frame2,text="Agendar",font=('Castellar',35,'bold' ))
        self.label1.place(relx=0.3,rely=0.02)
        
        self.entry1=customtkinter.CTkEntry(self.frame2,width=370,placeholder_text="Nome",placeholder_text_color=co0)
        self.entry1.place(relx=0.1,rely=0.14)

        self.entry2=customtkinter.CTkEntry(self.frame2,placeholder_text="CPF",placeholder_text_color=co0)
        self.entry2.place(relx=0.6,rely=0.24)

        self.entry3=customtkinter.CTkEntry(self.frame2,placeholder_text="RG",placeholder_text_color=co0)
        self.entry3.place(relx=0.1,rely=0.24)

        self.entry4=customtkinter.CTkEntry(self.frame2,width=370,placeholder_text="Endereço",placeholder_text_color=co0)
        self.entry4 .place(relx=0.1,rely=0.41)

        self.entry5=customtkinter.CTkEntry(self.frame2,placeholder_text="Celular",placeholder_text_color=co0)
        self.entry5.place(relx=0.1,rely=0.51)

        self.combobox_var2 = customtkinter.StringVar(value="Serviço")
        self.box2=customtkinter.CTkComboBox(self.frame2,values=["Fisioterapia","Psicologo",'Oftalmologista','Cardiologista','Oncologista'],variable=self.combobox_var2)
        self.box2.place(relx=0.6,rely=0.51)

        self.buttom=customtkinter.CTkButton(self.frame2,height=40,width=130, text="Agendar", command=self.agendar,hover_color=co0)
        self.buttom.place(relx=0.35,rely=0.67)

    def widgets_frame5(self):
        self.label3=customtkinter.CTkLabel(self.frame5,text=self.p_area,font=('Castellar',35,'bold','underline' ), text_color=co0)
        self.label3.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.label4=customtkinter.CTkLabel(self.frame5,text=self.proximo[0],font=('Castellar',20,'bold' ), wraplength=300, text_color=co7)
        self.label4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def mostrar_fila(self,null=0):
    # creating a treeview with dual scrollbars
        list_header = ["Pacientes","RG","CPF","Endereço","Número"]
        
        self.tree_pacientes = ttk.Treeview(self.frame4, selectmode="extended",columns=list_header, show="headings",height=18)
     
        # vertical scrollbar
        self.vsb = ttk.Scrollbar(self.frame4, orient="vertical", command=self.tree_pacientes.yview)   
        # horizontal scrollbar
        self.hsb = ttk.Scrollbar(self.frame4, orient="horizontal", command=self.tree_pacientes.xview)

        self.tree_pacientes.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.vsb.place(relx=0.95, rely=0, relheight=1)
        self.hsb.place(relx=0, rely=0.95, relwidth=0.95)
        self.tree_pacientes.configure(yscrollcommand= self.vsb.set, xscrollcommand=self.hsb.set)
        self.frame4.grid_rowconfigure(0, weight=1)
        self.frame4.grid_columnconfigure(0, weight=1)
        hd = ['nw', 'nw', 'nw', 'center', 'center']
        h = [250, 100, 150, 180, 109]
        n=0
        
        for col in list_header:
            self.tree_pacientes.heading(col, text=col.title(), anchor=NW)
            
            self.tree_pacientes.column(col, width=h[n],anchor=hd[n])

            n+=1 
        for item in self.df_list:
                self.tree_pacientes.insert('', 'end', values=item)
            
            
    def logo(self):
        self.app_logo=Image.open("imagem\cc.png")
        self.app_logo=self.app_logo.resize((72,72))
        self.app_logo=ImageTk.PhotoImage(self.app_logo)

        self.l_app_logo = Label(self.frame3,image=self.app_logo, text=" Computer Med Center", width=850, compound=LEFT, anchor=NW, font=('Castellar 30 bold'), bg=co0, fg=co15,)
        self.l_app_logo.place(x=10, y=0)

    def atualizar(self,null=0):
        self.p_area=self.box.get()
        if self.p_area=="Fisioterapia":
            self.df_list=self.Fisioterapia.imprimir()
        elif self.p_area=="Psicologo":
            self.df_list=self.Psicologo.imprimir()
        elif self.p_area=="Oftalmologista":
            self.df_list=self.Oftalmologista.imprimir()
        elif self.p_area=="Cardiologista":
            self.df_list=self.Cardiologista.imprimir()
        elif self.p_area=="Oncologista":
            self.df_list=self.Oncologista.imprimir()
        self.mostrar_fila()

    def areas(self):
        self.Fisioterapia=Fila()
        self.Psicologo=Fila()
        self.Oftalmologista=Fila()
        self.Cardiologista=Fila()
        self.Oncologista=Fila()
    def agendar(self):
        self.p_nome=self.entry1.get()
        self.p_RG=self.entry2.get()
        self.p_CPF=self.entry3.get()
        self.p_Endereco=self.entry4.get()
        self.p_Numero=self.entry5.get()
        self.p_area2=self.box2.get()
        teste=[self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero,self.p_area2]
        for item in teste:
            if item=="":
                CTkMessagebox(title='Erro', message='Preencha todos os campos',icon="cancel")
                return
        if self.p_area2=="Fisioterapia":
            self.Fisioterapia.inserir([self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero])
            self.df_list=self.Fisioterapia.imprimir()
        elif self.p_area2=="Psicologo":
            self.Psicologo.inserir([self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero])
            self.df_list=self.Psicologo.imprimir()
        elif self.p_area2=="Oftalmologista":
            self.Oftalmologista.inserir([self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero])
            self.df_list=self.Oftalmologista.imprimir()
        elif self.p_area2=="Cardiologista":
            self.Cardiologista.inserir([self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero])
            self.df_list=self.Cardiologista.imprimir()
        elif self.p_area2=="Oncologista":
            self.Oncologista.inserir([self.p_nome,self.p_RG,self.p_CPF,self.p_Endereco,self.p_Numero])
            self.df_list=self.Oncologista.imprimir()
        self.box.set(self.box2.get())
        self.mostrar_fila()
    def proximo(self):
        self.p_area=self.box.get()
        self.proximo=None
        if self.p_area=="Fisioterapia":
            self.proximo=self.Fisioterapia.deletar()
            self.df_list=self.Fisioterapia.imprimir()
        elif self.p_area=="Psicologo":
            self.proximo=self.Psicologo.deletar()
            self.df_list=self.Psicologo.imprimir()
        elif self.p_area=="Oftalmologista":
            self.proximo=self.Oftalmologista.deletar()
            self.df_list=self.Oftalmologista.imprimir()
        elif self.p_area=="Cardiologista":
            self.proximo=self.Cardiologista.deletar()
            self.df_list=self.Cardiologista.imprimir()
        elif self.p_area=="Oncologista":
            self.proximo=self.Oncologista.deletar()
            self.df_list=self.Oncologista.imprimir()
        self.atualizar()
        if self.proximo:
            self.tela_proximo()
    

sistema()