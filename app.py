from flask import Flask, render_template, request
import random #, time, decimal
# from decimal import Decimal

app = Flask(__name__)


@app.route('/')
def homepage():

    return render_template('homepage.html')


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
                              "Leather Whip": item_19, "Bronze Broadsword": item_20, "Oak Staff": item_21, "CQC Manual": item_22,

                              "Hardleather Helmet": item_101, "Hardleather Shoulderpads": item_102, "Hardleather Chest": item_103, "Hardleather Pants": item_104, "Hardleather Gloves": item_105, "Hardleather Boots": item_106,
                              "Iron Helmet": item_107, "Iron Pauldrons": item_108, "Iron Cuirass": item_109, "Iron Legguards": item_110, "Iron Handguards": item_111, "Iron Greaves": item_112,
                              "Silk Headwrap": item_113, "Silk Shoulderpads": item_114, "Silk Vesture": item_115, "Silk Kilt": item_116, "Silk Gloves": item_117, "Silk Slippers": item_118,
                              "Flintlock Pistol": item_119, "Iron Mace": item_120, "Amethyst Focus": item_121,
                              "Shiny Coin": item_122,

                              "Dragonscale Helmet": item_201, "Dragonscale Shoulderguards": item_202, "Dragonscale Chainmail": item_203, "Dragonscale Reinforced Kilt": item_204, "Dragonscale Gauntlets": item_205, "Dragonscale Wyrm-riders": item_206,
                              "Mithril Headguard": item_207, "Mithril Pauldrons": item_208, "Mithril Chestplate": item_209, "Mithril Legguards": item_210, "Mithril Gauntlets": item_211, "Mithril Greaves": item_212,
                              "Ceremonial Tiara": item_213, "Ceremonial Epaluettes": item_214, "Ceremonial Robe": item_215, "Ceremonial Trousers": item_216, "Ceremonial Gloves": item_217, "Ceremonial Shoes": item_218,
                              "Mageslayer Dagger": item_219, "Firebrand Sword": item_220, "Dragonwood Wand": item_221,

                              "Crown of Will": item_301, "Heart of the Mountain": item_302, "Tel'lar": item_303, "Blessed Aegis": item_304,

                              "???": item_404, "Memento": item_999, "Warframe": item_495, "Lucky Pebble": item_777}

            game.ability_dict = {"Lucky": ["What is this thing...? Nevertheless, it's presence somehow makes you feel a little bit more lucky~", "common"],
                                 "Combat 101": ["Dwarf will no longer punch or kick in melee combat during battle but instead opt to strike with his weapon.", "common"],
                                 "Unstable Concoction": ["At the start of the battle either you or the enemy takes 250 extra damage.", "common"],
                                 "Goblinbane": ["Deal 15% more damage to the goblins.", "common"],

                                 "Stun Chance": ["15% chance on weapon strike to stun the enemy for a turn.", "rare"],
                                 "Momentum": ["Gain 1% speed every time you take a turn.", "rare"],
                                 "Adrenaline": ["You start off with a massive 4x speed boost, but every turn, you lose 10% of your speed till the end of battle.", "rare"],
                                 "Hawkeye": ["Your critical attacks deal extra 50 damage.", "rare"],
                                 "Spiky Boots": ["Your kicks always crit!", "rare"],

                                 "Blade Mail": ["You reflect 15% of melee damage taken.", "epic"],
                                 "Pearl Armor": ["You reflect 15% of magic damage taken.", "epic"],
                                 "Energize": ["Gain 2% speed every time you take a turn.", "epic"],
                                 "Mind Sap": ["On hit decrease opponent's willpower or intelligence by 5%.", "epic"],
                                 "Disarm": ["Remove opponents weapon from the battle.", "epic"],    # On start of battle - how to disable the enemy specials?
                                 "Lifesteal": ["You heal for 10% of your damage done.", "epic"],
                                 "Firebrand": ["On weapon strike, deal 35 extra fire damage to the enemy.", "epic"],
                                 "Smoke Bomb": ["First 4 enemy hits will always miss!", "epic"],
                                 "Neurotoxin": ["At the start of the battle reduce enemy's willpower and agility by 30% and deal 500 extra damage.", "epic"],
                                 "Mageslayer": ["On weapon strike deal bonus damage equal to 25% of enemy's intelligence.", "epic"],

                                 "Earthbound": ["The legendary shield-sword Tel'lar protects you from harm. Every time you are struck in combat, gain 5% armor, agility and willpower.", "legendary"],
                                 "Soul Drain": ["On magical hit, steal 3% total health from the enemy.", "legendary"],
                                 "Soulrend": ["On weapon strike, deal 5% extra damage based off enemy's total health.", "legendary"],
                                 "Avatar": ["You assume the legendary form of Avatar of the Mountain. Take 20% less damage from all sources.", "legendary"],
                                 "Dominion": ["1.5x of your charisma and willpower translates into magic damage.", "legendary"],
                                 "Aegis": ["You take 50% less damage from special attacks.", "legendary"],

                                 "Cursed": ["Perhaps it would be wiser not to bring it into battle...", "cursed"],
                                 "Pipe Bomb": ["At the start of the battle either you or the enemy takes 1500 extra damage.", "cursed"],
                                 "Warframe": ["You somehow managed to fit inside... Strength and speed is tremendously increased but you will self-destruct in 10 turns - may your ashes scatter among the stars well, soldier.", "cursed"],
                                 "Nanomachines": ["You take 50% less damage from physical and magical attacks but 300% more from special attacks.", "cursed"]
                                 }
            game.backpack = []

            game_mode_easy()



        elif request.form.get('back', False) == 'Victory!' or request.form.get('back', False) == 'Retreat':
            return render_template('game.html', game=game)


        #   TRAIN
        #   Deadmines: Become superhuman
        #
        #   HTML form, string  ->  game.hero[dwarf].<stats>
        #
        #   Takes an input from the HTML form, adds stats from the input into the dwarf at the cost of days.
        #   If the training is too costly (ie. not enough days left), nothing will happen. Flash error message for this case is to be implemented in the future.

        elif request.form.get('train dwarf1', False) == 'Train':
            train('dwarf1')

        elif request.form.get('train dwarf2', False) == 'Train':
            train('dwarf2')

        elif request.form.get('train dwarf3', False) == 'Train':
            train('dwarf3')



        #   EQUIP
        #   It was a Barbie doll dress up game all along...
        #
        #   game.backpack, array  ->  HTML form, string  ->  game.item_dict, dictionary  ->  game.hero[dwarf].equipment, dictionary
        #
        #   Takes a string from HTML form option field (ex. "Leather Cap"), then searches for its object in item_dict which contains reference to all items in the game.
        #   Then takes that object and slams it into the corresponding equipment slot. Also there's an unequipment call somewhere in the middle.
        #   Stuff resets and recalculates at the end, as per tradition.

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
        #   Takes a string from HTML form option field (ex. "Leather Cap") and searches for it in the corresponding dwarf's equipment.
        #   Puts it into his backpack and deletes it from the equipment. Because both objects already have the actual object of the item inside them,
        #   there's no need to cross-reference anything with the help of item_dict.

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
                spoils = random.choices(item_list_common, k = 2) + random.choices(item_list_rare, k = 1) + [item_777]

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
                spoils = random.choices(item_list_cursed, k = 1)

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

            game.hero[dwarf].armor += game.hero[dwarf].equipment[item_slot].armor

            if game.hero[dwarf].equipment[item_slot].special is not None:
                game.hero[dwarf].specials_list.append(game.hero[dwarf].equipment[item_slot].special)


def update_equipment_enemy(goblin):

    # Updates multipliers and bonuses values based on current equipment
    for item_slot, item_name in game.enemy[goblin].equipment.items():
        if item_name is not None:

            rounded = game.enemy[goblin].str_mul + game.enemy[goblin].equipment[item_slot].str_mul
            game.enemy[goblin].str_mul = round(rounded,2)
            game.enemy[goblin].str_bonus += game.enemy[goblin].equipment[item_slot].str_bonus

            rounded = game.enemy[goblin].int_mul + game.enemy[goblin].equipment[item_slot].int_mul
            game.enemy[goblin].int_mul = round(rounded, 2)
            game.enemy[goblin].int_bonus += game.enemy[goblin].equipment[item_slot].int_bonus

            rounded = game.enemy[goblin].agi_mul + game.enemy[goblin].equipment[item_slot].agi_mul
            game.enemy[goblin].agi_mul = round(rounded, 2)
            game.enemy[goblin].agi_bonus += game.enemy[goblin].equipment[item_slot].agi_bonus

            rounded = game.enemy[goblin].will_mul + game.enemy[goblin].equipment[item_slot].will_mul
            game.enemy[goblin].will_mul = round(rounded, 2)
            game.enemy[goblin].will_bonus += game.enemy[goblin].equipment[item_slot].will_bonus

            rounded = game.enemy[goblin].end_mul + game.enemy[goblin].equipment[item_slot].end_mul
            game.enemy[goblin].end_mul = round(rounded, 2)
            game.enemy[goblin].end_bonus += game.enemy[goblin].equipment[item_slot].end_bonus

            rounded = game.enemy[goblin].char_mul + game.enemy[goblin].equipment[item_slot].char_mul
            game.enemy[goblin].char_mul = round(rounded, 2)
            game.enemy[goblin].char_bonus += game.enemy[goblin].equipment[item_slot].char_bonus

            rounded = game.enemy[goblin].lck_mul + game.enemy[goblin].equipment[item_slot].lck_mul
            game.enemy[goblin].lck_mul = round(rounded, 2)
            game.enemy[goblin].lck_bonus += game.enemy[goblin].equipment[item_slot].lck_bonus

            rounded = game.enemy[goblin].spd_mul + game.enemy[goblin].equipment[item_slot].spd_mul
            game.enemy[goblin].spd_mul = round(rounded, 2)
            game.enemy[goblin].spd_bonus += game.enemy[goblin].equipment[item_slot].spd_bonus

            game.enemy[goblin].armor += game.enemy[goblin].equipment[item_slot].armor

            if game.enemy[goblin].equipment[item_slot].special is not None:
                game.enemy[goblin].specials_list.append(game.enemy[goblin].equipment[item_slot].special)

def stat_reset(dwarf):

    # Resets all stats before equipment update
    game.hero[dwarf].str_mul = game.hero[dwarf].int_mul = game.hero[dwarf].agi_mul = game.hero[dwarf].will_mul = game.hero[dwarf].end_mul = game.hero[dwarf].char_mul = game.hero[dwarf].lck_mul = game.hero[dwarf].spd_mul = 1.0
    game.hero[dwarf].str_bonus = game.hero[dwarf].int_bonus = game.hero[dwarf].agi_bonus = game.hero[dwarf].will_bonus = game.hero[dwarf].end_bonus = game.hero[dwarf].char_bonus = game.hero[dwarf].lck_bonus = game.hero[dwarf].spd_bonus = 0
    game.hero[dwarf].armor = 0
    game.hero[dwarf].specials_list.clear()

def update_stats(dwarf):

    # Updates total stats based on the bases, multipliers and bonuses
    if game.hero[dwarf].str_mul <= 0.0:
        game.hero[dwarf].str_mul = 0.1
    game.hero[dwarf].str_total = round(game.hero[dwarf].strength * game.hero[dwarf].str_mul + game.hero[dwarf].str_bonus)
    if game.hero[dwarf].str_total <= 0:
        game.hero[dwarf].str_total = 1

    if game.hero[dwarf].int_mul <= 0.0:
        game.hero[dwarf].int_mul = 0.1
    game.hero[dwarf].int_total = round(game.hero[dwarf].intelligence * game.hero[dwarf].int_mul + game.hero[dwarf].int_bonus)
    if game.hero[dwarf].int_total <= 0:
        game.hero[dwarf].int_total = 1

    if game.hero[dwarf].agi_mul <= 0.0:
        game.hero[dwarf].agi_mul = 0.1
    game.hero[dwarf].agi_total = round(game.hero[dwarf].agility * game.hero[dwarf].agi_mul + game.hero[dwarf].agi_bonus)
    if game.hero[dwarf].agi_total <= 0:
        game.hero[dwarf].agi_total = 1

    if game.hero[dwarf].will_mul <= 0.0:
        game.hero[dwarf].will_mul = 0.1
    game.hero[dwarf].will_total = round(game.hero[dwarf].willpower * game.hero[dwarf].will_mul + game.hero[dwarf].will_bonus)
    if game.hero[dwarf].will_total <= 0:
        game.hero[dwarf].will_total = 1

    if game.hero[dwarf].end_mul <= 0.0:
        game.hero[dwarf].end_mul = 0.1
    game.hero[dwarf].end_total = round(game.hero[dwarf].endurance * game.hero[dwarf].end_mul + game.hero[dwarf].end_bonus)
    if game.hero[dwarf].end_total <= 0:
        game.hero[dwarf].end_total = 1

    if game.hero[dwarf].char_mul <= 0.0:
        game.hero[dwarf].char_mul = 0.1
    game.hero[dwarf].char_total = round(game.hero[dwarf].charisma * game.hero[dwarf].char_mul + game.hero[dwarf].char_bonus)
    if game.hero[dwarf].char_total <= 0:
        game.hero[dwarf].char_total = 1

    if game.hero[dwarf].lck_mul <= 0.0:
        game.hero[dwarf].lck_mul = 0.1
    game.hero[dwarf].lck_total = round(game.hero[dwarf].luck * game.hero[dwarf].lck_mul + game.hero[dwarf].lck_bonus)
    if game.hero[dwarf].lck_total <= 0:
        game.hero[dwarf].lck_total = 1

    if game.hero[dwarf].spd_mul <= 0.0:
        game.hero[dwarf].spd_mul = 0.1
    game.hero[dwarf].spd_total = round(game.hero[dwarf].speed * game.hero[dwarf].spd_mul + game.hero[dwarf].spd_bonus)
    if game.hero[dwarf].spd_total <= 0:
        game.hero[dwarf].spd_total = 1

def update_stats_enemy(goblin):

    # Updates total stats based on the bases, multipliers and bonuses
    if game.enemy[goblin].str_mul <= 0.0:
        game.enemy[goblin].str_mul = 0.1
    game.enemy[goblin].str_total = round(game.enemy[goblin].strength * game.enemy[goblin].str_mul + game.enemy[goblin].str_bonus)
    if game.enemy[goblin].str_total <= 0:
        game.enemy[goblin].str_total = 1

    if game.enemy[goblin].int_mul <= 0.0:
        game.enemy[goblin].int_mul = 0.1
    game.enemy[goblin].int_total = round(game.enemy[goblin].intelligence * game.enemy[goblin].int_mul + game.enemy[goblin].int_bonus)
    if game.enemy[goblin].int_total <= 0:
        game.enemy[goblin].int_total = 1

    if game.enemy[goblin].agi_mul <= 0.0:
        game.enemy[goblin].agi_mul = 0.1
    game.enemy[goblin].agi_total = round(game.enemy[goblin].agility * game.enemy[goblin].agi_mul + game.enemy[goblin].agi_bonus)
    if game.enemy[goblin].agi_total <= 0:
        game.enemy[goblin].agi_total = 1

    if game.enemy[goblin].will_mul <= 0.0:
        game.enemy[goblin].will_mul = 0.1
    game.enemy[goblin].will_total = round(game.enemy[goblin].willpower * game.enemy[goblin].will_mul + game.enemy[goblin].will_bonus)
    if game.enemy[goblin].will_total <= 0:
        game.enemy[goblin].will_total = 1

    if game.enemy[goblin].end_mul <= 0.0:
        game.enemy[goblin].end_mul = 0.1
    game.enemy[goblin].end_total = round(game.enemy[goblin].endurance * game.enemy[goblin].end_mul + game.enemy[goblin].end_bonus)
    if game.enemy[goblin].end_total <= 0:
        game.enemy[goblin].end_total = 1

    if game.enemy[goblin].char_mul <= 0.0:
        game.enemy[goblin].char_mul = 0.1
    game.enemy[goblin].char_total = round(game.enemy[goblin].charisma * game.enemy[goblin].char_mul + game.enemy[goblin].char_bonus)
    if game.enemy[goblin].char_total <= 0:
        game.enemy[goblin].char_total = 1

    if game.enemy[goblin].lck_mul <= 0.0:
        game.enemy[goblin].lck_mul = 0.1
    game.enemy[goblin].lck_total = round(game.enemy[goblin].luck * game.enemy[goblin].lck_mul + game.enemy[goblin].lck_bonus)
    if game.enemy[goblin].lck_total <= 0:
        game.enemy[goblin].lck_total = 1

    if game.enemy[goblin].spd_mul <= 0.0:
        game.enemy[goblin].spd_mul = 0.1
    game.enemy[goblin].spd_total = round(game.enemy[goblin].speed * game.enemy[goblin].spd_mul + game.enemy[goblin].spd_bonus)
    if game.enemy[goblin].spd_total <= 0:
        game.enemy[goblin].spd_total = 1

def train(dwarf):

    strength = int(request.form.get("str_increase"))
    intelligence = int(request.form.get("int_increase"))
    agility = int(request.form.get("agi_increase"))
    willpower = int(request.form.get("will_increase"))
    endurance = int(request.form.get("end_increase"))
    charisma = int(request.form.get("char_increase"))
    luck = int(request.form.get("lck_increase"))
    speed = int(request.form.get("spd_increase"))
    temp_days = strength * 2 + intelligence * 2 + agility + willpower + endurance * 2 + charisma + luck + speed * 3

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

    for key, value in game.hero[dwarf].equipment.items():
        if value is not None:
            game.backpack.append(value)
    game.hero[dwarf].equipment.update(
        {'Weapon': None, 'Headpiece': None, 'Shoulders': None, 'Chest': None, 'Pants': None, 'Gloves': None,
         'Boots': None, 'Artifact': None})

    stat_reset(dwarf)
    update_stats(dwarf)

def equip(dwarf):

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
    for goblin in game.enemy:
        game.enemy[goblin].str_total = random.randint(30, 45)
        game.enemy[goblin].int_total = random.randint(30, 45)
        game.enemy[goblin].agi_total = random.randint(25, 40)
        game.enemy[goblin].will_total = random.randint(25, 40)
        game.enemy[goblin].end_total = 1000
        game.enemy[goblin].char_total = 150
        game.enemy[goblin].luck_total = 150
        game.enemy[goblin].speed_total = random.randint(10, 20)

        game.enemy[goblin].equipment["Weapon"] = random.choice(item_list_weapon_rare)
        game.enemy[goblin].equipment["Headpiece"] = random.choice(item_list_headpiece_common)
        game.enemy[goblin].equipment["Shoulders"] = random.choice(item_list_shoulders_common)
        game.enemy[goblin].equipment["Chest"] = random.choice(item_list_chest_common)
        game.enemy[goblin].equipment["Pants"] = random.choice(item_list_pants_common)
        game.enemy[goblin].equipment["Gloves"] = random.choice(item_list_gloves_common)
        game.enemy[goblin].equipment["Boots"] = random.choice(item_list_boots_common)

        update_equipment_enemy(goblin)
        update_stats_enemy(goblin)


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
            hero_portrait = '/static/dwarf_portraits/' + str(random.randint(1,23)) + '.jpg'
        else:
            name = random.choice(goblin_names)
            surname = random.choice(goblin_surnames)
            name_surname = name + ' ' + surname
            hero_portrait = '/static/goblin_portraits/' + str(random.randint(1,10)) + '.jpg'

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
        self.charisma = 150
        self.char_mul = float(1.0)
        self.char_bonus = 0
        self.char_total = round(self.charisma * self.char_mul + self.char_bonus)
        self.luck = 150
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

        if starter_eq is not None:
            self.equipment.update({starter_eq: eq_choice})

        if self.hero_portrait == '/static/dwarf_portraits/23.jpg':
            self.hero_name = 'Stranger'
            self.equipment.update({'Weapon': item_20,
                                  'Headpiece': item_7,
                                  'Shoulders': item_8,
                                  'Chest': item_9,
                                  'Gloves': item_10,
                                  'Pants': item_11,
                                  'Boots': item_13,
                                  'Artifact': item_999})
            self.tactic = 'Frenzy'


# Item class - for designing and creating items
class Item:

    def __init__(self, item_name, item_slot, rarity, description, str_mul, str_bonus, int_mul, int_bonus, agi_mul, agi_bonus, will_mul, will_bonus, end_mul, end_bonus, char_mul, char_bonus, lck_mul, luck_bonus, spd_mul, spd_bonus, armor, special, special_desc):

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
        self.armor = armor

        self.special = special
        self.special_desc = special_desc


# LIST OF ITEMS

            # Common - Medium armor set

item_1 = Item('Leather Cap', 'Headpiece', 'common', 'A trusty, sturdy leather cap. Even most valiant of dwarves look like dorks while wearing it.',
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_2 = Item('Leather Shoulderpads', 'Shoulders', 'common', "Will not save him from losing an arm but will certainly soften up the blow.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_3 = Item('Leather Jacket', 'Chest', 'common', "Dope :D",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_4 = Item('Leather Pants', 'Pants', 'common', "It took a lot of convincing for him to wear it...",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_5 = Item('Leather Gloves', 'Gloves', 'common', "Sturdy leather Gloves - every dwarves' best friend.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_6 = Item('Leather Boots', 'Boots', 'common', "Solid, steel capped Boots may win or lose you a battle.",
              0.0, 2,   # Strength
              0.0, 0,   # Intelligence
              0.1, 0,   # Agility
              0.0, 0,   # Willpower
              0.0, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 0,   # Speed
              8,        # Armor
              None,     # Enchantment
              None)     # Enchantment description


            # Common - Heavy armor set

item_7 = Item('Rusty Helmet', 'Headpiece', 'common', 'Grandma always asked you to wear one when going into the mines.',
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_8 = Item('Rusty Pauldrons', 'Shoulders', 'common', 'These would look much more intimidating if not for the state they are in.',
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_9 = Item('Rusty Chainmail', 'Chest', 'common', "Taking a spear to the Chest will still hurt like hell but at least he won't bleed out.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_10 = Item('Rusty Tasset', 'Pants', 'common', "Noisy...",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_11 = Item('Rusty Gauntlets', 'Gloves', 'common', "For all those dirty disarming tricks that goblins are known for.",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_12 = Item('Rusty Greaves', 'Boots', 'common', "What's better than steel capped Boots? Full-steel Boots! Too bad these have rusty holes in them...",
              0.1, 2,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 2,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description


            # Common -  Light armor set

item_13 = Item('Tattered Hood', 'Headpiece', 'common', "It reduces the vision a tad bit, but at least it makes it easier to focus.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_14 = Item('Tattered Epaulettes', 'Shoulders', 'common', "Makes you look noble - too bad they don't offer much protection.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_15 = Item('Tattered Robe', 'Chest', 'common', "These must've looked magnificent before moths took a nest in them.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_16 = Item('Tattered Pants', 'Pants', 'common', "Offer unprecedented freedom of movement.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_17 = Item('Tattered Gloves', 'Gloves', 'common', "They give off a weird feeling of comfort.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_18 = Item('Tattered Shoes', 'Boots', 'common', "Pretty airy.",
              0.0, 0,   # Strength
              0.1, 0,   # Intelligence
              0.0, 0,   # Agility
              0.1, 0,   # Willpower
              0.0, 0,   # Endurance
              0.0, 2,   # Charisma
              0.0, 2,   # Luck
              0.0, 0,   # Speed
              4,        # Armor
              None,     # Enchantment
              None)     # Enchantment description


            # Common - Weapons

item_19 = Item('Leather Whip', 'Weapon', 'common', "Takes a bit of practice to use properly.",
              0.2, 12,   # Strength
              0.0, 0,   # Intelligence
              0.2, 12,   # Agility
              0.0, 0,   # Willpower
              0.1, 4,   # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              0,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_20 = Item('Bronze Broadsword', 'Weapon', 'common', "Every dwarf and their hogs know how to use one.",
              0.15, 6,   # Strength
              0.0, 0,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.15, 6,   # Endurance
              0.0, 0,   # Charisma
              0.15, 6,   # Luck
              0.0, 0,   # Speed
              0,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_21 = Item('Oak Staff', 'Weapon', 'common', "Provides just as much support for spellcasting as for melee combat.",
              0.15, 6,   # Strength
              0.15, 6,   # Intelligence
              0.0, 0,   # Agility
              0.0, 0,   # Willpower
              0.1, 4,   # Endurance
              0.15, 6,   # Charisma
              0.0, 0,   # Luck
              0.0, 0,   # Speed
              0,        # Armor
              None,     # Enchantment
              None)     # Enchantment description

            # Common - Artifacts

item_22 = Item('CQC Manual', 'Artifact', 'common', '"Even you can become a master of melee combat with this handy book!"',
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.0, 0,  # Speed
               2,       # Armor
               "Combat 101", # Enchantment
                "Dwarf will no longer punch or kick in melee combat during battle but instead opt to strike with his weapon.")    # Enchantment description

item_777 = Item('Lucky Pebble', 'Artifact', 'common', "What is this thing..?",
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.0, 0,  # Speed
               2,       # Armor
               "Lucky", # Enchantment
                "What is this thing...? Nevertheless, it's presence somehow makes you feel a little bit more lucky~")    # Enchantment description

item_999 = Item('Memento', 'Artifact', 'common', "Picture of unknown family, found among stranger's possessions. For some reason it fills you with unspeakable rage and sense of vengeance, making you act more recklessly.",
               0.0, 0,          # Strength
               0.0, 0,          # Intelligence
               0.0, 0,          # Agility
               0.0, 0,          # Willpower
               0.0, 0,          # Endurance
               0.0, 0,          # Charisma
               0.0, 0,          # Luck
               0.0, 0,          # Speed
               -15,              # Armor
               "Goblinbane",
                "Deal 15% more damage to the goblins.")    # Enchantment


# RARE ITEMS

            # Rare - Medium armor set

item_101 = Item('Hardleather Helmet', 'Headpiece', 'rare', "Reinforced version of leather helmet, now with 30% extra sturdiness!",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_102 = Item('Hardleather Shoulderpads', 'Shoulders', 'rare', "These may actually save him from losing an arm.",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_103 = Item('Hardleather Chest', 'Chest', 'rare', "Light as leather, hard as bronze!",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_104 = Item('Hardleather Pants', 'Pants', 'rare', "They limit his movement a bit but the protection they offer are well worth the trade.",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_105 = Item('Hardleather Gloves', 'Gloves', 'rare', "Manly.",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description

item_106 = Item('Hardleather Boots', 'Boots', 'rare', "For that extra amount of protection.",
              0.1, 4,   # Strength
              0.0, 0,   # Intelligence
              0.15, 0,  # Agility
              0.0, 0,   # Willpower
              0.15, 0,  # Endurance
              0.0, 0,   # Charisma
              0.0, 0,   # Luck
              0.1, 4,   # Speed
              12,       # Armor
              None,     # Enchantment
              None)     # Enchantment description


            # Rare - Heavy armor set

item_107 = Item('Iron Helmet', 'Headpiece', 'rare', "This is getting kinda heavy...",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description

item_108 = Item('Iron Pauldrons', 'Shoulders', 'rare', "Maybe if you polished them, they could blind the enemy.",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description

item_109 = Item('Iron Cuirass', 'Chest', 'rare', "Wouldn't recommend donning this one on a sunny day.",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description

item_110 = Item('Iron Legguards', 'Pants', 'rare', "Try kicking this you goblin bastards!",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description

item_111 = Item('Iron Handguards', 'Gloves', 'rare', "Why would you even need a Weapon with a pair of these?",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description

item_112 = Item('Iron Greaves', 'Boots', 'rare', "We are going full-metal, aw yeah!",
               0.2, 8,  # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.2, 8,  # Endurance
               0.0, 4,   # Charisma
               0.0, 4,   # Luck
               0.0, 0,   # Speed
               18,       # Armor
               None,     # Enchantment
               None)     # Enchantment description


            # Rare - Light armor set

item_113 = Item('Silk Headwrap', 'Headpiece', 'rare', "Softness of silk helps you concentrate on your manly thoughts.",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription

item_114 = Item('Silk Shoulderpads', 'Shoulders', 'rare', "These are just for show.",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription

item_115 = Item('Silk Vesture', 'Chestpiece', 'rare', "Might be mistaken for a bathrobe...",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription

item_116 = Item('Silk Kilt', 'Pants', 'rare', "No matter what others may say, it's a kilt alright, it's a kilt...",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription

item_117 = Item('Silk Gloves', 'Gloves', 'rare', "Silk's static inducing attributes have been thaumaturgically confirmed to enhance one's spellweaving abilities.",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription

item_118 = Item('Silk Slippers', 'Boots', 'rare', "...",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.1, 4,   # Charisma
               0.1, 4,   # Luck
               0.0, 0,   # Speed
               8,        # Armor
               None,     # Enchantment
               None)     # Enchantment desscription


            # Rare - Weapons

item_119 = Item('Flintlock Pistol', 'Weapon', 'rare', "Once you are out of ammo and gunpowder, it's sturdy handle fits right between goblin's eyes.",
               0.0, 0,   # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.0, 0,   # Endurance
               0.1, 4,  # Charisma
               0.2, 12,  # Luck
               0.15, 8,  # Speed
               0,        # Armor
               "Hawkeye",   # Enchantment
               "Your critical attacks deal extra 50 damage.")     # Enchantment description

item_120 = Item('Iron Mace', 'Weapon', 'rare', "They say it has been blessed by a hidden deity - for some reason holding it puts any dwarf in a mood for some goblin skull bashing.",
               0.2, 12,  # Strength
               0.0, 0,   # Intelligence
               0.15, 8,  # Agility
               0.0, 0,   # Willpower
               0.15, 8,  # Endurance
               0.0, 0,   # Charisma
               0.0, 0,   # Luck
               0.0, 0,   # Speed
               0,        # Armor
               "Stun Chance",   # Enchantment
               "15% chance on weapon strike to stun the enemy for a turn.")     # Enchantment description

item_121 = Item('Aquamarine Orb', 'Weapon', 'rare', "Having a proper focus speeds up the spellcasting quite a bit.",
               0.0, 0,   # Strength
               0.15, 8,  # Intelligence
               0.0, 0,   # Agility
               0.15, 8,  # Willpower
               0.0, 0,   # Endurance
               0.0, 0,   # Charisma
               0.0, 0,   # Luck
               0.25, 16,  # Speed
               0,        # Armor
               None,     # Enchantment
               None)     # Enchantment description


            # Rare - Artifacts

item_122 = Item('Shiny Coin', 'Artifact', 'rare', "Shiny coin. It's nice to the touch.",
               0.0, 0,   # Strength
               0.0, 0,   # Intelligence
               0.0, 0,   # Agility
               0.0, 0,   # Willpower
               0.0, 0,   # Endurance
               0.0, 0,   # Charisma
               0.15, 4,  # Luck
               0.15, 4,  # Speed
               0,        # Armor
               None,     # Enchantment
               None)     # Enchantment description


# EPIC ITEMS

            # Epic - Medium armor set

item_201 = Item('Dragonscale Helmet', 'Headpiece', 'epic', "Gives a quite mean look.",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description

item_202 = Item('Dragonscale Shoulderguards', 'Shoulders', 'epic', "Hard as metal, light as leather.",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description

item_203 = Item('Dragonscale Chainmail', 'Chest', 'epic', "Fireproof but not waterproof!",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description

item_204 = Item('Dragonscale Reinforced Kilt', 'Pants', 'epic', "A much cooler cousin of Silk Kilt.",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description

item_205 = Item('Dragonscale Gauntlets', 'Gloves', 'epic', "They've got spikes in case you get disarmed.",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description

item_206 = Item('Dragonscale Wyrm-riders', 'Boots', 'epic', "You could pack a really mean kick with those...",
               0.2, 12,   # Strength
               0.0, 0,    # Intelligence
               0.2, 12,   # Agility
               0.0, 0,    # Willpower
               0.15, 8,   # Endurance
               0.0, 0,    # Charisma
               0.0, 0,    # Luck
               0.15, 8,   # Speed
               24,        # Armor
               None,      # Enchantment
               None)      # Enchantment description


            # Epic - Heavy armor

item_207 = Item('Mithril Headguard', 'Headpiece', 'epic', "One of many symbols of dwarf race.",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_208 = Item('Mithril Pauldrons', 'Shoulders', 'epic', "Looking good chief!",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_209 = Item('Mithril Chestplate', 'Chest', 'epic', "Could deflect a fireball or two.",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_210 = Item('Mithril Legguards', 'Pants', 'epic', "To guard your jewels from grabby mage's hands.",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_211 = Item('Mithril Gauntlets', 'Gloves', 'epic', "Law enforcment uses these to arrest skilled magi.",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_212 = Item('Mithril Greaves', 'Boots', 'epic', "Grounds any and all magical discharges.",
               0.25, 16,    # Strength
               -0.2, -12,   # Intelligence
               0.0, 0,      # Agility
               0.25, 16,    # Willpower
               0.2, 12,     # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               0.0, 0,      # Speed
               32,          # Armor
               None,        # Enchantment
               None)        # Enchantment description


            # Epic - Light armor

item_213 = Item('Ceremonial Tiara', 'Headpiece', 'epic', "You look like a real princess :D",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_214 = Item('Ceremonial Epaluettes', 'Shoulders', 'epic', "They make you look bigger and more magnificent.",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_215 = Item('Ceremonial Robe', 'Chest', 'epic', "You feel like you could coronate a king in those.",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_216 = Item('Ceremonial Trousers', 'Pants', 'epic', "These might look silly but they are so comfortable...",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_217 = Item('Ceremonial Gloves', 'Gloves', 'epic', "They crackle with arcane energies...",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description

item_218 = Item('Ceremonial Shoes', 'Gloves', 'epic', "The silver-lining helps you gather mana from the ground.",
               0.0, 0,      # Strength
               0.35, 24,     # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.3, 20,     # Charisma
               0.1, 8,      # Luck
               0.0, 0,      # Speed
               12,           # Armor
               None,        # Enchantment
               None)        # Enchantment description


            # Epic - Weapons

item_219 = Item('Mageslayer Dagger', 'Weapon', 'epic', "A skilled fighter can deflect magic missiles with this blade. It was enchanted to home in into the mage's throats.",
               0.0, 0,          # Strength
               0.0, 0,          # Intelligence
               0.15, 12,        # Agility
               0.45, 32,        # Willpower
               0.0, 0,          # Endurance
               0.0, 0,          # Charisma
               0.15, 12,        # Luck
               0.35, 24,        # Speed
               0,               # Armor
               "Mageslayer",    # Enchantment
               "On weapon strike deal bonus damage equal to 25% of enemy's intelligence.")    # Enchantment description

item_220 = Item('Firebrand Sword', 'Weapon', 'epic', "A mageblade - forged out of meteorite, reinforced with dark iron. It can withstand a spell and a blade alike.",
               0.35, 24,        # Strength
               0.35, 24,        # Intelligence
               0.15, 8,         # Agility
               0.15, 8,         # Willpower
               0.0, 0,          # Endurance
               0.0, 0,          # Charisma
               0.0, 0,          # Luck
               -0.15, 0,        # Speed
               0,               # Armor
               "Firebrand",     # Enchantment
               "On weapon strike, deal 35 extra fire damage to the enemy.")     # Enchantment description

item_221 = Item('Dragonwood Wand', 'Weapon', 'epic', "Made of material known by it's arcane conductivity, this wand let's you cast a barrage of spells in a blink of an eye!",
               0.0, 0,          # Strength
               0.45, 32,        # Intelligence
               0.0, 0,          # Agility
               0.0, 0,          # Willpower
               0.0, 0,          # Endurance
               0.0, 0,          # Charisma
               0.0, 0,          # Luck
               0.45, 32,        # Speed
               0,               # Armor
               "Energize",      # Description
                "Gain 2% speed every time you take a turn.")      # Enchantment description


# LEGENDARY ITEMS

item_301 = Item('Crown of Will', 'Headpiece', 'legendary', "Crown of the Archlich - it is said to be capable of mind controlling entire armies...",
               0.0, 0,          # Strength
               0.0, 0,          # Intelligence
               0.0, 0,          # Agility
               2, 0,            # Willpower
               0.0, 0,          # Endurance
               3, 0,            # Charisma
               0.0, 0,          # Luck
               0.0, 0,          # Speed
               4,               # Armor
               "Dominion",      # Enchantment
               "1.5x of your charisma and willpower translates into magic damage.")      # Enchantment description

item_302 = Item('Heart of the Mountain', 'Artifact', 'legendary', "Legends say this such of crystal lies at the very bottom of every mountain. Some dwarf clans call it blasphemous to dig in search of them. Nevertheless, it's aura invigorates you to the very core.",
               0.33, 20,     # Strength
               0.33, 20,     # Intelligence
               0.33, 20,     # Agility
               0.33, 20,     # Willpower
               0.33, 20,     # Endurance
               0.33, 20,     # Charisma
               0.33, 20,     # Luck
               0.33, 20,     # Speed
               20,           # Armor
               "Avatar",     # Enchantment
                "You assume the legendary form of Avatar of the Mountain. Take 20% less damage from all sources.")    # Enchantment description

item_303 = Item("Tel'lar", 'Weapon', 'legendary', "Legendary shield-sword forged as a symbol of union between Dwarves and Elves many millennia ago during the War of the Ancients. The peace between us might be long gone, but the blade is still as sharp as ever.",
               0.35, 30,     # Strength
               0.0, 0,     # Intelligence
               0.0, 0,     # Agility
               0.0, 0,     # Willpower
               0.65, 50,     # Endurance
               0.0, 0,     # Charisma
               0.0, 0,     # Luck
               0.0, 0,     # Speed
               120,           # Armor
               "Earthbound",     # Enchantment
                "The legendary shield-sword Tel'lar protects you from harm. Every time you are struck in combat, gain 5% armor, agility and willpower.")    # Enchantment description

item_304 = Item("Blessed Aegis", 'Artifact', 'legendary', "Mithril shield casted in pearl-rainbow coating, said to be blessed by Goddess Nyure. It grants significant protection to the bearer from prismatic forces.",
               0.0, 0,     # Strength
               0.0, 0,     # Intelligence
               0.0, 0,     # Agility
               0.0, 0,     # Willpower
               0.0, 0,     # Endurance
               0.45, 64,     # Charisma
               0.45, 64,     # Luck
               0.0, 0,     # Speed
               45,           # Armor
               "Aegis",     # Enchantment
                "You take 50% less damage from special attacks.")    # Enchantment description



            # Special items

item_404 = Item('???', 'Artifact', 'cursed', "Amulet made of lips and closed eyes. It gives off a sinister aura.",
               -0.33, -20,   # Strength
               -0.33, -20,   # Intelligence
               -0.33, -20,   # Agility
               -0.33, -20,   # Willpower
               -0.33, -20,   # Endurance
               -0.33, -20,   # Charisma
               -0.33, -20,   # Luck
               -0.33, -20,   # Speed
               -20,          # Armor
               "Cursed",     # Enchantment
               "You feel dreadfully compelled to drench it in the blood of your enemies...")    # Enchantment description

item_495 = Item('Warframe', 'Artifact', 'cursed', "Some Gundam or Grendel, idk.",
               1.5, 64,     # Strength
               0.0, 0,      # Intelligence
               0.0, 0,      # Agility
               0.0, 0,      # Willpower
               0.0, 0,      # Endurance
               0.0, 0,      # Charisma
               0.0, 0,      # Luck
               1.5, 64,     # Speed
               120,          # Armor
               "Warframe",     # Enchantment
               "You have to get inside first to see what this beauty is capable of~")    # Enchantment description

item_list_common = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19, item_20, item_21, item_22]
item_list_rare = [item_101, item_102, item_103, item_104, item_105, item_106, item_107, item_108, item_109, item_110, item_111, item_112, item_113, item_114, item_115, item_116, item_117, item_118, item_119, item_120, item_121, item_122]
item_list_epic = [item_201, item_202, item_203, item_204, item_205, item_206, item_207, item_208, item_209, item_210, item_211, item_212, item_213, item_214, item_215, item_216, item_217, item_218, item_219, item_220, item_221]
item_list_legendary = [item_301, item_302, item_303, item_304]
item_list_cursed = [item_404, item_495]
item_list_special = [item_999, item_777]

item_list_weapon_common = [item_19, item_20, item_21]
item_list_headpiece_common = [item_1, item_7, item_13]
item_list_shoulders_common = [item_2, item_8, item_14]
item_list_chest_common = [item_3, item_9, item_15]
item_list_pants_common = [item_4, item_10, item_16]
item_list_gloves_common = [item_5, item_11, item_17]
item_list_boots_common = [item_6, item_12, item_18]

item_list_weapon_rare = [item_119, item_120, item_121]

class Game:

    def __init__(self):
        self.hero = {'dwarf1': Hero('dwarf'), 'dwarf2': Hero('dwarf'), 'dwarf3': Hero('dwarf')}
        self.enemy = {'goblin1': Hero('goblin'), 'goblin2': Hero('goblin'), 'goblin3': Hero('goblin')}
        self.backpack = []
        self.item_dict = {}
        self.ability_dict = {}
        self.days = 365


@app.route('/battleground', methods=['GET', 'POST'])
def battleground():

    if request.method == 'POST':

        if request.form.get('battle dwarf1', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf1', goblin='goblin1', battlelog=battle('dwarf1', 'goblin1'))

        elif request.form.get('battle dwarf2', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf2', goblin='goblin2', battlelog=battle('dwarf2', 'goblin2'))

        elif request.form.get('battle dwarf3', False) == 'Fight!':
            return render_template('battle.html', game=game, dwarf='dwarf3', goblin='goblin3', battlelog=battle('dwarf3', 'goblin3'))

def battle(dwarf, goblin):

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
    dwarf_health = game.hero[dwarf].end_total * 5
    dwarf_max_health = game.hero[dwarf].end_total * 5

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
    goblin_health = game.enemy[goblin].end_total * 5
    goblin_max_health = game.enemy[goblin].end_total * 5

    goblin_tactic = game.enemy[goblin].tactic

    goblin_special_attack_charge = 1
    goblin_special_attack_next = False


    damage = 1
    reduction_message = 1
    critical_message = dwarf_reduction_message = dwarf_increase_message = goblin_reduction_message = goblin_increase_message = goblin_dodge_message = goblin_absorb_message = dwarf_dodge_message = dwarf_absorb_message = False
    dwarf_reduction = []
    goblin_reduction = []
    dwarf_increase = []
    goblin_increase = []
    attack_message = ''
    absorb_message = ''
    attack_type = []

    dwarf_avoidance_message = False
    goblin_firebrand_message = False
    goblin_lifesteal_message = False
    goblin_hawkeye_message = False
    goblin_avoidance_message = False
    dwarf_firebrand_message = False
    dwarf_lifesteal_message = False
    dwarf_hawkeye_message = False
    goblin_stun_message = False
    dwarf_stun_message = False
    goblin_mindsap_will_message = False
    dwarf_mindsap_will_message = False
    goblin_mindsap_int_message = False
    dwarf_mindsap_int_message = False
    goblin_soulrend_message = False
    dwarf_soulrend_message = False
    goblin_souldrain_message = False
    dwarf_souldrain_message = False
    goblin_earthbound_message = False
    dwarf_earthbound_message = False
    goblin_warframe_message = False
    dwarf_warframe_message = False
    lifesteal = 0
    soulrend = 0
    souldrain = 0
    self_destruct = 10

    physical_attack_strings = [' <font class="gray">hits</font>', ' <font class="gray">punches</font>',
                               ' <font class="gray">kicks</font>', ' <font class="gray">attacks</font>',
                               ' <font class="gray">strikes</font>']

    better_physical_attack_strings = [' <font class="gray">hits</font>', ' <font class="gray">attacks</font>',
                                      ' <font class="gray">strikes</font>']

    magic_attack_strings = [' <font class="blue">freezes</font>', ' <font class="purple">arcane blasts</font>',
                            ' launches a <font class="orange">fireball</font> at',
                            ' sets <font class="red">aflame</font>',
                            ' <font class="deep_blue">electrocutes</font>']

    def roll_physical_attack_type(attack_type, roll):
        attack_type += ["physical"]
        if roll == 0:
            attack_type += ["hit"]
        elif roll == 1:
            attack_type += ["punch"]
        elif roll == 2:
            attack_type += ["kick"]
        elif roll == 3:
            attack_type += ["attack"]
        else:
            attack_type += ["strike"]

        return attack_type

    def roll_magical_attack_type(attack_type, roll):
        attack_type += ["magical"]
        if roll == 0:
            attack_type += ["freeze"]
        elif roll == 1:
            attack_type += ["arcane blast"]
        elif roll == 2:
            attack_type += ["fireball"]
        elif roll == 3:
            attack_type += ["aflame"]
        else:
            attack_type += ["electrocute"]

        return attack_type



    # SPECIAL ABILITIES
    # The ones that do something at the start of the encounter.
    if 'Adrenaline' in game.hero[dwarf].specials_list:
        dwarf_speed = dwarf_speed * 4
        dwarf_adrenaline_message = True

    if 'Adrenaline' in game.enemy[goblin].specials_list:
        goblin_speed = goblin_speed * 4
        goblin_adrenaline_message = True

    if 'Warframe' in game.hero[dwarf].specials_list:
        self_destruct = 10

    if 'Warframe' in game.enemy[goblin].specials_list:
        self_destruct = 10


    while not win_condition:

        if dwarf_speed >= goblin_speed:

            if dwarf_special_attack_next:
                factor = random.randint(10, 15)
                damage = (dwarf_physical + dwarf_magical) * round((factor / 10), 2)
                attack_message = random.choice([' unleashes his <font class="yellow">s</font><font class="orange">p</font><font class="red">e</font><font class="purple">c</font><font class="deep_blue">i</font><font class="blue">a</font><font class="green">l</font> <font class="yellow">a</font><font class="orange">t</font><font class="red">t</font><font class="purple">a</font><font class="deep_blue">c</font><font class="blue">k</font> on'])
                attack_type += ["special"]
                dwarf_special_attack_charge += 1
                dwarf_special_attack_next = False
            else:
                if dwarf_tactic == 'Frenzy':
                    factor = random.randint(10, 12)
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
                    attack_message = magic_attack_strings[roll]
                    roll_magical_attack_type(attack_type, roll)

                    dwarf_special_attack_charge += 1
                    if dwarf_special_attack_charge % 5 == 0:
                        dwarf_special_attack_next = True

                elif dwarf_tactic == 'Balanced':
                    damage_type = random.choice([dwarf_physical, dwarf_magical])
                    if damage_type == dwarf_physical:
                        factor = random.randint(10, 12)
                        damage = dwarf_physical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1

                    else:
                        factor = random.randint(8, 15)
                        damage = dwarf_magical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = magic_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1

                    if dwarf_special_attack_charge % 4 == 0:
                        dwarf_special_attack_next = True

                elif dwarf_tactic == 'Overconfidence':
                    damage_type = random.choice([dwarf_physical, dwarf_magical])
                    if damage_type == dwarf_physical:
                        factor = random.randint(10, 12)
                        damage = round(((dwarf_physical * round((factor / 10), 2)) * 0.85), 2)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1

                    else:
                        factor = random.randint(8, 15)
                        damage = round(((dwarf_magical * round((factor / 10), 2)) * 0.85), 2)

                        roll = random.randint(0, 4)
                        attack_message = magic_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        dwarf_special_attack_charge += 1

                    if dwarf_special_attack_charge % 3 == 0:
                        dwarf_special_attack_next = True

            roll_crit = random.randint(1,500)
            if dwarf_luck >= roll_crit:
                damage *= 1.5
                critical_message = True

            roll_charisma = random.randint(1,500)
            if dwarf_charisma >= roll_charisma:
                if random.choice(['reduce', 'increase']) == 'reduce':
                    roll_reduce = random.randint(65,85)
                    reduction = roll_reduce / 100
                    reduction_message = (roll_reduce - 100) * (-1)
                    dwarf_reduction.append(reduction)
                    dwarf_reduction_message = True
                else:
                    dwarf_increase_message = True

            while len(dwarf_increase) > 0:
                damage *= dwarf_increase.pop()

            while len(goblin_reduction) > 0:
                damage *= goblin_reduction.pop()

            if attack_type[0] == "physical":
                if (goblin_agility / (dwarf_strength * 3)) > 0.33:
                    goblin_dodge = 0.33
                elif (goblin_agility / (dwarf_strength * 3)) < 0:
                    goblin_dodge = 0
                else:
                    goblin_dodge = (goblin_agility / (dwarf_strength * 3))

                goblin_dodge = round((goblin_dodge * 100))
                hit_chance = random.randint(1,100)
                if goblin_dodge >= hit_chance:
                    damage = 0
                    goblin_dodge_message = True

            elif attack_type[0] == "magical":
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

            if (damage - goblin_armor) <= 0:
                damage = 0
            else:
                damage -= goblin_armor

            # SPECIAL ABILITIES
            # Oh boy...

            if 'Goblinbane' in game.hero[dwarf].specials_list:
                damage *= 1.15

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

            if 'Stun chance' in game.hero[dwarf].specials_list:
                if (attack_type[0] == "physical") and (attack_type[1] != "kick" or attack_type[1] != "punch"):
                    roll = random.randint(1,100)
                    if roll <= 15:
                        goblin_speed -= goblin_speed_base
                        dwarf_stun_message = True

            if 'Lucky' in game.hero[dwarf].specials_list:
                dwarf_agility = goblin_strength * 2
                if dwarf_luck <= 250:
                    dwarf_luck = 250

            if 'Adrenaline' in game.hero[dwarf].specials_list:
                dwarf_speed_base *= 0.9

            if 'Momentum' in game.hero[dwarf].specials_list:
                dwarf_speed_base *= 1.01

            if 'Energize' in game.hero[dwarf].specials_list:
                dwarf_speed_base *= 1.02

            if 'Avatar' in game.hero[dwarf].specials_list:
                damage *= 0.8

            if 'Dominion' in game.hero[dwarf].specials_list:
                if attack_type[0] == "magical":
                    damage += dwarf_willpower + dwarf_charisma

            if 'Firebrand' in game.hero[dwarf].specials_list:
                if attack_type[0] == "physical":
                    damage += 35
                    dwarf_firebrand_message = True

            if 'Avoidance' in game.enemy[goblin].specials_list:
                roll = random.randint(1,100)
                if roll <= 20:
                    damage = 0
                    goblin_avoidance_message = True

            if 'Lifesteal' in game.hero[dwarf].specials_list:
                lifesteal = damage * 0.1
                damage -= lifesteal
                dwarf_lifesteal_message = True

            if 'Earthbound' in game.enemy[goblin].specials_list:
                goblin_armor *= 1.05
                goblin_agility *= 1.05
                goblin_willpower *= 1.05
                goblin_earthbound_message = True

            if 'Aegis' in game.enemy[goblin].specials_list:
                if attack_type[0] == "special":
                    damage *= 0.5

            if 'Hawkeye' in game.hero[dwarf].specials_list:
                if critical_message:
                    damage += 50
                    dwarf_hawkeye_message = True

            if 'Mind Sap' in game.hero[dwarf].specials_list:
                roll = random.randint(0,1)
                if roll == 0:
                    goblin_willpower *= 0.95
                    dwarf_mindsap_will_message = True
                else:
                    goblin_intelligence *= 0.95
                    dwarf_mindsap_int_message = True

            if 'Spiky Boots' in game.hero[dwarf].specials_list:
                if (attack_type[0] == "physical") and (attack_type[1] == "kick") and critical_message != True:
                    damage *= 1.5

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
                    damage += souldrain
                    souldrain = round(souldrain)
                    dwarf_souldrain_message = True

            if 'Warframe' in game.hero[dwarf].specials_list:
                self_destruct -= 1
                if self_destruct <= 0:
                    dwarf_health -= 9999
                    dwarf_warframe_message = True

            if 'Dominion' in game.hero[dwarf].specials_list:
                damage += (dwarf_willpower + dwarf_charisma) * 1.5



            damage = round(damage)
            goblin_health -= damage

            if goblin_dodge_message:
                turn = '<div class="hero-turn">' + dwarf_name + ' tries to ' + attack_message + ' the goblin, but he manages to dodge the attack!'
                goblin_dodge_message = False
            elif goblin_avoidance_message:
                turn = '<div class="hero-turn">' + dwarf_name + ' tries to ' + attack_message + ' the goblin, but he manages to avoid the attack!'
                goblin_avoidance_message = False

            else:

                turn = '<div class="hero-turn">' + dwarf_name + attack_message + ' goblin for ' + str(damage)

                if dwarf_firebrand_message:
                    turn += ' <font class="orange">(+35)</font>'
                    dwarf_firebrand_message = False
                if dwarf_lifesteal_message:
                    turn += ' <font class="deep_purple">(+' + str(lifesteal) + ')</font>'
                    dwarf_lifesteal_message = False
                if dwarf_hawkeye_message:
                    turn += ' <font class="yellow">(+50)</font>'
                    dwarf_hawkeye_message = False

                if goblin_absorb_message:
                    turn += " damage! (Enemy's willpower mitigates +" + str(absorb_message) + " points of damage.)"
                else:
                    turn += ' damage!'

                goblin_absorb_message = False

                if critical_message and goblin_dodge_message != True:
                    turn += ' <font class="yellow italic">Critical strike!</font>'
                    critical_message = False

                if dwarf_increase_message:
                    roll_increase = random.randint(15, 35)
                    increase = 1 + (roll_increase / 100)
                    increase_message = roll_increase
                    dwarf_increase.append(increase)
                    turn += '<br><font class="italic">His rallying cry bolsters him up, increasing the power of his next attack by ' + str(increase_message) + '%!</font>'
                    dwarf_increase_message = False
                elif dwarf_reduction_message:
                    turn += '<br><font class="italic">His terrifying roar intimidates the goblin, decreasing the power of his next attack by ' + str(reduction_message) + '%!</font>'
                    dwarf_reduction_message = False

                if dwarf_stun_message:
                    turn += '<br>' + dwarf_name + ' manages to stun the opponent! They skip their next turn.'
                    dwarf_stun_message = False

                if dwarf_mindsap_will_message:
                    turn += '<br>' + dwarf_name + " saps goblin's willpower, reducing it by 5%!"
                    dwarf_mindsap_will_message = False

                if dwarf_mindsap_int_message:
                    turn += '<br>' + dwarf_name + " saps goblin's intelligence, reducing it by 5%!"
                    dwarf_mindsap_int_message = False

                if dwarf_soulrend_message:
                    turn += '<br>' + dwarf_name + " rends enemy's very soul, damaging the goblin for " + str(soulrend) + ' damage!'
                    dwarf_soulrend_message = False

                if dwarf_souldrain_message:
                    turn += '<br>' + dwarf_name + " drains enemy's very soul, healing himself and damaging the goblin for " + str(souldrain) + ' damage!'
                    dwarf_souldrain_message = False

                if goblin_earthbound_message:
                    turn += "<br><br>Tel'lar reacts to it's owner taking damage, bolstering up their defences!<br>Goblin's armor, agility and willpower is increased by 5%!"
                    goblin_earthbound_message = False

                if dwarf_warframe_message:
                    turn += '<br><br>"Beep, beep, beep!"<br>' + "Dwarf's warframe explodes into million pieces, damaging the pilot for 9999 damage!"
                    dwarf_warframe_message = False


            turn += '</div>'
            attack_type.clear()
            goblin_speed += goblin_speed_base

        else:

            if goblin_special_attack_next:
                factor = random.randint(10, 15)
                damage = (goblin_physical + goblin_magical) * round((factor / 10), 2)
                attack_message = random.choice([' unleashes his <font class="yellow">s</font><font class="orange">p</font><font class="red">e</font><font class="purple">c</font><font class="deep_blue">i</font><font class="blue">a</font><font class="green">l</font> <font class="yellow">a</font><font class="orange">t</font><font class="red">t</font><font class="purple">a</font><font class="deep_blue">c</font><font class="blue">k</font> on'])
                attack_type = ["special"]
                goblin_special_attack_charge += 1
                goblin_special_attack_next = False
            else:
                if goblin_tactic == 'Frenzy':
                    factor = random.randint(10, 12)
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
                    attack_message = magic_attack_strings[roll]
                    roll_magical_attack_type(attack_type, roll)

                    goblin_special_attack_charge += 1
                    if goblin_special_attack_charge % 5 == 0:
                        goblin_special_attack_next = True

                elif goblin_tactic == 'Balanced':
                    damage_type = random.choice([goblin_physical, goblin_magical])
                    if damage_type == goblin_physical:
                        factor = random.randint(10, 12)
                        damage = goblin_physical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1

                    else:
                        factor = random.randint(8, 15)
                        damage = goblin_magical * round((factor / 10), 2)

                        roll = random.randint(0, 4)
                        attack_message = magic_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1

                    if goblin_special_attack_charge % 4 == 0:
                        goblin_special_attack_next = True

                elif goblin_tactic == 'Overconfidence':
                    damage_type = random.choice([goblin_physical, goblin_magical])
                    if damage_type == goblin_physical:
                        factor = random.randint(10, 12)
                        damage = round(((goblin_physical * round((factor / 10), 2)) * 0.85), 0)

                        roll = random.randint(0, 4)
                        attack_message = physical_attack_strings[roll]
                        roll_physical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1
                    else:
                        factor = random.randint(8, 15)
                        damage = round(((goblin_magical * round((factor / 10), 2)) * 0.85), 0)

                        roll = random.randint(0, 4)
                        attack_message = magic_attack_strings[roll]
                        roll_magical_attack_type(attack_type, roll)

                        goblin_special_attack_charge += 1

                    if goblin_special_attack_charge % 3 == 0:
                        goblin_special_attack_next = True

            roll_crit = random.randint(1,500)
            if goblin_luck >= roll_crit:
                damage = damage * 1.5
                critical_message = True

            roll_charisma = random.randint(1,500)
            if goblin_charisma >= roll_charisma:
                if random.choice(['reduce', 'increase']) == 'reduce':
                    roll_reduce = random.randint(65,85)
                    reduction = roll_reduce / 100
                    reduction_message = (roll_reduce - 100) * (-1)
                    goblin_reduction.append(reduction)
                    goblin_reduction_message = True
                else:
                    goblin_increase_message = True

            while len(goblin_increase) > 0:
                damage *= goblin_increase.pop()

            while len(dwarf_reduction) > 0:
                damage *= dwarf_reduction.pop()

            if attack_type[0] == "physical":
                if (dwarf_agility / (goblin_strength * 3)) > 0.33:
                    dwarf_dodge = 0.33
                elif (dwarf_agility / (goblin_strength * 3)) < 0:
                    dwarf_dodge = 0
                else:
                    dwarf_dodge = (dwarf_agility / (goblin_strength * 3))

                dwarf_dodge = round((dwarf_dodge * 100))
                hit_chance = random.randint(1,100)
                if dwarf_dodge >= hit_chance:
                    damage = 0
                    dwarf_dodge_message = True

            elif attack_type[0] == "magical":
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


            if (damage - dwarf_armor) <= 0:
                damage = 0
            else:
                damage -= dwarf_armor

            # SPECIAL ABILITIES
            # Oh boy...

            if 'Combat 101' in game.enemy[goblin].specials_list:
                if attack_type[0] == "physical":
                    roll = random.randint(0, 2)
                    attack_message = better_physical_attack_strings[roll]

                    attack_type.clear()
                    attack_type += "physical"
                    if roll == 0:
                        attack_type += "hit"
                    elif roll == 1:
                        attack_type += "attack"
                    else:
                        attack_type += "strike"

            if 'Stun chance' in game.enemy[goblin].specials_list:
                if (attack_type[0] == "physical") and ((attack_type[1] != "kick") and (attack_type[1] != "punch")):
                    roll = random.randint(1,100)
                    if roll <= 15:
                        goblin_speed -= goblin_speed_base
                        goblin_stun_message = True

            if 'Lucky' in game.enemy[goblin].specials_list:
                goblin_agility = dwarf_strength * 2
                goblin_luck += 200
                if goblin_luck <= 250:
                    goblin_luck = 250

            if 'Adrenaline' in game.enemy[goblin].specials_list:
                goblin_speed_base *= 0.9

            if 'Momentum' in game.enemy[goblin].specials_list:
                goblin_speed_base *= 1.01

            if 'Energize' in game.enemy[goblin].specials_list:
                goblin_speed_base *= 1.02

            if 'Avatar' in game.enemy[goblin].specials_list:
                damage *= 0.8

            if 'Dominion' in game.enemy[goblin].specials_list:
                if attack_type[0] == "magical":
                    damage += goblin_willpower + goblin_charisma

            if 'Firebrand' in game.enemy[goblin].specials_list:
                if attack_type[0] == "physical":
                    damage += 35
                    goblin_firebrand_message = True

            if 'Avoidance' in game.hero[dwarf].specials_list:
                roll = random.randint(1,100)
                if roll <= 20:
                    damage = 0
                    dwarf_avoidance_message = True

            if 'Lifesteal' in game.enemy[goblin].specials_list:
                lifesteal = damage * 0.1
                damage -= lifesteal
                goblin_lifesteal_message = True

            if 'Earthbound' in game.hero[dwarf].specials_list:
                dwarf_armor *= 1.05
                dwarf_agility *= 1.05
                dwarf_willpower *= 1.05
                dwarf_earthbound_message = True

            if 'Aegis' in game.hero[dwarf].specials_list:
                if attack_type[0] == "special":
                    damage *= 0.5

            if 'Hawkeye' in game.enemy[goblin].specials_list:
                if critical_message:
                    damage += 50
                    goblin_hawkeye_message = True

            if 'Mind Sap' in game.enemy[goblin].specials_list:
                roll = random.randint(0,1)
                if roll == 0:
                    dwarf_willpower *= 0.95
                    goblin_mindsap_will_message = True
                else:
                    dwarf_intelligence *= 0.95
                    goblin_mindsap_int_message = True

            if 'Spiky Boots' in game.enemy[goblin].specials_list:
                if (attack_type[0] == "physical") and (attack_type[1] == "kick") and critical_message != True:
                    damage *= 1.5

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
                    damage += souldrain
                    souldrain = round(souldrain)
                    goblin_souldrain_message = True

            if 'Warframe' in game.enemy[goblin].specials_list:
                self_destruct -= 1
                if self_destruct <= 0:
                    goblin_health -= 9999
                    goblin_warframe_message = True

            if 'Dominion' in game.hero[dwarf].specials_list:
                damage += (goblin_willpower + goblin_charisma) * 1.5



            damage = round(damage)
            dwarf_health -= damage

            if dwarf_dodge_message:
                turn = '<div class="enemy-turn">' + goblin_name + ' tries to ' + attack_message + ' the dwarf, but he manages to dodge the attack!'
                dwarf_dodge_message = False
            elif dwarf_avoidance_message:
                turn = '<div class="enemy-turn">' + goblin_name + ' tries to ' + attack_message + ' the dwarf, but he manages to avoid the attack!'
                dwarf_avoidance_message = False

            else:

                turn = '<div class="enemy-turn">' + goblin_name + attack_message + ' dwarf for ' + str(damage)

                if goblin_firebrand_message:
                    turn += ' <font class="orange">(+35)</font>'
                    goblin_firebrand_message = False
                if goblin_lifesteal_message:
                    turn += ' <font class="deep_purple">(+' + str(lifesteal) + ')</font>'
                    goblin_lifesteal_message = False
                if goblin_hawkeye_message:
                    turn += ' <font class="yellow">(+50)</font>'
                    goblin_hawkeye_message = False

                if dwarf_absorb_message:
                    turn += " damage! (Hero's willpower mitigates +" + str(absorb_message) + " points of damage.)"
                else:
                    turn += ' damage'

                dwarf_absorb_message = False

                if critical_message and dwarf_dodge_message != True:
                    turn += ' <font class="yellow italic">Critical strike!</font>'
                    critical_message = False
                if goblin_increase_message:
                    roll_increase = random.randint(15, 35)
                    increase = 1 + (roll_increase / 100)
                    increase_message = roll_increase
                    goblin_increase.append(increase)
                    turn += '<br><font class="italic">His inspiring shriek invigorates him, increasing the power of his next attack by ' + str(increase_message) + '%!</font>'
                    goblin_increase_message = False
                elif goblin_reduction_message:
                    turn += '<br><font class="italic">His horrifying screech intimidates the dwarf, decreasing the power of his next attack by ' + str(reduction_message) + '%!</font>'
                    goblin_reduction_message = False

                if goblin_stun_message:
                    turn += '<br>' + goblin_name + ' manages to stun the opponent! They skip their next turn.'
                    goblin_stun_message = False

                if goblin_mindsap_will_message:
                    turn += '<br>' + goblin_name + " saps dwarf's willpower, reducing it by 5%!"
                    goblin_mindsap_will_message = False

                if goblin_mindsap_int_message:
                    turn += '<br>' + goblin_name + " saps dwarf's intelligence, reducing it by 5%!"
                    goblin_mindsap_int_message = False

                if goblin_soulrend_message:
                    turn += '<br>' + goblin_name + " rends hero's very soul, damaging the dwarf for " + str(soulrend) + ' damage!'
                    goblin_soulrend_message = False

                if goblin_souldrain_message:
                    turn += '<br>' + goblin_name + " drains hero's very soul, healing himself and damaging the dwarf for " + str(souldrain) + ' damage!'
                    goblin_souldrain_message = False

                if dwarf_earthbound_message:
                    turn += "<br><br>Tel'lar reacts to it's owner taking damage, bolstering up their defences!<br>Dwarf's armor, agility and willpower is increased by 5%!"
                    dwarf_earthbound_message = False

                if goblin_warframe_message:
                    turn += '<br><br>"Beep, beep, beep!"<br>' + "Goblin's warframe explodes into million pieces, damaging the pilot for 9999 damage!"
                    goblin_warframe_message = False

            turn += '</div>'
            attack_type.clear()
            dwarf_speed += dwarf_speed_base

        damage = 0
        battle_log.append(turn)

        if goblin_health <= 0:
            message = '<br>' + dwarf_name + ' slays ' + goblin_name + '!<br><h2>You win the battle!</h2>'
            win_condition = True
            game.hero[dwarf].win = True
            battle_log.append(message)
        elif dwarf_health <= 0:
            message = '<br>' + goblin_name + ' slays ' + dwarf_name + '!<br><h2>You lost the battle.</h2>'
            win_condition = True
            game.hero[dwarf].win = False
            battle_log.append(message)

    game.hero[dwarf].battle = True
    return battle_log


if __name__ == '__main__':
    app.run(host="wierzba.wzks.uj.edu.pl", port=5102, debug=True)
