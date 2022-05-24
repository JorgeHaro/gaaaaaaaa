#Librerias externas
from PIL import ImageTk
import PIL.Image
from tkinter import CENTER, Frame,Label,Button, StringVar,Tk    
from tkinter import filedialog
from tkinter.messagebox import askquestion, showinfo
#Librerias propias
from pruebaReko import comparar_rostros

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

celeste =(31,149,242)
turqueza= (49,191,202)
humoOscuro=(100,100,100) #96,96,98
humoClaro=(220,220,220) #249,249,249
humoMedio=(180,180,180) #220,220,220
humoNegro=(75,75,77)
rojoPaino = (128, 0, 0)

class Rekognition():
    def __init__(self,window):
        self.window = window
        self.window.config(bg=_from_rgb((humoOscuro)))
        self.window.resizable(width=False, height=False)

        self.frame1 = Frame(self.window,bg=_from_rgb((rojoPaino)))
        self.frame1.place(x=0,y=0,width=700,height=48)
        self.label_Titulo = Label(self.frame1,text='RECONOCIMIENTO BIOMETRICO',fg="white",bg=_from_rgb((rojoPaino)),font=('@Yu Gothic UI Semibold', 15),justify='center')

        #LOGO PAINO
        self.imagen_label1 = PIL.Image.open('./Imagenes/logo.png')
        self.imagen_resize = self.imagen_label1.resize((110,35))
        self.imagen_label1 = ImageTk.PhotoImage(self.imagen_resize)
        self.LabelLogo = Label(self.frame1,image=self.imagen_label1, bg=_from_rgb((rojoPaino)))

        #LOGO AWS
        self.imagen_aws = PIL.Image.open('./Imagenes/aws.png')
        self.awsresize = self.imagen_aws.resize((40,20))
        self.imagen_aws = ImageTk.PhotoImage(self.awsresize)
        self.LabelAws = Label(self.window, image=self.imagen_aws, bg=_from_rgb((humoOscuro)))

        self.texto_fe = StringVar()
        self.texto_fe.set('')
        self.label_file_explorer = Label(self.window,
                            anchor = CENTER,
                            justify = CENTER,
                            textvariable=self.texto_fe,
                            font=('@Yu Gothic UI Semibold', 10),
                            width = 40, height = 2,
                            fg = "White",
                            bg=_from_rgb((humoOscuro)))
        self.texto_fe2 = StringVar()
        self.texto_fe2.set('')
        self.label_file_explorer2 = Label(self.window,
                            anchor = CENTER,
                            justify = CENTER,
                            textvariable=self.texto_fe2,
                            font=('@Yu Gothic UI Semibold', 10),
                            width = 40, height = 2,
                            fg = "White",
                            bg=_from_rgb((humoOscuro)))
        
        #Frames para colocar las imagenes
        self.marco_imagen1 = Frame(self.window, bg=_from_rgb(humoClaro), width=200, height=266)
        self.marco_imagen2 = Frame(self.window, bg=_from_rgb(humoClaro), width=200, height=266)

        #Botones para abrir el buscador de archivos
        self.button_explore = Button(self.window,
                        text = "ABRIR",
                        cursor = "hand2",
                        command = self.Imagen1,
                        bg=_from_rgb((humoClaro)),
                        fg="black",
                        relief="groove"
                        )

        self.button_explore2 = Button(self.window,
                                text = "ABRIR",
                                cursor = "hand2",
                                command = self.Imagen2,
                                bg=_from_rgb((humoClaro)),
                                fg="black",
                                relief="groove"
                                )

        self.button_comparar = Button(self.window,relief="flat",cursor = "hand2",command=self.Resultado_comparacion,bg=_from_rgb((rojoPaino)),fg='White',activeforeground="#000000", text='COMPARAR')
        
        self.texto_lr = StringVar()
        self.texto_lr.set('')
        self.LabelResultado = Label(self.window,textvariable=self.texto_lr,bg=_from_rgb((humoOscuro)),fg = "White",font=('@Yu Gothic UI Semibold', 12),justify='center')

        #Posiciones de los botones y labels
        self.label_Titulo.place(x=15,y=7,width=300,height=30)
        self.label_file_explorer.place(x=40,y=80)
        self.label_file_explorer2.place(x=340, y=80)
        self.LabelLogo.place(x=575, y=5)
        self.LabelAws.place(x=640, y=560)
        self.LabelResultado.place(x= 200, y=500,width=300,height=80)
        self.marco_imagen1.place(x=100,y=130)
        self.marco_imagen2.place(x=400,y=130)

        self.button_explore.place(x=160, y=245,width=80, height=30)
        self.button_explore2.place(x=460,y=245,width=80, height=30)
        self.button_comparar.place(x=310,y=450,width=80, height=30)

    #Abrir el explorador de ARCHIVOS para la Imagen 1
    def browseFiles(self):
        self.filename1 = filedialog.askopenfilename(initialdir = r"C:\Users\DELL\Desktop\Rekognition\Imagenes",
                                            title = "Select a File",
                                            filetypes = (("Images",
                                                            "*.jpg*"),
                                                            ("Images",
                                                            "*.png*"),
                                                        ("all files",
                                                            "*.*")))
    # Change label contents
        lista_path = self.filename1.split('/')
        longitud = len(lista_path)-1
        path_recortado = lista_path[longitud]
        self.texto_fe.set("Imagen: "+path_recortado)
        return self.filename1  

    #Abrir el explorador de ARCHIVOS para la Imagen 2
    def browseFiles2(self):
        self.filename2 = filedialog.askopenfilename(initialdir = r"C:\Users\DELL\Desktop\Rekognition\Imagenes",
                                            title = "Select a File",
                                            filetypes = (("Images",
                                                            "*.jpg*"),
                                                            ("Images",
                                                            "*.png*"),
                                                        ("all files",
                                                            "*.*")))

    #Change label contents
        lista_path = self.filename2.split('/')
        longitud = len(lista_path)-1
        path_recortado = lista_path[longitud]
        self.texto_fe2.set("Imagen: "+ path_recortado)
        return self.filename2

    def Imagen1(self):
        self.pathImagen1 = self.browseFiles()
        if self.pathImagen1 != '':
            img = PIL.Image.open(self.pathImagen1)
            new_img = img.resize((200,266))
            render = ImageTk.PhotoImage(new_img)
            self.img1 = Label(self.window,image=render)
            self.img1.image= render
            self.img1.place(x=100,y=130)
            self.boton_eliminar1 = Button(self.window, bg=_from_rgb(rojoPaino), relief="flat", 
            command=lambda: self.EliminarImagen1(),
            fg='White',activeforeground="#000000", text='X')
            self.boton_eliminar1.configure(font="Arial 10 bold",cursor = "hand2")
            self.boton_eliminar1.place(x=285,y=130, width=20, height=20)
        else:
            self.texto_fe.set('')
            showinfo("ERROR", 'No selecciono una Imagen')
            self.img1.configure(image='',bg=_from_rgb((humoOscuro)))

    def Imagen2(self):
        self.pathImagen2 = self.browseFiles2()
        if self.pathImagen2 != '':
            img = PIL.Image.open(self.pathImagen2)
            new_img = img.resize((200,266))
            render = ImageTk.PhotoImage(new_img)
            self.img2 = Label(self.window,image=render)
            self.img2.image= render
            self.img2.place(x=400,y=130)
            self.boton_eliminar2 = Button(self.window, bg=_from_rgb(rojoPaino), relief="flat", 
            command=lambda: self.EliminarImagen2(),
            fg='White',activeforeground="#000000", text='X')
            self.boton_eliminar2.configure(font="Arial 10 bold",cursor = "hand2")
            self.boton_eliminar2.place(x=585,y=130, width=20, height=20)
        else:
            self.texto_fe2.set('')
            showinfo("ERROR", 'No selecciono una Imagen')
            self.img2.configure(image='',bg=_from_rgb((humoOscuro)))
    
    def EliminarImagen1(self):
        resultado = askquestion("Eliminar","¿Está seguro que desea eliminar esta imagen?")
        if resultado == "yes":
            self.img1.destroy()
            del self.filename1
            self.boton_eliminar1.destroy()
            self.texto_fe.set('')
            self.texto_lr.set('')
    def EliminarImagen2(self):
        resultado = askquestion("Eliminar","¿Está seguro que desea eliminar esta imagen?")
        if resultado == "yes":
            self.img2.destroy()
            del self.filename2
            self.boton_eliminar2.destroy()
            self.texto_fe2.set('')
            self.texto_lr.set('')

    #Funcion que muestra el resultado de la comparacion de las caras
    def Resultado_comparacion(self):
        try:
            # self.LabelResultado.configure(text='')
            self.resultado = comparar_rostros(self.filename1,self.filename2)
            self.texto_lr.set(self.resultado)
            self.LabelResultado.configure(font=('@Yu Gothic UI Semibold', 16), justify=CENTER)
        except:
            showinfo("ERROR", 'Seleccione 2 IMAGENES')

def inicializar_ventana():
    window = Tk()
    window.title('File Explorer')
    window.geometry("700x600")
    Rekognition(window)
    window.mainloop()