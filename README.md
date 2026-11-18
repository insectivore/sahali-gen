# sahali-gen

Hi! I'm insectivore, and this is a small project that fits into my larger hobby of worldbuilding & character creation.

**Sahalis** are members of my fictional anthropomorphic species, the Sahalians. I have a looooot of worldbuilding done
on them but none of it is public yet, which is why this is currently completely out of context. It will make more sense 
once I make the multitudes of documents on the Sahalian species available on my page. For now I'm just making this
project for myself. All you need to know is that this is a basic generator that creates a randomized Sahalian character,
listing basic physical and personality traits with each new generation.

## latest updates

I'm pleased to announce that **sahali-gen** is fully functional and now in alpha - **version 1.1.0**!

**new features**
- This game is now bundled -- it can be run as an executable on Windows or a Debian/Ubuntu-based Linux distro!
- If you generate a profile you really like, you now have the option to save it as a text file!
- Separate first and last names have been introduced, as well as weighting to certain options for realism

**upcoming**
- Generated text file names will contain the first & last name of the character profile saved to it.
- Improvements on weighting, accuracy & worldbuilding within generations

## requirements & how to run:

### Windows

**the executable**
- requirements: none

- click on "releases" and navigate to the latest release
- scroll down to the "assets" dropdown
- click on the file "sahali-gen.exe" to install it
- open file explorer and double-click the file to run it in the terminal

**the raw .py file**
- requirements: Python interpreter, rich

- download the latest python.exe from the official Python website
- command to install rich: ```pip install rich```
- download sahali-gen.py and the data folder from the repo page
- cd into the directory you downloaded them to (eg: ```cd Downloads```)
- command to run the program: ```python sahali-gen.py```

### Linux (Debian/Ubuntu-based)

**the executable**
- requirements: none

- click on "releases" and navigate to the latest release
- scroll down to the "assets" dropdown
- click on the file "sahali-gen-linux" to install it
- cd into the directory you downloaded it to (eg: ```cd Downloads```)
- command to grant file permission to run: ```chmod +x "sahali-gen-linux"```
- command to run the program: ```./"sahali-gen-linux"```

**the raw .py file**
- requirements: Python3, pip, venv, rich

- command to install python3, pip and venv: ```sudo apt install python3 python3-pip python3-venv -y```
- download sahali-gen.py and the data folder from the repo page
- put these files in a new subdirectory only for the game (eg: "sahaligame")
- cd into this new directory (eg: ```cd Downloads/sahaligame```)
- command to create virtual environment: ```python3 -m venv venv```
- command to activate virtual environment: ```source venv/bin/activate```
- command to install rich: ```pip install rich```
- command to run the program: ```python sahali-gen.py```

## gameplay

Upon startup, you're greeted by a menu with a quick explanation. Hit the enter key to begin the game, or enter "x"
to exit the program. Once you begin the game, a table appears with randomized traits. You can hit enter as many times
as you'd like to re-roll the traits. If you've taken a liking to a particular generation, you can enter "s" to save it
as a minimal text file. When this action is taken, a folder called saved_characters is created in the same directory as 
the game, and the text file is generated in that folder.