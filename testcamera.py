import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Initialiser la webcam
        self.cap = cv2.VideoCapture(0)

        # Créer un canevas pour afficher l'image
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Bouton pour fermer l'application
        self.quit_button = ttk.Button(window, text="Quitter", command=self.quit)
        self.quit_button.pack()

        # Mettre à jour l'image de la webcam
        self.update()

    def update(self):
        # Lire une image depuis la webcam
        ret, frame = self.cap.read()

        if ret:
            # Convertir l'image BGR en RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Détecter les visages dans l'image
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Dessiner un cercle rouge autour de chaque visage détecté
            for (x, y, w, h) in faces:
                cv2.circle(frame, (x + w // 2, y + h // 2), min(w, h) // 2, (0, 0, 255), 2)

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

# Créer une instance de la classe WebcamApp
root = tk.Tk()
app = WebcamApp(root, "Webcam App")
root.mainloop()
