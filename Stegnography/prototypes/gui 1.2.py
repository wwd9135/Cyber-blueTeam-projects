from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL as pd
import tkinter as tk
import pandas as pd  # Correct way to import pandas

class MyApp:
    def __init__(self, root):
        self.root = root
        self.InputTxt = None
        self.imgPath = None
        self.NewImg_name = None
        self.combo = None

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
        tk.Label(danger_frame, text='Enter hidden message text', bg="#2B2B2B", fg="#DADADA", width=35, takefocus= True).grid(column=1, row=2, pady=2)
        self.entryTxt = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryTxt.grid(column=1, row=3, pady=2)

        # Image path input
        tk.Label(danger_frame, text='Enter exact path to img you’d like to store text in', bg="#2B2B2B", fg="#DADADA", width=36).grid(column=1, row=5, pady=2)
        self.entryImg = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryImg.grid(column=1, row=6, padx=5, pady=2)

        # Output image name input
        tk.Label(danger_frame, text="Enter a name for your outputted image (containing png)", bg="#2B2B2B", fg="#DADADA", width=42).grid(column=1, row=9, pady=2)
        self.entryOutputImgName = tk.Entry(danger_frame, width=35, bg="#1E1E1E", fg="#DADADA", insertbackground="#DADADA", highlightthickness=1, highlightbackground="#3B8ED0")
        self.entryOutputImgName.grid(column=1, row=10, padx=5, pady=2)
    

        # File loading buttons
        tk.Button(danger_frame, text="Load Txt File", command=self.get_txt, width=30, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=1, row=4, pady=2)
        tk.Button(danger_frame, text="Load Img File", command=self.get_img, width=30, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=1, row=8, pady=2)

        # Hide button
        tk.Button(danger_frame, text="Hide Data", command=self.checker, width=12, bg="#3B8ED0", fg="white", activebackground="#2B2B2B").grid(column=2, row=11, padx=2, pady=5)

    def sideBar(self):
        SideBar_frame = LabelFrame(self.root, bg="#1E1E1E", fg="#DADADA", bd=2)
        SideBar_frame.grid(column=0, row=1, columnspan=1, rowspan=8, sticky=N+S+E+W)

        tk.Label(SideBar_frame, text="Data Hiding", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 10)).grid(column=0, row=1, pady=(10, 2))
        tk.Label(SideBar_frame, text="Signature Creation", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 10)).grid(column=0, row=4, pady=(10, 2))

        tk.Button(SideBar_frame, text="Mask Data", command=self.bulk, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=2, pady=2)
        tk.Button(SideBar_frame, text="Extract Data", command=self.extract_page, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=3, pady=2)
        tk.Button(SideBar_frame, text="Create Signature", command=self.sigCreator, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=5, pady=2)
        tk.Button(SideBar_frame, text="Embed Watermark", command=self.embeded_watermark, width=20, bg="#3B8ED0", fg="white").grid(column=0, row=6, pady=2)
    def checker(self):
        self.NewImg_name = self.entryOutputImgName.get()  # Get the image name when needed
        
        if self.imgPath is not None:
            if self.InputTxt is not None:
                if self.NewImg_name is not None:
                    self.combination()
                    return self.combo
                else:
                    return None
            else: return None
        else:
            return None
        
                    

    #New plan is creating the output, once all 3 are filled, pass to combination which will revalidate input, 
    #and if its correct i can exfiltrate it to the stego classes, Im calling this function repeatadly for this purpose
    def combination(self):
        self.combo = [self.InputTxt , self.imgPath , self.NewImg_name]
        print(f"desired output for checking {self.combo}")
        
        return self.combo
    

    def get_img(self):
        # File dialog to select an image
        self.imgPath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        print(f"Image path selected: {self.imgPath}")

    def get_txt(self):
        # File dialog to select a text file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(file_path, 'r') as file:
            self.InputTxt = file.read()
        print(f"Text path selected: {self.InputTxt}")        




    #Following are in beta add ons currently!
    def extract_page(self):
        pass

    def sigCreator(self):
        pass

    def embeded_watermark(self):
        pass


    
    # ------------------ Inputs class ------------------
class stego:
    def __init__(self,a,b,c):
        
        self.NewImg_name = c
        self.Txtinput = a
        self.data = ""
        self.fit = 0
        self.leftover = 0
        self.pixels = ""
        self.img = b
        self.df = pd.DataFrame(columns=['R', 'G', 'B'])





    def returner(self):
        return self.fit, self.leftover,self.data
    
 
    
    def txt(self):
        # Remove only spaces (leave \n etc. if needed)
        filed = [char for char in self.Txtinput if char != ' ']
        self.files = filed
        self.data = ''.join(format(ord(c), '08b') for c in self.files)
        self.fit = len(self.data) // 3
        self.leftover = len(self.data) % 3

        print(f"[inputs.dataStuct] Fit (triplets): {self.fit}")
        print(f"[inputs.dataStuct] Leftover characters: {self.leftover}\n \n")
        print(f"[inputs.txt] Filtered characters (without spaces):\n{filed}")
        print(f"[inputs.txt] Binary representation ({len(self.data)} bits):\n{self.data}")
    def update_image_from_df(self):
        if self.df.empty:
            print("DataFrame is empty. No image update performed.")
            return

        self.img = Image.open(self.img)
        self.pixels = self.img.load()

        for i in range(len(self.df)):
            x = i + 1
            y = i + 1
            row = self.df.loc[i]

            # Always get R, since it's guaranteed to exist
            r = int(row['R'], 2)

            # Handle G and B safely — only convert if valid
            g = int(row['G'], 2) if pd.notna(row.get('G')) and isinstance(row.get('G'), str) else self.pixels[x, y][1]
            b = int(row['B'], 2) if pd.notna(row.get('B')) and isinstance(row.get('B'), str) else self.pixels[x, y][2]

            self.pixels[x, y] = (r, g, b)
        NewNameAttempt = self.NewImg_name
        print(f"ERROR CHECKING IS THIS THE RIGHT NAME>{s}")
        self.img.save(NewNameAttempt)
        print("[update_image_from_df] Image updated and saved as output.png")


    def dataStuctAddition(self, a, b=None, c=None):
        """ This function appends bits to the last binary string of each column in the DataFrame """
        # Initialize DataFrame with empty rows if it's empty
        if self.df.empty:
            self.df = pd.DataFrame(columns=['R', 'G', 'B'])
            # Initialize columns with empty strings to ensure type consistency
            self.df['R'] = self.df['R'].astype(str)
            self.df['G'] = self.df['G'].astype(str)
            self.df['B'] = self.df['B'].astype(str)

        # If it's the first entry, create a new row for R, G, B
        if b is None:
            new_row = {'R': a}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        elif c is None:
            new_row = {'R': a, 'G': b}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        else:
            new_row = {'R': a, 'G': b, 'B': c}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def changer(self):
        bit_index = 0  # Index for data bits

        for i in range(len(self.df)):
            for channel in ['R', 'G', 'B']:
                if bit_index < len(self.data):
                    original_binary = self.df.at[i, channel]
                    if len(original_binary) == 8:  # Only modify if it's a full 8-bit string
                        modified_binary = original_binary[:-1] + self.data[bit_index]
                        self.df.at[i, channel] = modified_binary
                        bit_index += 1
                else:
                    break  # Stop if we run out of bits

        print("\n[Changer] DataFrame after LSB replacement:\n", self.df)

    def image(self):
        """ This function processes the image and adds binary data to the DataFrame """
        self.img = Image.open(self.img)
        print(f"Size of image is: {self.img.size}")
        print(f"Image mode is: {self.img.mode}")
        self.pixels = self.img.load()

        # Iterating over the pixels and extracting the RGB values
        for i in range(self.fit):
            x = i + 1
            y = i + 1
            self.current = self.pixels[x, y]
            a = self.current[0]
            b = self.current[1]
            c = self.current[2]

            # Convert RGB values to binary
            red = format(a, '08b')
            green = format(b, '08b') if b is not None else None
            blue = format(c, '08b') if c is not None else None

            # Add the binary triplet to the DataFrame
            self.dataStuctAddition(red, green, blue)

        # If leftover data is less than a full pixel, add one or two colour channels worth of data to end of output.
        if self.leftover == 1:
            self.dataStuctAddition(red)
        elif self.leftover == 2:
            self.dataStuctAddition(red, green)

        # Save the output image
        NewImgAttempt = self.NewImg_name
        
        self.img.save(NewImgAttempt)
        print(self.df)

# ------------------ Caesar Cipher Class ------------------
class Caesar:
    def __init__(self, stego_instance):
        self.shift = 5
        self.caller_data = stego_instance.data
        self.encryptionHeader = [""]

    def errorCheck(self):
        if not all(bit in '01' for bit in self.caller_data):
            return
        

    def caeser(self):
        if not self.caller_data or self.shift is None:
            print("No data or shift provided!")
            return None

        shifted_binary = ""
        print("HERE",self.caller_data)
        for i in range(0, len(self.caller_data) - 7, 8):
            byte = self.caller_data[i:i + 8]
            original_value = int(byte, 2)
            shifted_value = (original_value + self.shift) % 256
            
            shifted_binary += format(shifted_value, '08b')
        print("HERE TOO",shifted_binary)
        # Carry any remaining bits unmodified (no padding)
        remainder = len(self.caller_data) % 8
        if remainder:
            shifted_binary += self.caller_data[-remainder:]
 
        return shifted_binary
   
# Launch the GUI
root = Tk()
app = MyApp(root)
app.bulk()
app.sideBar()


# ------------------ Run the Program ------------------ 

s = app.checker()
app.combination()
print(f" Checker returned {s}")
# Check if data exists
while True:
    print(s)
    if s is not None:
        stego_instance = stego(s[0], s[1], s[2])
        print(f"stego_instance created: {stego_instance}")
        stego_instance.txt()  # Run the methods if valid data is provided
        caesar = Caesar(stego_instance)
        caesar.errorCheck()
        shifted_binary = caesar.caeser()
        print("test")

        stego_instance.data = shifted_binary  # Store the shifted_binary data in inputs
        stego_instance.image()
        stego_instance.changer()

        # Save the shifted_binary output to a file (optional)
        if shifted_binary:
            with open("dis.txt", "w") as file:
                file.write(f"The final outputted hash is:\n{shifted_binary}")
        else:
            print("No shifted binary data available to write.")

        stego_instance.update_image_from_df()  # Update the image based on the final dataframe
        
    else:
        print("Waiting for valid input data...")


    root.mainloop()
