from tkinter import *
from tkinter import ttk
from time import sleep
import threading
import subprocess
from tkinter import messagebox as mb
import os, sys
import webbrowser
from tkinter import font
import sys



serials = {
"Windows 10 Home":"TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
"Windows 10 Home N":"3KHY7-WNT83-DGQKR-F7HPR-844BM",
"Windows 10 Home Single Language":"7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
"Windows 10 Home Country Specific":"PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
"Windows 10 Professional":"W269N-WFGWX-YVC9B-4J6C9-T83GX",
"Windows 10 Professional N":"MH37W-N47XK-V7XM9-C7227-GCQG9",
"Windows 10 Enterprise":"NPPR9-FWDCX-D2C8J-H872K-2YT43",
"Windows 10 Enterprise N":"DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
"Windows Education":"NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
"Windows Education N":"2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
"Windows Enterprise 2015 LTSB":"M7XTQ-FN8P6-TTKYV-9D4CC-J462D",
}


kms_servers = {
"kms.digiboy.ir",
"kms8.msguides.com", 
"kms.loli.beer", 
"kms.cangshui.net", 
"kms.kirito.best", 
"kms.chinancce.com"}


current_kms_server = "kms.digiboy.ir"

class main_window:

	def __init__(self):
		root = Tk()
		root.title("Python Win10 Activador")
		icon = PhotoImage(file="resources/winactivador.png")
		root.iconphoto(True, icon)
		root.resizable(0,0)

		font_buttons = font.Font(family="Corbel")

		#VERSION SELECTION
		version_label = Label(root, text="Seleciona tu version de Windows:", font=font_buttons)
		version_label.grid(row=0, column=0, columnspan=2,pady=10)
		combo_list_version = ttk.Combobox(root, state="readonly",width=35,values=list(serials))
		combo_list_version.grid(row=1, column=0, columnspan=2)


		#STATE LABEL
		self.stateSV = StringVar()
		self.stateSV.set("Bienvenido")
		label_state = Label(root, textvariable=self.stateSV, fg="white", bg="green", width=35,font=font_buttons)
		label_state.grid(row=2, column=0, columnspan=2, pady=10)
		
		#BUTTONS - WINDOWS 
		button_activate = Button(root,font=font_buttons, text="Activar Windows", width=20, height=8, bg="#7CBB00", fg="white", command=lambda:self.activate_windows(combo_list_version.get()))
		button_activate.grid(row=3, column=1, padx=5, pady=5)

		button_gen_serial = Button(root,font=font_buttons, text="Generar Serial", width=20,height=8, bg="#00A1F1", fg="white", command=lambda:self.gen_serial(combo_list_version.get(), serials))
		button_gen_serial.grid(row=4, column=0, padx=5, pady=5)

		button_clean = Button(root,font=font_buttons, text="Elegir servidor", width=20, height=8,bg="#EA4335", fg="white", command=self.choice_server)
		button_clean.grid(row=3, column=0, padx=5, pady=5)

		button_creator = Button(root, font=font_buttons,text="Github", width=20, height=8,bg="#FFBB00", fg="black", command=lambda:webbrowser.open("https://www.instagram.com/arobin404/"))
		button_creator.grid(row=4, column=1, padx=5, pady=5)
		self.current_server_label = Label(root, font=font_buttons,text=f"Servidor seleccionado > > > {current_kms_server}", bg="blue",width=35,fg="white")
		self.current_server_label.grid(row=5, column=0,padx=5,pady=10,columnspan=2)

		root.mainloop()





	def cmd(self,command):
		subprocess.run(command, shell=True)



	def detele_windows_license(self):

		def delete():
			self.stateSV.set("Eliminando licencias anteriores...")
			self.cmd('slmgr.vbs -upk')
			self.stateSV.set("Bienvenido")

		cmd_thread = threading.Thread(target=delete)
		cmd_thread.start()



	def background_error(self, message):
		threading.Thread(target=mb.showerror(message=message))






	def activate_windows(self, version):

		def activate(version):		
			serial = serials[version]

			self.stateSV.set("Instalando Licencia...")

			sleep(10)
			try:
				self.cmd(f"slmgr /ipk {serial}")
				self.stateSV.set("Conectando a host KMS...")
				self.cmd("slmgr /skms kms.digiboy.ir")
				self.stateSV.set("Activando Windows...")
				self.cmd("slmgr /ato")
				self.stateSV.set("Windows ha sido activado con éxito")

			except:
				self.background_error("Ha ocurrido un error al activar Windows, asegurate de elegir correctamente tu versión de tu Windows.")


		if version != "":

			cmd_thread = threading.Thread(target=lambda:activate(version))
			cmd_thread.start()

		else:
			mb.showinfo(message="Debes seleccionar tu versión de windows para poder realizar la activación.")






	def choice_server(self):
		root=Toplevel()
		root.title("Cambiar servidor")
		root.resizable(0,0)

		selected_input = StringVar()
		selected_input.set("Manual")

		def select_recommended():

			combo_list_server.config(state="readonly")
			entry_manual_input.config(state="disabled")

		def select_manual_input():
			combo_list_server.config(state="disabled")
			entry_manual_input.config(state="normal")


		def select_input():
			if selected_input.get() == "Manual":
				current_kms_server = entry_manual_input.get()
				self.current_server_label.config(text=f"Servidor seleccionado > > > {current_kms_server}")
				root.destroy()

			if selected_input.get() == "Recommended":
				current_kms_server = combo_list_server.get()
				self.current_server_label.config(text=f"Servidor seleccionado > > > {current_kms_server}")
				root.destroy()


		# Radiobuttons
		Radiobutton(root, text="Recommended", variable=selected_input, value="Recommended", command=select_recommended).grid(row=0, column=0,pady=10,padx=5)
		Radiobutton(root, text="Manual", variable=selected_input, value="Manual", command=select_manual_input).grid(row=1, column=0, pady=10,padx=5)

		combo_list_server = ttk.Combobox(root,width=32,values=list(kms_servers),state="disabled")
		combo_list_server.grid(row=0, column=1, padx=10)

		entry_manual_input = Entry(root,width=35)
		entry_manual_input.grid(row=1, column=1,padx=10)

		select_button = Button(root, text="Aceptar", width=20, command=select_input)
		select_button.grid(row=2, columnspan=2,pady=15)

		root.mainloop()





	def gen_serial(self,version,serials):

		if version != "":
			root = Toplevel()
			root.title("Python Win10 Activador")
			root.resizable(0,0)

			label_version = Label(root, text=f"Serial válido para: {version}")
			label_version.grid(row=0, column=0, pady=10)

			entry_serialSV = StringVar()
			entry_serialSV.set(serials[version])
			entry_serial = Entry(root, textvariable=entry_serialSV, width=35)
			entry_serial.grid(row=1, column=0, pady=10, padx=25)

			button_accept = Button(root, text="Aceptar", command=lambda:root.destroy(), width=15, bg="#00A1F1", fg="white")
			button_accept.grid(row=2, column=0, pady=10)

			root.mainloop()

		else:
			mb.showinfo(message="Debes seleccionar una versión de Windows para generar el serial.")





window = main_window()