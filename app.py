from flask import Flask
from flask import render_template
from flask import request
from flask import session
from items import *
import random
import uuid

app = Flask(__name__)
app.secret_key = '8008135'

games = {}


# Base hero class - for generating both dwarves and goblins
class Hero:
    def __init__(self, token):
        dwarf_names = ['Karl', 'Bjourn', 'Boris', 'Darvis', 'Gamrid', 'Magni', 'Muradin', 'Dagran', 'Brann', 'Falstad',
                       'Ragnok']
        dwarf_surnames = ['Darkstone', 'Deeprock', 'Hammerblow', 'Buzzbeard', 'Surefoot', 'Copperfinger', 'Highcliff',
                          'Stoneborn', 'Ironbreaker', 'Bronzebeard']
        goblin_names = ['Zorgg', 'Timmy', 'Velrog', 'Borkle', 'Burd', 'Beerk', 'Gnarlak', "Ur'lok", "Zyg'fryd"]
        goblin_surnames = ['the Destroyer', 'Unbreakable', 'Markuth', 'Mudborn', 'Cogknife', 'Duskshiv', 'Darguun',
                           "Dhak'ar"]

        # Generating the names
        if token == "dwarf":
            name = random.choice(dwarf_names)
            surname = random.choice(dwarf_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1, 23)) + '.jpg'
        else:
            name = random.choice(goblin_names)
            surname = random.choice(goblin_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/goblin_portraits/' + str(random.randint(1, 10)) + '.jpg'

        # Generating starter equipment (only for the player)
        starter_eq = eq_choice = None
        if token == "dwarf":
            starter_eq = random.choice(['Headpiece', 'Pants', 'Boots', 'nothing lol'])
            if starter_eq == 'Headpiece':
                eq_choice = random.choice([item_1, item_7, item_13])
            elif starter_eq == 'Pants':
                eq_choice = random.choice([item_4, item_10, item_16])
            elif starter_eq == 'Boots':
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
        self.endurance = 1000
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
        self.armor = 0
        self.equipment = {'Weapon': None,
                          'Headpiece': None,
                          'Shoulders': None,
                          'Chest': None,
                          'Gloves': None,
                          'Pants': None,
                          'Boots': None,
                          'Artifact': None}
        self.tactic = random.choice(['Frenzy', 'Focus', 'Balanced', 'Overconfidence'])
        self.specials_list = []

        self.battle = False
        self.win = False
        self.sneak = False
        self.sneak_confirmed = False
        self.secret = False
        self.graveyard = False
        self.white_lotus = False
        self.white_lotus_taken = False
        self.cursed_amulet = False
        self.cursed_amulet_taken = False

        if starter_eq is not None:
            self.equipment.update({starter_eq: eq_choice})

        if self.hero_portrait == '/static/dwarf_portraits/23.jpg':
            self.hero_name = 'Stranger'
            self.equipment.update({'Weapon': item_51,
                                   'Headpiece': item_7,
                                   'Shoulders': item_8,
                                   'Chest': item_9,
                                   'Gloves': item_10,
                                   'Pants': item_11,
                                   'Boots': item_13,
                                   'Artifact': item_999})
            self.tactic = 'Frenzy'


# Class that sticks together all variables needed to run the game.
class Game:
    def __init__(self):
        self.hero = {'dwarf1': Hero('dwarf'), 'dwarf2': Hero('dwarf'), 'dwarf3': Hero('dwarf')}
        self.enemy = {'goblin1': Hero('goblin'), 'goblin2': Hero('goblin'), 'goblin3': Hero('goblin')}
        self.backpack = []
        self.item_dict = item_dict
        self.ability_dict = ability_dict
        self.days = 10000
        self.difficulty = None


@app.route('/', methods=['GET', 'POST'])
def homepage():
    
    if 'key' not in session:
        session['key'] = uuid.uuid4()

    return render_template('homepage.html')


@app.route('/difficulty', methods=['GET', 'POST'])
def difficulty_setting():
    
    games[session['key']] = Game()
    
    return render_template('difficulty.html')


@app.route('/ending', methods=['GET', 'POST'])
def ending():

    if request.method == 'POST':

        if request.form.get('ending', False) == 'Banish the goblins':
            ending_type = 'good ending'
            return render_template('ending.html', ending_type=ending_type)

        elif request.form.get('ending', False) == 'The goblins grow restless...':
            ending_type = 'normal ending plus'
            return render_template('ending.html', ending_type=ending_type)

        elif request.form.get('ending', False) == 'For this we shall not stand! To arms, brothers!':
            ending_type = 'normal ending minus'
            return render_template('ending.html', ending_type=ending_type)

        elif request.form.get('ending', False) == '. . .':
            ending_type = 'bad ending'
            return render_template('ending.html', ending_type=ending_type)

        elif request.form.get('secret ending fail', False) == 'Sacrifice':
            ending_type = 'weak sacrifice'
            return render_template('ending.html', ending_type=ending_type)

        elif request.form.get('secret ending', False) == 'Sacrifice':
            ending_type = 'eclipse'
            return render_template('ending.html', ending_type=ending_type)


@app.route('/game', methods=['GET', 'POST'])
def game():

    game = games[session['key']]

    if request.method == 'POST':

        # Difficulty setting
        if request.form.get('game_start', False) == 'Copper Soft':
            update_equipment('dwarf1')
            update_equipment('dwarf2')
            update_equipment('dwarf3')
            update_stats('dwarf1')
            update_stats('dwarf2')
            update_stats('dwarf3')
            game_mode_easy()

        elif request.form.get('game_start', False) == 'Steel Solid':
            update_equipment('dwarf1')
            update_equipment('dwarf2')
            update_equipment('dwarf3')
            update_stats('dwarf1')
            update_stats('dwarf2')
            update_stats('dwarf3')
            game_mode_normal()

        elif request.form.get('game_start', False) == 'Adamantite Hard':
            update_equipment('dwarf1')
            update_equipment('dwarf2')
            update_equipment('dwarf3')
            update_stats('dwarf1')
            update_stats('dwarf2')
            update_stats('dwarf3')
            game_mode_hard()

        elif request.form.get('game_start', False) == 'Dwarves must perish!':
            update_equipment('dwarf1')
            update_equipment('dwarf2')
            update_equipment('dwarf3')
            update_stats('dwarf1')
            update_stats('dwarf2')
            update_stats('dwarf3')
            game_mode_death()

        # Series of return renders
        elif request.form.get('back', False) == 'Victory!' or \
                request.form.get('back', False) == 'Retreat' or \
                request.form.get('back', False) == 'Return back home' or \
                request.form.get('back', False) == 'Return':
            return render_template('game.html', game=game)

        elif request.form.get('cursed_amulet dwarf1', False) == 'Take the amulet':
            if game.hero['dwarf1'].cursed_amulet_taken is not True:
                game.backpack += [item_404]
                game.hero['dwarf1'].cursed_amulet_taken = True

        elif request.form.get('cursed_amulet dwarf2', False) == 'Take the amulet':
            if game.hero['dwarf2'].cursed_amulet_taken is not True:
                game.backpack += [item_404]
                game.hero['dwarf2'].cursed_amulet_taken = True

        elif request.form.get('cursed_amulet dwarf3', False) == 'Take the amulet':
            if game.hero['dwarf3'].cursed_amulet_taken is not True:
                game.backpack += [item_404]
                game.hero['dwarf3'].cursed_amulet_taken = True

        elif request.form.get('back-sneak dwarf1', False) == 'Return':
            game.hero['dwarf1'].sneak_confirmed = True

        elif request.form.get('back-sneak dwarf2', False) == 'Return':
            game.hero['dwarf2'].sneak_confirmed = True

        elif request.form.get('back-sneak dwarf3', False) == 'Return':
            game.hero['dwarf3'].sneak_confirmed = True

        #   TRAIN
        #   Deadmines: Become superhuman
        #
        #   HTML form, string  ->  game.hero[dwarf].<stats>
        #
        # Takes an input from the HTML form, adds stats from the input into the dwarf at the cost of days. If the
        # training is too costly (i.e. not enough days left), nothing will happen. Flash error message for this case
        # is to be implemented in the future.

        elif request.form.get('train dwarf1', False) == 'Train':
            train('dwarf1')

        elif request.form.get('train dwarf2', False) == 'Train':
            train('dwarf2')

        elif request.form.get('train dwarf3', False) == 'Train':
            train('dwarf3')

        #   EQUIP
        #   It was a Barbie doll dress up game all along...
        #
        #   game.backpack, array  ->  HTML form, string  ->
        #   game.item_dict, dictionary  ->  game.hero[dwarf].equipment, dictionary
        #
        # Takes a string from HTML form option field (ex. "Leather Cap"), then searches for its object in item_dict
        # which contains reference to all items in the game. Then takes that object and slams it into the
        # corresponding equipment slot, also there's an unequipment call somewhere in the middle. Stuff resets and
        # recalculates at the end, as per tradition.

        elif request.form.get('equipment dwarf1', False) == 'Equip':
            equip('dwarf1')

        elif request.form.get('equipment dwarf2', False) == 'Equip':
            equip('dwarf2')

        elif request.form.get('equipment dwarf3', False) == 'Equip':
            equip('dwarf3')

        #   UNEQUIP
        #   For peeling the dwarves out of their juicy equipment.
        #
        #   HTML form, string  ->  game.hero[dwarf].equipment
        #
        # Takes a string from HTML form option field (ex. "Leather Cap") and searches for it in the corresponding
        # dwarf's equipment. Puts it into his backpack and deletes it from the equipment. Because both objects
        # already have the actual object of the item inside them, there's no need to cross-reference anything with
        # the help of item_dict.

        elif request.form.get('equipment dwarf1', False) == 'Unequip':
            unequip('dwarf1')

        elif request.form.get('equipment dwarf2', False) == 'Unequip':
            unequip('dwarf2')

        elif request.form.get('equipment dwarf3', False) == 'Unequip':
            unequip('dwarf3')

        #   ADVENTURE
        #   Your only source of loot.
        #
        #   random.choices()  ->  game.backpack
        #
        #   Randomises and distributes loot from adventures depending on its scale (cost in days).

        elif request.form.get('adventure', False) == 'Short venture':

            odds = random.randint(1, 100)
            temp_days = 15
            spoils = []

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils += random.choices(item_list_weapon_common, k=1)
                spoils += random.choices(item_list_headpiece_common, k=1)
                spoils += random.choices(item_list_shoulders_common, k=1)
                spoils += random.choices(item_list_chest_common, k=1)
                spoils += random.choices(item_list_pants_common, k=1)
                spoils += random.choices(item_list_gloves_common, k=1)
                spoils += random.choices(item_list_boots_common, k=1)
                spoils += random.choices(item_list_artifact_common, k=1)
            elif 46 <= odds <= 80:
                spoils = random.choices(item_list_common, k=4) + random.choices(item_list_rare, k=3)
            elif 81 <= odds <= 95:
                spoils += random.choices(item_list_weapon_rare, k=1)
                spoils += random.choices(item_list_headpiece_rare, k=1)
                spoils += random.choices(item_list_shoulders_rare, k=1)
                spoils += random.choices(item_list_chest_rare, k=1)
                spoils += random.choices(item_list_pants_rare, k=1)
                spoils += random.choices(item_list_gloves_rare, k=1)
                spoils += random.choices(item_list_boots_rare, k=1)
                spoils += random.choices(item_list_artifact_rare, k=1)
            else:
                spoils += random.choices(item_list_weapon_common, k=1)
                spoils += random.choices(item_list_headpiece_common, k=1)
                spoils += random.choices(item_list_shoulders_common, k=1)
                spoils += random.choices(item_list_chest_common, k=1)
                spoils += random.choices(item_list_pants_common, k=1)
                spoils += random.choices(item_list_gloves_common, k=1)
                spoils += random.choices(item_list_boots_common, k=1)
                spoils += [item_777]

            game.days -= temp_days
            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Risky adventure':

            odds = random.randint(1, 100)
            temp_days = 30
            spoils = []

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils += random.choices(item_list_weapon_rare, k=1)
                spoils += random.choices(item_list_headpiece_rare, k=1)
                spoils += random.choices(item_list_shoulders_rare, k=1)
                spoils += random.choices(item_list_chest_rare, k=1)
                spoils += random.choices(item_list_pants_rare, k=1)
                spoils += random.choices(item_list_gloves_rare, k=1)
                spoils += random.choices(item_list_boots_rare, k=1)
                spoils += random.choices(item_list_artifact_rare, k=1)
            elif 46 <= odds <= 80:
                spoils = random.choices(item_list_rare, k=4) + random.choices(item_list_epic, k=3)
            elif 81 <= odds <= 95:
                spoils += random.choices(item_list_weapon_epic, k=1)
                spoils += random.choices(item_list_headpiece_epic, k=1)
                spoils += random.choices(item_list_shoulders_epic, k=1)
                spoils += random.choices(item_list_chest_epic, k=1)
                spoils += random.choices(item_list_pants_epic, k=1)
                spoils += random.choices(item_list_gloves_epic, k=1)
                spoils += random.choices(item_list_boots_epic, k=1)
                spoils += random.choices(item_list_artifact_epic, k=1)
            else:
                spoils = random.choices(item_list_legendary, k=1)

            game.days -= temp_days
            game.backpack += spoils

        elif request.form.get('adventure', False) == 'Legendary expedition':

            odds = random.randint(1, 100)
            temp_days = 60
            spoils = []

            if game.days - temp_days <= 0:
                return render_template('game.html', game=game)

            if 1 <= odds <= 45:
                spoils += random.choices(item_list_weapon_epic, k=1)
                spoils += random.choices(item_list_headpiece_epic, k=1)
                spoils += random.choices(item_list_shoulders_epic, k=1)
                spoils += random.choices(item_list_chest_epic, k=1)
                spoils += random.choices(item_list_pants_epic, k=1)
                spoils += random.choices(item_list_gloves_epic, k=1)
                spoils += random.choices(item_list_boots_epic, k=1)
                spoils += random.choices(item_list_artifact_epic, k=1)
            elif 46 <= odds <= 80:
                spoils = random.choices(item_list_epic, k=4) + random.choices(item_list_legendary, k=1)
            elif 81 <= odds <= 95:
                random.choices(item_list_legendary, k=3)
            else:
                spoils = random.choices(item_list_cursed, k=1)

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
    game = games[session['key']]

    # Updates multipliers and bonuses values based on current equipment
    for item_slot, item_name in game.hero[dwarf].equipment.items():
        if item_name is not None:

            rounded = game.hero[dwarf].str_mul + game.hero[dwarf].equipment[
                item_slot].str_mul
            game.hero[dwarf].str_mul = round(rounded, 2)
            game.hero[dwarf].str_bonus += game.hero[dwarf].equipment[
                item_slot].str_bonus

            rounded = game.hero[dwarf].int_mul + game.hero[dwarf].equipment[
                item_slot].int_mul
            game.hero[dwarf].int_mul = round(rounded, 2)
            game.hero[dwarf].int_bonus += game.hero[dwarf].equipment[
                item_slot].int_bonus

            rounded = game.hero[dwarf].agi_mul + game.hero[dwarf].equipment[
                item_slot].agi_mul
            game.hero[dwarf].agi_mul = round(rounded, 2)
            game.hero[dwarf].agi_bonus += game.hero[dwarf].equipment[
                item_slot].agi_bonus

            rounded = game.hero[dwarf].will_mul + game.hero[dwarf].equipment[
                item_slot].will_mul
            game.hero[dwarf].will_mul = round(rounded, 2)
            game.hero[dwarf].will_bonus += game.hero[dwarf].equipment[
                item_slot].will_bonus

            rounded = game.hero[dwarf].end_mul + game.hero[dwarf].equipment[
                item_slot].end_mul
            game.hero[dwarf].end_mul = round(rounded, 2)
            game.hero[dwarf].end_bonus += game.hero[dwarf].equipment[
                item_slot].end_bonus

            rounded = game.hero[dwarf].char_mul + game.hero[dwarf].equipment[
                item_slot].char_mul
            game.hero[dwarf].char_mul = round(rounded, 2)
            game.hero[dwarf].char_bonus += game.hero[dwarf].equipment[
                item_slot].char_bonus

            rounded = game.hero[dwarf].lck_mul + game.hero[dwarf].equipment[
                item_slot].lck_mul
            game.hero[dwarf].lck_mul = round(rounded, 2)
            game.hero[dwarf].lck_bonus += game.hero[dwarf].equipment[
                item_slot].lck_bonus

            rounded = game.hero[dwarf].spd_mul + game.hero[dwarf].equipment[
                item_slot].spd_mul
            game.hero[dwarf].spd_mul = round(rounded, 2)
            game.hero[dwarf].spd_bonus += game.hero[dwarf].equipment[
                item_slot].spd_bonus

            game.hero[dwarf].armor += game.hero[dwarf].equipment[item_slot].armor

            if game.hero[dwarf].equipment[item_slot].special is not None:
                game.hero[dwarf].specials_list.append(
                    game.hero[dwarf].equipment[item_slot].special)


def update_equipment_enemy(goblin):
    game = games[session['key']]

    # Updates multipliers and bonuses values based on current equipment
    for item_slot, item_name in game.enemy[goblin].equipment.items():
        if item_name is not None:

            rounded = game.enemy[goblin].str_mul + game.enemy[goblin].equipment[
                item_slot].str_mul
            game.enemy[goblin].str_mul = round(rounded, 2)
            game.enemy[goblin].str_bonus += game.enemy[goblin].equipment[
                item_slot].str_bonus

            rounded = game.enemy[goblin].int_mul + game.enemy[goblin].equipment[
                item_slot].int_mul
            game.enemy[goblin].int_mul = round(rounded, 2)
            game.enemy[goblin].int_bonus += game.enemy[goblin].equipment[
                item_slot].int_bonus

            rounded = game.enemy[goblin].agi_mul + game.enemy[goblin].equipment[
                item_slot].agi_mul
            game.enemy[goblin].agi_mul = round(rounded, 2)
            game.enemy[goblin].agi_bonus += game.enemy[goblin].equipment[
                item_slot].agi_bonus

            rounded = game.enemy[goblin].will_mul + game.enemy[goblin].equipment[
                item_slot].will_mul
            game.enemy[goblin].will_mul = round(rounded, 2)
            game.enemy[goblin].will_bonus += game.enemy[goblin].equipment[
                item_slot].will_bonus

            rounded = game.enemy[goblin].end_mul + game.enemy[goblin].equipment[
                item_slot].end_mul
            game.enemy[goblin].end_mul = round(rounded, 2)
            game.enemy[goblin].end_bonus += game.enemy[goblin].equipment[
                item_slot].end_bonus

            rounded = game.enemy[goblin].char_mul + game.enemy[goblin].equipment[
                item_slot].char_mul
            game.enemy[goblin].char_mul = round(rounded, 2)
            game.enemy[goblin].char_bonus += game.enemy[goblin].equipment[
                item_slot].char_bonus

            rounded = game.enemy[goblin].lck_mul + game.enemy[goblin].equipment[
                item_slot].lck_mul
            game.enemy[goblin].lck_mul = round(rounded, 2)
            game.enemy[goblin].lck_bonus += game.enemy[goblin].equipment[
                item_slot].lck_bonus

            rounded = game.enemy[goblin].spd_mul + game.enemy[goblin].equipment[
                item_slot].spd_mul
            game.enemy[goblin].spd_mul = round(rounded, 2)
            game.enemy[goblin].spd_bonus += game.enemy[goblin].equipment[
                item_slot].spd_bonus

            game.enemy[goblin].armor += game.enemy[goblin].equipment[item_slot].armor

            if game.enemy[goblin].equipment[item_slot].special is not None:
                game.enemy[goblin].specials_list.append(
                    game.enemy[goblin].equipment[item_slot].special)


def stat_reset(dwarf):
    game = games[session['key']]

    # Resets all stats before equipment update
    game.hero[dwarf].str_mul = game.hero[dwarf].int_mul = game.hero[
        dwarf].agi_mul = game.hero[dwarf].will_mul = 1.0
    game.hero[dwarf].end_mul = game.hero[dwarf].char_mul = game.hero[
        dwarf].lck_mul = game.hero[dwarf].spd_mul = 1.0
    game.hero[dwarf].str_bonus = game.hero[dwarf].int_bonus = \
        game.hero[dwarf].agi_bonus = 0
    game.hero[dwarf].end_bonus = game.hero[dwarf].char_bonus = \
        game.hero[dwarf].lck_bonus = 0
    game.hero[dwarf].will_bonus = game.hero[dwarf].spd_bonus = 0
    game.hero[dwarf].armor = 0
    game.hero[dwarf].specials_list.clear()


def update_stats(dwarf):
    game = games[session['key']]

    # Updates total stats based on the bases, multipliers and bonuses
    if game.hero[dwarf].str_mul <= 0.0:
        game.hero[dwarf].str_mul = 0.1
    game.hero[dwarf].str_total = round(
        game.hero[dwarf].strength * game.hero[dwarf].str_mul +
        game.hero[dwarf].str_bonus)
    if game.hero[dwarf].str_total <= 0:
        game.hero[dwarf].str_total = 1

    if game.hero[dwarf].int_mul <= 0.0:
        game.hero[dwarf].int_mul = 0.1
    game.hero[dwarf].int_total = round(
        game.hero[dwarf].intelligence * game.hero[dwarf].int_mul +
        game.hero[dwarf].int_bonus)
    if game.hero[dwarf].int_total <= 0:
        game.hero[dwarf].int_total = 1

    if game.hero[dwarf].agi_mul <= 0.0:
        game.hero[dwarf].agi_mul = 0.1
    game.hero[dwarf].agi_total = round(
        game.hero[dwarf].agility * game.hero[dwarf].agi_mul +
        game.hero[dwarf].agi_bonus)
    if game.hero[dwarf].agi_total <= 0:
        game.hero[dwarf].agi_total = 1

    if game.hero[dwarf].will_mul <= 0.0:
        game.hero[dwarf].will_mul = 0.1
    game.hero[dwarf].will_total = round(
        game.hero[dwarf].willpower * game.hero[dwarf].will_mul +
        game.hero[dwarf].will_bonus)
    if game.hero[dwarf].will_total <= 0:
        game.hero[dwarf].will_total = 1

    if game.hero[dwarf].end_mul <= 0.0:
        game.hero[dwarf].end_mul = 0.1
    game.hero[dwarf].end_total = round(
        game.hero[dwarf].endurance * game.hero[dwarf].end_mul +
        game.hero[dwarf].end_bonus)
    if game.hero[dwarf].end_total <= 0:
        game.hero[dwarf].end_total = 1

    if game.hero[dwarf].char_mul <= 0.0:
        game.hero[dwarf].char_mul = 0.1
    game.hero[dwarf].char_total = round(
        game.hero[dwarf].charisma * game.hero[dwarf].char_mul +
        game.hero[dwarf].char_bonus)
    if game.hero[dwarf].char_total <= 0:
        game.hero[dwarf].char_total = 1

    if game.hero[dwarf].lck_mul <= 0.0:
        game.hero[dwarf].lck_mul = 0.1
    game.hero[dwarf].lck_total = round(
        game.hero[dwarf].luck * game.hero[dwarf].lck_mul + game.hero[
            dwarf].lck_bonus)
    if game.hero[dwarf].lck_total <= 0:
        game.hero[dwarf].lck_total = 1

    if game.hero[dwarf].spd_mul <= 0.0:
        game.hero[dwarf].spd_mul = 0.1
    game.hero[dwarf].spd_total = round(
        game.hero[dwarf].speed * game.hero[dwarf].spd_mul +
        game.hero[dwarf].spd_bonus)
    if game.hero[dwarf].spd_total <= 0:
        game.hero[dwarf].spd_total = 1


def update_stats_enemy(goblin):
    game = games[session['key']]

    # Updates total stats based on the bases, multipliers and bonuses (but for goblins)
    # "Wow having separate functions for dwarves and goblins is like racist and stuff."
    if game.enemy[goblin].str_mul <= 0.0:
        game.enemy[goblin].str_mul = 0.1
    game.enemy[goblin].str_total = round(
        game.enemy[goblin].strength * game.enemy[goblin].str_mul +
        game.enemy[goblin].str_bonus)
    if game.enemy[goblin].str_total <= 0:
        game.enemy[goblin].str_total = 1

    if game.enemy[goblin].int_mul <= 0.0:
        game.enemy[goblin].int_mul = 0.1
    game.enemy[goblin].int_total = round(
        game.enemy[goblin].intelligence * game.enemy[goblin].int_mul +
        game.enemy[goblin].int_bonus)
    if game.enemy[goblin].int_total <= 0:
        game.enemy[goblin].int_total = 1

    if game.enemy[goblin].agi_mul <= 0.0:
        game.enemy[goblin].agi_mul = 0.1
    game.enemy[goblin].agi_total = round(
        game.enemy[goblin].agility * game.enemy[goblin].agi_mul +
        game.enemy[goblin].agi_bonus)
    if game.enemy[goblin].agi_total <= 0:
        game.enemy[goblin].agi_total = 1

    if game.enemy[goblin].will_mul <= 0.0:
        game.enemy[goblin].will_mul = 0.1
    game.enemy[goblin].will_total = round(
        game.enemy[goblin].willpower * game.enemy[goblin].will_mul +
        game.enemy[goblin].will_bonus)
    if game.enemy[goblin].will_total <= 0:
        game.enemy[goblin].will_total = 1

    if game.enemy[goblin].end_mul <= 0.0:
        game.enemy[goblin].end_mul = 0.1
    game.enemy[goblin].end_total = round(
        game.enemy[goblin].endurance * game.enemy[goblin].end_mul +
        game.enemy[goblin].end_bonus)
    if game.enemy[goblin].end_total <= 0:
        game.enemy[goblin].end_total = 1

    if game.enemy[goblin].char_mul <= 0.0:
        game.enemy[goblin].char_mul = 0.1
    game.enemy[goblin].char_total = round(
        game.enemy[goblin].charisma * game.enemy[goblin].char_mul +
        game.enemy[goblin].char_bonus)
    if game.enemy[goblin].char_total <= 0:
        game.enemy[goblin].char_total = 1

    if game.enemy[goblin].lck_mul <= 0.0:
        game.enemy[goblin].lck_mul = 0.1
    game.enemy[goblin].lck_total = round(
        game.enemy[goblin].luck * game.enemy[goblin].lck_mul +
        game.enemy[goblin].lck_bonus)
    if game.enemy[goblin].lck_total <= 0:
        game.enemy[goblin].lck_total = 1

    if game.enemy[goblin].spd_mul <= 0.0:
        game.enemy[goblin].spd_mul = 0.1
    game.enemy[goblin].spd_total = round(
        game.enemy[goblin].speed * game.enemy[goblin].spd_mul +
        game.enemy[goblin].spd_bonus)
    if game.enemy[goblin].spd_total <= 0:
        game.enemy[goblin].spd_total = 1


def train(dwarf):
    game = games[session['key']]

    if request.form.get("str_increase") != '':
        strength = int(request.form.get("str_increase"))
    else:
        strength = 0
    if request.form.get("int_increase") != '':
        intelligence = int(request.form.get("int_increase"))
    else:
        intelligence = 0
    if request.form.get("agi_increase") != '':
        agility = int(request.form.get("agi_increase"))
    else:
        agility = 0
    if request.form.get("will_increase") != '':
        willpower = int(request.form.get("will_increase"))
    else:
        willpower = 0
    if request.form.get("end_increase") != '':
        endurance = int(request.form.get("end_increase"))
    else:
        endurance = 0
    if request.form.get("char_increase") != '':
        charisma = int(request.form.get("char_increase"))
    else:
        charisma = 0
    if request.form.get("lck_increase") != '':
        luck = int(request.form.get("lck_increase"))
    else:
        luck = 0
    if request.form.get("spd_increase") != '':
        speed = int(request.form.get("spd_increase"))
    else:
        speed = 0

    temp_days = strength * 2 + intelligence * 2 + agility + willpower + endurance * 3 + charisma + luck + speed * 3

    if game.days - temp_days <= 0:
        return render_template('game.html', game=game)

    game.hero[dwarf].strength += strength
    game.hero[dwarf].intelligence += intelligence
    game.hero[dwarf].agility += agility
    game.hero[dwarf].willpower += willpower
    game.hero[dwarf].endurance += endurance
    game.hero[dwarf].charisma += charisma
    game.hero[dwarf].luck += luck
    game.hero[dwarf].speed += speed

    update_stats(dwarf)

    game.days -= temp_days


def unequip(dwarf):
    game = games[session['key']]

    for key, value in game.hero[dwarf].equipment.items():
        if value is not None:
            game.backpack.append(value)
    game.hero[dwarf].equipment.update(
        {'Weapon': None, 'Headpiece': None, 'Shoulders': None, 'Chest': None, 'Pants': None, 'Gloves': None,
         'Boots': None, 'Artifact': None})

    stat_reset(dwarf)
    update_stats(dwarf)


def equip(dwarf):
    game = games[session['key']]

    # Declaring stuff cuz otherwise PyCharm screams, even though there's no way for these to ever be unassigned I think.
    weapon = headpiece = shoulders = chest = pants = gloves = boots = artifact = None

    # Iterating through global item dictionary in search for objects.
    for key, value in game.item_dict.items():
        if key == request.form.get("Weapon"):
            weapon = value
            game.backpack.remove(value)
        elif key == request.form.get("Headpiece"):
            headpiece = value
            game.backpack.remove(value)
        elif key == request.form.get("Shoulders"):
            shoulders = value
            game.backpack.remove(value)
        elif key == request.form.get("Chest"):
            chest = value
            game.backpack.remove(value)
        elif key == request.form.get("Pants"):
            pants = value
            game.backpack.remove(value)
        elif key == request.form.get("Gloves"):
            gloves = value
            game.backpack.remove(value)
        elif key == request.form.get("Boots"):
            boots = value
            game.backpack.remove(value)
        elif key == request.form.get("Artifact"):
            artifact = value
            game.backpack.remove(value)

    # Sneaky unequipment call before we overwrite the current one.
    # Unnecessary stat refresh as part of the package that is unequip()
    unequip(dwarf)

    # Assigning items from the library to the equipment dictionary.
    if request.form.get("Weapon") is not None:
        game.hero[dwarf].equipment.update({'Weapon': weapon})

    if request.form.get("Headpiece") is not None:
        game.hero[dwarf].equipment.update({'Headpiece': headpiece})

    if request.form.get("Shoulders") is not None:
        game.hero[dwarf].equipment.update({'Shoulders': shoulders})

    if request.form.get("Chest") is not None:
        game.hero[dwarf].equipment.update({'Chest': chest})

    if request.form.get("Gloves") is not None:
        game.hero[dwarf].equipment.update({'Gloves': gloves})

    if request.form.get("Pants") is not None:
        game.hero[dwarf].equipment.update({'Pants': pants})

    if request.form.get("Boots") is not None:
        game.hero[dwarf].equipment.update({'Boots': boots})

    if request.form.get("Artifact") is not None:
        game.hero[dwarf].equipment.update({'Artifact': artifact})

    # Refreshing stats
    stat_reset(dwarf)
    update_equipment(dwarf)
    update_stats(dwarf)


def game_mode_easy():
    game = games[session['key']]

    for goblin in game.enemy:
        game.enemy[goblin].strength = random.randint(15, 25)
        game.enemy[goblin].intelligence = random.randint(15, 25)
        game.enemy[goblin].agility = random.randint(25, 35)
        game.enemy[goblin].willpower = random.randint(25, 35)
        game.enemy[goblin].endurance = 1000
        game.enemy[goblin].charisma = random.randint(25, 35)
        game.enemy[goblin].luck = random.randint(25, 35)
        game.enemy[goblin].speed = random.randint(15, 25)

        game.enemy[goblin].equipment["Weapon"] = item_154
        game.enemy[goblin].equipment["Headpiece"] = random.choice(item_list_headpiece_common)
        game.enemy[goblin].equipment["Shoulders"] = random.choice(item_list_shoulders_common)
        game.enemy[goblin].equipment["Chest"] = random.choice(item_list_chest_common)
        game.enemy[goblin].equipment["Pants"] = random.choice(item_list_pants_common)
        game.enemy[goblin].equipment["Gloves"] = random.choice(item_list_gloves_common)
        game.enemy[goblin].equipment["Boots"] = random.choice(item_list_boots_common)

        update_equipment_enemy(goblin)
        update_stats_enemy(goblin)
        game.difficulty = "easy"


def game_mode_normal():
    game = games[session['key']]

    for goblin in game.enemy:
        game.enemy[goblin].strength = random.randint(25, 40)
        game.enemy[goblin].intelligence = random.randint(25, 40)
        game.enemy[goblin].agility = random.randint(35, 50)
        game.enemy[goblin].willpower = random.randint(35, 50)
        game.enemy[goblin].endurance = random.randint(45, 70)
        game.enemy[goblin].charisma = random.randint(50, 75)
        game.enemy[goblin].luck = random.randint(50, 75)
        game.enemy[goblin].speed = random.randint(25, 35)

        game.enemy[goblin].equipment["Weapon"] = random.choice(item_list_weapon_epic)
        game.enemy[goblin].equipment["Headpiece"] = random.choice(item_list_headpiece_rare)
        game.enemy[goblin].equipment["Shoulders"] = random.choice(item_list_shoulders_rare)
        game.enemy[goblin].equipment["Chest"] = random.choice(item_list_chest_rare)
        game.enemy[goblin].equipment["Pants"] = random.choice(item_list_pants_rare)
        game.enemy[goblin].equipment["Gloves"] = random.choice(item_list_gloves_rare)
        game.enemy[goblin].equipment["Boots"] = random.choice(item_list_boots_rare)

        update_equipment_enemy(goblin)
        update_stats_enemy(goblin)
        game.difficulty = "normal"


def game_mode_hard():
    game = games[session['key']]

    for goblin in game.enemy:
        game.enemy[goblin].strength = random.randint(25, 40)
        game.enemy[goblin].intelligence = random.randint(25, 40)
        game.enemy[goblin].agility = random.randint(35, 50)
        game.enemy[goblin].willpower = random.randint(35, 50)
        game.enemy[goblin].endurance = random.randint(45, 70)
        game.enemy[goblin].charisma = random.randint(50, 75)
        game.enemy[goblin].luck = random.randint(50, 75)
        game.enemy[goblin].speed = random.randint(25, 35)

        game.enemy[goblin].equipment["Weapon"] = random.choice(item_list_weapon_rare)
        game.enemy[goblin].equipment["Headpiece"] = random.choice(item_list_headpiece_common)
        game.enemy[goblin].equipment["Shoulders"] = random.choice(item_list_shoulders_common)
        game.enemy[goblin].equipment["Chest"] = random.choice(item_list_chest_common)
        game.enemy[goblin].equipment["Pants"] = random.choice(item_list_pants_common)
        game.enemy[goblin].equipment["Gloves"] = random.choice(item_list_gloves_common)
        game.enemy[goblin].equipment["Boots"] = random.choice(item_list_boots_common)

        update_equipment_enemy(goblin)
        update_stats_enemy(goblin)
        game.difficulty = "hard"


def game_mode_death():
    game = games[session['key']]

    # TO DO LATER
    # I will make around 20 custom-built goblins made out of most broken builds I can think of :)
    for goblin in game.enemy:
        game.enemy[goblin].strength = random.randint(25, 40)
        game.enemy[goblin].intelligence = random.randint(25, 40)
        game.enemy[goblin].agility = random.randint(35, 50)
        game.enemy[goblin].willpower = random.randint(35, 50)
        game.enemy[goblin].endurance = random.randint(45, 70)
        game.enemy[goblin].charisma = random.randint(50, 75)
        game.enemy[goblin].luck = random.randint(50, 75)
        game.enemy[goblin].speed = random.randint(25, 35)

        game.enemy[goblin].equipment["Weapon"] = random.choice(item_list_weapon_rare)
        game.enemy[goblin].equipment["Headpiece"] = random.choice(item_list_headpiece_common)
        game.enemy[goblin].equipment["Shoulders"] = random.choice(item_list_shoulders_common)
        game.enemy[goblin].equipment["Chest"] = random.choice(item_list_chest_common)
        game.enemy[goblin].equipment["Pants"] = random.choice(item_list_pants_common)
        game.enemy[goblin].equipment["Gloves"] = random.choice(item_list_gloves_common)
        game.enemy[goblin].equipment["Boots"] = random.choice(item_list_boots_common)

        update_equipment_enemy(goblin)
        update_stats_enemy(goblin)
        game.difficulty = "death"


@app.route('/battleground', methods=['GET', 'POST'])
def battleground():
    game = games[session['key']]

    if request.method == 'POST':

        if request.form.get('battle dwarf1', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf1', goblin='goblin1',
                                   battlelog=battle('dwarf1', 'goblin1'))

        elif request.form.get('battle dwarf2', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf2', goblin='goblin2',
                                   battlelog=battle('dwarf2', 'goblin2'))

        elif request.form.get('battle dwarf3', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf3', goblin='goblin3',
                                   battlelog=battle('dwarf3', 'goblin3'))

        elif request.form.get('white_lotus dwarf1', False) == 'Take the flower':
            if game.hero['dwarf1'].white_lotus_taken is not True:
                game.backpack += [item_555]
                game.hero['dwarf1'].white_lotus_taken = True
            return render_template('battle.html', game=game, dwarf='dwarf1', goblin='goblin1')

        elif request.form.get('white_lotus dwarf2', False) == 'Take the flower':
            if game.hero['dwarf2'].white_lotus_taken is not True:
                game.backpack += [item_555]
                game.hero['dwarf2'].white_lotus_taken = True
            return render_template('battle.html', game=game, dwarf='dwarf2', goblin='goblin2')

        elif request.form.get('white_lotus dwarf3', False) == 'Take the flower':
            if game.hero['dwarf3'].white_lotus_taken is not True:
                game.backpack += [item_555]
                game.hero['dwarf3'].white_lotus_taken = True
            return render_template('battle.html', game=game, dwarf='dwarf3', goblin='goblin3')

        elif request.form.get('go_to_cursed_amulet dwarf1', False) == 'Return':
            game.hero['dwarf1'].cursed_amulet = True
            return render_template('special.html', game=game, dwarf='dwarf1', cursed_amulet=True)

        elif request.form.get('go_to_cursed_amulet dwarf2', False) == 'Return':
            game.hero['dwarf2'].cursed_amulet = True
            return render_template('special.html', game=game, dwarf='dwarf2', cursed_amulet=True)

        elif request.form.get('go_to_cursed_amulet dwarf3', False) == 'Return':
            game.hero['dwarf3'].cursed_amulet = True
            return render_template('special.html', game=game, dwarf='dwarf3', cursed_amulet=True)

        elif request.form.get('sneak dwarf1', False) == 'Sneak':
            if game.hero['dwarf1'].sneak is False:
                game.enemy["goblin1"].str_total *= 0.75
                game.enemy["goblin1"].int_total *= 0.75
                game.enemy["goblin1"].agi_total *= 0.75
                game.enemy["goblin1"].will_total *= 0.75
                game.enemy["goblin1"].end_total *= 0.75
                game.enemy["goblin1"].char_total *= 0.75
                game.enemy["goblin1"].lck_total *= 0.75
                game.enemy["goblin1"].spd_total *= 0.75
                game.hero['dwarf1'].sneak = True
            return render_template('special.html', game=game, dwarf='dwarf1', sneak=True)

        elif request.form.get('sneak dwarf2', False) == 'Sneak':
            if game.hero['dwarf2'].sneak is False:
                game.enemy["goblin2"].str_total *= 0.75
                game.enemy["goblin2"].int_total *= 0.75
                game.enemy["goblin2"].agi_total *= 0.75
                game.enemy["goblin2"].will_total *= 0.75
                game.enemy["goblin2"].end_total *= 0.75
                game.enemy["goblin2"].char_total *= 0.75
                game.enemy["goblin2"].lck_total *= 0.75
                game.enemy["goblin2"].spd_total *= 0.75
                game.hero['dwarf2'].sneak = True
            return render_template('special.html', game=game, dwarf='dwarf2', sneak=True)

        elif request.form.get('sneak dwarf3', False) == 'Sneak':
            if game.hero['dwarf3'].sneak is False:
                game.enemy["goblin3"].str_total *= 0.75
                game.enemy["goblin3"].int_total *= 0.75
                game.enemy["goblin3"].agi_total *= 0.75
                game.enemy["goblin3"].will_total *= 0.75
                game.enemy["goblin3"].end_total *= 0.75
                game.enemy["goblin3"].char_total *= 0.75
                game.enemy["goblin3"].lck_total *= 0.75
                game.enemy["goblin3"].spd_total *= 0.75
                game.hero['dwarf3'].sneak = True
            return render_template('special.html', game=game, dwarf='dwarf3', sneak=True)

        # I need dwarf=dwarf for the return button to send to the correct HTML ID element.
        # It's the little things, you know.
        elif request.form.get('spy dwarf1', False) == 'Spy':
            return render_template('special.html', game=game, dwarf='dwarf1', goblin='goblin1',
                                   spy=True)

        elif request.form.get('spy dwarf2', False) == 'Spy':
            return render_template('special.html', game=game, dwarf='dwarf2', goblin='goblin2',
                                   spy=True)

        elif request.form.get('spy dwarf3', False) == 'Spy':
            return render_template('special.html', game=game, dwarf='dwarf3', goblin='goblin3',
                                   spy=True)


def battle(dwarf, goblin):
    game = games[session['key']]

    battle_log = []
    win_condition = False

    dwarf_name = game.hero[dwarf].hero_name

    dwarf_physical = game.hero[dwarf].str_total * 3
    dwarf_magical = game.hero[dwarf].int_total * 4

    dwarf_speed = game.hero[dwarf].spd_total
    dwarf_speed_base = game.hero[dwarf].spd_total
    dwarf_charisma = game.hero[dwarf].char_total
    dwarf_luck = game.hero[dwarf].lck_total
    dwarf_willpower = game.hero[dwarf].will_total
    dwarf_agility = game.hero[dwarf].agi_total
    dwarf_strength = game.hero[dwarf].str_total
    dwarf_intelligence = game.hero[dwarf].int_total

    dwarf_armor = game.hero[dwarf].armor
    dwarf_health = game.hero[dwarf].end_total * 10
    dwarf_max_health = game.hero[dwarf].end_total * 10

    dwarf_tactic = game.hero[dwarf].tactic

    dwarf_special_attack_charge = 1
    dwarf_special_attack_next = False

    goblin_name = game.enemy[goblin].hero_name

    goblin_physical = game.enemy[goblin].str_total * 3
    goblin_magical = game.enemy[goblin].int_total * 4

    goblin_speed = game.enemy[goblin].spd_total
    goblin_speed_base = game.enemy[goblin].spd_total
    goblin_charisma = game.enemy[goblin].char_total
    goblin_luck = game.enemy[goblin].lck_total
    goblin_willpower = game.enemy[goblin].will_total
    goblin_agility = game.enemy[goblin].agi_total
    goblin_strength = game.enemy[goblin].str_total
    goblin_intelligence = game.enemy[goblin].int_total

    goblin_armor = game.enemy[goblin].armor
    goblin_health = game.enemy[goblin].end_total * 10
    goblin_max_health = game.enemy[goblin].end_total * 10

    goblin_tactic = game.enemy[goblin].tactic

    goblin_special_attack_charge = 1
    goblin_special_attack_next = False

    damage = 1
    reduction_message = 1
    critical_message = dwarf_reduction_message = dwarf_increase_message = goblin_reduction_message = \
        goblin_increase_message = goblin_dodge_message = goblin_absorb_message = dwarf_dodge_message = \
        dwarf_absorb_message = False
    dwarf_reduction = []
    goblin_reduction = []
    dwarf_increase = []
    goblin_increase = []
    attack_message = ''
    absorb_message = ''
    attack_type = []

    dwarf_avoidance_message = False
    dwarf_firebrand_message = False
    dwarf_lifesteal_message = False
    dwarf_hawkeye_message = False
    dwarf_stun_message = False
    dwarf_mindsap_will_message = False
    dwarf_mindsap_int_message = False
    dwarf_soulrend_message = False
    dwarf_souldrain_message = False
    dwarf_earthbound_message = False
    dwarf_mageslayer_message = False
    dwarf_neurotoxin_message = False
    dwarf_multitool_message = False
    dwarf_counterattack_message = False
    goblin_avoidance_message = False
    goblin_firebrand_message = False
    goblin_lifesteal_message = False
    goblin_hawkeye_message = False
    goblin_stun_message = False
    goblin_mindsap_will_message = False
    goblin_mindsap_int_message = False
    goblin_soulrend_message = False
    goblin_souldrain_message = False
    goblin_earthbound_message = False
    goblin_mageslayer_message = False
    goblin_neurotoxin_message = False
    goblin_multitool_message = False
    goblin_counterattack_message = False

    goblin_reload_message = False
    dwarf_reload_message = False
    goblin_reload = False
    dwarf_reload = False
    goblin_warframe_message = False
    dwarf_warframe_message = False
    goblin_neurotoxin_payload = False
    dwarf_neurotoxin_payload = False
    dwarf_self_destruct = 10
    goblin_self_destruct = 10
    lifesteal = 0
    mageslayer = 0
    soulrend = 0
    souldrain = 0
    counterattack = 0
    dwarf_avoidance_stacks = 0
    goblin_avoidance_stacks = 0

    physical_attack_strings = [' <span class="gray">hits</span>', ' <span class="gray">punches</span>',
                               ' <span class="gray">kicks</span>', ' <span class="gray">attacks</span>',
                               ' <span class="gray">strikes</span>']

    better_physical_attack_strings = [' <span class="gray">hits</span>', ' <span class="gray">attacks</span>',
                                      ' <span class="gray">strikes</span>']

    magical_attack_strings = [' <span class="blue">freezes</span>', ' <span class="purple">arcane blasts</span>',
                              ' launches a <span class="orange">fireball</span> at',
                              ' sets <span class="red">aflame</span>',
                              ' <span class="deep_blue">electrocutes</span>']

    better_magical_attack_strings = ' launches a <span class="shadow_bolt">shadow bolt</span>'

    def roll_physical_attack_type(attack, chance):
        attack += ["physical"]
        if chance == 0:
            attack += ["hit"]
        elif chance == 1:
            attack += ["punch"]
        elif chance == 2:
            attack += ["kick"]
        elif chance == 3:
            attack += ["attack"]
        else:
            attack += ["strike"]

        return attack

    def roll_magical_attack_type(attack, chance):
        attack += ["magical"]
        if chance == 0:
            attack += ["freeze"]
        elif chance == 1:
            attack += ["arcane blast"]
        elif chance == 2:
            attack += ["fireball"]
        elif chance == 3:
            attack += ["aflame"]
        else:
            attack += ["electrocute"]

        return attack

    # SPECIAL ABILITIES
    # The ones that do something at the start of the encounter or need to be set up at the start of the encounter.
    if 'Adrenaline' in game.hero[dwarf].specials_list:
        dwarf_speed_base = dwarf_speed_base * 4
        turn = '<div class="hero-turn">' + dwarf_name + ' injects himself with Adrenalinium, ' \
                                                        'increasing his speed tremendously!</div>'
        battle_log.append(turn)

    if 'Adrenaline' in game.enemy[goblin].specials_list:
        goblin_speed_base = goblin_speed_base * 4
        turn = '<div class="enemy-turn">' + goblin_name + ' injects himself with Adrenalinium, ' \
                                                          'increasing his speed tremendously!</div>'
        battle_log.append(turn)

    if 'Mist' in game.hero[dwarf].specials_list:
        dwarf_avoidance_stacks = 4

    if 'Mist' in game.enemy[goblin].specials_list:
        goblin_avoidance_stacks = 4

    if 'Neurotoxin' in game.hero[dwarf].specials_list:
        dwarf_neurotoxin_payload = True

    if 'Neurotoxin' in game.enemy[goblin].specials_list:
        goblin_neurotoxin_payload = True

    if 'Armor Up!' in game.hero[dwarf].specials_list:
        dwarf_armor *= 1.25

    if 'Armor Up!' in game.enemy[goblin].specials_list:
        goblin_armor *= 1.25

    # I put goblin's Authority first, so that if both player and the
    # computer has it, the player will gain more charisma as a recompensation.
    if 'Authority' in game.enemy[goblin].specials_list:
        steal = dwarf_charisma * 0.65
        goblin_charisma += steal

    if 'Authority' in game.hero[dwarf].specials_list:
        steal = goblin_charisma * 0.65
        dwarf_charisma += steal

    if 'Dominion' in game.hero[dwarf].specials_list:
        dwarf_magical += (goblin_willpower + goblin_charisma) * 1.5
        turn = '<div class="hero-turn">' + dwarf_name + "'s magical powers are " \
                                                        "empowered by the Crown of Will!</div>"
        battle_log.append(turn)

    if 'Dominion' in game.enemy[goblin].specials_list:
        goblin_magical += (goblin_willpower + goblin_charisma) * 1.5
        turn = '<div class="goblin-turn">' + goblin_name + "'s magical powers are " \
                                                           "empowered by the Crown of Will!</div>"
        battle_log.append(turn)

    if 'Unstable Concoction' in game.hero[dwarf].specials_list and dwarf_health > 0:
        roll = random.randint(0, 1)
        if roll == 0:
            turn = '<div class="hero-turn">' + dwarf_name + ' throws the concoction at the enemy...!<br>' \
                                                            '...unfortunately, in a freak accident, it splashes ' \
                                                            'right on his face, dealing 250 damage!</div>'
            dwarf_health -= 250
            battle_log.append(turn)
        else:
            turn = '<div class="hero-turn">' + dwarf_name + ' throws the concoction at the enemy...!<br>' \
                                                            '...it hits the opponent, splashing all over him, ' \
                                                            'dealing 250 damage!</div>'
            goblin_health -= 250
            battle_log.append(turn)

    if 'Unstable Concoction' in game.enemy[goblin].specials_list and goblin_health > 0:
        roll = random.randint(0, 1)
        if roll == 0:
            turn = '<div class="enemy-turn">' + goblin_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                              '...fortunately, in a freak accident, it splashes ' \
                                                              'right on his face, dealing 250 damage!</div>'
            goblin_health -= 250
            battle_log.append(turn)
        else:
            turn = '<div class="enemy-turn">' + goblin_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                              '...it hits the opponent, splashing all over him, ' \
                                                              'dealing 250 damage!</div>'
            dwarf_health -= 250
            battle_log.append(turn)

    if 'Pipe Bomb' in game.hero[dwarf].specials_list and dwarf_health > 0:
        roll = random.randint(0, 1)
        if roll == 0:
            turn = '<div class="hero-turn">' + dwarf_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                            '...unfortunately, in a freak accident, it explodes ' \
                                                            'right in his face, dealing 2500 damage!</div>'
            dwarf_health -= 2500
            battle_log.append(turn)
        else:
            turn = '<div class="hero-turn">' + dwarf_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                            '...it hits the opponent, exploding on contact, ' \
                                                            'dealing 2500 damage!</div>'
            goblin_health -= 2500
            battle_log.append(turn)

    if 'Pipe Bomb' in game.enemy[goblin].specials_list and goblin_health > 0:
        roll = random.randint(0, 1)
        if roll == 0:
            turn = '<div class="enemy-turn">' + goblin_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                              '...fortunately, in a freak accident, it explodes ' \
                                                              'right in his face, dealing 2500 damage!</div>'
            goblin_health -= 2500
            battle_log.append(turn)
        else:
            turn = '<div class="enemy-turn">' + goblin_name + ' throws a Pipe Bomb at the enemy...!<br>' \
                                                              '...it hits the opponent, exploding on contact, ' \
                                                              'dealing 2500 damage!</div>'
            dwarf_health -= 2500
            battle_log.append(turn)

    if game.hero[dwarf].battle is not True:
        while not win_condition:

            if dwarf_speed >= goblin_speed and goblin_health > 0 and dwarf_health > 0:

                dwarf_physical = game.hero[dwarf].str_total * 3

                if 'Dominion' in game.hero[dwarf].specials_list:
                    dwarf_magical = game.hero[dwarf].int_total * 4 + (
                            dwarf_willpower + dwarf_charisma) * 1.5
                else:
                    dwarf_magical = game.hero[dwarf].int_total * 4

                if dwarf_special_attack_next:
                    factor = random.randint(10, 11)
                    damage = (dwarf_physical + dwarf_magical) * round((factor / 10), 2)
                    attack_message = random.choice([' unleashes his <span class="yellow">s</span>'
                                                    '<span class="orange">p</span><span class="red">e</span>'
                                                    '<span class="purple">c</span><span class="deep_blue">i</span>'
                                                    '<span class="blue">a</span><span class="green">l</span> '
                                                    '<span class="yellow">a</span><span class="orange">t</span>'
                                                    '<span class="red">t</span><span class="purple">a</span>'
                                                    '<span class="deep_blue">c</span><span class="blue">k</span> on'])
                    attack_type += ["special"]
                    attack_type += ["special"]
                    dwarf_special_attack_charge += 1
                    dwarf_special_attack_next = False
                else:
                    if dwarf_tactic == 'Frenzy':
                        factor = random.randint(10, 13)
                        damage = dwarf_physical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1
                        if dwarf_special_attack_charge % 5 == 0:
                            dwarf_special_attack_next = True

                    elif dwarf_tactic == 'Focus':
                        factor = random.randint(8, 15)
                        damage = dwarf_magical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = magical_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1
                        if dwarf_special_attack_charge % 5 == 0:
                            dwarf_special_attack_next = True

                    elif dwarf_tactic == 'Balanced':
                        damage_type = random.choice([dwarf_physical, dwarf_magical])
                        if damage_type == dwarf_physical:
                            factor = random.randint(10, 13)
                            damage = dwarf_physical * round((factor / 10), 2)

                            roll = random.randint(0, 4)
                            attack_message = physical_attack_strings[roll]
                            roll_physical_attack_type(attack_type, roll)

                            dwarf_special_attack_charge += 1

                        else:
                            factor = random.randint(8, 15)
                            damage = dwarf_magical * round((factor / 10), 2)

                            roll = random.randint(0, 4)
                            attack_message = magical_attack_strings[roll]
                            roll_magical_attack_type(attack_type, roll)

                            dwarf_special_attack_charge += 1

                        if dwarf_special_attack_charge % 4 == 0:
                            dwarf_special_attack_next = True

                    elif dwarf_tactic == 'Overconfidence':
                        damage_type = random.choice([dwarf_physical, dwarf_magical])
                        if damage_type == dwarf_physical:
                            factor = random.randint(10, 13)
                            damage = round(((dwarf_physical * round((factor / 10), 2)) * 0.8), 2)

                            roll = random.randint(0, 4)
                            attack_message = physical_attack_strings[roll]
                            roll_physical_attack_type(attack_type, roll)

                            dwarf_special_attack_charge += 1

                        else:
                            factor = random.randint(8, 15)
                            damage = round(((dwarf_magical * round((factor / 10), 2)) * 0.8), 2)

                            roll = random.randint(0, 4)
                            attack_message = magical_attack_strings[roll]
                            roll_magical_attack_type(attack_type, roll)

                            dwarf_special_attack_charge += 1

                        if dwarf_special_attack_charge % 3 == 0:
                            dwarf_special_attack_next = True

                if 'Spiked Boots' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and (attack_type[1] == "kick"):
                        damage *= 1.5
                        critical_message = True

                if 'Barbed Fists' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and (attack_type[1] == "punch"):
                        damage *= 1.5
                        critical_message = True

                # Luck effect chance
                roll_crit = random.randint(1, 100)
                if (dwarf_luck >= roll_crit) and (critical_message is not True):
                    damage *= 1.5
                    critical_message = True

                # Reload mechanic has to happen before charisma effect for the stacking to occur.
                if 'Reload' in game.hero[dwarf].specials_list:
                    if dwarf_reload:
                        damage = 0
                        dwarf_special_attack_charge -= 1
                        dwarf_reload = False
                        dwarf_reload_message = True
                    else:
                        dwarf_reload = True

                # Charisma effect chance
                roll_charisma = random.randint(1, 100)
                if dwarf_charisma >= roll_charisma:
                    if random.choice(['reduce', 'increase']) == 'reduce':
                        roll_reduce = random.randint(65, 85)
                        reduction = roll_reduce / 100
                        reduction_message = (roll_reduce - 100) * (-1)
                        dwarf_reduction.append(reduction)
                        dwarf_reduction_message = True
                    else:
                        dwarf_increase_message = True

                # Notice how charisma effects can stack - multiple debuffs can often stack but multiple positive buffs
                # can only really affect weapons with Reload ability. For the Reload charisma stacking to work,
                # the "damage > 0" is necessary.
                while len(dwarf_increase) > 0 and damage > 0:
                    damage *= dwarf_increase.pop()

                while len(goblin_reduction) > 0:
                    damage *= goblin_reduction.pop()

                # Armor reduction - happens after willpower absorption to make it less powerful.
                # The difference between (250 - 100) * 0.5 and 250 * 05 - 100 is unwelcome.
                if damage > 0:
                    if (damage - goblin_armor) <= 0:
                        damage = 0
                    elif 'Armor Penetration' in game.hero[dwarf].specials_list:
                        if (attack_type[0] == "physical") and (
                                (attack_type[1] != "kick") and (attack_type[1] != "punch")):
                            damage -= goblin_armor * 0.5
                    elif attack_type[0] == "special":
                        damage -= (goblin_armor * 1.5)
                    else:
                        damage -= goblin_armor

                # Special abilities that modify damage type
                if 'Dark Arts' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "magical":
                        attack_type[1] = "shadow bolt"
                        attack_message = better_magical_attack_strings

                if 'Combat 101' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "physical":
                        roll = random.randint(0, 2)
                        attack_message = better_physical_attack_strings[roll]

                        attack_type.clear()
                        attack_type += ["physical"]
                        if roll == 0:
                            attack_type += ["hit"]
                        elif roll == 1:
                            attack_type += ["attack"]
                        else:
                            attack_type += ["strike"]

                # Dodge effect chance
                if attack_type[0] == "physical":
                    if (goblin_agility / (dwarf_strength * 3)) > 0.33:
                        goblin_dodge = 0.33
                    elif (goblin_agility / (dwarf_strength * 3)) < 0:
                        goblin_dodge = 0
                    else:
                        goblin_dodge = (goblin_agility / (dwarf_strength * 3))

                    goblin_dodge = round((goblin_dodge * 100))
                    hit_chance = random.randint(1, 100)
                    if goblin_dodge >= hit_chance:
                        damage = 0
                        attack_type.clear()
                        attack_type += ["dodged"]
                        attack_type += ["dodged"]
                        goblin_dodge_message = True

                # Willpower effect
                elif attack_type[0] == "magical" and attack_type[1] != "shadow bolt":
                    if (goblin_willpower / (dwarf_intelligence * 2)) > 0.5:
                        goblin_absorb = 0.5
                    elif (goblin_willpower / (dwarf_intelligence * 2)) < 0:
                        goblin_absorb = 0
                    else:
                        goblin_absorb = (goblin_willpower / (dwarf_intelligence * 2))

                    if round(goblin_absorb, 2) > 0:
                        absorb_message = damage * goblin_absorb
                        absorb_message = round(absorb_message)
                        damage -= (damage * goblin_absorb)
                        goblin_absorb_message = True

                # Avoidance effect chance
                if 'Avoidance' in game.enemy[goblin].specials_list and attack_type[0] != "dodged":
                    roll = random.randint(1, 100)
                    if roll <= 20:
                        damage = 0
                        attack_type.clear()
                        attack_type += ["avoided"]
                        attack_type += ["avoided"]
                        goblin_avoidance_message = True
                        goblin_absorb_message = False

                elif goblin_avoidance_stacks > 0 and attack_type[0] != "dodged":
                    damage = 0
                    attack_type.clear()
                    attack_type += ["avoided"]
                    attack_type += ["avoided"]
                    goblin_avoidance_stacks -= 1
                    goblin_avoidance_message = True
                    goblin_absorb_message = False
                    # I've got to put absorb message as false so that we don't end up "absorbing" next physical attack
                    # accidentally.

                if 'Crating' in game.enemy[goblin].specials_list:
                    if goblin_dodge_message:
                        factor = random.randint(10, 13)
                        counterattack = (goblin_physical * 1.3) * round((factor / 10), 2)
                        dwarf_health -= counterattack
                        counterattack = round(counterattack)
                        goblin_counterattack_message = True

                # Specific damage type reduction special abilities that reduce damage after armor and willpower
                # calculation, but don't reduce damage of other special abilities.
                if 'Aegis' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "special":
                        damage *= 0.35

                if 'Fireproof' in game.enemy[goblin].specials_list:
                    if attack_type[1] == "aflame" or attack_type[1] == "fireball":
                        damage *= 0.5

                if 'Anti-magic Zone' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "magical":
                        damage *= 0.8

                # Special abilities that modify the damage...
                # ...but do not increase or modify the damage of other special abilities
                if 'Ouch!' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "physical" and attack_type[1] == "kick":
                        damage *= 1.2

                if 'Static' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "magical" and attack_type[1] == "electrocute":
                        damage *= 1.5

                if 'Crating' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "physical" and attack_type[1] == "punch":
                        damage *= 1.3

                # Since Goblinbane increases damage against goblins, this ability does not
                # work against dwarves even if they somehow manage to put their grubby hands on this special.
                if 'Goblinbane' in game.hero[dwarf].specials_list:
                    damage *= 1.15

                # General special abilities
                # Deal more damage, add more damage, on hit effects, update on enemy and/or friendly turn, etc.

                # Lucky effect is meant to be updated on every turn in case of agility and luck debuffs.
                if 'Lucky' in game.hero[dwarf].specials_list:
                    if dwarf_agility < (goblin_strength * 2):
                        dwarf_agility = goblin_strength * 2
                    if dwarf_luck < 50:
                        dwarf_luck = 50

                if 'Stun chance' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        roll = random.randint(1, 100)
                        if roll <= 15:
                            goblin_speed -= goblin_speed_base
                            dwarf_stun_message = True

                if 'Adrenaline' in game.hero[dwarf].specials_list:
                    dwarf_speed_base *= 0.85

                if 'Momentum' in game.hero[dwarf].specials_list:
                    dwarf_speed_base *= 1.01

                if 'Energize' in game.hero[dwarf].specials_list:
                    dwarf_speed_base *= 1.03

                if 'Firebrand' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        damage += 45
                        dwarf_firebrand_message = True

                if 'Hawkeye' in game.hero[dwarf].specials_list:
                    if critical_message:
                        damage += 50
                        dwarf_hawkeye_message = True

                if 'Multi-tool' in game.hero[dwarf].specials_list:
                    if attack_type[0] != "dodged" or attack_type[0] != "avoided":
                        roll = random.randint(1, 100)
                        if roll <= 15:
                            dwarf_avoidance_stacks += 1
                            dwarf_multitool_message = True

                if 'Mind Sap' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "magical":
                        roll = random.randint(0, 1)
                        if roll == 0:
                            goblin_willpower *= 0.95
                            dwarf_mindsap_will_message = True
                        else:
                            goblin_intelligence *= 0.95
                            dwarf_mindsap_int_message = True

                if 'Soulrend' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        soulrend = goblin_max_health * 0.05
                        damage += soulrend
                        soulrend = round(soulrend)
                        dwarf_soulrend_message = True

                if 'Soul Drain' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "magical":
                        souldrain = goblin_max_health * 0.03
                        dwarf_health += souldrain
                        goblin_health -= souldrain
                        souldrain = round(souldrain)
                        dwarf_souldrain_message = True

                if 'Warframe' in game.hero[dwarf].specials_list:
                    dwarf_self_destruct -= 1
                    if dwarf_self_destruct <= 0:
                        dwarf_health -= 9999
                        dwarf_warframe_message = True

                if 'Mageslayer' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        mageslayer = (goblin_intelligence * 1.5)
                        damage += mageslayer
                        mageslayer = round(mageslayer)
                        dwarf_mageslayer_message = True

                # Defensive special abilities...
                # ...that either react to damage or can reduce most sources of damage.
                if 'Avatar' in game.enemy[goblin].specials_list:
                    damage *= 0.8

                if 'Earthbound' in game.enemy[goblin].specials_list:
                    if damage > 0:
                        goblin_armor *= 1.05
                        goblin_agility *= 1.05
                        goblin_willpower *= 1.05
                        goblin_earthbound_message = True

                # Lifesteal at the end of everything
                if 'Lifesteal' in game.hero[dwarf].specials_list:
                    lifesteal = damage * 0.2
                    damage -= lifesteal
                    lifesteal = round(lifesteal)
                    dwarf_lifesteal_message = True

                # Neurotoxin is an exception and needs to be checked after all avoidance and dodge rolls have already
                # happened.
                if 'Neurotoxin' in game.hero[dwarf].specials_list:
                    if (attack_type[0] == "physical") and (
                            (attack_type[1] != "kick") and (attack_type[1] != "punch")) and dwarf_neurotoxin_payload:
                        goblin_willpower *= 0.65
                        goblin_agility *= 0.65
                        goblin_charisma *= 0.65
                        goblin_luck *= 0.65
                        dwarf_neurotoxin_payload = False
                        dwarf_neurotoxin_message = True

                # This is where all the accumulated damage in a turn is really dealt.
                if damage < 0:
                    damage = 0
                goblin_health -= damage
                damage = round(damage)

                #
                # THE MESSAGES
                #
                # And before you start to scream - I tried giving charisma effect-message some kind of function,
                # but it just wouldn't work, I couldn't make it work. I'm going to think about a fix later.
                # For now - enjoy the copypaste.

                # Reload weapon must be the first case to check - it would be silly if the opponent
                # somehow dodged or avoided you reloading.
                if dwarf_reload_message:
                    turn = '<div class="hero-turn">' + dwarf_name + ' is busy reloading his weapon.'
                    dwarf_reload_message = False
                    if dwarf_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        dwarf_increase.append(increase)
                        turn += '<br><span class="italic">His rallying cry bolsters him up, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        dwarf_increase_message = False
                    elif dwarf_reduction_message:
                        turn += '<br><span class="italic">His terrifying roar intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        dwarf_reduction_message = False
                    goblin_absorb_message = False
                    goblin_dodge_message = False

                elif goblin_dodge_message:
                    turn = '<div class="hero-turn">' + dwarf_name + ' tries to ' + attack_message + \
                           ' the goblin, but he manages to dodge the attack!'
                    goblin_dodge_message = False
                    if goblin_counterattack_message:
                        turn += '<br>' + goblin_name + " counterattacks with a punch, dealing " + str(
                            counterattack) + ' damage!'
                        goblin_counterattack_message = False
                    if dwarf_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        dwarf_increase.append(increase)
                        turn += '<br><span class="italic">His rallying cry bolsters him up, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        dwarf_increase_message = False
                    elif dwarf_reduction_message:
                        turn += '<br><span class="italic">His terrifying roar intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        dwarf_reduction_message = False
                    goblin_absorb_message = False
                    goblin_avoidance_message = False

                elif goblin_avoidance_message:
                    turn = '<div class="hero-turn">' + dwarf_name + ' tries to ' + attack_message + \
                           ' the goblin, but he manages to avoid the attack!'
                    goblin_avoidance_message = False
                    if dwarf_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        dwarf_increase.append(increase)
                        turn += '<br><span class="italic">His rallying cry bolsters him up, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        dwarf_increase_message = False
                    elif dwarf_reduction_message:
                        turn += '<br><span class="italic">His terrifying roar intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        dwarf_reduction_message = False
                    goblin_absorb_message = False
                    goblin_dodge_message = False

                else:

                    turn = '<div class="hero-turn">' + dwarf_name + attack_message + ' goblin for ' + str(damage)

                    if dwarf_firebrand_message:
                        turn += ' <span class="orange">(+45)</span>'
                        dwarf_firebrand_message = False

                    if dwarf_mageslayer_message:
                        turn += ' <span class="purple">(+' + str(mageslayer) + ')</span>'
                        dwarf_mageslayer_message = False

                    if dwarf_hawkeye_message:
                        turn += ' <span class="yellow">(+50)</span>'
                        dwarf_hawkeye_message = False

                    # In case of willpower absorption...
                    if goblin_absorb_message:
                        turn += " damage! (Opponent's willpower mitigates +" + str(
                            absorb_message) + " points of damage.)"
                    else:
                        turn += ' damage!'
                    goblin_absorb_message = False

                    if critical_message and goblin_dodge_message is not True:
                        turn += ' <span class="yellow italic">Critical strike!</span>'
                        critical_message = False

                    # In case of charisma effect...
                    if dwarf_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        dwarf_increase.append(increase)
                        turn += '<br><span class="italic">His rallying cry bolsters him up, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        dwarf_increase_message = False
                    elif dwarf_reduction_message:
                        turn += '<br><span class="italic">His terrifying roar intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        dwarf_reduction_message = False

                    if dwarf_stun_message:
                        turn += '<br>' + dwarf_name + ' manages to stun the opponent! They skip their next turn.'
                        dwarf_stun_message = False

                    if dwarf_lifesteal_message:
                        turn += '<br>' + dwarf_name + ' heals for ' + str(lifesteal) + ' from damage dealt!.'
                        dwarf_lifesteal_message = False

                    if dwarf_mindsap_will_message:
                        turn += '<br>' + dwarf_name + " saps opponent's willpower, reducing it by 5%!"
                        dwarf_mindsap_will_message = False

                    if dwarf_mindsap_int_message:
                        turn += '<br>' + dwarf_name + " saps opponent's intelligence, reducing it by 5%!"
                        dwarf_mindsap_int_message = False

                    if dwarf_soulrend_message:
                        turn += '<br>' + dwarf_name + " rends enemy's very soul, damaging the opponent for " + str(
                            soulrend) + ' damage!'
                        dwarf_soulrend_message = False

                    if dwarf_souldrain_message:
                        turn += '<br>' + dwarf_name + " drains enemy's very soul, healing himself " \
                                                      "and damaging the opponent for " + str(souldrain) + ' damage!'
                        dwarf_souldrain_message = False

                    if dwarf_multitool_message:
                        turn += "<br>" + dwarf_name + " manages to briefly blind the opponent, " \
                                                      "making their next attack a sure miss!"
                        dwarf_multitool_message = False

                    if goblin_earthbound_message:
                        turn += "<br><br>Tel'lar reacts to it's owner taking damage, bolstering up their " \
                                "defences!<br>Goblin's armor, agility and willpower is increased by 5%!"
                        goblin_earthbound_message = False

                    if 'Warframe' in game.hero[dwarf].specials_list \
                            and dwarf_warframe_message is not True:
                        turn += '<br><br>' + str(dwarf_self_destruct) + '...'

                    if dwarf_warframe_message:
                        turn += '<br><br>"Beep, beep, beep!"<br>' + "Dwarf's warframe explodes into " \
                                                                    "million pieces, damaging the pilot " \
                                                                    "for 9999 damage!"
                        dwarf_warframe_message = False

                    if dwarf_neurotoxin_message:
                        turn += '<br><br>' + "Powerful neurotoxin that coats dwarf's weapon poisons " \
                                             "the enemy, decreasing their agility, willpower, " \
                                             "charisma and luck by 35% " \
                                             "and dealing 500 extra damage!"
                        dwarf_neurotoxin_message = False

                turn += '</div>'

                attack_type.clear()
                goblin_speed += goblin_speed_base
                damage = 0
                battle_log.append(turn)
                # Do not move it outside the while loop,
                # otherwise the "at the start of the battle" effects append twice.

            elif goblin_speed > dwarf_speed and goblin_health > 0 and dwarf_health > 0:

                goblin_physical = game.enemy[goblin].str_total * 3

                if 'Dominion' in game.enemy[goblin].specials_list:
                    goblin_magical = game.enemy[goblin].int_total * 4 + (
                            goblin_willpower + goblin_charisma) * 1.5
                else:
                    goblin_magical = game.enemy[goblin].int_total * 4

                if goblin_special_attack_next:
                    factor = random.randint(10, 11)
                    damage = (goblin_physical + goblin_magical) * round((factor / 10), 2)
                    attack_message = random.choice([
                        'unleashes his <span class="yellow">s</span><span class="orange">p</span><span '
                        'class="red">e</span><span class="purple">c</span><span class="deep_blue">i</span><span '
                        'class="blue">a</span><span class="green">l</span> <span class="yellow">a</span><span '
                        'class="orange">t</span><span class="red">t</span><span class="purple">a</span><span '
                        'class="deep_blue">c</span><span class="blue">k</span> on'])
                    attack_type = ["special"]
                    attack_type += ["special"]
                    goblin_special_attack_charge += 1
                    goblin_special_attack_next = False
                else:
                    if goblin_tactic == 'Frenzy':
                        factor = random.randint(10, 13)
                        damage = goblin_physical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1
                        if goblin_special_attack_charge % 5 == 0:
                            goblin_special_attack_next = True

                    elif goblin_tactic == 'Focus':
                        factor = random.randint(8, 15)
                        damage = goblin_magical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = magical_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1
                        if goblin_special_attack_charge % 5 == 0:
                            goblin_special_attack_next = True

                    elif goblin_tactic == 'Balanced':
                        damage_type = random.choice([goblin_physical, goblin_magical])
                        if damage_type == goblin_physical:
                            factor = random.randint(10, 13)
                            damage = goblin_physical * round((factor / 10), 2)

                            roll = random.randint(0, 4)
                            attack_message = physical_attack_strings[roll]
                            roll_physical_attack_type(attack_type, roll)

                            goblin_special_attack_charge += 1

                        else:
                            factor = random.randint(8, 15)
                            damage = goblin_magical * round((factor / 10), 2)

                            roll = random.randint(0, 4)
                            attack_message = magical_attack_strings[roll]
                            roll_magical_attack_type(attack_type, roll)

                            goblin_special_attack_charge += 1

                        if goblin_special_attack_charge % 4 == 0:
                            goblin_special_attack_next = True

                    elif goblin_tactic == 'Overconfidence':
                        damage_type = random.choice([goblin_physical, goblin_magical])
                        if damage_type == goblin_physical:
                            factor = random.randint(10, 13)
                            damage = round(((goblin_physical * round((factor / 10), 2)) * 0.8), 0)

                            roll = random.randint(0, 4)
                            attack_message = physical_attack_strings[roll]
                            roll_physical_attack_type(attack_type, roll)

                            goblin_special_attack_charge += 1
                        else:
                            factor = random.randint(8, 15)
                            damage = round(((goblin_magical * round((factor / 10), 2)) * 0.8), 0)

                            roll = random.randint(0, 4)
                            attack_message = magical_attack_strings[roll]
                            roll_magical_attack_type(attack_type, roll)

                            goblin_special_attack_charge += 1

                        if goblin_special_attack_charge % 3 == 0:
                            goblin_special_attack_next = True

                if 'Spiked Boots' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and (attack_type[1] == "kick"):
                        damage = damage * 1.5
                        critical_message = True

                if 'Barbed Fists' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and (attack_type[1] == "punch"):
                        damage = damage * 1.5
                        critical_message = True

                # Luck effect chance
                roll_crit = random.randint(1, 100)
                if (goblin_luck >= roll_crit) and (critical_message is not True):
                    damage = damage * 1.5
                    critical_message = True

                # Reload mechanic has to happen before charisma effect for the stacking to occur.
                if 'Reload' in game.enemy[goblin].specials_list:
                    if goblin_reload:
                        damage = 0
                        goblin_special_attack_charge -= 1
                        goblin_reload = False
                        goblin_reload_message = True
                    else:
                        goblin_reload = True

                # Charisma effect chance
                roll_charisma = random.randint(1, 100)
                if goblin_charisma >= roll_charisma:
                    if random.choice(['reduce', 'increase']) == 'reduce':
                        roll_reduce = random.randint(65, 85)
                        reduction = roll_reduce / 100
                        reduction_message = (roll_reduce - 100) * (-1)
                        goblin_reduction.append(reduction)
                        goblin_reduction_message = True
                    else:
                        goblin_increase_message = True

                # Notice how charisma effects can stack - multiple debuffs can often stack but positive buffs can only
                # really affect weapons with Reload ability. For the Reload charisma stacking to work, the "damage > 0"
                # is necessary.
                while len(goblin_increase) > 0 and damage > 0:
                    damage *= goblin_increase.pop()

                while len(dwarf_reduction) > 0:
                    damage *= dwarf_reduction.pop()

                # Armor reduction - happens after willpower absorption to make it less powerful.
                # The difference between (250 - 100) * 0.5 and 250 * 05 - 100 is unwelcome.
                if damage > 0:
                    if (damage - dwarf_armor) <= 0:
                        damage = 0
                    elif 'Armor Penetration' in game.enemy[goblin].specials_list:
                        if (attack_type[0] == "physical") and (
                                (attack_type[1] != "kick") and (attack_type[1] != "punch")):
                            damage -= dwarf_armor * 0.5
                    elif attack_type[0] == "special":
                        damage -= (dwarf_armor * 1.5)
                    else:
                        damage -= dwarf_armor

                # Special abilities that modify damage type
                if 'Dark Arts' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "magical":
                        attack_type[1] = "shadow bolt"
                        attack_message = better_magical_attack_strings

                if 'Combat 101' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "physical":
                        roll = random.randint(0, 2)
                        attack_message = better_physical_attack_strings[roll]

                        attack_type.clear()
                        attack_type += ["physical"]
                        if roll == 0:
                            attack_type += ["hit"]
                        elif roll == 1:
                            attack_type += ["attack"]
                        else:
                            attack_type += ["strike"]

                # Dodge effect chance
                if attack_type[0] == "physical":
                    if (dwarf_agility / (goblin_strength * 3)) > 0.33:
                        dwarf_dodge = 0.33
                    elif (dwarf_agility / (goblin_strength * 3)) < 0:
                        dwarf_dodge = 0
                    else:
                        dwarf_dodge = (dwarf_agility / (goblin_strength * 3))

                    dwarf_dodge = round((dwarf_dodge * 100))
                    hit_chance = random.randint(1, 100)
                    if dwarf_dodge >= hit_chance:
                        damage = 0
                        attack_type.clear()
                        attack_type += ["dodged"]
                        attack_type += ["dodged"]
                        dwarf_dodge_message = True

                # Willpower effect
                if attack_type[0] == "magical" and attack_type[1] != "shadow bolt":
                    if (dwarf_willpower / (goblin_intelligence * 2)) > 0.5:
                        dwarf_absorb = 0.5
                    elif (dwarf_willpower / (goblin_intelligence * 2)) < 0:
                        dwarf_absorb = 0
                    else:
                        dwarf_absorb = (dwarf_willpower / (goblin_intelligence * 2))

                    if round(dwarf_absorb, 2) > 0:
                        absorb_message = damage * dwarf_absorb
                        absorb_message = round(absorb_message)
                        damage = damage - (damage * dwarf_absorb)
                        dwarf_absorb_message = True

                # Avoidance effect chance
                if 'Avoidance' in game.hero[dwarf].specials_list and attack_type[0] != "dodged":
                    roll = random.randint(1, 100)
                    if roll <= 20:
                        damage = 0
                        attack_type.clear()
                        attack_type += ["avoided"]
                        attack_type += ["avoided"]
                        dwarf_avoidance_message = True
                        dwarf_absorb_message = False

                elif dwarf_avoidance_stacks > 0 and attack_type[0] != "dodged":
                    damage = 0
                    attack_type.clear()
                    attack_type += ["avoided"]
                    attack_type += ["avoided"]
                    dwarf_avoidance_stacks -= 1
                    dwarf_avoidance_message = True
                    dwarf_absorb_message = False
                    # I've got to put absorb message as false so that we don't end up "absorbing" next physical attack
                    # accidentally.

                if 'Crating' in game.hero[dwarf].specials_list:
                    if dwarf_dodge_message:
                        factor = random.randint(10, 13)
                        counterattack = (dwarf_physical * 1.3) * round((factor / 10), 2)
                        goblin_health -= counterattack
                        counterattack = round(counterattack)
                        dwarf_counterattack_message = True

                # Specific defensive special abilities that reduce damage after armor and willpower calculation,
                # but don't reduce damage of other special abilities.
                if 'Aegis' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "special":
                        damage *= 0.35

                if 'Fireproof' in game.hero[dwarf].specials_list:
                    if attack_type[1] == "aflame" or attack_type[1] == "fireball":
                        damage *= 0.5

                if 'Anti-magic Zone' in game.hero[dwarf].specials_list:
                    if attack_type[0] == "magical":
                        damage *= 0.8

                # Special abilities that modify the damage...
                # ...but do not increase or modify the damage of other special abilities
                if 'Ouch!' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "physical" and attack_type[1] == "kick":
                        damage *= 1.2

                if 'Static' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "magical" and attack_type[1] == "electrocute":
                        damage *= 1.5

                if 'Crating' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "physical" and attack_type[1] == "punch":
                        damage *= 1.3

                # General special abilities
                # Deal more damage, add more damage, on hit effects, update on enemy and/or friendly turn, etc.

                # Lucky effect is meant to be updated on every turn in case of agility and luck debuffs.
                if 'Lucky' in game.enemy[goblin].specials_list:
                    if goblin_agility < (dwarf_strength * 2):
                        goblin_agility = dwarf_strength * 2
                    if goblin_luck < 50:
                        goblin_luck = 50

                if 'Stun chance' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        roll = random.randint(1, 100)
                        if roll <= 15:
                            dwarf_speed -= dwarf_speed_base
                            goblin_stun_message = True

                if 'Adrenaline' in game.enemy[goblin].specials_list:
                    goblin_speed_base *= 0.85

                if 'Momentum' in game.enemy[goblin].specials_list:
                    goblin_speed_base *= 1.01

                if 'Energize' in game.enemy[goblin].specials_list:
                    goblin_speed_base *= 1.03

                if 'Firebrand' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        damage += 45
                        goblin_firebrand_message = True

                if 'Hawkeye' in game.enemy[goblin].specials_list:
                    if critical_message:
                        damage += 50
                        goblin_hawkeye_message = True

                if 'Multi-tool' in game.enemy[goblin].specials_list:
                    roll = random.randint(1, 100)
                    if roll <= 15:
                        goblin_avoidance_stacks += 1
                        goblin_multitool_message = True

                if 'Mind Sap' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "magical":
                        roll = random.randint(0, 1)
                        if roll == 0:
                            dwarf_willpower *= 0.95
                            goblin_mindsap_will_message = True
                        else:
                            dwarf_intelligence *= 0.95
                            goblin_mindsap_int_message = True

                if 'Soulrend' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") or (attack_type[1] != "punch")):
                        soulrend = dwarf_max_health * 0.05
                        damage += soulrend
                        soulrend = round(soulrend)
                        goblin_soulrend_message = True

                if 'Soul Drain' in game.enemy[goblin].specials_list:
                    if attack_type[0] == "magical":
                        souldrain = dwarf_max_health * 0.03
                        goblin_health += souldrain
                        dwarf_health -= souldrain
                        souldrain = round(souldrain)
                        goblin_souldrain_message = True

                if 'Warframe' in game.enemy[goblin].specials_list:
                    goblin_self_destruct -= 1
                    if goblin_self_destruct <= 0:
                        goblin_health -= 9999
                        goblin_warframe_message = True

                if 'Mageslayer' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                        mageslayer = (dwarf_intelligence * 1.5)
                        damage += mageslayer
                        mageslayer = round(mageslayer)
                        goblin_mageslayer_message = True

                # Defensive special abilities...
                # ...that react to damage or can reduce most sources of damage.
                if 'Avatar' in game.hero[dwarf].specials_list:
                    damage *= 0.8

                if 'Earthbound' in game.hero[dwarf].specials_list:
                    if damage > 0:
                        dwarf_armor *= 1.05
                        dwarf_agility *= 1.05
                        dwarf_willpower *= 1.05
                        dwarf_earthbound_message = True

                # Lifesteal at the end of everything
                if 'Lifesteal' in game.enemy[goblin].specials_list:
                    lifesteal = damage * 0.2
                    damage -= lifesteal
                    lifesteal = round(lifesteal)
                    goblin_lifesteal_message = True

                # Neurotoxin is an exception and needs to be checked after all avoidance and dodge rolls have already
                # happened.
                if 'Neurotoxin' in game.enemy[goblin].specials_list:
                    if (attack_type[0] == "physical") and (
                            (attack_type[1] != "kick") and (attack_type[1] != "punch")) and goblin_neurotoxin_payload:
                        dwarf_willpower *= 0.65
                        dwarf_agility *= 0.65
                        dwarf_charisma *= 0.65
                        dwarf_luck *= 0.65
                        goblin_neurotoxin_payload = False
                        goblin_neurotoxin_message = True

                # This is where all the accumulated damage in a turn is really dealt.
                if damage < 0:
                    damage = 0
                dwarf_health -= damage
                damage = round(damage)

                #
                # THE MESSAGES
                #
                # And before you start to scream - I tried giving charisma effect-message some kind of function,
                # but it just wouldn't work, I couldn't make it work. I'm going to think about a fix later.
                # For now - enjoy the copypaste.

                # Reload weapon must be the first case to check - it would be silly if the opponent somehow dodged or
                # avoided you reloading.
                if goblin_reload_message:
                    turn = '<div class="enemy-turn">' + goblin_name + ' is busy reloading his weapon.'
                    goblin_reload_message = False
                    if goblin_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        goblin_increase.append(increase)
                        turn += '<br><span class="italic">His inspiring shriek invigorates him, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        goblin_increase_message = False
                    elif goblin_reduction_message:
                        turn += '<br><span class="italic">His horrifying screech intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        goblin_reduction_message = False
                    dwarf_absorb_message = False
                    dwarf_dodge_message = False

                elif dwarf_dodge_message:
                    turn = '<div class="enemy-turn">' + goblin_name + ' tries to ' + attack_message + \
                           ' the dwarf, but he manages to dodge the attack!'
                    dwarf_dodge_message = False
                    if dwarf_counterattack_message:
                        turn += '<br>' + dwarf_name + " counterattacks with a punch, dealing " + str(
                            counterattack) + ' damage!'
                        dwarf_counterattack_message = False
                    if goblin_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        goblin_increase.append(increase)
                        turn += '<br><span class="italic">His inspiring shriek invigorates him, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        goblin_increase_message = False
                    elif goblin_reduction_message:
                        turn += '<br><span class="italic">His horrifying screech intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        goblin_reduction_message = False
                    dwarf_absorb_message = False
                    dwarf_avoidance_message = False

                elif dwarf_avoidance_message:
                    turn = '<div class="enemy-turn">' + goblin_name + ' tries to ' + attack_message + \
                           ' the dwarf, but he manages to avoid the attack!'
                    dwarf_avoidance_message = False
                    if goblin_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        goblin_increase.append(increase)
                        turn += '<br><span class="italic">His inspiring shriek invigorates him, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        goblin_increase_message = False
                    elif goblin_reduction_message:
                        turn += '<br><span class="italic">His horrifying screech intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        goblin_reduction_message = False
                    dwarf_absorb_message = False
                    dwarf_dodge_message = False

                else:

                    turn = '<div class="enemy-turn">' + goblin_name + attack_message + ' dwarf for ' + str(damage)

                    if goblin_firebrand_message:
                        turn += ' <span class="orange">(+45)</span>'
                        goblin_firebrand_message = False

                    if goblin_mageslayer_message:
                        turn += ' <span class="purple">(+' + str(mageslayer) + ')</span>'
                        goblin_mageslayer_message = False

                    if goblin_hawkeye_message:
                        turn += ' <span class="yellow">(+50)</span>'
                        goblin_hawkeye_message = False

                    # In case of willpower absorption...
                    if dwarf_absorb_message:
                        turn += " damage! (Opponent's willpower mitigates +" + str(
                            absorb_message) + " points of damage.)"
                    else:
                        turn += ' damage'
                    dwarf_absorb_message = False

                    if critical_message and dwarf_dodge_message is not True:
                        turn += ' <span class="yellow italic">Critical strike!</span>'
                        critical_message = False

                    # In case of charisma effect....
                    if goblin_increase_message:
                        roll_increase = random.randint(15, 35)
                        increase = 1 + (roll_increase / 100)
                        increase_message = roll_increase
                        goblin_increase.append(increase)
                        turn += '<br><span class="italic">His inspiring shriek invigorates him, ' \
                                'increasing the power of his next attack by ' + str(increase_message) + '%!</span>'
                        goblin_increase_message = False
                    elif goblin_reduction_message:
                        turn += '<br><span class="italic">His horrifying screech intimidates the opponent, ' \
                                'decreasing the power of his next attack by ' + str(reduction_message) + '%!</span>'
                        goblin_reduction_message = False

                    if goblin_stun_message:
                        turn += '<br>' + goblin_name + ' manages to stun the opponent! They skip their next turn.'
                        goblin_stun_message = False

                    if goblin_lifesteal_message:
                        turn += '<br>' + goblin_name + ' heals for ' + str(lifesteal) + ' from damage dealt!.'
                        goblin_lifesteal_message = False

                    if goblin_mindsap_will_message:
                        turn += '<br>' + goblin_name + " saps opponent's willpower, reducing it by 5%!"
                        goblin_mindsap_will_message = False

                    if goblin_mindsap_int_message:
                        turn += '<br>' + goblin_name + " saps opponent's intelligence, reducing it by 5%!"
                        goblin_mindsap_int_message = False

                    if goblin_soulrend_message:
                        turn += '<br>' + goblin_name + " rends hero's very soul, damaging the opponent for " + str(
                            soulrend) + ' damage!'
                        goblin_soulrend_message = False

                    if goblin_souldrain_message:
                        turn += '<br>' + goblin_name + "drains hero's very soul, healing himself and damaging the " \
                                                       "opponent for " + str(souldrain) + ' damage!'
                        goblin_souldrain_message = False

                    if goblin_multitool_message:
                        turn += "<br>" + goblin_name + "manages to briefly blind the opponent, " \
                                                       "making their next attack a sure miss!"
                        goblin_multitool_message = False

                    if dwarf_earthbound_message:
                        turn += "<br><br>Tel'lar reacts to it's owner taking damage, bolstering up their " \
                                "defences!<br>Dwarf's armor, agility and willpower is increased by 5%! "
                        dwarf_earthbound_message = False

                    if 'Warframe' in game.enemy[goblin].specials_list and \
                            goblin_warframe_message is not True:
                        turn += '<br><br>' + str(goblin_self_destruct) + '...'

                    if goblin_warframe_message:
                        turn += '<br><br>"Beep, beep, beep!"<br>' + "Goblin's warframe explodes into million pieces, " \
                                                                    "damaging the pilot for 9999 damage! "
                        goblin_warframe_message = False

                    if goblin_neurotoxin_message:
                        turn += '<br><br>' + "Powerful neurotoxin that coats goblin's weapon poisons the opponent, " \
                                             "decreasing their agility, willpower, charisma and luck by 35% " \
                                             "and dealing 500 extra damage! "
                        goblin_neurotoxin_message = False

                turn += '</div>'

                attack_type.clear()
                dwarf_speed += dwarf_speed_base
                damage = 0
                battle_log.append(turn)
                # Do not move it outside the while loop,
                # otherwise the "at the start of the battle" effects append twice.

            if goblin_health <= 0:
                message = '<br>' + dwarf_name + ' slays ' + goblin_name + '!<br><h2>You win the battle!</h2>'
                win_condition = True
                if 'Cursed' in game.hero[dwarf].specials_list:
                    game.hero[dwarf].secret = True
                else:
                    game.hero[dwarf].win = True
                battle_log.append(message)
            elif dwarf_health <= 0:
                message = '<br>' + goblin_name + ' slays ' + dwarf_name + '!<br><h2>You lost the battle.</h2>'
                win_condition = True
                game.hero[dwarf].win = False
                battle_log.append(message)

        game.hero[dwarf].battle = True
        return battle_log
    else:
        game.hero[dwarf].graveyard = True
        if game.hero[dwarf].white_lotus_taken is False:
            roll = random.randint(1, 4)
            if roll == 1:
                game.hero[dwarf].white_lotus = True


if __name__ == '__main__':
    app.run(host="wierzba.wzks.uj.edu.pl", port=5102, debug=True)
