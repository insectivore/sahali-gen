import random
import sys
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

# save into a "saved_characters" folder in the same directory as this script
OUTPUT_DIR = Path(__file__).resolve().parent / "saved_characters"

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

def build_table(profile: dict[str, str | int]) -> Table:
    table = Table(title="Random Sahali Profile", show_header=False)
    table.add_column("Field", style="bold")
    table.add_column("Value")

    table.add_row("[purple4]Overview[/]", "")
    for field in ("Name", "Sex", "Age", "Sexuality", "District", "Social class"):
        table.add_row(f"[medium_purple4]{field}:[/]", str(profile[field]))

    table.add_section()
    table.add_row("[red]Appearance[/]", "")
    for field in ("Morph", "Eye color", "Stature", "Frame", "Body mass", "Unusual features"):
        table.add_row(f"[light_pink4]{field}:[/]", str(profile[field]))

    table.add_section()
    table.add_row("[orange4]Behavior[/]", "")
    for field in ("Personality", "Profession", "Likes", "Dislikes"):
        table.add_row(f"[wheat4]{field}:[/]", str(profile[field]))

    return table

def save_table(table: Table) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = OUTPUT_DIR / f"sahali_{timestamp}.txt"
    with open(filepath, "w", encoding="utf-8") as file:
        Console(file=file, width=80).print(table)
    return filepath

def run_generator() -> None:
    current_profile = generate_profile()
    current_table = build_table(current_profile)
    status = ""

    while True:
        console.clear()
        console.print(current_table)
        if status:
            console.print(status, style="dark_cyan")
        choice = console.input("enter to generate again, s to save character sheet, x to exit >> ").strip().lower()
        if choice == "x":
            break
        elif choice == "s":
            saved_path = save_table(current_table)
            status = f"Saved to: {saved_path}"
        else:
            current_profile = generate_profile()
            current_table = build_table(current_profile)
            status = ""

    sys.exit()

def main() -> None:
    print("Welcome to the official Sahali character generator (version 1.0.0)")
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