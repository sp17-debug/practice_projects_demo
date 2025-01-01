from tkinter import *

root = Tk()

def send():
    send = "You: " + e.get()
    text.insert(END, "\n" + send)

    user_input = e.get().lower()

    if user_input == 'hi':
        text.insert(END, "\n" + "Bot: Hello!")
    elif user_input == 'hello':
        text.insert(END, "\n" + "Bot: Hi!")
    elif user_input == 'how are you?':
        text.insert(END, "\n" + "Bot: I'm fine, and you?")
    elif user_input == "i'm fine too":
        text.insert(END, "\n" + "Bot: Nice to hear that!")
    elif user_input == "what's your name?":
        text.insert(END, "\n" + "Bot: My name is TechSappy!")
    elif user_input == "what do you do?":
        text.insert(END, "\n" + "Bot: I chat with awesome people like you!")
    elif user_input == "what's your favorite color?":
        text.insert(END, "\n" + "Bot: I like all colors, but pink is cool!")
    elif user_input == "tell me a joke":
        text.insert(END, "\n" + "Bot: Why don't scientists trust atoms? Because they make up everything!")
    elif user_input == "bye":
        text.insert(END, "\n" + "Bot: Goodbye! Have a great day!")
    else:
        text.insert(END, "\n" + "Bot: Sorry, I didn't get that.")

    e.delete(0, END)


text = Text(root, bg='black', fg='white')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_button = Button(root, text='Send', bg='deeppink', fg='white', width=8, command=send)
send_button.grid(row=1, column=1)

root.title('TechSappy')
root.mainloop()
