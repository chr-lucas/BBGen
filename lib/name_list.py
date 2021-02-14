# import os
import random

# dir_path = os.path.dirname(os.path.realpath(__file__))
# DATA_DIR = f"{dir_path}/../data/SpeciesNames"

DATA_DIR = "data/Olaxis/SpeciesNames"


class NameGen:
    def driftling_name(self):
        name_list = []
        with open(f"{DATA_DIR}/Driftling/DriftlingNames.txt") as file:
            # with open(f"{DATA}Driftling/DriftlingNames.txt") as file:
            for line in file:
                name = line.strip()
                name_list.append(line.strip())
        name = random.choice(name_list).capitalize()
        return f"Your name is {name}."

    def glean_name(self):
        name_list = []
        reliquary_list = []
        with open(f"{DATA_DIR}/Glean/GleanFirst.txt") as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        with open(f"{DATA_DIR}/Glean/GleanReliquary.txt") as file:
            for line in file:
                reliquary = line.strip()
                reliquary_list.append(reliquary)
        name = random.choice(name_list).capitalize() + " " + random.choice(reliquary_list).capitalize()
        return f"Your name is {name}."

    def ino_name(self):
        given_list = []
        star_list = []
        pack_list = []
        house_list = []
        with open(f"{DATA_DIR}/Ino/InoGiven.txt") as file:
            for line in file:
                given = line.strip()
                given_list.append(given)
        with open(f"{DATA_DIR}/Ino/InoStar.txt") as file:
            for line in file:
                star = line.strip()
                star_list.append(star)
        with open(f"{DATA_DIR}/Ino/InoPack.txt") as file:
            for line in file:
                pack = line.strip()
                pack_list.append(pack)
        with open(f"{DATA_DIR}/Ino/InoHouse.txt") as file:
            for line in file:
                house = line.strip()
                house_list.append(house)
        given_name = random.choice(given_list).capitalize()
        house_name = random.choice(house_list).capitalize()
        name = "{star}{given_father}{given_mother}{pack1}{house}{given}{pack2}".format(
            star=random.choice(star_list).capitalize(),
            given_father=random.choice(given_list).capitalize(),
            given_mother=random.choice(given_list).capitalize(),
            pack1=random.choice(pack_list).capitalize(),
            house=house_name,
            given=given_name,
            pack2=random.choice(pack_list).capitalize(),
        )
        nickname = f"{house_name}{given_name}"
        return f"Your name is {name}.\nInformally, you go by {nickname}."

    def kithuk_name(self):
        name_list = []
        with open(f"{DATA_DIR}/Kithuk/KithukNames.txt") as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        name = "{first} {parent1}{parent2}".format(
            first=random.choice(name_list).capitalize(),
            parent1=random.choice(name_list).capitalize(),
            parent2=random.choice(name_list),
        )
        return f"Your name is {name}."

    def peacecraft_name(self):
        adj_list = []
        noun_list = []
        with open(f"{DATA_DIR}/Peacecraft/PeacecraftAdj.txt") as file:
            for line in file:
                adj = line.strip()
                adj_list.append(adj)
        with open(f"{DATA_DIR}/Peacecraft/PeacecraftNoun.txt") as file:
            for line in file:
                noun = line.strip()
                noun_list.append(noun)
        name = random.choice(adj_list).capitalize() + " " + random.choice(noun_list).capitalize()
        return f"Your name is {name}."

    def rornan_name(self):
        name_list = []
        connector_list = ["", "", "", "", "'", "'", "-"]
        with open(f"{DATA_DIR}/Rornan/RornanNames.txt") as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        name = random.choice(name_list).capitalize() + random.choice(connector_list) + random.choice(name_list)
        return f"Your name is {name}."

    def ulran_name(self):
        start_list = []
        end_list = []
        last_list = []
        with open(f"{DATA_DIR}/Ulran/UlranStart.txt") as file:
            for line in file:
                start = line.strip()
                start_list.append(start)
        with open(f"{DATA_DIR}/Ulran/UlranEnd.txt") as file:
            for line in file:
                end = line.strip()
                end_list.append(end)
        with open(f"{DATA_DIR}/Ulran/UlranLast.txt") as file:
            for line in file:
                last = line.strip()
                last_list.append(last)
        name = "{fstart}{fend} {lstart}{lpart1}{lpart2}{lpart3}".format(
            fstart=random.choice(start_list).capitalize(),
            fend=random.choice(end_list),
            lstart=random.choice(start_list).capitalize(),
            lpart1=random.choice(last_list),
            lpart2=random.choice(last_list),
            lpart3=random.choice(last_list),
        )
        return f"Your name is {name}."

    def zivoy_name(self):
        first_list = []
        last_list = []
        with open(f"{DATA_DIR}/Zivoy/ZivoyFirst.txt") as file:
            for line in file:
                first = line.strip()
                first_list.append(first)
        with open(f"{DATA_DIR}/Zivoy/ZivoyLast.txt") as file:
            for line in file:
                last = line.strip()
                last_list.append(last)
        name = f"{random.choice(first_list).capitalize()} {random.choice(last_list).capitalize()}"
        return f"Your name is {name}."
