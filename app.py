from flask import Flask, render_template, request
import random #, time, decimal
# from decimal import Decimal

app = Flask(__name__)


@app.route('/')
def homepage():

    return render_template('homepage.html')

@app.route('/game', methods=['GET', 'POST'])
def game():

    global game

    if request.method == 'POST':
        if request.form.get('game_start', False) == 'Rock and Stone!':

            game = Game()
            update_equipment('dwarf1')
            update_equipment('dwarf2')
            update_equipment('dwarf3')
            update_stats('dwarf1')
            update_stats('dwarf2')
            update_stats('dwarf3')
            game.item_dict = {"Leather Cap": item_1, "Leather Shoulderpads": item_2, "Leather Jacket": item_3, "Leather Pants": item_4, "Leather Gloves": item_5, "Leather Boots": item_6,
                              "Rusty Helmet": item_7, "Rusty Pauldrons": item_8, "Rusty Chainmail": item_9, "Rusty Tasset": item_10, "Rusty Gauntlets": item_11, "Rusty Greaves": item_12,
                              "Tattered Hood": item_13, "Tattered Epaulettes": item_14, "Tattered Robe": item_15, "Tattered Pants": item_16, "Tattered Gloves": item_17, "Tattered Shoes": item_18,
                              "Leather Whip": item_19, "Bronze Broadsword": item_20, "Oak Staff": item_21,

                              "Hardleather Helmet": item_22, "Hardleather Shoulderpads": item_23, "Hardleather Chestplate": item_24, "Hardleather Pants": item_25, "Hardleather Gloves": item_26, "Hardleather Boots": item_27}
            game.backpack = []


        #   TRAIN
        #   Deadmines: Become superhuman
        #
        #   HTML form, string  ->  game.hero[dwarf].<stats>
        #
        #   Takes an input from the HTML form, adds stats from the input into the dwarf at the cost of days.
        #   If the training is too costly (ie. not enough days left), nothing will happen. Flash error message for this case is to be implemented in the future.

        elif request.form.get('train dwarf1', False) == 'Train':

            strength = int(request.form.get("str_increase"))
            intelligence = int(request.form.get("int_increase"))
            agility = int(request.form.get("agi_increase"))
            willpower = int(request.form.get("will_increase"))
            endurance = int(request.form.get("end_increase"))
            charisma = int(request.form.get("char_increase"))
            luck = int(request.form.get("lck_increase"))
            speed = int(request.form.get("spd_increase"))
            temp_days = strength*2 + intelligence*2 + agility + willpower + endurance*2 + charisma + luck + speed*2

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            game.hero['dwarf1'].strength += strength
            game.hero['dwarf1'].intelligence += intelligence
            game.hero['dwarf1'].agility += agility
            game.hero['dwarf1'].willpower += willpower
            game.hero['dwarf1'].endurance += endurance
            game.hero['dwarf1'].charisma += charisma
            game.hero['dwarf1'].luck += luck
            game.hero['dwarf1'].speed += speed

            update_stats('dwarf1')

            game.days -= temp_days

        elif request.form.get('train dwarf2', False) == 'Train':

            strength = int(request.form.get("str_increase"))
            intelligence = int(request.form.get("int_increase"))
            agility = int(request.form.get("agi_increase"))
            willpower = int(request.form.get("will_increase"))
            endurance = int(request.form.get("end_increase"))
            charisma = int(request.form.get("char_increase"))
            luck = int(request.form.get("lck_increase"))
            speed = int(request.form.get("spd_increase"))
            temp_days = strength*2 + intelligence*2 + agility + willpower + endurance*2 + charisma + luck + speed*2

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            game.hero['dwarf2'].strength += strength
            game.hero['dwarf2'].intelligence += intelligence
            game.hero['dwarf2'].agility += agility
            game.hero['dwarf2'].willpower += willpower
            game.hero['dwarf2'].endurance += endurance
            game.hero['dwarf2'].charisma += charisma
            game.hero['dwarf2'].luck += luck
            game.hero['dwarf2'].speed += speed

            update_stats('dwarf2')

            game.days -= temp_days

        elif request.form.get('train dwarf3', False) == 'Train':

            strength = int(request.form.get("str_increase"))
            intelligence = int(request.form.get("int_increase"))
            agility = int(request.form.get("agi_increase"))
            willpower = int(request.form.get("will_increase"))
            endurance = int(request.form.get("end_increase"))
            charisma = int(request.form.get("char_increase"))
            luck = int(request.form.get("lck_increase"))
            speed = int(request.form.get("spd_increase"))
            temp_days = strength*2 + intelligence*2 + agility + willpower + endurance*2 + charisma + luck + speed*2

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            game.hero['dwarf3'].strength += strength
            game.hero['dwarf3'].intelligence += intelligence
            game.hero['dwarf3'].agility += agility
            game.hero['dwarf3'].willpower += willpower
            game.hero['dwarf3'].endurance += endurance
            game.hero['dwarf3'].charisma += charisma
            game.hero['dwarf3'].luck += luck
            game.hero['dwarf3'].speed += speed

            update_stats('dwarf3')

            game.days -= temp_days



        #   EQUIP
        #   It was a Barbie doll dress up game all along...
        #
        #   game.backpack, array  ->  HTML form, string  ->  game.item_dict, dictionary  ->  game.hero[dwarf].equipment, dictionary
        #
        #   Takes a string from HTML form option field (ex. "Leather Cap"), then searches for its object in item_dict which contains reference to all items in the game.
        #   Then takes that object and slams it into the corresponding equipment slot. Also there's an unequipment call somewhere in the middle.
        #   Stuff resets and recalculates at the end, as per tradition.

        elif request.form.get('equipment dwarf1', False) == 'Equip':

            # Declaring stuff cuz otherwise PyCharm screams, even though there's no way for these to ever be unassigned I think.
            weapon = headpiece = shoulders = chest = pants = gloves = boots = artefact = None

            # Iterating through global item dictionary in search for objects.
            for key, value in game.item_dict.items():
                if key == request.form.get("weapon"):
                    weapon = value
                    game.backpack.remove(value)
                elif key == request.form.get("headpiece"):
                    headpiece = value
                    game.backpack.remove(value)
                elif key == request.form.get("shoulders"):
                    shoulders = value
                    game.backpack.remove(value)
                elif key == request.form.get("chest"):
                    chest = value
                    game.backpack.remove(value)
                elif key == request.form.get("pants"):
                    pants = value
                    game.backpack.remove(value)
                elif key == request.form.get("gloves"):
                    gloves = value
                    game.backpack.remove(value)
                elif key == request.form.get("boots"):
                    boots = value
                    game.backpack.remove(value)
                elif key == request.form.get("artefact"):
                    artefact = value
                    game.backpack.remove(value)

            # Sneaky unequipment call
            for key, value in game.hero['dwarf1'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf1'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            # Assigning items from the library to the equipment dictionary.
            if request.form.get("weapon") is not None:
                game.hero['dwarf1'].equipment.update({'weapon': weapon})

            if request.form.get("headpiece") is not None:
                game.hero['dwarf1'].equipment.update({'headpiece': headpiece})

            if request.form.get("shoulders") is not None:
                game.hero['dwarf1'].equipment.update({'shoulders': shoulders})

            if request.form.get("chest") is not None:
                game.hero['dwarf1'].equipment.update({'chest': chest})

            if request.form.get("gloves") is not None:
                game.hero['dwarf1'].equipment.update({'gloves': gloves})

            if request.form.get("pants") is not None:
                game.hero['dwarf1'].equipment.update({'pants': pants})

            if request.form.get("boots") is not None:
                game.hero['dwarf1'].equipment.update({'boots': boots})

            if request.form.get("artefact") is not None:
                game.hero['dwarf1'].equipment.update({'artefact': artefact})

            # Updating stuff
            stat_reset('dwarf1')
            update_equipment('dwarf1')
            update_stats('dwarf1')

        elif request.form.get('equipment dwarf2', False) == 'Equip':

            weapon = headpiece = shoulders = chest = pants = gloves = boots = artefact = None

            for key, value in game.item_dict.items():
                if key == request.form.get("weapon"):
                    weapon = value
                    game.backpack.remove(value)
                elif key == request.form.get("headpiece"):
                    headpiece = value
                    game.backpack.remove(value)
                elif key == request.form.get("shoulders"):
                    shoulders = value
                    game.backpack.remove(value)
                elif key == request.form.get("chest"):
                    chest = value
                    game.backpack.remove(value)
                elif key == request.form.get("pants"):
                    pants = value
                    game.backpack.remove(value)
                elif key == request.form.get("gloves"):
                    gloves = value
                    game.backpack.remove(value)
                elif key == request.form.get("boots"):
                    boots = value
                    game.backpack.remove(value)
                elif key == request.form.get("artefact"):
                    artefact = value
                    game.backpack.remove(value)

            for key, value in game.hero['dwarf2'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf2'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            if request.form.get("weapon") is not None:
                game.hero['dwarf2'].equipment.update({'weapon': weapon})

            if request.form.get("headpiece") is not None:
                game.hero['dwarf2'].equipment.update({'headpiece': headpiece})

            if request.form.get("shoulders") is not None:
                game.hero['dwarf2'].equipment.update({'shoulders': shoulders})

            if request.form.get("chest") is not None:
                game.hero['dwarf2'].equipment.update({'chest': chest})

            if request.form.get("gloves") is not None:
                game.hero['dwarf2'].equipment.update({'gloves': gloves})

            if request.form.get("pants") is not None:
                game.hero['dwarf2'].equipment.update({'pants': pants})

            if request.form.get("boots") is not None:
                game.hero['dwarf2'].equipment.update({'boots': boots})

            if request.form.get("artefact") is not None:
                game.hero['dwarf2'].equipment.update({'artefact': artefact})

            stat_reset('dwarf2')
            update_equipment('dwarf2')
            update_stats('dwarf2')

        elif request.form.get('equipment dwarf3', False) == 'Equip':

            weapon = headpiece = shoulders = chest = pants = gloves = boots = artefact = None

            for key, value in game.item_dict.items():
                if key == request.form.get("weapon"):
                    weapon = value
                    game.backpack.remove(value)
                elif key == request.form.get("headpiece"):
                    headpiece = value
                    game.backpack.remove(value)
                elif key == request.form.get("shoulders"):
                    shoulders = value
                    game.backpack.remove(value)
                elif key == request.form.get("chest"):
                    chest = value
                    game.backpack.remove(value)
                elif key == request.form.get("pants"):
                    pants = value
                    game.backpack.remove(value)
                elif key == request.form.get("gloves"):
                    gloves = value
                    game.backpack.remove(value)
                elif key == request.form.get("boots"):
                    boots = value
                    game.backpack.remove(value)
                elif key == request.form.get("artefact"):
                    artefact = value
                    game.backpack.remove(value)

            for key, value in game.hero['dwarf3'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf3'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            if request.form.get("weapon") is not None:
                game.hero['dwarf3'].equipment.update({'weapon': weapon})

            if request.form.get("headpiece") is not None:
                game.hero['dwarf3'].equipment.update({'headpiece': headpiece})

            if request.form.get("shoulders") is not None:
                game.hero['dwarf3'].equipment.update({'shoulders': shoulders})

            if request.form.get("chest") is not None:
                game.hero['dwarf3'].equipment.update({'chest': chest})

            if request.form.get("gloves") is not None:
                game.hero['dwarf3'].equipment.update({'gloves': gloves})

            if request.form.get("pants") is not None:
                game.hero['dwarf3'].equipment.update({'pants': pants})

            if request.form.get("boots") is not None:
                game.hero['dwarf3'].equipment.update({'boots': boots})

            if request.form.get("artefact") is not None:
                game.hero['dwarf3'].equipment.update({'artefact': artefact})

            stat_reset('dwarf3')
            update_equipment('dwarf3')
            update_stats('dwarf3')



        #   UNEQUIP
        #   For peeling the dwarves out of their juicy equipment.
        #
        #   HTML form, string  ->  game.hero[dwarf].equipment
        #
        #   Takes a string from HTML form option field (ex. "Leather Cap") and searches for it in the corresponding dwarf's equipment.
        #   Puts it into his backpack and deletes it from the equipment. Because both objects already have the actual object of the item inside them,
        #   there's no need to cross-reference anything with the help of item_dict.

        elif request.form.get('equipment dwarf1', False) == 'Unequip':
            for key, value in game.hero['dwarf1'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf1'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            stat_reset('dwarf1')
            update_stats('dwarf1')

        elif request.form.get('equipment dwarf2', False) == 'Unequip':
            for key, value in game.hero['dwarf2'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf2'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            stat_reset('dwarf2')
            update_stats('dwarf2')

        elif request.form.get('equipment dwarf3', False) == 'Unequip':
            for key, value in game.hero['dwarf3'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf3'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artifact': None})

            stat_reset('dwarf3')
            update_stats('dwarf3')


        #   ADVENTURE
        #   Your only source of loot.
        #
        #   random.choices()  ->  game.backpack
        #
        #   Randomises and distributes loot from adventures depending on its scale (cost in days).

        elif request.form.get('adventure', False) == 'Short venture':

            odds = random.randint(1, 100)
            spoils = None
            temp_days = 14

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_common, k = 3)
            elif 46 <= odds <= 85:
                spoils = random.choices(item_list_common, k = 2) + random.choices(item_list_rare, k = 1)
            elif 86 <= odds <= 95:
                spoils = random.choices(item_list_rare, k = 3)
            elif 96 <= odds == 100:
                spoils = random.choices(item_list_epic, k = 1)

            game.days -= temp_days

            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Risky adventure':

            odds = random.randint(1, 100)
            spoils = None
            temp_days = 31

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_rare, k = 3)
            elif 46 <= odds <= 85:
                spoils = random.choices(item_list_rare, k = 2) + random.choices(item_list_epic, k = 1)
            elif 86 <= odds <= 95:
                spoils = random.choices(item_list_epic, k = 3)
            elif 96 <= odds == 100:
                spoils = random.choices(item_list_legendary, k = 1)

            game.days -= temp_days

            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Legendary expedition':

            odds = random.randint(1, 100)
            spoils = None
            temp_days = 90

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_epic, k = 4)
            elif 46 <= odds <= 85:
                spoils = random.choices(item_list_legendary, k = 1) + random.choices(item_list_epic, k = 2)
            elif 86 <= odds <= 95:
                spoils = random.choices(item_list_legendary, k = 2)
            elif 96 <= odds == 100:
                spoils = random.choices(item_list_legendary, k = 3)

            game.days -= temp_days

            game.backpack += spoils


        #   TACTICS
        #   Change the personality of your dwarf with one click of a button.
        #
        #   HTML form, string  ->  game.hero[dwarf].tactic
        #
        #   Takes the string from HTML form radio field and puts it directly into your dwarf.

        elif request.form.get('tactics dwarf1', False) == 'Confirm':
            game.hero['dwarf1'].tactic = request.form.get('tactic')

        elif request.form.get('tactics dwarf2', False) == 'Confirm':
            game.hero['dwarf2'].tactic = request.form.get('tactic')

        elif request.form.get('tactics dwarf3', False) == 'Confirm':
            game.hero['dwarf3'].tactic = request.form.get('tactic')




    return render_template('game.html', game=game)

def update_equipment(dwarf):

    # Updates multipliers and bonuses values based on current equipment
    for item_slot, item_name in game.hero[dwarf].equipment.items():
        if item_name is not None:

            rounded = game.hero[dwarf].str_mul + game.hero[dwarf].equipment[item_slot].str_mul
            game.hero[dwarf].str_mul = round(rounded,2)
            game.hero[dwarf].str_bonus += game.hero[dwarf].equipment[item_slot].str_bonus

            rounded = game.hero[dwarf].int_mul + game.hero[dwarf].equipment[item_slot].int_mul
            game.hero[dwarf].int_mul = round(rounded, 2)
            game.hero[dwarf].int_bonus += game.hero[dwarf].equipment[item_slot].int_bonus

            rounded = game.hero[dwarf].agi_mul + game.hero[dwarf].equipment[item_slot].agi_mul
            game.hero[dwarf].agi_mul = round(rounded, 2)
            game.hero[dwarf].agi_bonus += game.hero[dwarf].equipment[item_slot].agi_bonus

            rounded = game.hero[dwarf].will_mul + game.hero[dwarf].equipment[item_slot].will_mul
            game.hero[dwarf].will_mul = round(rounded, 2)
            game.hero[dwarf].will_bonus += game.hero[dwarf].equipment[item_slot].will_bonus

            rounded = game.hero[dwarf].end_mul + game.hero[dwarf].equipment[item_slot].end_mul
            game.hero[dwarf].end_mul = round(rounded, 2)
            game.hero[dwarf].end_bonus += game.hero[dwarf].equipment[item_slot].end_bonus

            rounded = game.hero[dwarf].char_mul + game.hero[dwarf].equipment[item_slot].char_mul
            game.hero[dwarf].char_mul = round(rounded, 2)
            game.hero[dwarf].char_bonus += game.hero[dwarf].equipment[item_slot].char_bonus

            rounded = game.hero[dwarf].lck_mul + game.hero[dwarf].equipment[item_slot].lck_mul
            game.hero[dwarf].lck_mul = round(rounded, 2)
            game.hero[dwarf].lck_bonus += game.hero[dwarf].equipment[item_slot].lck_bonus

            rounded = game.hero[dwarf].spd_mul + game.hero[dwarf].equipment[item_slot].spd_mul
            game.hero[dwarf].spd_mul = round(rounded, 2)
            game.hero[dwarf].spd_bonus += game.hero[dwarf].equipment[item_slot].spd_bonus

def stat_reset(dwarf):

    # Resets all stats before equipment update
    game.hero[dwarf].str_mul = 1.0
    game.hero[dwarf].str_bonus = 0
    game.hero[dwarf].int_mul = 1.0
    game.hero[dwarf].int_bonus = 0
    game.hero[dwarf].agi_mul = 1.0
    game.hero[dwarf].agi_bonus = 0
    game.hero[dwarf].will_mul = 1.0
    game.hero[dwarf].will_bonus = 0
    game.hero[dwarf].end_mul = 1.0
    game.hero[dwarf].end_bonus = 0
    game.hero[dwarf].char_mul = 1.0
    game.hero[dwarf].char_bonus = 0
    game.hero[dwarf].lck_mul = 1.0
    game.hero[dwarf].lck_bonus = 0
    game.hero[dwarf].spd_mul = 1.0
    game.hero[dwarf].spd_bonus = 0

def update_stats(dwarf):

    # Updates total stats based on the bases, multipliers and bonuses
    game.hero[dwarf].str_total = round(game.hero[dwarf].strength * game.hero[dwarf].str_mul + game.hero[dwarf].str_bonus)
    game.hero[dwarf].int_total = round(game.hero[dwarf].intelligence * game.hero[dwarf].int_mul + game.hero[dwarf].int_bonus)
    game.hero[dwarf].agi_total = round(game.hero[dwarf].agility * game.hero[dwarf].agi_mul + game.hero[dwarf].agi_bonus)
    game.hero[dwarf].will_total = round(game.hero[dwarf].willpower * game.hero[dwarf].will_mul + game.hero[dwarf].will_bonus)
    game.hero[dwarf].end_total = round(game.hero[dwarf].endurance * game.hero[dwarf].end_mul + game.hero[dwarf].end_bonus)
    game.hero[dwarf].char_total = round(game.hero[dwarf].charisma * game.hero[dwarf].char_mul + game.hero[dwarf].char_bonus)
    game.hero[dwarf].lck_total = round(game.hero[dwarf].luck * game.hero[dwarf].lck_mul + game.hero[dwarf].lck_bonus)
    game.hero[dwarf].spd_total = round(game.hero[dwarf].speed * game.hero[dwarf].spd_mul + game.hero[dwarf].spd_bonus)


# Base hero class - for generating both dwarves and goblins
class Hero:
    def __init__(self, token):
        dwarf_names = ['Karl', 'Bjourn', 'Boris', 'Darvis', 'Gamrid', 'Magni', 'Muradin', 'Dagran', 'Brann', 'Falstad', 'Ragnok']
        dwarf_surnames = ['Darkstone', 'Deeprock', 'Hammerblow', 'Buzzbeard', 'Surefoot', 'Copperfinger', 'Highcliff', 'Stoneborn', 'Ironbreaker', 'Bronzebeard']
        goblin_names = ['Zorgg', 'Timmy', 'Velrog', 'Borkle', 'Burd', 'Beerk', 'Gnarlak', "Ur'lok", "Zyg'fryd"]
        goblin_surnames = ['the Destroyer', 'Unbreakable', 'Markuth', 'Mudborn', 'Cogknife', 'Duskshiv', 'Darguun', "Dhak'ar"]

        # Generating the names
        if token == "dwarf":
            name = random.choice(dwarf_names)
            surname = random.choice(dwarf_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1,9)) + '.jpg'
        else:
            name = random.choice(goblin_names)
            surname = random.choice(goblin_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1,9)) + '.jpg'

        # Generating starter equipment (only for the player)
        starter_eq = eq_choice = None
        if token == "dwarf":
            starter_eq = random.choice(['headpiece', 'pants', 'boots', 'nothing lol'])
            if starter_eq == 'headpiece':
                eq_choice = random.choice([item_1, item_7, item_13])
            elif starter_eq == 'pants':
                eq_choice = random.choice([item_4, item_10, item_16])
            elif starter_eq == 'boots':
                eq_choice = random.choice([item_6, item_12, item_18])
            else:
                eq_choice = starter_eq = None

        self.hero_name = name_surname
        self.hero_portrait = hero_portrait
        self.strength = random.randint(10, 20)
        self.str_mul = float(1.0)
        self.str_bonus = 0
        self.str_total = round(self.strength * self.str_mul + self.str_bonus)
        self.intelligence = random.randint(10, 20)
        self.int_mul = float(1.0)
        self.int_bonus = 0
        self.int_total = round(self.intelligence * self.int_mul + self.int_bonus)
        self.agility = random.randint(10, 20)
        self.agi_mul = float(1.0)
        self.agi_bonus = 0
        self.agi_total = round(self.agility * self.agi_mul + self.agi_bonus)
        self.willpower = random.randint(10, 20)
        self.will_mul = float(1.0)
        self.will_bonus = 0
        self.will_total = round(self.willpower * self.will_mul + self.will_bonus)
        self.endurance = random.randint(10, 20)
        self.end_mul = float(1.0)
        self.end_bonus = 0
        self.end_total = round(self.endurance * self.end_mul + self.end_bonus)
        self.charisma = random.randint(10, 20)
        self.char_mul = float(1.0)
        self.char_bonus = 0
        self.char_total = round(self.charisma * self.char_mul + self.char_bonus)
        self.luck = random.randint(10, 20)
        self.lck_mul = float(1.0)
        self.lck_bonus = 0
        self.lck_total = round(self.luck * self.lck_mul + self.lck_bonus)
        self.speed = random.randint(10, 20)
        self.spd_mul = float(1.0)
        self.spd_bonus = 0
        self.spd_total = round(self.speed * self.spd_mul + self.spd_bonus)
        self.equipment = {'weapon': None,
                          'headpiece': None,
                          'shoulders': None,
                          'chest': None,
                          'gloves': None,
                          'pants': None,
                          'boots': None,
                          'artefact': None}
        self.tactic = random.choice(['Frenzy', 'Focus', 'Balance', 'Overconfidence'])
        self.special_list = []

        if starter_eq is not None:
            self.equipment.update({starter_eq: eq_choice})


# Item class - for designing and creating items
class Item:

    def __init__(self, item_name, item_slot, description, str_mul, str_bonus, int_mul, int_bonus, agi_mul, agi_bonus, will_mul, will_bonus, end_mul, end_bonus, char_mul, char_bonus, lck_mul, luck_bonus, spd_mul, spd_bonus, special):

        self.item_name = item_name
        self.item_slot = item_slot
        self.description = description

        self.str_mul = str_mul
        self.str_bonus = str_bonus
        self.int_mul = int_mul
        self.int_bonus = int_bonus
        self.agi_mul = agi_mul
        self.agi_bonus = agi_bonus
        self.will_mul = will_mul
        self.will_bonus = will_bonus
        self.end_mul = end_mul
        self.end_bonus = end_bonus
        self.char_mul = char_mul
        self.char_bonus = char_bonus
        self.lck_mul = lck_mul
        self.lck_bonus = luck_bonus
        self.spd_mul = spd_mul
        self.spd_bonus = spd_bonus

        self.special = special


# LIST OF ITEMS

        # Common - Medium armor set

item_1 = Item('Leather Cap', 'headpiece', 'A trusty, sturdy leather cap. Even most valiant of dwarves look like dorks while wearing it.',
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_2 = Item('Leather Shoulderpads', 'shoulders', "Will not save him from losing an arm but will certainly soften up the blow.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_3 = Item('Leather Jacket', 'chest', "Dope :D",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_4 = Item('Leather Pants', 'pants', "It took a lot of convincing for him to wear it...",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_5 = Item('Leather Gloves', 'gloves', "Sturdy leather gloves - every dwarves' best friend.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_6 = Item('Leather Boots', 'boots', "Solid, steel capped boots may win or lose you a battle.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment


        # Common - Heavy armor set

item_7 = Item('Rusty Helmet', 'headpiece', 'Grandma always asked you to wear one while going into the mines.',
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_8 = Item('Rusty Pauldrons', 'shoulders', 'These would look much more intimidating if not for the state they are in.',
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_9 = Item('Rusty Chainmail', 'chest', "Taking a spear to the chest will still hurt like hell but at least he won't bleed out.",
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_10 = Item('Rusty Tasset', 'pants', "Noisy...",
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_11 = Item('Rusty Gauntlets', 'gloves', "For all those dirty disarming tricks that goblins are known for.",
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_12 = Item('Rusty Greaves', 'boots', "What's better than steel capped boots? Full-steel boots! Too bad these have rusty holes in them...",
              0.15, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment


        # Common -  Light armor set

item_13 = Item('Tattered Hood', 'headpiece', "It reduces the vision a tad bit, but at least it makes it easier to focus.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_14 = Item('Tattered Epaulettes', 'shoulders', "Makes you look noble - too bad they don't offer much protection.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_15 = Item('Tattered Robe', 'chest', "These must've looked magnificent before moths took a nest in them.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_16 = Item('Tattered Pants', 'pants', "Offer unprecedented freedom of movement.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_17 = Item('Tattered Gloves', 'gloves', "They give off a weird feeling of comfort.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_18 = Item('Tattered Shoes', 'boots', "Pretty airy.",
              0.0, 0,   # Strength
              0.1, 3,   # Intelligence
              0.0, 0,   # Agility
              0.1, 3,   # Willpower
              0.0, 0,   # Endurance
              0.1, 2,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment


            # Common - Weapons

item_19 = Item('Leather Whip', 'weapon', "Takes a bit of practice to use properly.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.2, 4,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.2, 4,   # Speed
              None)     # Enchantment

item_20 = Item('Bronze Broadsword', 'weapon', "Every dwarf and their hogs know how to use one.",
              0.2, 4,   # Strength
              0.0, 0,   # Intelligence
              0.2, 4,   # Agility
              0.0, 0,   # Willpower
              0.2, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_21 = Item('Oak Staff', 'weapon', "Provides just as much support for spellcasting as for melee combat.",
              0.0, 0,   # Strength
              0.2, 4,   # Intelligence
              0.0, 0,   # Agility
              0.2, 4,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.2, 4,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

# RARE ITEMS

        # Rare - Medium armor set

item_22 = Item('Hardleather Helmet', 'headpiece', "Reinforced version of leather helmet, now with 30% extra sturdiness!",
              0.2, 4,   # Strength
              0.0, 0,   # Intelligence
              0.2, 4,   # Agility
              0.0, 0,   # Willpower
              0.2, 4,   # Endurance
              0.0, 0,   # Charisma
              0.1, 2,   # Luck
              0.1, 2,   # Speed
              None)     # Enchantment

item_23 = Item('Hardleather Shoulderpads', 'shoulders', "These may actually save him from losing an arm.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_24 = Item('Hardleather Chestplate', 'chest', "Light as leather, hard as bronze!",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_25 = Item('Hardleather Pants', 'pants', "They limit his movement a bit but the protection they offer are well worth the trade.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_26 = Item('Hardleather Gloves', 'gloves', "Manly.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment

item_27 = Item('Hardleather Boots', 'boots', "For that extra amount of protection.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 2,   # Agility
              0.1, 2,   # Willpower
              0.0, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 2,   # Speed
              None)     # Enchantment


item_list_common = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19, item_20, item_21]
item_list_rare = [item_22, item_23, item_24, item_25, item_26, item_27]
item_list_epic = []
item_list_legendary = []

class Game:

    def __init__(self):
        self.hero = {'dwarf1': Hero('dwarf'), 'dwarf2': Hero('dwarf'), 'dwarf3': Hero('dwarf')}
        self.enemy = {'goblin1': Hero('goblin'), 'goblin2': Hero('goblin'), 'goblin3': Hero('goblin')}
        self.backpack = []
        self.item_dict = {}
        self.days = 365


if __name__ == '__main__':
    app.run(host="wierzba.wzks.uj.edu.pl", port=5102, debug=True)
