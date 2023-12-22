import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dessinateur interactif")

        self.color = "red"
        self.eraser_mode = False  # Mode gomme désactivé par défaut
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.color_button = tk.Button(self.root, text="Choisir Couleur", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.eraser_button = tk.Button(self.root, text="Gomme", command=self.toggle_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.root, text="Effacer Tout", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)

        if self.eraser_mode:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white", width=2)
        else:
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=2)

    def choose_color(self):
        chosen_color = colorchooser.askcolor(initialcolor=self.color)[1]
        if chosen_color:
            self.color = chosen_color

    def clear_canvas(self):
        self.canvas.delete("all")

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(text="Crayon")
        else:
            self.eraser_button.config(text="Gomme")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
