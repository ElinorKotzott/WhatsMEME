import json
import os
import random
from data.json_data_manager import load_users, add_user, save_users


def is_new_user(chat_id):
    """Checks whether the user is new or returning.
        Adds the user to the system if they don't exist.
        Args:
            chat_id - the unique chat id to check
        Returns:
            bool: True if the user is new, False otherwise.
        """
    users = load_users()
    print(users)

    if chat_id in users.keys():
        return False
    else:
        users[chat_id] = {
            "seen_memes": [],
            "last_meme": None
            }
        save_users(users)
        return True

def welcome_user(user_id):
    """
    Greets the user based on whether they are new or returning.
    For new users, prompts for their name and stores it.
    Returns the welcome message to be sent via WhatsApp.
    """
    users = load_users()

    if user_id in users:
        name = users[user_id].get("name", "friend")
        message = f"Welcome back, {name}! Ready for some fresh laughs? 😂"
    else:
        # New user flow
        message = "Hi there! Welcome to WhatsMEME – A place to lighten up your mood with some funny memes! 😄\n"
        name = input("Before we start, what’s your name? ").strip()

        users[user_id] = {
            "name": name,
            "seen_memes": [],
            "last_meme": None
        }
        save_users(users)

        message += f"\nNice to meet you, {name}!\nLet’s dive into some hilarious content!"

    return message, name

def display_menu():
    print("\nWould you like to explore some more hilarious memes?")
    print("Here is how I can help you today! Just make a choice:")
    print("1 - Get a random meme")
    print("2 - Choose a meme based on a topic or mood")
    print("3 - Generate your own meme")
    print("Type 'help' to get indepth explanations of the various choices and 'exit' to quit.")


def show_help_menu():
    """Displays help instructions for navigating the WhatsMEME app.
    Explains how to choose options and use the available features."""
    print("\n--- WhatsMEME Help Menu ---")
    print("Here's a quick guide to brighten your day with memes:")
    print("1 - Get a random meme:")
    print("    We'll surprise you with a meme from our hilarious collection.")
    #print("2 - Choose a meme by topic or mood:")
    #print("    Feeling something specific? Just tell us your vibe – like 'cats', 'work', or 'weekend' – and we’ll match a meme to it.")
    print("3 - Generate your own meme:")
    print("    Be the meme-maker! Describe your ideal meme and add your own caption.")
    print("'help' - View this menu anytime.")
    print("'exit' - Leave WhatsMEME (but come back soon for more laughs!)\n")


def get_random_meme(user_name):
    """Fetches and displays a random meme from an external API.
    Stores the meme in the user's seen history.
    Args:
        user_name (str): The name of the current user."""
    
    if user_name not in user_db:
        user_db[user_name] = {"seen_memes": []}

    seen = user_db[user_name]["seen_memes"]
    unseen_memes = [meme for meme in meme_bank if meme not in seen]

    if not unseen_memes:
        print("😅 Uh-oh! You’ve seen all our memes for now.")
        print("Check back later when we've got more meme madness for you!")
        return

    selected_meme = random.choice(unseen_memes)
    user_db[user_name]["seen_memes"].append(selected_meme)

    print("\nHere's your random meme! 😂")
    print(f"{selected_meme}")


def get_meme_by_topic(user_name, topic):
    """Fetches and displays a meme related to a specific topic or mood.
    Updates the user's meme history.
    Args:
        user_name (str): The name of the current user.
        topic (str): The keyword/topic for the meme search."""
    pass


def generate_custom_meme(user_name, template_description, text):
    """Uses AI to create a custom meme
    based on the user’s template description and caption/text.
    Args:
        user_name (str): The name of the current user.
        template_description (str): A description of the desired meme template.
        text (str): Caption or content for the meme."""
    pass
