from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def generic(root):
    # Create style for the frame
    s = ttk.Style()
    s.configure('Danger.TFrame', background='grey', borderwidth=5, relief='raised')
    

    # Create the frame and assign it to a variable
    danger_frame = ttk.Frame(root, style='Danger.TFrame')
    danger_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=1, pady=1)

    # Add a label inside the frame
    ttk.Label(danger_frame, text='Stego Ver 2.1.1').grid(column=3, row=0, padx=10, pady=10, sticky=W)

    # Load and resize image
    raw_img = Image.open("ad84ddbf-6877-4b88-82ab-3357ace4f595.png")
    resized_img = raw_img.resize((30, 30))
    image = ImageTk.PhotoImage(resized_img)

    # Display image next to the label
    img_label = Label(danger_frame, image=image, background='grey')
    img_label.image = image  # Keep a reference
    img_label.grid(column=5, row=0, padx=5, pady=5, sticky=E)
    d = ttk.Scale(danger_frame, orient=HORIZONTAL, length=200, from_=1.0, to=100.0)

    ttk.Label(danger_frame,text= 'Enter hidden message txt file' ).grid(column=4,row=1)
    TxtFileEntry = ttk.Entry(danger_frame, width=25, textvariable=StringVar)
    TxtFileEntry.grid(column=4, row=2, sticky=(E))
    #TODO- Add drag and drop here

    #TODO- Finish rest of input buttons, they should create an output i can pass to code classes.
        
    
    
    #Making new page
    #ttk.Button(danger_frame, alternate)
    #def alternate(root):
      #  alternate_frame = ttk.Frame(danger_frame, style='Danger.TFrame')
       # alternate_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=1, pady=1)
    #    
root = Tk()
root.title("Stego - Steganography Toolkit")
generic(root)
root.mainloop()