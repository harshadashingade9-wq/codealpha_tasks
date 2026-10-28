"""
CodeAlpha Python Internship - Task 4: Basic Chatbot
A simple rule-based chatbot that replies to predefined user messages.
"""

import random
import string
from datetime import datetime

BOT_NAME = "CodeBot"

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer wear glasses? Because he couldn't C!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
]

HELP_TEXT = (
    "You can try: hello, how are you, my name is <name>, what is your name, "
    "time, date, joke, thanks, bye"
)


def clean_text(text):
    """Make the message lowercase and remove punctuation."""
    text = text.lower().strip()
    return text.translate(str.maketrans("", "", string.punctuation))


def get_reply(message, memory):
    """
    Return (reply, should_exit) for the user's message.
    memory is a dict used to remember the user's name.
    """
    text = clean_text(message)
    words = text.split()

    if not text:
        return "Please type something.", False

    # Goodbye
    elif any(w in words for w in ("bye", "goodbye", "exit", "quit")):
        return "Goodbye!", True

    # User tells their name
    elif "my name is" in text:
        name = text.split("my name is", 1)[1].strip().title()
        if name:
            memory["name"] = name
            return f"Nice to meet you, {name}!", False
        return "I didn't catch your name. Try: my name is Sam", False

    # Asking the bot about the user's name
    elif "what is my name" in text or "who am i" in text:
        if "name" in memory:
            return f"Your name is {memory['name']}.", False
        return "I don't know your name yet. Tell me: my name is ...", False

    # Asking the bot's name
    elif "your name" in text or "who are you" in text:
        return f"I'm {BOT_NAME}, a simple rule-based chatbot.", False

    # How are you
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?", False

    # Greeting
    elif any(w in words for w in ("hello", "hi", "hey")):
        if "name" in memory:
            return f"Hi, {memory['name']}!", False
        return "Hi!", False

    # Time and date
    elif "time" in words:
        return "The time is " + datetime.now().strftime("%I:%M %p") + ".", False

    elif "date" in words or "today" in words:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + ".", False

    # Joke
    elif "joke" in words:
        return random.choice(JOKES), False

    # Thanks
    elif "thanks" in words or "thank" in words:
        return "You're welcome!", False

    # Help
    elif "help" in words:
        return HELP_TEXT, False

    # Anything else
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do.", False


def chat():
    """Run the chat loop until the user says bye."""
    memory = {}
    print(f"=== {BOT_NAME} ===")
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        reply, should_exit = get_reply(message, memory)
        print(f"{BOT_NAME}: {reply}\n")

        if should_exit:
            break


if __name__ == "__main__":
    chat()
