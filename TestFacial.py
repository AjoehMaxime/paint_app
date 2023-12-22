import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pickle

# import matplotlib.pyplot as plt

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Initialiser la webcam
        self.cap = cv2.VideoCapture(0)

        # Créer un canevas pour afficher l'image
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Boutons avec des icônes
        # self.load_image_icon = Image.open("load.jpg")
        # self.load_image_icon = self.load_image_icon.resize((32, 32), Image.LANCZOS)
        # self.load_image_icon = ImageTk.PhotoImage(self.load_image_icon)
        # self.load_image_button = ttk.Button(window, text="Charger une image", image=self.load_image_icon, compound=tk.TOP, command=self.load_image)
        # self.load_image_button.pack()

        self.quit_icon = Image.open("quit.png")
        self.quit_icon = self.quit_icon.resize((32, 32), Image.LANCZOS)
        self.quit_icon = ImageTk.PhotoImage(self.quit_icon)
        self.quit_button = ttk.Button(window, text="Quitter", image=self.quit_icon, compound=tk.RIGHT, command=self.quit)
        self.quit_button.pack()

        # self.save_icon = Image.open("save.png")
        # self.save_icon = self.save_icon.resize((32, 32), Image.LANCZOS)
        # self.save_icon = ImageTk.PhotoImage(self.save_icon)
        # self.save_button = ttk.Button(window, text="Sauvegarder", image=self.save_icon, compound=tk.BOTTOM, command=self.save_state)
        # self.save_button.pack()

        # self.new_work_icon = Image.open("new.jpg")
        # self.new_work_icon = self.new_work_icon.resize((32, 32), Image.LANCZOS)
        # self.new_work_icon = ImageTk.PhotoImage(self.new_work_icon)
        # self.new_work_button = ttk.Button(window, text="Nouveau travail", image=self.new_work_icon, compound=tk.TOP, command=self.new_work)
        # self.new_work_button.pack()

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_image)
        menu_bar.add_cascade(label="detection", menu=file_menu)
        file_menu.add_command(label="filtre", command=self.update1)

        self.open_work_icon = Image.open("télécharger.jpg")
        self.open_work_icon = self.open_work_icon.resize((32, 32), Image.LANCZOS)
        self.open_work_icon = ImageTk.PhotoImage(self.open_work_icon)
        self.open_work_button = ttk.Button(window, text="Ouvrir travail", image=self.open_work_icon, compound=tk.LEFT, command=self.open_work)
        self.open_work_button.pack()

        # Image à superposer sur le nez
        self.overlay_image = None

        # Mettre à jour l'image de la webcam
        self.update()

        # Mettre à jour l'image de la webcam
        self.update1()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.overlay_image = cv2.imread(file_path)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            ret, frame = self.cap.read()
            while True:

                # Display the resulting frame
                # cv2.imshow('frame', frame)
                # self.cap.release()
                cv2.imwrite(file_path, self.cap)

    def new_work(self):
        # Créer un nouvel objet WebcamApp
        new_webcam_app = WebcamApp(self.window, "Nouveau travail")
        new_webcam_app.window.mainloop()

    def open_work(self):
        # Ouvrir un travail depuis un fichier
        file_path = filedialog.askopenfilename(filetypes=[("Pickled files", "*.pkl")])
        if file_path:
            with open(file_path, "rb") as file:
                saved_webcam_app = pickle.load(file)
                # Afficher l'interface utilisateur du travail sauvegardé
                saved_webcam_app.window.mainloop()

    def update(self):
        # Lire une image depuis la webcam
        ret, frame = self.cap.read()

        if ret:
            # Convertir l'image BGR en RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Détecter les visages dans l'image
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Appliquer un flou sur le fond de l'image
            # blurred = cv2.GaussianBlur(frame, (15, 15), 0)
            # frame = cv2.addWeighted(frame, 1.5, blurred, -0.5, 0)

            # Superposer l'image sur les yeux détectés
            if self.overlay_image is not None:
                for (x, y, w, h) in faces:
                    roi_gray = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
                    eyes = eyes_cascade.detectMultiScale(roi_gray)

                    for (ex, ey, ew, eh) in eyes:
                        # Redimensionner l'image à la taille des yeux
                        overlay_resized = cv2.resize(self.overlay_image, (ew, eh))

                        # Superposer l'image sur les yeux
                        for i in range(overlay_resized.shape[0]):
                            for j in range(overlay_resized.shape[1]):
                                if overlay_resized[i, j].any() > 0:  # Ignorer les pixels noirs
                                    rgb_image[y + ey + i, x + ex + j] = overlay_resized[i, j]

            # Convertir l'image en format compatible avec Tkinter
            img = Image.fromarray(rgb_image)
            imgtk = ImageTk.PhotoImage(image=img)

            # Mettre à jour le canevas avec la nouvelle image
            self.canvas.imgtk = imgtk
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        # Mettre à jour l'image après un certain délai (en millisecondes)
        self.window.after(10, self.update)

    def quit(self):
        # Libérer les ressources de la webcam
        self.cap.release()
        self.window.destroy()
    def update1(self):
        # Lire une image depuis la webcam
        ret, frame = self.cap.read()

        if ret:
            # Convertir l'image BGR en RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Détecter les visages dans l'image
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Superposer l'image chargée sur chaque visage détecté
            if self.overlay_image is not None:
                for (x, y, w, h) in faces:
                    # Redimensionner l'image à la taille du visage
                    overlay_resized = cv2.resize(self.overlay_image, (w, h))

                    # Superposer l'image sur le visage
                    for i in range(overlay_resized.shape[0]):
                        for j in range(overlay_resized.shape[1]):
                            if overlay_resized[i, j].any() > 0:  # Ignorer les pixels noirs
                                rgb_image[y + i, x + j] = overlay_resized[i, j]

            # Convertir l'image en format compatible avec Tkinter
            img = Image.fromarray(rgb_image)
            imgtk = ImageTk.PhotoImage(image=img)

            # Mettre à jour le canevas avec la nouvelle image
            self.canvas.imgtk = imgtk
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        # Mettre à jour l'image après un certain délai (en millisecondes)
        self.window.after(10, self.update)
# Créer une instance de la classe WebcamApp
root = tk.Tk()
app = WebcamApp(root, "Webcam App")
root.mainloop()
