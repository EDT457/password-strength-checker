# Password Checker (Tkinter)

This is a small Python program that checks how strong a password is.  
It uses Tkinter to show a window where you can type a password and see its strength in real-time.

## What the program does

- Lets the user type a password into a box  
- Shows or hides the password with a button  
- Counts how many characters are typed and displays a color-coded indicator (red = below threshold, green = meets threshold)
- Checks if the password:
  - Is longer than the set minimum length (default: 12 characters)  
  - Has at least one upper-case letter  
  - Has at least one number  
- Gives a score based on these rules and shows one of four strength labels:
  - **Weaker** (score 0)
  - **Weak** (score 1)
  - **Strong** (score 2)
  - **Very Strong** (score 3)

## How the score works

The `check_password` function gives points for:
1. Passing the length limit  
2. Having at least one upper-case letter  
3. Having at least one digit  

The score goes from **0 to 3**, and the strength label shown in the app matches this score. The character counter also provides visual feedback by changing from red to green when the minimum length is reached.

## How to run it

1. Make sure you have Python 3 installed.
2. Save the code to a file, for example: `password_checker.py`
3. Run the file with:
   ```bash
   python password_checker.py
   ```

**Note:** Tkinter comes built-in with Python, so there are no additional dependencies to install.

## Features

- **Real-time character counter** - See how many characters you've typed
- **Show/Hide toggle** - Securely view or hide your password with a button click
- **Color-coded feedback** - Character counter turns green when minimum length is met
- **Instant strength rating** - Get immediate feedback on password strength
- **Clean GUI** - Simple, intuitive interface built with Tkinter

## What I Learned

Building this project helped me understand:

- How to create GUIs with Tkinter widgets (Entry, Button, Label)
- Event binding and handling user input with `.bind()`
- String manipulation and validation logic
- Organizing code with functions for reusability
- How to update widget properties dynamically with `.config()`
- Variable scoping with the `global` keyword
- Color-coded user feedback to improve UX

## Future Improvements

- Display which specific criteria are missing in real-time
- Add visual requirement indicators (checkmarks/X marks) for each criterion
- Clear the result label when the user starts typing a new password
- Allow users to copy strong passwords to clipboard
- Add custom minimum length configuration
- Implement additional strength criteria (special characters, common password checking, etc.)
- Add a reset button to clear all fields

## Author

Built as a portfolio project while learning Python and GUI development.
