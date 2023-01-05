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
                              "A Lucky Pebble": item_22,

                              "Hardleather Helmet": item_101, "Hardleather Shoulderpads": item_102, "Hardleather Chest": item_103, "Hardleather Pants": item_104, "Hardleather Gloves": item_105, "Hardleather Boots": item_106,
                              "Iron Helmet": item_107, "Iron Pauldrons": item_108, "Iron Cuirass": item_109, "Iron Legguards": item_110, "Iron Handguards": item_111, "Iron Greaves": item_112,
                              "Silk Headwrap": item_113, "Silk Shoulderpads": item_114, "Silk Vesture": item_115, "Silk Kilt": item_116, "Silk Gloves": item_117, "Silk Slippers": item_118,
                              "Flintlock Pistol": item_119, "Iron Mace": item_120, "Amethyst Focus": item_121,
                              "Shiny Coin": item_121,

                              "Dragonscale Helmet": item_201, "Dragonscale Shoulderguards": item_202, "Dragonscale Chainmail": item_203, "Dragonscale Reinforced Kilt": item_204, "Dragonscale Gauntlets": item_205, "Dragonscale Wyrm-riders": item_206,
                              "Mithril Headguard": item_207, "Mithril Pauldrons": item_208, "Mithril Chestplate": item_209, "Mithril Legguards": item_210, "Mithril Gauntlets": item_211, "Mithril Greaves": item_212,
                              "Ceremonial Tiara": item_213, "Ceremonial Epaluettes": item_214, "Ceremonial Robe": item_215, "Ceremonial Trousers": item_216, "Ceremonial Gloves": item_217, "Ceremonial Shoes": item_218,
                              "Mageslayer Dagger": item_219, "Firebrand Sword": item_220, "Dragonwood Wand": item_221,

                              "Crown of Will": item_301, "Heart of the Mountain": item_302,

                              "???": item_404}
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
            game.hero['dwarf1'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

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
            game.hero['dwarf2'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

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
            game.hero['dwarf3'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

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
            game.hero['dwarf1'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

            stat_reset('dwarf1')
            update_stats('dwarf1')

        elif request.form.get('equipment dwarf2', False) == 'Unequip':
            for key, value in game.hero['dwarf2'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf2'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

            stat_reset('dwarf2')
            update_stats('dwarf2')

        elif request.form.get('equipment dwarf3', False) == 'Unequip':
            for key, value in game.hero['dwarf3'].equipment.items():
                if value is not None:
                    game.backpack.append(value)
            game.hero['dwarf3'].equipment.update({'weapon': None, 'headpiece': None, 'shoulders': None, 'chest': None, 'pants': None, 'gloves': None, 'boots': None, 'artefact': None})

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
            temp_days = 14

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_common, k = 6)
            elif 46 <= odds <= 75:
                spoils = random.choices(item_list_common, k = 4) + random.choices(item_list_rare, k = 2)
            elif 76 <= odds <= 90:
                spoils = random.choices(item_list_rare, k = 5)
            elif 91 <= odds == 100:
                spoils = random.choices(item_list_epic, k = 2) + random.choices(item_list_rare, k = 2)
            else:
                spoils = random.choices(item_list_common, k = 3) + random.choices(item_list_rare, k = 1)

            game.days -= temp_days

            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Risky adventure':

            odds = random.randint(1, 100)
            temp_days = 31

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_rare, k = 6)
            elif 46 <= odds <= 75:
                spoils = random.choices(item_list_rare, k = 4) + random.choices(item_list_epic, k = 2)
            elif 76 <= odds <= 90:
                spoils = random.choices(item_list_epic, k = 5)
            elif 91 <= odds == 100:
                spoils = random.choices(item_list_legendary, k = 1)
            else:
                spoils = random.choices(item_list_rare, k=4) + random.choices(item_list_epic, k=2)

            game.days -= temp_days

            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Legendary expedition':

            odds = random.randint(1, 100)
            temp_days = 90

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils = random.choices(item_list_epic, k = 5)
            elif 46 <= odds <= 75:
                spoils = random.choices(item_list_epic, k = 7)
            elif 76 <= odds <= 90:
                spoils = random.choices(item_list_legendary, k = 1)
            elif 91 <= odds == 100:
                spoils = random.choices(item_list_legendary, k = 2)
            else:
                spoils = random.choices(item_list_special, k = 1)

            game.days -= temp_days

            game.backpack += spoils


        #   TACTICS
        #   Change the personality of your dwarf with one click of a button.
        #
        #   HTML form, string  ->  game.hero[dwarf].tactic
        #
        #   Takes the string from HTML form radio field and puts it directly into your dwarf.
        #   If player sends an empty HTML form, tactic remains unchanged.

        elif request.form.get('tactics dwarf1', False) == 'Confirm':
            if request.form.get('tactic') is None:
                pass
            else:
                game.hero['dwarf1'].tactic = request.form.get('tactic')

        elif request.form.get('tactics dwarf2', False) == 'Confirm':
            if request.form.get('tactic') is None:
                pass
            else:
                game.hero['dwarf2'].tactic = request.form.get('tactic')

        elif request.form.get('tactics dwarf3', False) == 'Confirm':
            if request.form.get('tactic') is None:
                pass
            else:
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
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1,22)) + '.jpg'
        else:
            name = random.choice(goblin_names)
            surname = random.choice(goblin_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1,22)) + '.jpg'

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
        self.tactic = random.choice(['Frenzy', 'Focus', 'Balanced', 'Overconfidence'])
        self.special_list = []

        if starter_eq is not None:
            self.equipment.update({starter_eq: eq_choice})


# Item class - for designing and creating items
class Item:

    def __init__(self, item_name, item_slot, rarity, description, str_mul, str_bonus, int_mul, int_bonus, agi_mul, agi_bonus, will_mul, will_bonus, end_mul, end_bonus, char_mul, char_bonus, lck_mul, luck_bonus, spd_mul, spd_bonus, special):

        self.item_name = item_name
        self.item_slot = item_slot
        self.rarity = rarity
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

item_1 = Item('Leather Cap', 'headpiece', 'common', 'A trusty, sturdy leather cap. Even most valiant of dwarves look like dorks while wearing it.',
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment

item_2 = Item('Leather Shoulderpads', 'shoulders', 'common', "Will not save him from losing an arm but will certainly soften up the blow.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment

item_3 = Item('Leather Jacket', 'chest', 'common', "Dope :D",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment

item_4 = Item('Leather Pants', 'pants', 'common', "It took a lot of convincing for him to wear it...",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment

item_5 = Item('Leather Gloves', 'gloves', 'common', "Sturdy leather gloves - every dwarves' best friend.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment

item_6 = Item('Leather Boots', 'boots', 'common', "Solid, steel capped boots may win or lose you a battle.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              None)     # Enchantment


            # Common - Heavy armor set

item_7 = Item('Rusty Helmet', 'headpiece', 'common', 'Grandma always asked you to wear one while going into the mines.',
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_8 = Item('Rusty Pauldrons', 'shoulders', 'common', 'These would look much more intimidating if not for the state they are in.',
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_9 = Item('Rusty Chainmail', 'chest', 'common', "Taking a spear to the chest will still hurt like hell but at least he won't bleed out.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_10 = Item('Rusty Tasset', 'pants', 'common', "Noisy...",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_11 = Item('Rusty Gauntlets', 'gloves', 'common', "For all those dirty disarming tricks that goblins are known for.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_12 = Item('Rusty Greaves', 'boots', 'common', "What's better than steel capped boots? Full-steel boots! Too bad these have rusty holes in them...",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment


            # Common -  Light armor set

item_13 = Item('Tattered Hood', 'headpiece', 'common', "It reduces the vision a tad bit, but at least it makes it easier to focus.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_14 = Item('Tattered Epaulettes', 'shoulders', 'common', "Makes you look noble - too bad they don't offer much protection.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_15 = Item('Tattered Robe', 'chest', 'common', "These must've looked magnificent before moths took a nest in them.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_16 = Item('Tattered Pants', 'pants', 'common', "Offer unprecedented freedom of movement.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_17 = Item('Tattered Gloves', 'gloves', 'common', "They give off a weird feeling of comfort.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_18 = Item('Tattered Shoes', 'boots', 'common', "Pretty airy.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment


            # Common - Weapons

item_19 = Item('Leather Whip', 'weapon', 'common', "Takes a bit of practice to use properly.",
              0.0, 0,   # Strength
              0.0, 0,   # Intelligence
              0.1, 4,   # Agility
              0.0, 0,   # Willpower
              0.1, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              None)     # Enchantment

item_20 = Item('Bronze Broadsword', 'weapon', 'common', "Every dwarf and their hogs know how to use one.",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 4,   # Endurance
              0.0, 0,   # Charisma
              0.1, 4,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

item_21 = Item('Oak Staff', 'weapon', 'common', "Provides just as much support for spellcasting as for melee combat.",
              0.0, 0,   # Strength
              0.1, 4,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 0,   # Endurance
              0.1, 4,   # Charisma
              0.1, 4,   # Luck
              0.0, 0,   # Speed
              None)     # Enchantment

            # Common - Artefact

item_22 = Item('A Lucky Pebble', 'artefact', 'common', "His name is Steeve :D",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.2, 4,  # Speed
               None)    # Enchantment


# RARE ITEMS

            # Rare - Medium armor set

item_101 = Item('Hardleather Helmet', 'headpiece', 'rare', "Reinforced version of leather helmet, now with 30% extra sturdiness!",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment

item_102 = Item('Hardleather Shoulderpads', 'shoulders', 'rare', "These may actually save him from losing an arm.",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment

item_103 = Item('Hardleather Chest', 'chest', 'rare', "Light as leather, hard as bronze!",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment

item_104 = Item('Hardleather Pants', 'pants', 'rare', "They limit his movement a bit but the protection they offer are well worth the trade.",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment

item_105 = Item('Hardleather Gloves', 'gloves', 'rare', "Manly.",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment

item_106 = Item('Hardleather Boots', 'boots', 'rare', "For that extra amount of protection.",
              0.0, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 0,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 4,   # Speed
              None)     # Enchantment


            # Rare - Heavy armor set

item_107 = Item('Iron Helmet', 'headpiece', 'rare', "This is getting kinda heavy...",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_108 = Item('Iron Pauldrons', 'shoulders', 'rare', "Maybe if you polished them, they could blind the enemy.",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_109 = Item('Iron Cuirass', 'chest', 'rare', "Wouldn't recommend donning this one on a sunny day.",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_110 = Item('Iron Legguards', 'pants', 'rare', "Try kicking this you goblin bastards!",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_111 = Item('Iron Handguards', 'gloves', 'rare', "Why would you even need a weapon with a pair of these?",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_112 = Item('Iron Greaves', 'boots', 'rare', "We are going full-metal, aw yeah!",
               0.15, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 0,  # Endurance
               0.0, 4,  # Charisma
               0.0, 4,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment


            # Rare - Light armor set

item_113 = Item('Silk Headwrap', 'headpiece', 'rare', "Softness of silk helps you concentrate on your manly thoughts.",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_114 = Item('Silk Shoulderpads', 'shoulders', 'rare', "These are just for show.",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_115 = Item('Silk Vesture', 'chestpiece', 'rare', "Might be mistaken for a bathrobe...",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_116 = Item('Silk Kilt', 'pants', 'rare', "No matter what others may say, it's a kilt alright, it's a kilt...",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_117 = Item('Silk Gloves', 'gloves', 'rare', "Silk's static inducing attributes have been thaumaturgically confirmed to enhance one's spellweaving abilities.",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_118 = Item('Silk Slippers', 'boots', 'rare', "...",
               0.0, 0,  # Strength
               0.15, 0,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.0, 0,  # Endurance
               0.4, 0,  # Charisma
               0.4, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment


            # Rare - Weapons

item_119 = Item('Flintlock Pistol', 'weapon', 'rare', "Once you are out of ammo and gunpowder, it's sturdy handle fits right between goblin's eyes.",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.15, 4,  # Charisma
               0.15, 4,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_120 = Item('Iron Mace', 'weapon', 'rare', "They say it has been blessed by a hidden deity - for some reason holding it puts any dwarf in a mood for some goblin skull bashing.",
               0.15, 4,  # Strength
               0.0, 0,  # Intelligence
               0.15, 4,  # Agility
               0.0, 0,  # Willpower
               0.15, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_121 = Item('Amethyst Focus', 'weapon', 'rare', "Every respecting spellcaster has an expensive focus through which they channel their spells.",
               0.0, 0,  # Strength
               0.15, 4,  # Intelligence
               0.0, 0,  # Agility
               0.15, 4,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment


            # Rare - Trinkets

item_122 = Item('Lucky Coin', 'artefact', 'rare', "Shiny coin. It's nice to the touch.",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.15, 4,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment


# EPIC ITEMS

            # Epic - Medium armor set

item_201 = Item('Dragonscale Helmet', 'headpiece', 'epic', "Gives a quite mean look.",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_202 = Item('Dragonscale Shoulderguards', 'shoulders', 'epic', "Hard as metal, light as leather.",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_203 = Item('Dragonscale Chainmail', 'chest', 'epic', "Fireproof but not waterproof!",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_204 = Item('Dragonscale Reinforced Kilt', 'pants', 'epic', "A much cooler cousin of Silk Kilt.",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_205 = Item('Dragonscale Gauntlets', 'gloves', 'epic', "They've got spikes in case you get disarmed.",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment

item_206 = Item('Dragonscale Wyrm-riders', 'boots', 'epic', "You could pack a really mean kick with those...",
               0.2, 6,  # Strength
               0.0, 0,  # Intelligence
               0.2, 6,  # Agility
               0.0, 0,  # Willpower
               0.15, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.15, 4,  # Speed
               None)  # Enchantment


            # Epic - Heavy armor

item_207 = Item('Mithril Headguard', 'headpiece', 'epic', "One of many symbols of dwarf race.",
               0.2, 6,  # Strength
               -0.1, -2,  # Intelligence
               0.0, 0,  # Agility
               0.15, 0,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_208 = Item('Mithril Pauldrons', 'shoulders', 'epic', "Looking good chief!",
               0.2, 6,  # Strength
               -0.15, -4,  # Intelligence
               0.0, 0,  # Agility
               0.25, 4,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_209 = Item('Mithril Chestplate', 'chest', 'epic', "Could deflect a fireball or two.",
               0.2, 6,  # Strength
               -0.15, -4,  # Intelligence
               0.0, 0,  # Agility
               0.25, 4,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_210 = Item('Mithril Legguards', 'pants', 'epic', "To guard your jewels from grabby mage's hands.",
               0.2, 6,  # Strength
               -0.15, -4,  # Intelligence
               0.0, 0,  # Agility
               0.25, 4,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_211 = Item('Mithril Gauntlets', 'gloves', 'epic', "Law enforcment uses these to arrest skilled magi.",
               0.2, 6,  # Strength
               -0.15, -4,  # Intelligence
               0.0, 0,  # Agility
               0.25, 4,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_212 = Item('Mithril Gauntlets', 'gloves', 'epic', "Law enforcment uses these to arrest skilled magi.",
               0.2, 6,  # Strength
               -0.15, -4,  # Intelligence
               0.0, 0,  # Agility
               0.25, 4,  # Willpower
               0.2, 6,  # Endurance
               0.0, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment


            # Epic - Light armor

item_213 = Item('Ceremonial Tiara', 'headpiece', 'epic', "You look like a real princess :D",
               0.0, 0,  # Strength
               0.35, 10,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_214 = Item('Ceremonial Epaluettes', 'shoulders', 'epic', "They make you look bigger and more magnificent.",
               0.0, 0,  # Strength
               0.35, 10,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_215 = Item('Ceremonial Robe', 'chest', 'epic', "You feel like you could coronate a king in those.",
               0.0, 0,  # Strength
               0.35, 8,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_216 = Item('Ceremonial Trousers', 'pants', 'epic', "These might look silly but they are so comfortable...",
               0.0, 0,  # Strength
               0.35, 8,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_217 = Item('Ceremonial Gloves', 'gloves', 'epic', "They crackle with arcane energies...",
               0.0, 0,  # Strength
               0.35, 8,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment

item_218 = Item('Ceremonial Shoes', 'gloves', 'epic', "The silver-lining helps you gather mana from the ground.",
               0.0, 0,  # Strength
               0.35, 8,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.25, 6,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               None)  # Enchantment


            # Epic - weapons

item_219 = Item('Mageslayer Dagger', 'weapon', 'epic', "A skilled fighter can deflect magic missiles with this blade. It was enchanted to home in into the mage's throats.",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.15, 8,  # Agility
               0.45, 18,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.15, 8,  # Luck
               0.25, 10,  # Speed
               "Mageslayer")  # Enchantment

item_220 = Item('Firebrand Sword', 'weapon', 'epic', "A mageblade - forged out of meteorite, reinforced with dark iron. It can withstand a spell and a blade alike.",
               0.35, 12,  # Strength
               0.35, 12,  # Intelligence
               0.15, 8,  # Agility
               0.15, 8,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               "Firebrand")  # Enchantment

item_221 = Item('Dragonwood Wand', 'weapon', 'epic', "Known by it's arcane conductivity, this wand let's you cast a barrage of spells in a blink of an eye!",
               0.0, 0,  # Strength
               0.45, 18,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.35, 12,  # Speed
               "Energize")  # Enchantment

# LEGENDARY ITEMS

item_301 = Item('Crown of Will', 'headpiece', 'legendary', "",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               3, 0,  # Willpower
               0.0, 0,  # Endurance
               5, 0,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               "Dominion")  # Enchantment

item_302 = Item('Heart of the Mountain', 'artefact', 'legendary', "",
               0.5, 20,  # Strength
               0.5, 20,  # Intelligence
               0.5, 20,  # Agility
               0.5, 20,  # Willpower
               0.5, 20,  # Endurance
               0.5, 20,  # Charisma
               0.5, 20,  # Luck
               0.5, 20,  # Speed
               "Avatar of the Mountain")  # Enchantment



            # Special items

item_404 = Item('???', 'artefact', 'cursed', "",
               -0.5, -20,  # Strength
               -0.5, -20,  # Intelligence
               -0.5, -20,  # Agility
               -0.5, -20,  # Willpower
               -0.5, -20,  # Endurance
               -0.5, -20,  # Charisma
               -0.5, -20,  # Luck
               -0.5, -20,  # Speed
               "Cursed")  # Enchantment


item_list_common = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19, item_20, item_21, item_22]
item_list_rare = [item_101, item_102, item_103, item_104, item_105, item_106, item_107, item_108, item_109, item_110, item_111, item_112, item_113, item_114, item_115, item_116, item_117, item_118, item_119, item_120, item_121, item_122]
item_list_epic = [item_201, item_202, item_203, item_204, item_205, item_206, item_207, item_208, item_209, item_210, item_211, item_212, item_213, item_214, item_215, item_216, item_217, item_218, item_219, item_220, item_221]
item_list_legendary = [item_301, item_302]
item_list_special = [item_404]

class Game:

    def __init__(self):
        self.hero = {'dwarf1': Hero('dwarf'), 'dwarf2': Hero('dwarf'), 'dwarf3': Hero('dwarf')}
        self.enemy = {'goblin1': Hero('goblin'), 'goblin2': Hero('goblin'), 'goblin3': Hero('goblin')}
        self.backpack = []
        self.item_dict = {}
        self.days = 365


if __name__ == '__main__':
    app.run(host="wierzba.wzks.uj.edu.pl", port=5102, debug=True)
