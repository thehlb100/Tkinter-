import tkinter as tk


#TheHlb100 Python Webpage
window = tk.Tk()
Frame_A = tk.Frame()
Frame_A.pack()
Título_1 = tk.Label(text = 'Bienvenido a la página de TheHlb100', width= 250, fg = 'White', bg = 'Black', master= Frame_A)
Introduccion = tk.Label(text = 'Esta página ha sido utlizada para aprender el funcionamiento de tkinter', master = Frame_A)
Título_1.pack()
Introduccion.pack()
Antes_Opiniones = tk.Label(text = 'Tus opiniones son:', fg = 'Red', background= 'White')
Opiniones1 = tk.Entry()
entry = tk.Label(text = '', fg = 'Red')
Opiniones1.pack()
Antes_Opiniones.pack()

def upd_edad(eve1):

 entry['text']= entry['text'] + eve1.char
Opiniones1.bind('<Key>', upd_edad)
entry.pack()
window.mainloop()