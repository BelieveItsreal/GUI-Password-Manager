# GUI-Password-Manager
 this program provides a simple password manager interface where users can generate secure passwords, store website credentials, and retrieve them when needed. Note that the code includes file paths specific to the author's system and will need to be modified accordingly to work on different systems.

1)
Password Generation: The program includes a function generate_password() that generates a random password consisting of 8 letters, 4 symbols, and 2 numbers. The generated password is then displayed in the password entry field.

2)
Saving Passwords: The program allows users to enter details such as the website, email/username, and password. When the "Add" button is clicked, the function save_to_csv() is executed. It checks if the website and password fields are not empty. If they are not empty, it prompts the user to confirm saving the details. The entered data is then stored in a JSON file named "password_data.json" (located at the specified file path) as a dictionary with the website as the key and the corresponding email and password as values. If the JSON file does not exist, a new file is created.

3)
Finding Passwords: The program includes a function find_password() that retrieves the saved email and password for a given website. When the "Search" button is clicked, it reads the data from the JSON file and checks if the entered website exists in the data. If the website is found, it displays a message box with the email and password for that website. If the website is not found, it displays an error message.

4)
User Interface Setup: The program creates a graphical user interface window using the Tkinter library. It includes labels for website, email, and password fields, as well as corresponding entry fields for user input. The window also includes buttons for generating passwords, adding details, and searching for passwords. Additionally, a logo image is displayed using the Tkinter canvas.
