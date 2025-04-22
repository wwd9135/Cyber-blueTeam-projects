from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")

# Load and resize images
def load_image(path):
    img = Image.open(path)
    img = img.resize((300, 300), Image.LANCZOS)  # Resize to 300x300
    return ImageTk.PhotoImage(img)

# List of images
images = [
    load_image("img1.png"),
    load_image("img2.png"),
    load_image("img3.png")
]

# Initial image setup
img_index = 0
img_label = Label(root, image=images[img_index])
img_label.grid(row=0, column=0, columnspan=3)

# Navigation functions
def forward():
    global img_index, img_label
    if img_index < len(images) - 1:
        img_index += 1
        img_label.config(image=images[img_index])

def backward():
    global img_index, img_label
    if img_index > 0:
        img_index -= 1
        img_label.config(image=images[img_index])

# Buttons
back_btn = Button(root, text="<<", command=backward)
exit_btn = Button(root, text="Exit", command=root.quit)
forward_btn = Button(root, text=">>", command=forward)

back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)

root.mainloop()
