import random

def generator():
    print("--overview---------------------------------------------------------------------")
    print("Name:             ", name)
    print("Sex:              ", sex)
    print("Age:              ", age)
    print("Sexuality:        ", sexuality)
    print("District:         ", district)
    print("Social class:     ", social)
    print("--appearance-------------------------------------------------------------------")
    print("Morph:            ", morph)
    print("Eye color:        ", eye_color)
    print("Stature:          ", stature)
    print("Frame:            ", frame)
    print("Body mass:        ", body_mass)
    print("Unusual features: ", unusual)
    print("--behavior---------------------------------------------------------------------")
    print("Personality:      ", personality)
    print("Profession:       ", job)
    print("Likes:            ", likes)
    print("Dislikes:         ", dislikes)
    print("")
    while True:
        choice = input(">> ").strip().lower()
        if choice == "n":
            generator()
        elif choice == "m":
            menu()
        elif choice == "x":
            print("Goodbye!")
            break
        else:
            print("Not a recognized command.")

def menu():
    print("Welcome to the official Sahali character generator (version 0.0.2)")
    print("-------------------------------------------------------------------------------")
    print("Sahalis are members of my fictional anthropomorphic species, the Sahalians.")
    print("I have a looooot of worldbuilding done on them but none of it is public yet,")
    print("which is why this is currently completely out of context. It will make more")
    print("sense once I make the docs on the Sahalian species available on my page.")
    print("")
    print(">> g -------------------------------------------------------- generate a Sahali")
    print(">> x --------------------------------------------------------------------- exit")
    print("")

    while True:
        choice = input(">> ").strip().lower()
        if choice == "g":
            generator()
        elif choice == "x":
            print("Goodbye!")
            break
        else:
            print("Not a recognized command.")

def main():
    menu()

if __name__ == "__main__":
    main()