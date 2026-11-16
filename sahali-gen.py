import random

def generator():
    """ no code yet... """

def main():
    print("Welcome to the official Sahali character generator (version 0.0.1)")
    print("-------------------------------------------------------------------------------")
    print("Sahalis are members of my fictional anthropomorphic species, the Sahalians.")
    print("I have a looooot of worldbuilding done on them but none of it is public yet,")
    print("which is why this is currently completely out of context. It will make more")
    print("sense once I make the multitudes of documents on the Sahalian species available")
    print("on my page. For now I'm just making this project for myself. All you need to")
    print("know is that this is a basic generator that creates a randomized Sahalian")
    print("character, listing basic physical and personality traits with each iteration.")
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

if __name__ == "__main__":
    main()