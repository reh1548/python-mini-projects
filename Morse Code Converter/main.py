from tkinter import *

#-------------CONSTANTS------------------


#----------------UTILITY FUNCTION------------

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',

    ' ': '/'  # Three spaces represent a space in Morse code
}


def text_to_morse_converter():
    # Convert text to Morse code
    text = entry1.get().upper()
    morse = " ".join([morse_code[c] for c in text])
    morse_label.config(text=morse) 

def morse_to_text_converter():
    # Convert Morse code to text
    text = entry2.get()
    text = ''.join([k for k, v in morse_code.items() if v == text])
    print(text)
    text_label.config(text=text) 


#----------------UI SETUP----------------
window = Tk()
window.title("Morse Code Converter")
window.config(padx=20, pady=20)
window.geometry("500x500")

# Create a label widget
label1 = Label(
    window,
    text="Text Here:",
    anchor="w",
    justify="left",
    width=25
)

label1.grid(sticky=W, column=0, row=1)

#----------------TEXT TO MORSE CODE------------------------------
#Entry for Text
entry1 = Entry(width=50)
entry1.insert(END, string="")
entry1.grid(sticky=W, column=0, row=2)

#button to submit the text
button1 = Button(width=20, text="Convert To Morse Code", command=text_to_morse_converter)
button1.grid(sticky=W, column=0, row=3)

# Label to display Morse code
message1 = Label(text="Your Morse Code:\n", width=50)
message1.grid(sticky=W, column=0, row=4)
morse_label = Label(text="", width=50)
morse_label.grid(sticky=W, column=0, row=5)



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
button2 = Button(width=20, text="Convert To Text", command=morse_to_text_converter)
button2.grid(sticky=W, column=0, row=8)

# Label to display the Text
message2 = Label(text="Your Text:\n", width=50)
message2.grid(sticky=W, column=0, row=9)
text_label = Label(text="", width=50)
text_label.grid(sticky=W, column=0, row=10)


window.mainloop()
