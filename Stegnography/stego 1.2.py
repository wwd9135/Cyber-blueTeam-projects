import pandas as pd
import random
from PIL import Image

# ------------------ Inputs class ------------------
class inputs:
    def __init__(self):
        self.Txtinput = ""
        self.data = ""
        self.files = []
        self.fit = 0
        self.leftover = 0
        self.pixels = ""
        self.img = ""
        self.df = pd.DataFrame(columns=['R', 'G', 'B'])

    
    def txt_import(self):
        try:
            with open(input("Enter your text file name: "), "r") as file:
                contents = file.read()
           #     print(f"[inputs.txt_import] Raw characters (with spacing):\n{contents}")
                return contents
        except FileNotFoundError:
            print("Error: The file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def txt(self, text):
        # Remove only spaces (leave \n etc. if needed)
        filed = [char for char in text if char != ' ']
        self.files = filed
        self.data = ''.join(format(ord(c), '08b') for c in self.files)
        self.fit = len(self.data) // 3
        self.leftover = len(self.data) % 3
       
        print(f"[inputs.dataStuct] Fit (triplets): {self.fit}")
        print(f"[inputs.dataStuct] Leftover characters: {self.leftover}\n \n")
        print(f"[inputs.txt] Filtered characters (without spaces):\n{filed}")
        print(f"[inputs.txt] Binary representation ({len(self.data)} bits):\n{self.data}")

        


    def dataStuctAddition(self, a , b = None , c = None): 
        
        if b is None:
            new_row = {'R': a}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

        elif c is None:
            new_row = {'R': a, 'G': b}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        
        else:
            new_row = {'R': a, 'G': b, 'B': c}
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

        # Go through, append i to the last elemet of each j. use [ 0::] or whatever it was
    




    def image(self):
        self.img = Image.open("sd.webp")
        print(f"Size of image is: {self.img.size}")
        print(f"Image mode is: {self.img.mode}")
        self.pixels = self.img.load()
        for i in range(self.fit):
            
            x = i + 1
            y = i + 1
            self.current = self.pixels[x,y]
            a = self.current[0]
            b = self.current[1]
            c = self.current[2] 
            #Data passed must be done in iterations, this
            red = format(a , '08b')
            green = format(b, '08b') if b is not None else None 
            blue = format(c, '08b') if c is not None else None

            self.dataStuctAddition(red,green,blue)

        #If left over data is less than a full pixel, add one or two colour channels worth of data to end of output.
        if self.leftover == 1:
            self.dataStuctAddition(red)
        elif self.leftover == 2:
            self.dataStuctAddition(red,green)
        
        self.img.save("output.png")
        
        print( self.df )
        
    def changer(self):
        for i in range(len(self.data)):#
            for index, row in self.df.iterrows():
                self.data[i].append(row['R'][::0])
                self.data[i+1].append(row['G'][::0])
                self.data[i+2].append(row['B'][::0])
                i + 3                
    
        

# ------------------ Caesar Cipher Class ------------------
class Caesar:
    def __init__(self, caller_instance, shift=None):
        self.shift = shift
        self.caller_data = caller_instance.data
        self.encryptionHeader = [""]

    def errorCheck(self):
        if not all(bit in '01' for bit in self.caller_data):
         #   print("Data is not binary!")
            return
    #    print("[Caesar.errorCheck] Binary data valid.")

    def take_shift(self):
        self.shift = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
        self.encryptionHeader.append(self.shift)
        #print(f"Random Caesar shift chosen: {self.shift}")
        return self.encryptionHeader

    def caeser(self):
        if not self.caller_data or self.shift is None:
            print("No data or shift provided!")
            return None

        shifted_binary = ""
        for i in range(0, len(self.caller_data) - 7, 8):
            byte = self.caller_data[i:i + 8]
            original_value = int(byte, 2)
            shifted_value = (original_value + self.shift) % 256
            shifted_binary += format(shifted_value, '08b')

        # Carry any remaining bits unmodified (no padding)
        remainder = len(self.caller_data) % 8
        if remainder:
            shifted_binary += self.caller_data[-remainder:]

  #      print("\n[Caesar.caeser] Original binary length:", len(self.caller_data))
   #     print("[Caesar.caeser] Shifted binary length:", len(shifted_binary))
        return shifted_binary


# ------------------ Run the Program ------------------

caller_instance = inputs()
raw_text = caller_instance.txt_import()

caller_instance.txt(raw_text)


caesar = Caesar(caller_instance)
caesar.errorCheck()
caesar.take_shift()
shifted_binary = caesar.caeser()

caller_instance.image()

if shifted_binary:
    with open("dis.txt", "w") as file:
        file.write(f"The final outputted hash is:\n{shifted_binary}")
   #     print(f"\n[Main] Encrypted data written to 'dis.txt'.")
else:
    print("No shifted binary data available to write.")

    
