import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

ejercicios = {
    "pecho": [
        {
            "nombre": "Press de banca",
            "descripcion": "Acostado en un banco, empuja una barra con peso desde el pecho hacia arriba.",
            "series": 4,
            "repeticiones": 12,
            "video": "https://www.youtube.com/watch?v=GeLq8cMODLc",
            "imagen": "https://i.blogs.es/fb8403/pexels-frame-kings-812746/1366_2000.webp"
        },
        {
            "nombre": "Aperturas con mancuernas",
            "descripcion": "Acostado en un banco plano, abre los brazos sosteniendo mancuernas y luego junta sobre el pecho.",
            "series": 3,
            "repeticiones": 10,
            "video": "https://www.youtube.com/watch?v=xyHdY99F640",
            "imagen": "https://www.hsnstore.com/blog/wp-content/uploads/2011/01/aperturas-fit-ball.gif"
        },
    ],
    "piernas": [
        {
            "nombre": "Sentadilla",
            "descripcion": "Mantén la espalda recta y flexiona las rodillas bajando el cuerpo como si te fueras a sentar.",
            "series": 4,
            "repeticiones": 15,
            "video": "https://www.youtube.com/watch?v=80dKqPruEMo",
            "imagen": "https://static.wixstatic.com/media/c94d75_5da40ebd254249df861fb7cd7070fbcb~mv2.gif"
        },
        {
            "nombre": "Zancadas",
            "descripcion": "Da un paso hacia adelante y baja la rodilla de la pierna trasera hasta casi tocar el suelo.",
            "series": 3,
            "repeticiones": 12,
            "video": "https://www.youtube.com/watch?v=Xcfs_3DMKlc",
            "imagen": "https://deporteshalcon.net/blog/wp-content/uploads/2022/02/2-Zancada-avanzando-CANVA.gif"
        },
    ],
    "espalda": [
        {
            "nombre": "Dominadas",
            "descripcion": "Sujeta la barra con las manos y levanta tu cuerpo hasta que la barbilla sobrepase la barra.",
            "series": 4,
            "repeticiones": 8,
            "video": "https://www.youtube.com/watch?v=8mhDd9Ahl1M",
            "imagen": "https://cdn.shopify.com/s/files/1/0568/6280/2107/files/traction-pronation_480x480.gif?v=1698642250"
        },
        {
            "nombre": "Remo con barra",
            "descripcion": "Con los pies al ancho de los hombros, inclina el torso hacia adelante y rema la barra hacia el abdomen.",
            "series": 4,
            "repeticiones": 10,
            "video": "https://www.youtube.com/watch?v=TVFeA5HKy4k",
            "imagen": "https://www.entrenador.fit/wp-content/uploads/Remo-con-barra-invertido.gif"
        },
    ],
    "hombros": [
        {
            "nombre": "Press militar",
            "descripcion": "De pie, empuja la barra hacia arriba desde la altura de los hombros.",
            "series": 4,
            "repeticiones": 10,
            "video": "https://www.youtube.com/watch?v=O4yTrz6qfaA",
            "imagen": "https://static.wixstatic.com/media/c94d75_b80347cc587f435cb33cdf5502e7e6db~mv2.gif"
        },
        {
            "nombre": "Elevaciones laterales",
            "descripcion": "De pie, eleva las mancuernas hacia los lados hasta que los brazos estén paralelos al suelo.",
            "series": 3,
            "repeticiones": 12,
            "video": "https://www.youtube.com/watch?v=hgLpdwMtEEs",
            "imagen": "https://static.wixstatic.com/media/c94d75_86585c1261ef4d0aaa235280b21a560d~mv2.gif"
        },
    ],
    "abdominales": [
        {
            "nombre": "Crunch abdominal",
            "descripcion": "Acostado boca arriba, eleva el torso hacia las rodillas.",
            "series": 4,
            "repeticiones": 15,
            "video": "https://www.youtube.com/watch?v=JWUyng_c-G0",
            "imagen": "https://www.icegif.com/wp-content/uploads/2022/07/icegif-470.gif"
        },
        {
            "nombre": "Elevación de piernas",
            "descripcion": "Acostado boca arriba, eleva las piernas manteniéndolas rectas.",
            "series": 3,
            "repeticiones": 12,
            "video": "https://www.youtube.com/watch?v=oxJj5FoBycQ",
            "imagen": "https://www.hsnstore.com/blog/wp-content/uploads/2021/03/elevacion-piernas-suelo.gif"
        },
    ]
}

class BodyBuilderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plataforma BodyBuilder")
        self.geometry("800x600")

        self.estilo_widgets()
        self.mostrar_portada()
        self.ejercicio_actual = None  
        self.contador_repeticiones = 0  

    def estilo_widgets(self):
        style = ttk.Style(self)
        self.configure(bg="#f0f0f0")
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 12), padding=10, background="#4CAF50", foreground="white", borderwidth=2)
        style.configure('TLabel', background="#f0f0f0", font=('Arial', 14))

    def mostrar_portada(self):
        self.clear_window()
        self.cargar_imagen("https://www.mikencube.co.uk/wp-content/uploads/2021/12/google-ads-for-gyms.jpg")

        self.btn_inicio = ttk.Button(self, text="Comenzar", command=self.mostrar_menu_principal)
        self.btn_inicio.place(relx=0.5, rely=0.8, anchor='center')

    def cargar_imagen(self, url):
        try:
            response = requests.get(url)
            image_data = Image.open(BytesIO(response.content))
            image_data = image_data.resize((800, 600), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(image_data)

            self.panel = ttk.Label(self, image=self.img)
            self.panel.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def mostrar_menu_principal(self):
        self.clear_window()
        self.cargar_imagen("https://www.mikencube.co.uk/wp-content/uploads/2021/12/google-ads-for-gyms.jpg")

        self.label = ttk.Label(self, text="Seleccione la parte del cuerpo a entrenar:")
        self.label.place(relx=0.5, rely=0.1, anchor='center')

        for index, parte in enumerate(ejercicios.keys()):
            btn_ejercicio = ttk.Button(self, text=parte.capitalize(), command=lambda p=parte: self.mostrar_ejercicios(p))
            btn_ejercicio.place(relx=0.5, rely=0.2 + index * 0.1, anchor='center')

        self.btn_salir = ttk.Button(self, text="Salir", command=self.salir)
        self.btn_salir.place(relx=0.5, rely=0.8, anchor='center')

    def mostrar_ejercicios(self, parte_cuerpo):
        self.clear_window()
        self.ejercicio_actual = parte_cuerpo  
        self.cargar_imagen("https://www.mikencube.co.uk/wp-content/uploads/2021/12/google-ads-for-gyms.jpg")

        self.label = ttk.Label(self, text=f"Ejercicios para {parte_cuerpo.capitalize()}:")
        self.label.place(relx=0.5, rely=0.1, anchor='center')

        for index, ejercicio in enumerate(ejercicios[parte_cuerpo]):
            btn_ejercicio = ttk.Button(self, text=ejercicio['nombre'], command=lambda e=ejercicio: self.iniciar_ejercicio(e))
            btn_ejercicio.place(relx=0.5, rely=0.2 + index * 0.1, anchor='center')

        self.btn_regresar = ttk.Button(self, text="Volver", command=self.mostrar_menu_principal)
        self.btn_regresar.place(relx=0.5, rely=0.8, anchor='center')

    def iniciar_ejercicio(self, ejercicio):
        self.clear_window()
        self.cargar_imagen(ejercicio['imagen'])

        self.label_nombre = ttk.Label(self, text=ejercicio['nombre'])
        self.label_nombre.place(relx=0.5, rely=0.1, anchor='center')

        self.label_descripcion = ttk.Label(self, text=ejercicio['descripcion'])
        self.label_descripcion.place(relx=0.5, rely=0.2, anchor='center')

        self.label_series_reps = ttk.Label(self, text=f"Series: {ejercicio['series']}, Repeticiones: {ejercicio['repeticiones']}")
        self.label_series_reps.place(relx=0.5, rely=0.3, anchor='center')

        self.btn_video = ttk.Button(self, text="Ver Video", command=lambda: webbrowser.open(ejercicio['video']))
        self.btn_video.place(relx=0.5, rely=0.4, anchor='center')

        self.btn_regresar = ttk.Button(self, text="Volver", command=self.mostrar_ejercicios_regresar)
        self.btn_regresar.place(relx=0.5, rely=0.5, anchor='center')

        self.cronometro = ttk.Label(self, text="¡Listo para comenzar!")
        self.cronometro.place(relx=0.5, rely=0.6, anchor='center')

        self.btn_iniciar_cronometro = ttk.Button(self, text="Iniciar Cronómetro", command=lambda: self.iniciar_cronometro(30))
        self.btn_iniciar_cronometro.place(relx=0.35, rely=0.7, anchor='center')

        self.btn_reiniciar = ttk.Button(self, text="Reiniciar Cronómetro", command=lambda: self.reiniciar_cronometro(30))
        self.btn_reiniciar.place(relx=0.5, rely=0.7, anchor='center')

        self.btn_detener = ttk.Button(self, text="Detener Cronómetro", command=self.detener_cronometro)
        self.btn_detener.place(relx=0.65, rely=0.7, anchor='center')

        self.btn_contar_repeticiones = ttk.Button(self, text="Contar Repeticiones", command=self.contar_repeticiones)
        self.btn_contar_repeticiones.place(relx=0.5, rely=0.8, anchor='center')

        self.label_repeticiones = ttk.Label(self, text=f"Repeticiones: {self.contador_repeticiones}")
        self.label_repeticiones.place(relx=0.5, rely=0.9, anchor='center')

    def iniciar_cronometro(self, segundos):
        self.tiempo_restante = segundos
        self.actualizar_cronometro()

    def reiniciar_cronometro(self, segundos):
        if hasattr(self, 'after_id'):
            self.after_cancel(self.after_id)
        self.iniciar_cronometro(segundos)

    def detener_cronometro(self):
        if hasattr(self, 'after_id'):
            self.after_cancel(self.after_id)
        self.cronometro.config(text="¡Cronómetro detenido!")

    def contar_repeticiones(self):
        self.contador_repeticiones += 1
        self.label_repeticiones.config(text=f"Repeticiones: {self.contador_repeticiones}")

    def actualizar_cronometro(self):
        if self.tiempo_restante > 0:
            self.cronometro.config(text=f"Tiempo restante: {self.tiempo_restante} segundos")
            self.tiempo_restante -= 1
            self.after_id = self.after(1000, self.actualizar_cronometro)
        else:
            self.cronometro.config(text="¡Tiempo terminado!")

    def mostrar_ejercicios_regresar(self):
        if self.ejercicio_actual:
            self.mostrar_ejercicios(self.ejercicio_actual)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def salir(self):
        self.quit()

if __name__ == "__main__":
    app = BodyBuilderApp()
    app.mainloop()
