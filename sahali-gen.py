import random
import sys
from rich.console import Console, Group
from rich.text import Text
from rich.live import Live
from rich.table import Table
console = Console()

# trait lists
NAME = ["WIP"]
SEX = ["male", "female", "intersex"]
SEXUALITY = ["heterosexual", "homosexual", "bisexual", "asexual"]
DISTRICT = ["WIP"]
SOCIAL = ["lower lower-class", "middle lower-class", "upper lower-class", "lower middle-class", "middle middle-class", "upper middle-class", "lower higher-class", "middle higher-class", "higher higher-class"]
MORPH = ["WIP"]
EYES = ["WIP"]
STATURE = ["quite short", "short", "on the shorter side", "average", "on the taller side", "tall", "quite tall"]
FRAME = ["ectomorphic", "mesomorphic", "endomorphic"]
MASS = ["slim", "athletic", "curvy", "muscular", "beefy", "chubby", "typical", "fat", "obese", "skinny"]
UNUSUAL = ["WIP"]
PERSONALITY = ["WIP"]
JOB = ["WIP"]
LIKES = ["WIP"]
DISLIKES = ["WIP"]

def generate_profile() -> dict[str, str | int]:
    return {
        "Name": random.choice(NAME),
        "Sex": random.choice(SEX),
        "Age": random.randint(1, 100),
        "Sexuality": random.choice(SEXUALITY),
        "District": random.choice(DISTRICT),
        "Social class": random.choice(SOCIAL),
        "Morph": random.choice(MORPH),
        "Eye color": random.choice(EYES),
        "Stature": random.choice(STATURE),
        "Frame": random.choice(FRAME),
        "Body mass": random.choice(MASS),
        "Unusual features": random.choice(UNUSUAL),
        "Personality": random.choice(PERSONALITY),
        "Profession": random.choice(JOB),
        "Likes": random.choice(LIKES),
        "Dislikes": random.choice(DISLIKES),
    }

def generator() -> Table:
    table = Table(title="Random Sahali Profile", show_header=False)
    table.add_column("Field", style="bold")
    table.add_column("Value")
    name = random.choice(NAME)
    sex = random.choice(SEX)
    age = random.randint(1, 100)
    sexuality = random.choice(SEXUALITY)
    district = random.choice(DISTRICT)
    social = random.choice(SOCIAL)
    morph = random.choice(MORPH)
    eyes = random.choice(EYES)
    stature = random.choice(STATURE)
    frame = random.choice(FRAME)
    mass = random.choice(MASS)
    unusual = random.choice(UNUSUAL)
    personality = random.choice(PERSONALITY)
    job = random.choice(JOB)
    likes = random.choice(LIKES)
    dislikes = random.choice(DISLIKES)
    char_profile = [name, sex, age, sexuality, district, social, morph, eyes, stature, frame, mass, unusual, personality, job, likes, dislikes]

    table.add_row("[purple4]Overview[/]", "")
    table.add_row("[medium_purple4]Name:[/]", name)
    table.add_row("[medium_purple4]Sex:[/]", sex)
    table.add_row("[medium_purple4]Age:[/]", str(age))
    table.add_row("[medium_purple4]Sexuality:[/]", sexuality)
    table.add_row("[medium_purple4]District:[/]", district)
    table.add_row("[medium_purple4]Social class:[/]", social)

    table.add_section()
    table.add_row("[red]Appearance[/]", "")
    table.add_row("[light_pink4]Morph:[/]", morph)
    table.add_row("[light_pink4]Eye color:[/]", eyes)
    table.add_row("[light_pink4]Stature:[/]", stature)
    table.add_row("[light_pink4]Frame:[/]", frame)
    table.add_row("[light_pink4]Body mass:[/]", mass)
    table.add_row("[light_pink4]Unusual features:[/]", unusual)

    table.add_section()
    table.add_row("[orange4]Behavior[/]", "")
    table.add_row("[wheat4]Personality:[/]", personality)
    table.add_row("[wheat4]Profession:[/]", job)
    table.add_row("[wheat4]Likes:[/]", likes)
    table.add_row("[wheat4]Dislikes:[/]", dislikes)
    return table

def get_data():
    """ unsure """

def save_profile(char_profile, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for item in char_profile:
            file.write(f"{item}\n")

def build_view() -> Group:
    return Group(
        generator(),
        Text("enter to generate again, s to save character sheet, x to exit >> "),
    )

def run_generator() -> None:
    with Live(build_view(), console=console, auto_refresh=False, screen=True) as live:
        while True:
            choice = input("").strip().lower()
            if choice == "x":
                break
            elif choice == "s":
                char_data = get_data()
                save_profile(char_data, "random_char.txt")
            live.update(build_view(), refresh=True)
    sys.exit()

def main() -> None:
    print("Welcome to the official Sahali character generator (version 0.0.2)")
    print("-------------------------------------------------------------------------------")
    print("Sahalis are members of my fictional anthropomorphic species, the Sahalians.")
    print("I have a looooot of worldbuilding done on them but none of it is public yet,")
    print("which is why this is currently completely out of context. It will make more")
    print("sense once I make the docs on the Sahalian species available on my page.")
    print("")
    print(">> enter ---------------------------------------------------- generate a Sahali")
    print(">> x --------------------------------------------------------------------- exit")
    print("")

    while True:
        choice = input(">> ").strip().lower()
        if choice == "x":
            sys.exit()
        run_generator()

if __name__ == "__main__":
    main()