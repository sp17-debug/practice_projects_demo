# SappyTech Chatbot

## Description

SappyTech is a simple chatbot application built using Python's Tkinter library. This application provides a basic interface where users can send messages to the bot and receive predefined responses. It serves as a foundation for creating more advanced chatbot functionalities.

## Features

- Simple graphical user interface (GUI) using Tkinter.
- Basic response mechanism for predefined user inputs.
- Text display area for conversation history.
- Entry field for user input.
- Send button to send user messages.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installations)

## Usage

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your machine.
3. Run the script using a Python interpreter:

   ```bash
   python chatbot.py
   ```

4. A window titled "SappyTech" will open.
5. Type your message in the entry field and click the "Send" button to communicate with the bot.
6. The bot will respond based on predefined rules.

## Code Explanation

The main components of the code are:

- **Importing Tkinter Library**: `from tkinter import *`
- **Creating Main Window**: `root = Tk()`
- **Defining the `send` Function**: This function handles the sending of messages and the bot's responses. 
- **Text Widget**: `text = Text(root, bg='black', fg='white')` - This widget is used to display the conversation history.
- **Entry Widget**: `e = Entry(root, width=80)` - This widget is used to take user input.
- **Send Button**: `send = Button(root, text='Send', bg='deeppink', fg='white', width=2, command=send).grid(row=1, column=1)` - This button triggers the `send` function.
- **Layout Management**: The grid layout manager is used to place the widgets in the window.
- **Window Title**: `root.title('SappyTech')`
- **Main Loop**: `root.mainloop()` - This starts the Tkinter event loop.

## Predefined Responses

The chatbot responds based on the following predefined rules:

- If the user types "hi", the bot responds with "hello".
- If the user types "hello", the bot responds with "hi".
- If the user types "how are you?", the bot responds with "i'm fine and you?".
- If the user types "i'm fine too", the bot responds with "nice to hear that".
- For any other input, the bot responds with "Sorry I didn't get it."

## Customization

To add more responses or modify existing ones, you can update the `send` function by adding more `elif` conditions.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

## Acknowledgements

- This project uses the Tkinter library for creating the GUI.

---

Feel free to reach out if you have any questions or suggestions for improvement. Enjoy chatting with SappyTech!
