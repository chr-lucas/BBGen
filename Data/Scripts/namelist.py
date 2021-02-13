import random
# import os
# import sys

# os.chdir(sys.path[0])

class NameGen:

    def driftling_name(self):
        name_list = []
        with open(r'Data\SpeciesNames\Driftling\DriftlingNames.txt') as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        name = random.choice(name_list).capitalize()
        return (f'Your name is {name}.')


    def glean_name(self):
        name_list = []
        reliquary_list = []
        with open(r'Data\SpeciesNames\Glean\GleanFirst.txt') as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        with open(r'Data\SpeciesNames\Glean\GleanReliquary.txt') as file:
            for line in file:
                reliquary = line.strip()
                reliquary_list.append(reliquary)
        name = random.choice(name_list).capitalize() + " " + random.choice(reliquary_list).capitalize()
        return (f'Your name is {name}.')


    def ino_name(self):
        given_list = []
        star_list = []
        pack_list = []
        house_list = []
        with open(r'Data\SpeciesNames\Ino\InoGiven.txt') as file:
            for line in file:
                given = line.strip()
                given_list.append(given)
        with open(r'Data\SpeciesNames\Ino\InoStar.txt') as file:
            for line in file:
                star = line.strip()
                star_list.append(star)
        with open(r'Data\SpeciesNames\Ino\InoPack.txt') as file:
            for line in file:
                pack = line.strip()
                pack_list.append(pack)
        with open(r'Data\SpeciesNames\Ino\InoHouse.txt') as file:
            for line in file:
                house = line.strip()
                house_list.append(house)
        given_name = random.choice(given_list).capitalize()
        house_name = random.choice(house_list).capitalize()
        name = (f'{random.choice(star_list).capitalize()}{random.choice(given_list).capitalize()}{random.choice(given_list).capitalize()}{random.choice(pack_list).capitalize()}{house_name}{given_name}{random.choice(pack_list).capitalize()}')
        nickname = (f'{house_name}{given_name}')
        return (f'Your name is {name}.\nInformally, you go by {nickname}.')


    def kithuk_name(self):
        name_list = []
        with open(r'Data\SpeciesNames\Kithuk\KithukNames.txt') as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        name = (f'{random.choice(name_list).capitalize()} {random.choice(name_list).capitalize()}{random.choice(name_list)}')
        return (f'Your name is {name}.')


    def peacecraft_name(self):
        adj_list = []
        noun_list = []
        with open(r'Data\SpeciesNames\Peacecraft\PeacecraftAdj.txt') as file:
            for line in file:
                adj = line.strip()
                adj_list.append(adj)
        with open(r'Data\SpeciesNames\Peacecraft\PeacecraftNoun.txt') as file:
            for line in file:
                noun = line.strip()
                noun_list.append(noun)
        name = random.choice(adj_list).capitalize() + ' ' + random.choice(noun_list).capitalize()
        return (f'Your name is {name}.')


    def rornan_name(self):
        name_list = []
        connector_list = ["", "", "", "", "'", "'", "-"]
        with open(r'Data\SpeciesNames\Rornan\RornanNames.txt') as file:
            for line in file:
                name = line.strip()
                name_list.append(name)
        name = random.choice(name_list).capitalize() + random.choice(connector_list) + random.choice(name_list)
        return (f'Your name is {name}.')


    def ulran_name(self):
        start_list = []
        end_list = []
        last_list = []
        with open(r'Data\SpeciesNames\Ulran\UlranStart.txt') as file:
            for line in file:
                start = line.strip()
                start_list.append(start)
        with open(r'Data\SpeciesNames\Ulran\UlranEnd.txt') as file:
            for line in file:
                end = line.strip()
                end_list.append(end)
        with open(r'Data\SpeciesNames\Ulran\UlranLast.txt') as file:
            for line in file:
                last = line.strip()
                last_list.append(last)
        name = f'{random.choice(start_list).capitalize()}{random.choice(end_list)} {random.choice(start_list).capitalize()}{random.choice(last_list)}{random.choice(last_list)}{random.choice(last_list)}'
        return (f'Your name is {name}.')


    def zivoy_name(self):
        first_list = []
        last_list = []
        with open(r'Data\SpeciesNames\Zivoy\ZivoyFirst.txt') as file:
            for line in file:
                first = line.strip()
                first_list.append(first)
        with open(r'Data\SpeciesNames\Zivoy\ZivoyLast.txt') as file:
            for line in file:
                last = line.strip()
                last_list.append(last)
        name = f'{random.choice(first_list).capitalize()} {random.choice(last_list).capitalize()}'
        return (f'Your name is {name}.')