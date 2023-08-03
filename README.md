# Simple Password Manager

Simple Password Manager is a Python-based graphical user interface (GUI) application built using tkinter. It serves as a secure and easy-to-use password manager that allows users to generate strong passwords and store website login details in a JSON file.

## Features

### Password Generation

The application provides a "Generate Password" button that creates strong and random passwords for you. The passwords are a combination of letters (both uppercase and lowercase), numbers, and symbols. The password length is automatically set to be between 8 and 10 characters for letters, and between 2 and 4 characters for symbols and numbers. This ensures that the passwords generated are highly secure.

### Password Storage in JSON

The application uses a JSON file named "data.json" to store the website login details. When you add a new website, the application will store the website, email, and password details in JSON format. The data is organized as a dictionary with the website as the key and the associated email and password as its values. This allows for easy retrieval and updating of the stored information.

### Search Feature

You can search for a saved password by entering the website name and clicking the "Search" button. If the website name is found in the data, the application will display the corresponding username and password in a message box, allowing you to easily retrieve your login details.

### Password Visibility

To ensure the privacy and security of your passwords, the password field displays asterisks ('*') instead of showing the actual characters. This prevents others from seeing your passwords while you enter them.

### Persistent Data

The application saves your data even after you close the program. When you reopen the password manager, you will find all your previously saved website login details intact. This way, you can conveniently access and manage your passwords without worrying about losing them.

### Default Values
The application provides default email address for your convenience which can be edited if required.

### Clipboard Support

The application uses the `pyperclip` library to copy the generated password to the clipboard. This makes it easy for you to paste the generated password into password fields when signing up or logging into websites or applications.

### Error Handling

The password manager includes error handling for various scenarios, such as when the "data.json" file is not found, or when the file contains invalid JSON data. This ensures that the application remains stable and user-friendly even in unexpected situations.

## How to Use

1. Run the Python script to launch the password manager application.
2. Use the "Generate Password" button to create strong and secure passwords.
3. Enter the website name, email/username, and password in the corresponding fields.
4. Click the "Add" button to save the website login details in the "data.json" file.
5. To find a password, enter the website name and click the "Search" button.
6. The password manager will display the username and password associated with the website.

PS: Ensure that you keep the "data.json" file secure since it contains your password information.
