import tkinter as tk
from tkinter import scrolledtext, font
import datetime


class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("BlenderBot Chat Application")
        master.geometry("600x500")
        master.configure(bg='#f0f0f0')

        # Custom fonts
        self.chat_font = font.Font(family="Helvetica", size=12)
        self.input_font = font.Font(family="Helvetica", size=12)

        # Chat history display
        self.chat_history = scrolledtext.ScrolledText(
            master,
            wrap=tk.WORD,
            width=60,
            height=20,
            font=self.chat_font,
            bg='white',
            fg='black',
            state='disabled'
        )
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # User input field
        self.user_input = tk.Text(
            master,
            wrap=tk.WORD,
            width=50,
            height=3,
            font=self.input_font,
            bg='white',
            fg='black'
        )
        self.user_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Send button
        self.send_button = tk.Button(
            master,
            text="Send",
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            font=self.input_font,
            relief=tk.FLAT
        )
        self.send_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Bind Enter key to send message
        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Configure grid weights for resizing
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Initial greeting
        self.display_message("Bot", "Hello! How can I help you today?")

    def send_message(self):
        """Get user input and process it"""
        message = self.user_input.get("1.0", tk.END).strip()
        if message:
            self.display_message("You", message)
            self.user_input.delete("1.0", tk.END)
            self.process_message(message)

    def display_message(self, sender, message):
        """Display a message in the chat history"""
        self.chat_history.config(state='normal')

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Format the message
        if sender == "You":
            display_text = f"You [{current_time}]: {message}\n\n"
            tag = "user"
        else:
            display_text = f"{sender} [{current_time}]: {message}\n\n"
            tag = "bot"

        # Insert the message
        self.chat_history.insert(tk.END, display_text, tag)

        # Configure tags for different senders
        self.chat_history.tag_config("user", foreground="blue")
        self.chat_history.tag_config("bot", foreground="green")

        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)  # Auto-scroll to bottom

    def process_message(self, message):
        """Process user message and generate response"""
        # Simple echo bot logic - replace this with your LSTM model integration
        response = self.generate_response(message.lower())
        self.display_message("Bot", response)

    def generate_response(self, message):
        """Simple response logic - replace with your actual model"""
        if any(word in message for word in ["hi", "hello", "hey"]):
            return "Hello there! How can I assist you?"
        elif "how are you" in message:
            return "I'm just a computer program, but I'm functioning well! How about you?"
        elif "thank" in message:
            return "You're welcome!"
        elif "bye" in message:
            return "Goodbye! Have a great day!"
        elif "name" in message:
            return "I'm a simple chatbot. You can call me ChatPy!"
        else:
            return "I'm not sure how to respond to that. Could you ask me something else?"


# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    chat_app = ChatGUI(root)
    root.mainloop()