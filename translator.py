"""
    Name: translator.py
    Author: William A Loring
    Created: 11/11/2023
    Purpose: Translate English to Spanish using deep-translator library
"""

# https://customtkinter.tomschimansky.com
# pip install customtkinter
import customtkinter as ct
# https://pypi.org/project/deep-translatorcustom
# pip install deep-translator
from deep_translator import GoogleTranslator


class TranslationApp(ct.CTk):
    def __init__(self):
        """Initializes the TranslationApp object"""
        super().__init__()
        self.title("Translation App")
        # Add icon to program title bar
        self.iconbitmap('translate.ico')

        # Set up the appearance and default color theme of the
        # CustomTkinter application window
        # Modes: system (default), light, dark
        ct.set_appearance_mode("dark")
        # Themes: blue (default), dark-blue, green
        ct.set_default_color_theme("blue")

        # Call the create_widgets method to create and
        # configure widgets for the application
        self.create_widgets()

    def create_widgets(self):
        """Create and Grid widgets"""
        # Create main frame to contain the widgets
        self.main_frame = ct.CTkFrame(master=self)
        # Fill the frame to the width of the window
        self.main_frame.pack(fill=ct.X)
        # Keep the frame size regardless of the widget sizes
        self.main_frame.pack_propagate(False)

        # Create widgets
        self.lbl_input = ct.CTkLabel(
            self.main_frame,
            text="Enter text:",
            anchor=ct.E
        )
        self.entry_input = ct.CTkEntry(
            self.main_frame,
            width=150
        )
        self.btn_spanish = ct.CTkButton(
            self.main_frame,
            text="Translate to Spanish",
            command=self.translate_to_spanish
        )
        self.btn_english = ct.CTkButton(
            self.main_frame,
            text="Translate to English",
            command=self.translate_to_english
        )
        self.lbl_result = ct.CTkLabel(
            self.main_frame,
            text="",
            width=100,
            anchor=ct.W
        )

        # Grid widgets
        self.lbl_input.grid(row=0, column=0, sticky=ct.E)
        self.entry_input.grid(row=0, column=1)
        self.btn_spanish.grid(row=1, column=0)
        self.btn_english.grid(row=1, column=1)
        self.lbl_result.grid(row=2, column=0, columnspan=2, sticky=ct.W)

        # Set padding between frame and window
        self.main_frame.pack_configure(padx=20, pady=10)

        # Set padding for all widgets
        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Bind the enter key to the method
        # When the Enter key is pressed, the method will be fired
        # self.entry_input.bind('<Return>', self.translate_to_spanish)
        # self.entry_input.bind('<KP_Enter>', self.translate_to_spanish)

        # Set the focus on the entry widget for easy data entry
        # Delay setting the focus for 10 ms after program is loaded
        self.entry_input.after(
            10,
            self.entry_input.focus_set
        )

    def translate_to_spanish(self):
        """
        Translates the input text from English to Spanish using the GoogleTranslator library.

        Inputs:
        - self: The instance of the TranslationApp class.

        Flow:
        1. Get the input text from the text_input widget.
        2. Check if there is any input text.
        3. If there is input text, use the GoogleTranslator library to translate the text from English to Spanish.
        4. Update the text of the lbl_result widget with the translated text, prefixed with "Spanish: ".
        5. If there is no input text, update the text of the lbl_result widget with "Please enter text!".

        Outputs:
        - The translated text is displayed in the lbl_result widget, prefixed with "Spanish: ".
        """
        input_text = self.entry_input.get()
        if input_text:
            # If there's input text, translate using GoogleTranslator
            translated_text = GoogleTranslator(
                source='en', target='es').translate(input_text)
            self.lbl_result.configure(
                text=f"Spanish: {translated_text}")
        else:
            self.lbl_result.configure(text="Please enter text!")

        # Select all text in the entrybox to allow user
        # to type and replace the entered text quickly
        self.entry_input.select_range(0, ct.END)

    def translate_to_english(self):
        """
        Translates input text from Spanish to English using the GoogleTranslator library.

        Inputs:
        - self: The instance of the TranslationApp class.

        Flow:
        1. Get the input text from the text_input widget.
        2. Check if there is any input text.
        3. If there is input text, use the GoogleTranslator library
          to translate the text from Spanish to English.
        4. Update the text of the lbl_result widget with the translated text, prefixed with "English: ".
        5. If there is no input text, update the text of the lbl_result widget with "Please enter text!".

        Outputs:
        - The translated text is displayed in the lbl_result widget, prefixed with "English: ".
        """
        input_text = self.entry_input.get()
        if input_text:
            # If there's input text, translate using GoogleTranslator
            translated_text = GoogleTranslator(
                source='es', target='en').translate(input_text)
            # Display translated text
            self.lbl_result.configure(
                text=f"English: {translated_text}")
        else:
            self.lbl_result.configure(text="Please enter text!")

        # Select all text in the entrybox to allow user
        # to type and replace the entered text quickly
        self.entry_input.select_range(0, ct.END)


if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
