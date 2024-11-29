import os
import json
from faker import Faker

# Initialize Faker
fake = Faker()

# File to store results
STORAGE_FILE = "matchmaking_results.json"

def load_results():
    """Load existing matchmaking results from the file."""
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                else:
                    print("Corrupted data detected. Reinitializing the file.")
        except json.JSONDecodeError:
            print("Invalid or empty file detected. Reinitializing the file.")
    return {}

def save_results(results):
    """Save matchmaking results to the file."""
    with open(STORAGE_FILE, "w") as file:
        json.dump(results, file, indent=4)

def get_user_gender():
    """Prompt the user to select their gender."""
    while True:
        gender = input("""Select your Gender!\nM: ---> for Male\nF: ---> for Female\nYour choice: """).strip().upper()
        if gender in ("M", "F"):
            return gender
        print("Invalid input. Please select either 'M' or 'F'.")

def get_user_name():
    """Prompt the user to enter their name."""
    while True:
        name = input("Enter your name: ").strip().capitalize()
        if name:
            return name
        print("Name cannot be empty. Please try again.")

def assign_partner(name, gender):
    """Assign a partner based on the user's gender."""
    if gender == "M":
        partner_name = fake.first_name_female()
        relationship = f"Hey {name}, {partner_name} is your Girlfriend 💖"
    else:  # gender == "F"
        partner_name = fake.first_name_male()
        relationship = f"Hey {name}, {partner_name} is your Boyfriend 💖"
    return partner_name, relationship

def display_results(results):
    """Display all stored matchmaking results."""
    print("\nAll Matchmaking Results:")
    for user, partner in results.items():
        print(f"{user} 💖 {partner}")

# Main Program
if __name__ == "__main__":
    stored_results = load_results()

    # Get user inputs
    user_gender = get_user_gender()
    user_name = get_user_name()

    # Check if the user already has a partner assigned
    if user_name in stored_results:
        print(f"Welcome back, {user_name}! Your assigned partner is {stored_results[user_name]} 💖")
    else:
        partner_name, relationship = assign_partner(user_name, user_gender)
        stored_results[user_name] = partner_name
        save_results(stored_results)
        print(relationship)

    # Display all results
    display_results(stored_results)

    print("\nThank you for using this matchmaking program!")
