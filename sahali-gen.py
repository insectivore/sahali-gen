"""
Created by Jasper Martin (@insectivore on Github).
Gemini AI was used to aid/develop the following features:
- rich shell static position in terminal/refreshing
- text file creation and saving
- weighting data stored in .json files
- bundling this project as an .exe

!!! All other code in this project, I developed myself, or developed with aid from
studying/referencing other human-made projects !!!

My end goal as a developer is to use as little AI as possible in my creations, only
putting it to use when absolutely necessary. To be clear, I don't align myself as
staunchly "pro-AI" or "anti-AI" -- that's assigning a black-and-white perspective to
a definitively gray area, one that I don't fully comprehend yet.

I simply desire for myself to learn rather than imitate. As such, I try to use AI as
a stepping stone in my minor projects, using it to learn new programming techniques
which I can go on to implement myself in later projects rather than relying on
generative AI to keep doing the work for me.

Project begun 11/16/2026

current version: 1.1.0
"""

# witerawy impowt the heckin wesouwces
import random # for random selection
import sys # for safely, cleanly exiting the program
import json # to access my stored character data
from datetime import datetime # for assigning datetime-based names to the text files
from pathlib import Path # for handling file paths
from rich.console import Console # for the rich interface
from rich.table import Table # also for the rich interface

console = Console()

# resolve paths cleanly both in development and inside pyinstaller executable
if getattr(sys, "frozen", False):
    BUNDLE_DIR = Path(sys._MEIPASS)
    APP_DIR = Path(sys.executable).resolve().parent
else:
    BUNDLE_DIR = Path(__file__).resolve().parent
    APP_DIR = BUNDLE_DIR

# assigning paths for data & character profiles
DATA_DIR = BUNDLE_DIR / "data"
OUTPUT_DIR = APP_DIR / "saved_characters"

# function to load the json files containing the data
def load_json(filename: str, fallback_key: str = "name") -> list[dict]:
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return [{fallback_key: "WIP"}]
    return json.loads(filepath.read_text(encoding="utf-8"))

# picks weighting for future json selections --
# 1st base case returns empty dictionary if records is empty
# 2nd base case picks any record w/equal probability if no weights are provided
# get choice weighting from weight_fn function -- if no valid output, return a truly random choice
def pick_weighted(records: list[dict], weight_fn=None) -> dict:
    if not records:
        return {}
    if weight_fn is None:
        return random.choice(records)

    weights = [max(0.0, float(weight_fn(item))) for item in records]
    if sum(weights) <= 0:
        return random.choice(records)
    return random.choices(records, weights=weights, k=1)[0]

# picks an option from a dictionary given its weights
def pick_dict_choice(options: dict[str, float]) -> str:
    return random.choices(list(options.keys()), weights=list(options.values()), k=1)[0]

# load character traits from json files
SURNAMES = load_json("surnames.json", "surname")
FORENAMES = load_json("forenames.json", "forename")
DISTRICTS = load_json("districts.json", "district")
SOCIAL_CLASSES = load_json("social.json", "status")
MORPHS = load_json("morphs.json", "morph")
JOBS = load_json("jobs.json", "title")
EYES = load_json("eyes.json", "color")
UNUSUAL = load_json("unusual.json", "feature")
PERSONALITIES = load_json("personalities.json", "trait")
LIKES = load_json("likes.json", "like")
DISLIKES = load_json("dislikes.json", "dislike")

# weighted dictionary for sex
SEX_WEIGHTS = {
    "male": 48,
    "female": 48,
    "intersex": 2
}

# weighted dictionary for sexuality
SEXUALITY_WEIGHTS = {
    "heterosexual": 84,
    "homosexual": 6,
    "bisexual": 8,
    "asexual": 2
}

# weighted dictionary for social class
SOCIAL_TIER_WEIGHTS = {
    "lower-class": 64,
    "middle-class": 25,
    "higher-class": 11
}

# weighted dictionary for likelihood of job class received based on social class assigned
CLASS_TO_JOB_WEIGHTS = {
    "lower-class": {"low": 86, "middle": 14, "high": 0},
    "middle-class": {"low": 17, "middle": 81, "high": 2},
    "higher-class": {"low": 0, "middle": 10, "high": 90}
}

# weighted dictionary for morphs
MORPH_RARITY_WEIGHTS = {
    "normal": 75.00,
    "melanistic": 12.44,
    "leucistic": 12.34,
    "hypermelanistic": 0.11,
    "albino": 0.09,
    "xanthic": 0.01,
}
"""
WEALTH
--high class-----
huaha fara - capital
katqar't il gatif - religous area
qetnijalaa - markets, artisanal work
--middle class---
eli - markets, textiles, specialized farmland
ilmuzid - soldier barracks
sagir - smithy & mineral processing
ajaf qo - precious mineral mining sites (fragment of lithtorqa)
---low class-----
tif nala - farmland 
tajut - fiber processing (fragment of thejit)
dafi - farmland (fragment of eli)
thejit - farmland
lithtorqa - mining sites

LAND SIZE
lithtorqa - mining sites
tif nala - farmland 
thejit - farmland
eli - markets, textiles, specialized farmland
tajut - fiber processing (fragment of thejit)
dafi - farmland (fragment of eli)
sagir - smithy & mineral processing
qetnijalaa - markets, artisanal work
ilmuzid - soldier barracks
huaha fara - capital
ajaf qo - precious mineral mining sites (fragment of lithtorqa)
katqar't il gatif - religous area

GROSS POPULATION
tif nala - farmland 
thejit - farmland
lithtorqa - mining sites
tajut - fiber processing (fragment of thejit)
qetnijalaa - markets, artisanal work
huaha fara - capital
ilmuzid - soldier barracks
sagir - smithy & mineral processing
eli - markets, textiles, specialized farmland
dafi - farmland (fragment of eli)
katqar't il gatif - religous area
ajaf qo - precious mineral mining sites (fragment of lithtorqa)

POPULATION DENSITY
ilmuzid - soldier barracks
qetnijalaa - markets, artisanal work
huaha fara - capital
katqar't il gatif - religous area
eli - markets, textiles, specialized farmland
tajut - fiber processing (fragment of thejit)
tif nala - farmland
sagir - smithy & mineral processing
lithtorqa - mining sites
thejit - farmland
dafi - farmland (fragment of eli)
ajaf qo - precious mineral mining sites (fragment of lithtorqa)
"""

DISTRICT_MODIFIERS: dict[str, dict] = {
    "ajaf qo": {
        "class_weights": {"lower-class": 30, "middle-class": 40, "higher-class": 30},
        "morph_bases": {"red": 23, "brown": 20.99, "gray": 30, "purple": 26, "yellow": 0.01},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "dāfi": {
        "class_weights": {"lower-class": 85, "middle-class": 10, "higher-class": 5},
        "morph_bases": {"red": 19, "brown": 74.99999, "gray": 4, "purple": 2, "yellow": 0.00001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "eli": {
        "class_weights": {"lower-class": 18, "middle-class": 58, "higher-class": 24},
        "morph_bases": {"red": 28, "brown": 25, "gray": 27, "purple": 19.9999, "yellow": 0.0001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "huāhā fārā": {
        "class_weights": {"lower-class": 20, "middle-class": 40, "higher-class": 40},
        "morph_bases": {"red": 30.9, "brown": 24, "gray": 18, "purple": 27, "yellow": 0.1},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "īlmuzīd": {
        "class_weights": {"lower-class": 40, "middle-class": 40, "higher-class": 20},
        "morph_bases": {"red": 36, "brown": 21, "gray": 30, "purple": 12.999, "yellow": 0.001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "kātqār't īl gātīf": {
        "class_weights": {"lower-class": 10, "middle-class": 50, "higher-class": 40},
        "morph_bases": {"red": 33.999, "brown": 7, "gray": 20, "purple": 39, "yellow": 0.001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "līthtorqa": {
        "class_weights": {"lower-class": 90, "middle-class": 9, "higher-class": 1},
        "morph_bases": {"red": 7.99999, "brown": 10, "gray": 80, "purple": 2, "yellow": 0.00001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "qetnījālāā": {
        "class_weights": {"lower-class": 18, "middle-class": 52, "higher-class": 30},
        "morph_bases": {"red": 29, "brown": 20.9, "gray": 25, "purple": 25, "yellow": 0.1},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "sagir": {
        "class_weights": {"lower-class": 35, "middle-class": 50, "higher-class": 15},
        "morph_bases": {"red": 23, "brown": 20, "gray": 40, "purple": 16.999, "yellow": 0.001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "tājut": {
        "class_weights": {"lower-class": 75, "middle-class": 21, "higher-class": 3},
        "morph_bases": {"red": 17, "brown": 75, "gray": 6, "purple": 1.99999, "yellow": 0.00001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "thejīt": {
        "class_weights": {"lower-class": 86, "middle-class": 12, "higher-class": 2},
        "morph_bases": {"red": 17, "brown": 75, "gray": 6, "purple": 1.99999, "yellow": 0.00001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
    "tīf nalā": {
        "class_weights": {"lower-class": 70, "middle-class": 25, "higher-class": 5},
        "morph_bases": {"red": 17, "brown": 75, "gray": 6, "purple": 1.99999, "yellow": 0.00001},
        "stature": {"quite short": 1, "short": 2, "on the shorter side": 3, "average": 4, "on the taller side": 2, "tall": 1, "quite tall": 1}
    },
}

DEFAULT_STATURE = {
    "quite short": 5, "short": 12, "on the shorter side": 18,
    "average": 30, "on the taller side": 18, "tall": 12, "quite tall": 5,
}

DEFAULT_MASS = {
    "slim": 10, "athletic": 12, "curvy": 10, "muscular": 10, "beefy": 8,
    "chubby": 10, "typical": 18, "fat": 8, "obese": 4, "skinny": 10,
}

FRAME_WEIGHTS = {"ectomorphic": 30, "mesomorphic": 40, "endomorphic": 30}

# function to choose forename based on sex
def choose_forename(sex: str) -> str:
    # nested function weight_fn that returns a weighting for another choice based on assigned sex
    def weight_fn(entry: dict) -> float:
        gender = entry.get("gender", "neuter")
        if sex == "intersex":
            return 10 if gender == "neuter" else 5
        if gender == sex:
            return 10
        if gender == "neuter":
            return 4
        return 0
    chosen = pick_weighted(FORENAMES, weight_fn)

    # 25% chance to use a variant name spelling, if one exists
    if chosen.get("variant") and random.random() < 0.25:
        return f"{chosen['variant']} ('{chosen['meaning']}')"
    if chosen.get("meaning"):
        return f"{chosen['forename']} ('{chosen['meaning']}')"
    return chosen.get("forename", "WIP")

def choose_profession(age: int, social: dict, sex: str) -> str:
    if age < 5:
        return "none (young child)"
    if age < 12:
        return "apprentice / student"
    if age >= 80 and random.random() < 0.65:
        return "retired"

    abs_class = social.get("absolute", "middle-class")
    class_weights = CLASS_TO_JOB_WEIGHTS.get(abs_class, {"low": 5, "middle": 5, "high": 5})

    def weight_fn(job: dict) -> float:
        w = class_weights.get(job.get("class", "middle"), 1)
        # Example age/sex modifiers:
        if age < 18 and job.get("type") in ("authority", "religious"):
            w *= 0.1
        if sex == "female" and job.get("title") == "soldier":
            w *= 0.5  # adjust or remove to match your canon
        return w

    chosen = pick_weighted(JOBS, weight_fn)
    return chosen.get("title", "WIP")

def choose_morph(district_name: str) -> str:
    mods = DISTRICT_MODIFIERS.get(district_name, {})
    base_weights = mods.get("morph_bases", {})
    def weight_fn(m: dict) -> float:
        rarity = MORPH_RARITY_WEIGHTS.get(m.get("type", "normal"), 5.0)
        regional = base_weights.get(m.get("base", ""), 1.0)
        return rarity * regional
    chosen = pick_weighted(MORPHS, weight_fn)
    return f"{chosen['morph']} ({chosen['type']} {chosen['base']})"

def choose_unusual(age: int, profession: str, none_chance: float = 0.60) -> str:
    actual_features = [u for u in UNUSUAL if u.get("feature") != "none"]
    if not actual_features or random.random() < none_chance:
        return "none"

    def weight_fn(entry: dict) -> float:
        w = 1.0
        # Optional: weight specific features by age or profession
        if entry.get("feature") == "scarred-over" and profession in ("soldier", "guard", "miner"):
            w *= 2.5
        if age < 12 and entry.get("feature") in ("scarred-over", "worn-down", "broken"):
            w *= 0.2
        return w

    chosen = pick_weighted(actual_features, weight_fn)
    feature = chosen.get("feature", "WIP")
    part = chosen.get("part", "")
    if not part or part == "none":
        return feature
    return f"{feature} {part}"

def generate_profile() -> dict[str, str | int]:
    # age, sex, sexuality
    age = random.randint(1, 100)
    sex = pick_dict_choice(SEX_WEIGHTS)
    sexuality = pick_dict_choice(SEXUALITY_WEIGHTS)

    # social class -> district
    social = pick_weighted(
        SOCIAL_CLASSES,
        lambda s: SOCIAL_TIER_WEIGHTS.get(s.get("absolute", "middle-class"), 10),
    )
    abs_class = social.get("absolute", "middle-class")

    district_rec = pick_weighted(
        DISTRICTS,
        lambda d: DISTRICT_MODIFIERS.get(d["district"], {}).get("class_weights", {}).get(abs_class, 3),
    )
    district = district_rec.get("district", "WIP")

    # names
    surname_rec = pick_weighted(SURNAMES)
    surname = (
        f"{surname_rec['surname']} ('{surname_rec['meaning']}')"
        if surname_rec.get("meaning")
        else surname_rec.get("surname", "WIP")
    )
    forename = choose_forename(sex)

    # profession (age, social class, and sex affect job)
    profession = choose_profession(age, social, sex)

    # appearance (district & age affect morph, stature, and body mass)
    morph = choose_morph(district)
    eyes = pick_weighted(EYES).get("color", "WIP")

    district_stature = DISTRICT_MODIFIERS.get(district, {}).get("stature", DEFAULT_STATURE)
    stature = "small (child)" if age < 12 else pick_dict_choice(district_stature)

    mass_weights = dict(DEFAULT_MASS)
    if abs_class == "lower-class":
        mass_weights["skinny"] *= 2
        mass_weights["obese"] *= 0.2
    elif abs_class == "higher-class":
        mass_weights["chubby"] *= 1.8
        mass_weights["skinny"] *= 0.4
    body_mass = pick_dict_choice(mass_weights)
    frame = pick_dict_choice(FRAME_WEIGHTS)

    unusual = choose_unusual(age, profession)

    # behavior
    personality = pick_weighted(PERSONALITIES).get("trait", "WIP")
    likes = pick_weighted(LIKES).get("like", "WIP")
    dislikes = pick_weighted(DISLIKES).get("dislike", "WIP")

    return {
        "Surname": surname,
        "Forename": forename,
        "Sex": sex,
        "Age": age,
        "Sexuality": sexuality,
        "District": district,
        "Social class": f"{social['status']} ({social['absolute']})",
        "Morph": morph,
        "Eyes": eyes,
        "Stature": stature,
        "Frame": frame,
        "Body mass": body_mass,
        "Unusual features": unusual,
        "Personality": personality,
        "Profession": profession,
        "Likes": likes,
        "Dislikes": dislikes,
    }

def build_table(profile: dict[str, str | int]) -> Table:
    table = Table(title="Random Sahali Profile", show_header=False)
    table.add_column("Field", style="bold")
    table.add_column("Value")

    table.add_row("[purple4]Overview[/]", "")
    for field in ("Surname", "Forename", "Sex", "Age", "Sexuality", "District", "Social class"):
        table.add_row(f"[medium_purple4]{field}:[/]", str(profile[field]))

    table.add_section()
    table.add_row("[red]Appearance[/]", "")
    for field in ("Morph", "Eyes", "Stature", "Frame", "Body mass", "Unusual features"):
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
    print("Welcome to the official Sahali character generator (version 1.1.0)")
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