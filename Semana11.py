#Melvin Josue Perez Garcia 
#Jaime Arnoldo Rodriguez Meza

from tkinter import Label,Button,filedialog,Tk,messagebox
from PIL import Image,ImageTk,ImageFilter
ventana = Tk()
ventana.title("Visualizador de Imagenes")
ventana.geometry('500x500')
ventana.resizable(0,0)
label1 = Label(ventana,text="Imagen: ",bg = "yellow")
label1.place(x= 40,y=40, width=300,height=300)
etiqueta = Label ( ventana, text = " Carga Imagen Actividad Semana 11 " )
etiqueta.pack ( )

def cargarimagen():
    global archivo
    archivo = filedialog.askopenfilename()
    boton = Image.open(archivo)
    imagen2resiz = boton.resize((300,300),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagen2resiz)
    label1.configure(image=render2)
    label1.image = render2

def blanconegro():
    if archivo !="":
        imagen4 = Image.open(archivo)
        imagenbn = imagen4.convert("L")
        imagenbnresiz = imagenbn.resize((300,300),Image.Resampling.LANCZOS)
        render4 = ImageTk.PhotoImage(imagenbnresiz)
        label1.configure(image=render4)
        label1.image = render4
        imagenbn.save("blanconegro.jpg")
        messagebox.showinfo("Imagen","Tu imagen esta en blanco y negro")
    else:
        messagebox.showerror("Imagen","No has seleccionado niguna imagen")


def Resolucion():
    if archivo !="":
        imagen3 = Image.open(archivo)
        imagendes = imagen3.filter(ImageFilter.BLUR)
        imagenbnresiz = imagendes.resize((300,300),Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagenbnresiz)
        label1.configure(image=render3)
        label1.image = render3
        imagendes.save("Resolucion.jpg")
        messagebox.showinfo("Seleccion Imagen","Tu imagen se ha desenfoque")
    else:
        messagebox.showerror("Seleccion Imagen","No has seleccionado niguna imagen")

def contor(): 
    if archivo !="":
        imagen3 = Image.open(archivo)
        imagencon = imagen3.filter(ImageFilter.CONTOUR)
        imagenbnresiz = imagencon.resize((300,300),Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagenbnresiz)
        label1.configure(image=render3)
        label1.image = render3
        imagencon.save("contor.jpg")
        messagebox.showinfo("Seleccion Imagen","Tu imagen tiene el efecto de contorno")
    else:
        messagebox.showerror("Seleccion Imagen","No has seleccionado niguna imagen")

def resaltar():
    if archivo !="":
        imagen3 = Image.open(archivo)
        imagenresal = imagen3.filter(ImageFilter.EMBOSS)
        imagenbnresiz = imagenresal.resize((300,300),Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagenbnresiz)
        label1.configure(image=render3)
        label1.image = render3
        imagenresal.save("resaltar.jpg")
        messagebox.showinfo("Seleccion Imagen","Tu imagen se ha resaltado")
    else:
        messagebox.showerror("Seleccion Imagen","No has seleccionado niguna imagen")


boton = Button(ventana,text="Cargar Tu imagen",command= cargarimagen,bg="black",fg="white")
boton.place(x=345,y=180,width=150,height=40)
boton1 = Button(ventana,text="Blanco/Negro",command=blanconegro,bg="black",fg="white")
boton1.place(x= 45, y= 350,width=100, height=40)
boton2 = Button(ventana,text="Desenfocar",command=Resolucion,bg="black",fg="white")
boton2.place(x= 150, y= 350,width=100, height=40)
boton3 = Button(ventana,text="Contorno",command=contor,bg="black",fg="white")
boton3.place(x= 260, y= 350,width=100, height=40)
boton4 = Button(ventana,text="Resaltar",command=resaltar,bg="black",fg="white")
boton4.place(x= 370, y= 350,width=100, height=40)
ventana.mainloop()


