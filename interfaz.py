#Librerias externas
from PIL import ImageTk
import PIL.Image
from tkinter import Frame,Label,Button,Tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
#Librerias propias
from pruebaReko import comparar_rostros

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

celeste =(31,149,242)
turqueza= (49,191,202)
humoOscuro=(100,100,100) #96,96,98
humoClaro=(249,249,249)
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
        self.label_Titulo = Label(self.frame1,text='COMPARACION CARAS',fg="white",bg=_from_rgb((rojoPaino)),font=('@Yu Gothic UI Semibold', 15),justify='center')

        #LOGO PAINO
        self.imagen_label1 = PIL.Image.open('./Imagenes/logo.png')
        self.imagen_resize = self.imagen_label1.resize((110,35))
        self.imagen_label2 = ImageTk.PhotoImage(self.imagen_resize)
        self.LabelLogo = Label(self.frame1,image=self.imagen_label2, bg=_from_rgb((rojoPaino)))

        #LOGO AWS
        self.imagen_aws = PIL.Image.open('./Imagenes/aws.png')
        self.awsresize = self.imagen_aws.resize((40,20))
        self.imagen_aws = ImageTk.PhotoImage(self.awsresize)
        self.LabelAws = Label(self.window, image=self.imagen_aws, bg=_from_rgb((humoOscuro)))

        self.label_file_explorer = Label(self.window,
                            text = "IMAGEN 1",
                            font=('@Yu Gothic UI Semibold', 10),
                            width = 40, height = 2,
                            fg = "White",
                            bg=_from_rgb((humoOscuro)))

        self.label_file_explorer2 = Label(self.window,
                            text = "IMAGEN 2",
                            font=('@Yu Gothic UI Semibold', 10),
                            width = 40, height = 2,
                            fg = "White",
                            bg=_from_rgb((humoOscuro)))
        
        #Frame para colocar las imagenes

        self.marco_imagen1 = Frame(self.window, bg=_from_rgb(humoClaro), width=200, height=266)
        self.marco_imagen2 = Frame(self.window, bg=_from_rgb(humoClaro), width=200, height=266)

        #Botones para abrir el buscador de archivos
        self.button_explore = Button(self.window,
                        text = "ABRIR",
                        command = self.Imagen1,
                        bg=_from_rgb((humoMedio)),
                        fg="black",
                        relief="flat"
                        )

        self.button_explore2 = Button(self.window,
                                text = "ABRIR",
                                command = self.Imagen2,
                                bg=_from_rgb((humoMedio)),
                                fg="black",
                                relief="flat"
                                )

        self.boton_eliminar1 = Button(self.window, bg=_from_rgb(rojoPaino), relief="flat", command=lambda: self.EliminarImagen1,fg='White',activeforeground="#000000", text='X')
        self.boton_eliminar2 = Button(self.window, bg=_from_rgb(rojoPaino), relief="flat", command=lambda: self.EliminarImagen2,fg='White',activeforeground="#000000", text='X')

        self.button_comparar = Button(self.window,relief="flat",command=self.Resultado_comparacion,bg=_from_rgb((rojoPaino)),fg='White',activeforeground="#000000", text='COMPARAR')   #relief="flat",command=self.Resultado_comparacion,bg=_from_rgb((rojoPaino)),fg='White',activeforeground="#000000",
        self.LabelResultado = Label(self.window, text='RESULTADO:',bg=_from_rgb((humoOscuro)),fg = "White",font=('@Yu Gothic UI Semibold', 12),justify='left')

        #Posiciones de los botones y labels
        self.label_Titulo.place(x=15,y=7,width=240,height=30)
        self.label_file_explorer.place(x=40,y=80)
        self.label_file_explorer2.place(x=340, y=80)
        self.LabelLogo.place(x=575, y=5)
        self.LabelAws.place(x=640, y=560)
        self.LabelResultado.place(x= 225, y=500,width=250,height=80)
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
        self.label_file_explorer.configure(text="Imagen: "+path_recortado, font=('@Yu Gothic UI Semibold', 10))
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
        self.label_file_explorer2.configure(text="Imagen: "+ path_recortado,font=('@Yu Gothic UI Semibold', 10))
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
            self.boton_eliminar1.place(x=80,y=80)
        else:
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
            self.boton_eliminar2.place(x=380,y=80)
        else:
            showinfo("ERROR", 'No selecciono una Imagen')
            self.img2.configure(image='',bg=_from_rgb((humoOscuro)))
    
    def EliminarImagen1(self):
        self.img1.destroy()
        #self.boton_eliminar1.pack_forget()
    def EliminarImagen2(self):
        self.img2.destroy()
        #self.boton_eliminar2.pack_forget()

    #Funcion que muestra el resultado de la comparacion de las caras
    def Resultado_comparacion(self):
        try:
            # self.LabelResultado.configure(text='')
            self.resultado = comparar_rostros(self.filename1,self.filename2)
            self.LabelResultado.configure(text= self.resultado,font=('@Yu Gothic UI Semibold', 16))
        except:
            showinfo("ERROR", 'Seleccione 2 IMAGENES')

def inicializar_ventana():
    window = Tk()
    window.title('File Explorer')
    window.geometry("700x600")
    Rekognition(window)
    # ConsultaVehicular(window,page,page1,page2,page3,monto,pathRegistro)
    window.mainloop()

# inicializar_ventana()