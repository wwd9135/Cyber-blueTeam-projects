import random
from PIL import Image



# Class to take txt file and an img to hide it within
class inputs:
    def __init__(self):
    
        self.Txtinput = ""
    
    def image():
            # Open an image
            img = Image.open("dl.webp")

            # View size and mode
            print(f"Size of image is: {img.size}")  # (width, height)
            print(f"Image mode is: {img.mode}")  # 'RGB', 'RGBA', 'L', etc.

            # Access pixels
            pixels = img.load()
            print(pixels[0, 0])  # RGB values of the top-left pixel
            print(pixels[740, 1124])  # RGB values of the that position

            # Modify pixels
            pixels[0, 0] = (255, 0, 0)  # Change top-left to red
            print(pixels[0,0])


            # Save image
            img.save("output.png")

    image()

    def txt():
        with open("txts.txt", 'r') as file:
            files = file.read()
            print("Original text:\n", files)

            # Initialize a list to store characters without spaces or newlines
            filed = []

            for char in files:
                # Add character to list if it's not a space or newline
                if char != ' ' and char != '\n':
                    filed.append(char)

            # Print the result after removing spaces and newlines
            print("Filtered characters (without spaces and newlines):")
            print(filed)

    # Call the function


    def txt_import(self):
        try:
            with open(input("Enter your text file name: "), "r") as file:
                # Read the file contents
                contents = file.read()  # Reads the entire file as a string
                binary_representation = ''.join(format(ord(c), '08b') for c in contents)
                self.data = binary_representation
                print(f"Contents of txt file: {contents} ")
        except FileNotFoundError:
            print("Error: The file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

instance = inputs()
#instance.txt_import()
#instance.img()


class Caesar:
    def __init__(self, caller_instance, shift=None):
        self.shift = shift  # Default to None if not provided
        self.database = []  # Initialize the database as an empty list
        self.caller_data = caller_instance.data  # Access 'data' from Caller class
        self.encryptionHeader = ["",]

    def errorCheck(self):
        while True:
            try: 
                self.caller_data  # Access 'data' from Caller class
                if all(bit in '01' for bit in self.caller_data):
                    # The data is binary (only contains 0's and 1's)
                    break  # Break the loop once the data is valid
                else:
                    # The data is not binary
                    print("Data is not binary!")
                    caller_instance.decider()  # Re-run the decider if not binary
                    return  # Ensure we don't re-enter the errorCheck loop
            except ValueError as e:
                print("An error occurred:", e)
                break  # In case of ValueError, break the loop

    def take_shift(self):
        shift = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
        self.shift = shift
        print(f"Random Caesar shift chosen: {shift}")
        self.encryptionHeader.append(self.shift)
        return self.encryptionHeader

           
    def caeser(self):
        if not self.caller_data or self.shift is None:
            print("No data or shift provided!")
            return None

        shifted_binary = ""
        
        # Process the binary data in 8-bit chunks (1 byte)
        for i in range(0, len(self.caller_data), 8):
            byte = self.caller_data[i:i+8]
            if len(byte) < 8:
                # Pad if final chunk is less than 8 bits
                byte = byte.ljust(8, '0')

            original_value = int(byte, 2)
            shifted_value = (original_value + self.shift) % 256  # Wrap at 256 for byte range
            shifted_byte = format(shifted_value, '08b')

            shifted_binary += shifted_byte

        print(f"Original binary: {self.caller_data}\n")

        return shifted_binary




# Create an instance of the Caller class
caller_instance = inputs()

# Start the decider method to make file handling decisions
caller_instance.txt_import()

# Example usage:
caesar = Caesar(caller_instance)  # Pass caller_instance to Caesar

caesar.errorCheck()  # Check if the data is binary
caesar.take_shift()   # Prompt for the shift digit
shifted_binary = caesar.caeser()  # Apply the Caesar cipher shift

caller_instance.image()
# Writing the result to a file
if shifted_binary is not None:  # Ensure the shifted binary is valid
    shifted_binary_str = ''.join(str(binary) for binary in shifted_binary)  # Convert to string
    print(f"Writing the following encrypted to the dis.txt file: {shifted_binary_str} \n")  # Debugging step

    with open("dis.txt", "w") as file:  # Use "w" mode to overwrite the file
        file.write(f"The final outputted hash is:\n{shifted_binary_str}")
        file.flush()  # Explicitly flush the file buffer
else:
    print("No shifted binary data available to write to the file.")

