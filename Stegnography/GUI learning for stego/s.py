from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.txtInput = None
        self.imgInput = None
        self.entryImg = None
        self.entryTxt = None
        root.title("Stego - Steganography Toolkit")
        root.iconbitmap(r'C:\Users\theri\downloads\ad84ddbf-6877-4b88-82ab-3357ace4f595.ico') 

        # Create styled frame
        s = ttk.Style()
        s.configure('Danger.TFrame', background='#4F4F4F', borderwidth=5, relief='raised')

        danger_frame = LabelFrame(root, fg="black", bg="#4F4F4F")
        danger_frame.grid(columnspan=8, rowspan=9, column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

        # Title and Icon
        ttk.Label(danger_frame, text='Stego Ver 2.1.1').grid(column=0, row=0)
        raw_img = Image.open("ad84ddbf-6877-4b88-82ab-3357ace4f595.png")
        resized_img = raw_img.resize((30, 30))
        image = ImageTk.PhotoImage(resized_img)
        img_label = Label(danger_frame, image=image, background='#333333')
        img_label.image = image  # Keep a reference
        img_label.grid(column=7, row=0, padx=5, pady=5, sticky=E)

                # Label for text input
        ttk.Label(danger_frame, text='Enter hidden message text', width=35).grid(column=1, row=1,pady=2)
        self.entryImg = ttk.Entry(danger_frame,width=35)
        self.entryImg.grid(column=1, row= 2,pady=2)
        # Label for image path input
        ttk.Label(danger_frame, text='Enter exact path to img youd like to store text in', width=35).grid(column=1, row=5, pady=2, sticky= S)

        # Entry box
        self.entryTxt = ttk.Entry(danger_frame, width=35)
        self.entryTxt.grid(column=1, row=6,  padx=5, pady=2)

        # Img name entry box
        ttk.Label(danger_frame,text="Enter a name for your outputted image", width= 35).grid(column=1, row=8, pady=2)
        self.entryOutputImgName =  ttk.Entry(danger_frame,width=35)
        self.entryOutputImgName.grid(column=1, row=9, padx=5, pady=2)


        # Button
        tk.Button(danger_frame, text= "Load Txt file" , command= self.get_txt, width=30). grid(column=1, row=3, pady=2)
        tk.Button(danger_frame, text="Load Img File", command=self.get_img, width=30).grid(column=1, row=7, pady=2)


        

    def get_img(self):
        pass
    def get_txt(self):
        input_path = self.entry.get()
        print(input_path)
        try:
            if input_path.endswith(".txt"):
                with open(input_path, "r") as file:
                    self.txtInput = file.read()
                print("Text file loaded:\n", self.txtInput)

            elif input_path.endswith(".png"):
                with open(input_path, "rb") as file:
                    self.imgInput = file.read()
                print("Image file loaded (in bytes)")

            else:
                print("Unsupported file type.")
        except Exception as e:
            print("Error loading file:", e)

# Launch the GUI
root = Tk()
app = MyApp(root)
root.mainloop()
