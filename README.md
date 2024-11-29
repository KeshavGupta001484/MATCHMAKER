# Matchmaking Program

Welcome to the Matchmaking Program! This Python application is a fun project designed to randomly assign you a partner based on your gender. The program uses the `Faker` library to generate random names and stores the matchmaking results locally in a JSON file.

## Features

- **Interactive Input**: The program prompts users to select their gender and enter their name.
- **Random Partner Assignment**: Based on the user's gender, the program assigns a random partner.
- **Persistent Storage**: Matchmaking results are stored in a local JSON file, allowing you to retrieve your assigned partner when you revisit the program.
- **View All Matches**: Displays all previous matchmaking results.

## Requirements

- Python 3.6 or higher
- `Faker` library (install using `pip install faker`)

## How to Run

1. Clone this repository or download the `matchmaking_program.py` file.
2. Ensure Python is installed on your system.
3. Install the required dependency:
   ```bash
   pip install faker
   ```
4. Run the program:
   ```bash
   python matchmaking_program.py
   ```

## How It Works

1. The program checks for an existing `matchmaking_results.json` file.
   - If the file exists, it loads previous matchmaking results.
   - If the file is missing or corrupted, a new file is initialized.
2. The user selects their gender and provides their name.
3. The program assigns a partner based on the user's gender.
4. The partner's name is generated using the `Faker` library.
5. Results are saved to the JSON file and displayed.
6. All stored matches are displayed for the user.

## Sample Output

```
Select your Gender!
M: ---> for Male
F: ---> for Female
Your choice: M
Enter your name: John
Hey John, Emma is your Girlfriend 💖

All Matchmaking Results:
John 💖 Emma
Sarah 💖 Michael

Thank you for using this matchmaking program!
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions and improvements are always welcome!

Thank you for using the Matchmaking Program! Have fun finding your random match! 💖
