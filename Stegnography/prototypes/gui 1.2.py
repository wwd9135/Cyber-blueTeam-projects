from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.txtInput = None
        self.imgInput = None
        self.entryImg = None
        self.entryTxt = None

    def bulk(self):
        self.root.title("Stego - Steganography Toolkit")
        self.root.iconbitmap(r'C:\Users\student\downloads\ad84ddbf-6877-4b88-82ab-3357ace4f595.ico') 
        self.root.configure(bg="#2B2B2B")

        danger_frame = LabelFrame(root, fg="#DADADA", bg="#2B2B2B", bd=2)
        danger_frame.grid(columnspan=8, rowspan=9, column=1, row=2, sticky=(N, W, E, S), padx=10, pady=10)

        # Title and Icon
        tk.Label(danger_frame, text='Stego Ver 2.1.1', bg="#2B2B2B", fg="#DADADA", font=("Segoe UI", 12, "bold")).grid(column=1, row=0)
        raw_img = Image.open("ad84ddbf-6877-4b88-82ab-3357ace4f595.png")
        resized_img = raw_img.resize((30, 30))
        image = ImageTk.PhotoImage(resized_img)
        img_label = Label(danger_frame, image=image, bg='#2B2B2B')
        img_label.image = image
        img_label.grid(column=7, row=0, sticky=E)

        # Description Label
        tk.Label(danger_frame, text='Hide text data inside harmless looking image files', bg="#2B2B2B", fg="#A0A0A0", width=40).grid(column=1, row=1, pady=10)

        # Text input
        tk.Label(danger_frame, text='Enter hidden message text', bg="#2B2B2B", fg="#DADADA", width=35).grid(column=1, row=2, pady=2)
        self.entryImg = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryImg.grid(column=1, row=3, pady=2)

        # Image path input
        tk.Label(danger_frame, text='Enter exact path to img you’d like to store text in', bg="#2B2B2B", fg="#DADADA", width=36).grid(column=1, row=5, pady=2)
        self.entryTxt = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryTxt.grid(column=1, row=6, padx=5, pady=2)

        # Output image name input
        tk.Label(danger_frame, text="Enter a name for your outputted image", bg="#2B2B2B", fg="#DADADA", width=35).grid(column=1, row=9, pady=2)
        self.entryOutputImgName = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryOutputImgName.grid(column=1, row=10, padx=5, pady=2)

        # File loading buttons
        tk.Button(danger_frame, text="Load Txt File", command=self.get_txt, width=30, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=1, row=4, pady=2)
        tk.Button(danger_frame, text="Load Img File", command=self.get_img, width=30, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=1, row=8, pady=2)

        # Hide button
        tk.Button(danger_frame, text="Hide Data", command=self.combination, width=12, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=2, row=11, padx=2, pady=5)

    def sideBar(self):
        SideBar_frame = LabelFrame(self.root, bg="#1E1E1E", fg="#DADADA", bd=2)
        SideBar_frame.grid(column=0, row=1, columnspan=1, rowspan=8, sticky=N+S+E+W)

        tk.Label(SideBar_frame, text="Data Hiding", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 10)).grid(column=0, row=1, pady=(10, 2))
        tk.Label(SideBar_frame, text="Signature Creation", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 10)).grid(column=0, row=4, pady=(10, 2))

        tk.Button(SideBar_frame, text="Mask Data", command=self.bulk, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=2, pady=2)
        tk.Button(SideBar_frame, text="Extract Data", command=self.extract_page, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=3, pady=2)
        tk.Button(SideBar_frame, text="Create Signature", command=self.sigCreator, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=5, pady=2)
        tk.Button(SideBar_frame, text="Embed Watermark", command=self.embeded_watermark, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=6, pady=2)


    #New plan is creating the output, once all 3 are filled, pass to combination which will revalidate input, 
    #and if its correct i can exfiltrate it to the stego classes, Im calling this function repeatadly for this purpose
    def combination(self):
        pass

    #def get_img(self):
     #   pass

    def get_txt(self):
        input_path = self.entryImg.get()
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

    def output(self):
        output1 = self.combination

    def extract_page(self):
        pass

    def sigCreator(self):
        pass

    def embeded_watermark(self):
        pass

class stego:
    def __init__(self, a,b,c):
        self.InputTxt = a
        self.imgPath = b
        self.NewImg_name = c
        #Add rest of class variables
    
    #Add rest of stego and caeser
    def main(self):
        pass
# Launch the GUI
root = Tk()
app = MyApp(root)
app.bulk()
app.sideBar()

#Taking the 3 outputs from MyApp class, feeding them to stego.
s = app.combination()
stego(s[1],s[2],s[3])
root.mainloop()
