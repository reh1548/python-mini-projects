from tkinter import *
import pyperclip
#-------------CONSTANTS------------------


#----------------UTILITY FUNCTION------------
# Define the Morse code dictionary.
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Convert a message to Morse code.
def to_morse_code():
    message = entry1.get()
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
            morse_label.config(text=morse_code) 

# Convert a Morse code sequence to a message.
def from_morse_code():
    morse_code = entry2.get()
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
                text_label.config(text=message) 

def copy_morse():
    morse = morse_label.cget("text")
    pyperclip.copy(morse)

def copy_text():
    text = text_label.cget("text")
    pyperclip.copy(text)

#----------------UI SETUP----------------
window = Tk()
window.title("Morse Code Converter")
window.config(padx=20, pady=20)
window.geometry("500x500")

#----------------TEXT TO MORSE CODE------------------------------

# Create a label widget
label1 = Label(
    window,
    text="Text Here:",
    anchor="w",
    justify="left",
    width=25
)

label1.grid(sticky=W, column=0, row=1)

#Entry for Text
entry1 = Entry(width=50)
entry1.insert(END, string="")
entry1.grid(sticky=W, column=0, row=2)

#button to submit the text
button1 = Button(width=20, text="Convert To Morse Code", command=to_morse_code)
button1.grid(sticky=W, column=0, row=3)

# Label to display Morse code
message1 = Label(text="Your Morse Code:\n", width=50)
message1.grid(sticky=W, column=0, row=4)
morse_label = Label(text="", width=50)
morse_label.grid(sticky=W, column=0, row=5)

# Button to copy the Morse code
copy_morse_button = Button(width=20, text="Copy Morse Code", command=copy_morse)
copy_morse_button.grid(sticky=W, column=1, row=3)

#----------------MORSE CODE TO TEXT------------------------------
# Create a label widget
label2 = Label(
    window,
    text="Morse Code Here:",
    anchor="w",
    justify="left",
    width=25
)

label2.grid(sticky=W, column=0, row=6)

#Entry for Text
entry2 = Entry(width=50)
entry2.insert(END, string="")
entry2.grid(sticky=W, column=0, row=7)

#Button to submit the morse code
button2 = Button(width=20, text="Convert To Text", command=from_morse_code)
button2.grid(sticky=W, column=0, row=8)

# Label to display the Text
message2 = Label(text="Your Text:\n", width=50)
message2.grid(sticky=W, column=0, row=9)
text_label = Label(text="", width=50)
text_label.grid(sticky=W, column=0, row=10)

# Button to copy the text
copy_text_button = Button(width=20, text="Copy Text", command=copy_text)
copy_text_button.grid(sticky=W, column=1, row=8)


window.mainloop()
