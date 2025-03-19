# remove_background_gui.py

import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk
import io

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        global input_image
        input_image = Image.open(file_path)
        input_photo = ImageTk.PhotoImage(input_image)
        input_label.config(image=input_photo)
        input_label.image = input_photo

def remove_background():
    if 'input_image' in globals():
        output_image = remove(input_image)
        output_byte_array = io.BytesIO()
        output_image.save(output_byte_array, format="PNG")
        output_photo = ImageTk.PhotoImage(output_image)
        output_label.config(image=output_photo)
        output_label.image = output_photo
        # Sauvegarde de l'image modifiée
        output_image.save("output_image.png")
    else:
        print("Veuillez d'abord charger une image.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Suppression d'Arrière-Plan")

# Bouton pour choisir l'image
open_button = tk.Button(root, text="Ouvrir une Image", command=open_image)
open_button.pack()

# Affichage de l'image d'entrée
input_label = tk.Label(root)
input_label.pack()

# Bouton pour supprimer l'arrière-plan
remove_button = tk.Button(root, text="Supprimer l'Arrière-Plan", command=remove_background)
remove_button.pack()

# Affichage de l'image de sortie
output_label = tk.Label(root)
output_label.pack()

root.mainloop()
