# Password Generator (Linux) by Aniket Ahlawat

A simple Password Generator application built using Python and Tkinter. This tool allows users to create strong and secure passwords by customizing the length and character types used in the password.

## Features

- Generate random passwords with customizable length.
- Options to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Validations to ensure the password meets minimum security requirements.

## Requirements
- Git
  ```bash
  sudo dnf install git-all
  
- Python 3.x
     ```bash
     #Step 1 : preconditions
     sudo apt-get install build-essential checkinstall
     sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
      libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
     
     #Step 2: download an unpack python
     cd /usr/src
     sudo wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
     sudo tar xzf Python-3.7.2.tgz

     #Step 3 : compile
     cd Python-3.7.2
     sudo ./configure --enable-optimizations
     #use altinstall used to keep original python, if no python environment use sudo make install
     sudo make altinstall 
   
- Tkinter (usually included with Python installations)
  if not found try:
  ```bash
  pip install tkinter

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aniket-Ahlawat/Linux_Project.git
2. Navigate to the project directory:
   
    ```bash
   cd password-generator
3. Run the application:

    ```bash
   python3 password_generator.py

## Usage
1. Enter the desired password length (minimum 4 characters).
2. Select the types of characters you want to include in the password.
3. Click the "Generate Password" button to create a strong password.
4. The generated password will appear in the designated field.
