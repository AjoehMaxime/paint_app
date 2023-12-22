import cv2
import numpy as np

# Variables globales
drawing = False
ix, iy = -1, -1

# Fonction de rappel pour les événements de la souris
def draw_on_white(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (ix, iy), (x, y), (0, 0, 0), 2)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Créer une image blanche
img = np.ones((512, 512, 3), np.uint8) * 255  # 255 représente la couleur blanche

# Nommer la fenêtre
cv2.namedWindow('Dessiner avec Fond Blanc')

# Lier la fonction de rappel de la souris à la fenêtre
cv2.setMouseCallback('Dessiner avec Fond Blanc', draw_on_white)

while True:
    cv2.imshow('Dessiner avec Fond Blanc', img)

    # Attendre que l'utilisateur appuie sur la touche 'Esc' pour quitter
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
