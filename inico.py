import tkinter as tk
def validar(): 
    usuario = e_login.get()
    contra = e_pass.get()
    
    if usuario=="ususario" and contra=="1234":
        l_mensaje.configure(text="Bienvenido al programa")
    else:
        l_mensaje.configure(text="credenciales imcorrecta")


ventana = tk.Tk()
ventana.geometry("800x500")
ventana.title("mi primer ventana")
titulo = tk.Label(ventana, text="programa de gestion comercial")
titulo.place(x=100,y=50)
l_login = tk.Label(ventana, text="ususario: ")
l_login.place(x=50,y=100)
e_login = tk.Entry(width=15)
e_login.place(x=150,y=100)
l_pass = tk.Label(ventana, text="contraseña: ")
l_pass.place(x=50,y=130)
e_pass = tk.Entry(show="*",width=15)
e_pass.place(x=130,y=130)
b_ingresar = tk.Button(ventana,text="ingresar",command=validar)
b_ingresar.place(x=90,y=180)
l_mensaje = tk.Label(ventana,text="")
l_mensaje.place(x=50,y=210)

ventana.mainloop()