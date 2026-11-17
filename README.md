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
- This game can now be run as an .exe for ease of use!
- If you generate a profile you really like, you now have the option to save it as a text file!
- Separate first and last names have been introduced, as well as weighting to certain options for realism

**upcoming**
- Generated text file names will contain the first & last name of the character profile saved to it.
- Improvements on weighting, accuracy & worldbuilding within generations

## requirements:

- platform: a functional computer
- software: none (if running .exe), Python interpreter & rich library (if running raw .py file)

## how to run:

### the executable

- click on "releases" and navigate to the latest release
- click on the file "sahali-gen.exe" to install it
- double-click the file to run it in the terminal

### the raw python file

- install rich in for your terminal if you don't have it already: ```pip install rich```
- download the game files from the repo page
- cd into the directory you downloaded them to (eg: ```cd Downloads```)
- run the following command: ```python sahali-gen.py```

## gameplay

Upon startup, you're greeted by a menu with a quick explanation. Hit the enter key to begin the game, or enter "x"
to exit the program. Once you begin the game, a table appears with randomized traits. You can hit enter as many times
as you'd like to re-roll the traits. If you've taken a liking to a particular generation, you can enter "s" to save it
as a minimal text file. When this action is taken, a folder called saved_characters is created in the same directory as 
the game, and the text file is generated in that folder.