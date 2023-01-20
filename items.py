# Item class - for designing and creating items
class Item:

    def __init__(self, item_name, item_slot, rarity, description, str_mul, str_bonus, int_mul, int_bonus, agi_mul,
                 agi_bonus, will_mul, will_bonus, end_mul, end_bonus, char_mul, char_bonus, lck_mul, luck_bonus,
                 spd_mul, spd_bonus, armor, special, special_desc):
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

item_1 = Item('Leather Cap', 'Headpiece', 'common',
              'A trusty, sturdy leather cap. Even most valiant of dwarves look like dorks while wearing one.',
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_2 = Item('Leather Shoulderpads', 'Shoulders', 'common',
              "Will not save you from losing an arm but will certainly soften up the blow.",
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_3 = Item('Leather Jacket', 'Chest', 'common',
              "Lookin' gooood!",
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_4 = Item('Leather Jeans', 'Pants', 'common',
              "Not a usual Dwarven garment...",
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_5 = Item('Leather Gloves', 'Gloves', 'common',
              "Sturdy leather gloves - every dwarves' best friend.",
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_6 = Item('Leather Boots', 'Boots', 'common',
              "Solid, steel capped boots may win or lose you a battle.",
              0.1, 2,  # Strength
              0.0, 0,  # Intelligence
              0.1, 2,  # Agility
              0.0, 0,  # Willpower
              0.1, 4,  # Endurance
              0.0, 0,  # Charisma
              0.0, 0,  # Luck
              0.1, 0,  # Speed
              12,  # Armor
              "Ouch!",  # Enchantment
              "Your kicks deal 20% more damage.")  # Enchantment description

# Common - Heavy armor set

item_7 = Item('Rusty Helmet', 'Headpiece', 'common',
              'Grandma always asked you to wear one before heading into the mines.',
              0.15, 2,  # Strength
              0.0, 0,  # Intelligence
              0.0, 0,  # Agility
              0.0, 0,  # Willpower
              0.15, 6,  # Endurance
              0.1, 2,  # Charisma
              0.0, 0,  # Luck
              0.0, 0,  # Speed
              16,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_8 = Item('Rusty Pauldrons', 'Shoulders', 'common',
              'These would look much more intimidating if not for the state they are in.',
              0.15, 2,  # Strength
              0.0, 0,  # Intelligence
              0.0, 0,  # Agility
              0.0, 0,  # Willpower
              0.15, 6,  # Endurance
              0.1, 2,  # Charisma
              0.0, 0,  # Luck
              0.0, 0,  # Speed
              16,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_9 = Item('Rusty Chainmail', 'Chest', 'common',
              "Taking a spear to the chest will still hurt like hell but at least you won't bleed out.",
              0.15, 2,  # Strength
              0.0, 0,  # Intelligence
              0.0, 0,  # Agility
              0.0, 0,  # Willpower
              0.15, 6,  # Endurance
              0.1, 2,  # Charisma
              0.0, 0,  # Luck
              0.0, 0,  # Speed
              16,  # Armor
              None,  # Enchantment
              None)  # Enchantment description

item_10 = Item('Rusty Tasset', 'Pants', 'common', "Noisy...",
               0.15, 2,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 6,  # Endurance
               0.1, 2,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               16,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_11 = Item('Rusty Gauntlets', 'Gloves', 'common',
               "For all those dirty disarming tricks that goblins are known for.",
               0.15, 2,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 6,  # Endurance
               0.1, 2,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               16,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_12 = Item('Rusty Greaves', 'Boots', 'common',
               "What's better than steel capped boots? Steel boots! Too bad these have rusty holes in them...",
               0.15, 2,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 6,  # Endurance
               0.1, 2,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               16,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

# Common -  Light armor set

item_13 = Item('Tattered Hood', 'Headpiece', 'common',
               "It reduces the vision a tad bit, but at least it makes it easier to focus.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_14 = Item('Tattered Epaulettes', 'Shoulders', 'common',
               "Make you look noble - too bad they don't offer much protection.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_15 = Item('Tattered Robe', 'Chest', 'common',
               "This robe must've looked magnificent before moths took a nest in it.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_16 = Item('Tattered Pants', 'Pants', 'common',
               "Offer unprecedented freedom of movement.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_17 = Item('Tattered Gloves', 'Gloves', 'common',
               "They give off a weird feeling of comfort.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_18 = Item('Tattered Shoes', 'Boots', 'common',
               "Pretty airy.",
               0.0, 0,  # Strength
               0.1, 2,  # Intelligence
               0.0, 0,  # Agility
               0.1, 2,  # Willpower
               0.0, 4,  # Endurance
               0.0, 0,  # Charisma
               0.0, 2,  # Luck
               0.15, 0,  # Speed
               8,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

# Common - Weapons

item_50 = Item('Leather Whip', 'Weapon', 'common',
               "Takes a bit of practice to use properly.",
               0.15, 4,  # Strength
               0.0, 0,  # Intelligence
               0.15, 4,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.0, 0,  # Charisma
               0.15, 4,  # Luck
               0.0, 0,  # Speed
               0,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_51 = Item('Bronze Broadsword', 'Weapon', 'common',
               "Every dwarf and their hogs know how to use one.",
               0.15, 6,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.15, 6,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               0,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

item_52 = Item('Oak Staff', 'Weapon', 'common',
               "Provides just as much support for spellcasting as for melee combat.",
               0.1, 4,  # Strength
               0.1, 4,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.1, 2,  # Charisma
               0.1, 2,  # Luck
               0.0, 0,  # Speed
               0,  # Armor
               None,  # Enchantment
               None)  # Enchantment description

# Common - Artifacts

item_99 = Item('CQC Manual', 'Artifact', 'common',
               '"Even you can become a master of melee combat with this handy book!"',
               0.0, 2,  # Strength
               0.0, 0,  # Intelligence
               0.0, 2,  # Agility
               0.0, 0,  # Willpower
               0.0, 2,  # Endurance
               0.0, 0,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               0,  # Armor
               "Combat 101",  # Enchantment
               "Dwarf will no longer punch or kick in melee combat during battle "
               "but instead opt to strike with his weapon.")  # Enchantment description

item_98 = Item('Volatile Flask', 'Artifact', 'common',
               'People take you a bit more serious when you hold this thing so carelessly.',
               0.0, 0,  # Strength
               0.0, 0,  # Intelligence
               0.0, 0,  # Agility
               0.0, 0,  # Willpower
               0.0, 0,  # Endurance
               0.1, 4,  # Charisma
               0.0, 0,  # Luck
               0.0, 0,  # Speed
               0,  # Armor
               "Unstable Concoction",  # Enchantment
               "At the start of the battle either you or the enemy takes 250 extra damage.")  # Enchantment description

# RARE ITEMS
# Rare - Medium armor set

item_101 = Item('Hardleather Helmet', 'Headpiece', 'rare',
                "Reinforced version of leather helmet, now 30% extra sturdy!",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_102 = Item('Hardleather Shoulderpads', 'Shoulders', 'rare', "These may actually save him from losing an arm.",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_103 = Item('Hardleather Chest', 'Chest', 'rare', "Light as leather, hard as bronze!",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_104 = Item('Hardleather Pants', 'Pants', 'rare',
                "They limit his movement a bit but the protection they offer are well worth the trade.",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_105 = Item('Hardleather Gloves', 'Gloves', 'rare',
                "Manly.",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_106 = Item('Hardleather Boots', 'Boots', 'rare',
                "For that extra amount of protection.",
                0.15, 4,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.15, 6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.1, 2,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Rare - Heavy armor set

item_107 = Item('Iron Helmet', 'Headpiece', 'rare',
                "This is getting kinda heavy...",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_108 = Item('Iron Pauldrons', 'Shoulders', 'rare',
                "Maybe if you polished them, they could blind the enemy.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_109 = Item('Iron Cuirass', 'Chest', 'rare',
                "Wouldn't recommend donning this one on a sunny day.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_110 = Item('Iron Legguards', 'Pants', 'rare',
                "Try kicking deez you goblin bastards!",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_111 = Item('Iron Handguards', 'Gloves', 'rare',
                "Why would you even need a Weapon with a pair of these?",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_112 = Item('Iron Greaves', 'Boots', 'rare',
                "We are going full-metal, aw yeah!",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.15, 4,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                24,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Rare - Light armor set

item_113 = Item('Silk Headwrap', 'Headpiece', 'rare',
                "Softness of silk helps you concentrate on your manly thoughts.",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_114 = Item('Silk Shoulderpads', 'Shoulders', 'rare',
                "These are just for show.",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_115 = Item('Silk Vesture', 'Chestpiece', 'rare',
                "Might be mistaken for a bathrobe...",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_116 = Item('Silk Kilt', 'Pants', 'rare',
                "No matter what others may say, it's a kilt alright, it's a kilt...",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_117 = Item('Silk Gloves', 'Gloves', 'rare',
                "Silk's static inducing attributes have been thaumaturgically "
                "confirmed to enhance one's spellweaving abilities. Or something like that.",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_118 = Item('Silk Slippers', 'Boots', 'rare', "Not a battle armament but you didn't have anything better, so...",
                0.0, 0,  # Strength
                0.2, 6,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.1, 4,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 4,  # Speed
                12,  # Armor
                "Static",  # Enchantment
                "Your electrocute spell deals 50% more damage.")  # Enchantment description

# Rare - Other armor pieces

item_119 = Item('Boots of Swiftness', 'Boots', 'rare',
                "They have little feathers attached at the ankle level to let you know that they are enchanted.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.15, 4,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.25, 8,  # Speed
                8,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Rare - Weapons

item_150 = Item('Flintlock Pistol', 'Weapon', 'rare',
                "Once you are out of ammo and gunpowder, it's sturdy handle fits right between goblin's eyes.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.2, 8,  # Charisma
                0.2, 8,  # Luck
                0.15, 6,  # Speed
                0,  # Armor
                "Hawkeye",  # Enchantment
                "Your critical attacks deal extra 50 damage.")  # Enchantment description

item_151 = Item('Iron Mace', 'Weapon', 'rare',
                "They say it has been blessed by a hidden deity - for some reason "
                "holding it puts any dwarf in a mood for some goblin skull bashing.",
                0.2, 8,  # Strength
                0.0, 0,  # Intelligence
                0.1, 4,  # Agility
                0.0, 0,  # Willpower
                0.2, 8,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Stun Chance",  # Enchantment
                "On weapon strike, 15% chance to stun the enemy for a turn.")  # Enchantment description

item_152 = Item('Scrying Orb', 'Weapon', 'rare',
                "Some adept magi can use them to spy on others, but "
                "those truly knowledgeable in the arcane arts can use them to see into past and future.",
                0.0, 0,  # Strength
                0.15, 6,  # Intelligence
                0.0, 0,  # Agility
                0.15, 6,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 6,  # Speed
                0,  # Armor
                "Mind Sap",  # Enchantment
                "On magical attack hit, decrease opponent's "
                "willpower or intelligence by 5%.")  # Enchantment description

item_153 = Item('Crossbow', 'Weapon', 'rare',
                '"Just a crossbow" is exactly what you want your enemies to think. '
                'Even though in reality it really is "just a crossbow", '
                'its bolts can penetrate the thickest of armors. At least partially.',
                0.15, 6,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.15, 6,  # Speed
                0,  # Armor
                "Armor Penetration",  # Enchantment
                "Your physical attacks with a weapon ignore 50% of enemy's armor.")  # Enchantment description

item_154 = Item('Iron-clad Gauntlets', 'Weapon', 'rare',
                'This odd pair of enormous gauntlets originate from an ancient fighting '
                'technique called "crating". They are big enough that you can use them '
                'while wearing another pair of regular gloves underneath!',
                0.15, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 8,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 6,  # Speed
                0,  # Armor
                "Crating",  # Enchantment
                "Your punches deal 30% more damage. On top of that, everytime "
                "you dodge an attack, you counterattack with a punch.")  # Enchantment description

# Rare - Artifacts

item_199 = Item('Shiny Coin', 'Artifact', 'rare',
                "Shiny coin. It's nice to the touch.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.15, 6,  # Luck
                0.15, 6,  # Speed
                0,  # Armor
                "Critical Boost",  # Enchantment
                "Your critical attacks now deal x2.0 damage instead of x1.5")  # Enchantment description

item_198 = Item('Buckler', 'Artifact', 'rare',
                "Handy buckler, useful in deflecting attacks.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.15, 6,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.15, 5,  # Speed
                0,  # Armor
                "Armor Up!",  # Enchantment
                "Increase your total armor value by 25%.")  # Enchantment description

# EPIC ITEMS

# Epic - Medium armor set

item_201 = Item('Dragonscale Helmet', 'Headpiece', 'epic',
                "Gives you quite a mean look.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_202 = Item('Dragonscale Shoulderguards', 'Shoulders', 'epic',
                "Hard as metal, light as leather.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_203 = Item('Dragonscale Chainmail', 'Chest', 'epic',
                "Fireproof but not waterproof!",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                "Fireproof",  # Enchantment
                "You take 50% less damage from fire based spells.")  # Enchantment description

item_204 = Item('Dragonscale Reinforced Kilt', 'Pants', 'epic',
                "A much cooler cousin of Silk Kilt.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_205 = Item('Dragonscale Gauntlets', 'Gloves', 'epic',
                "They've got spikes in case you lose your weapon.",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                "Barbed Fists",  # Enchantment
                "Your punches always crit.")  # Enchantment description

item_206 = Item('Dragonscale Wyrm-riders', 'Boots', 'epic',
                "You could pack a really mean kick with those...",
                0.2, 6,  # Strength
                0.0, 0,  # Intelligence
                0.2, 6,  # Agility
                0.0, 0,  # Willpower
                0.2, 9,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                27,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Epic - Heavy armor

item_207 = Item('Mithril Headguard', 'Headpiece', 'epic',
                "One of many symbols of our race.",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_208 = Item('Mithril Pauldrons', 'Shoulders', 'epic',
                "Looking good chief!",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_209 = Item('Mithril Chestplate', 'Chest', 'epic',
                "Could deflect a fireball or two.",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                "Anti-magic Zone",  # Enchantment
                "You take 20% less damage from magical attacks.")  # Enchantment description

item_210 = Item('Mithril Legguards', 'Pants', 'epic',
                "To guard your jewels from grabby mage's hands.",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_211 = Item('Mithril Gauntlets', 'Gloves', 'epic',
                "Law enforcement uses these as cuffs tw arrest skilled magi.",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_212 = Item('Mithril Greaves', 'Boots', 'epic',
                "Grounds any and all magical discharges.",
                0.25, 8,  # Strength
                -0.2, -8,  # Intelligence
                0.0, 0,  # Agility
                0.25, 8,  # Willpower
                0.25, 12,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                36,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Epic - Light armor

item_213 = Item('Ceremonial Tiara', 'Headpiece', 'epic',
                "You look like a real princess :D",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_214 = Item('Ceremonial Epaluettes', 'Shoulders', 'epic',
                "They make you look bigger and more magnificent.",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_215 = Item('Ceremonial Robe', 'Chest', 'epic',
                "You feel like you could coronate a king in these.",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                "Authority",  # Enchantment
                "Steal 35% of your opponent's charisma.")  # Enchantment description

item_216 = Item('Ceremonial Trousers', 'Pants', 'epic',
                "These might look silly but they are so comfortable!",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_217 = Item('Ceremonial Gloves', 'Gloves', 'epic',
                "They crackle with arcane discharges...",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_218 = Item('Ceremonial Shoes', 'Boots', 'epic',
                "The silver-lining helps you gather mana from the ground.",
                0.0, 0,  # Strength
                0.25, 8,  # Intelligence
                0.0, 0,  # Agility
                0.2, 6,  # Willpower
                0.15, 9,  # Endurance
                0.15, 6,  # Charisma
                0.0, 0,  # Luck
                0.2, 6,  # Speed
                18,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Epic - Other armor pieces

item_219 = Item('Red Boots of Swiftness', 'Boots', 'epic',
                "Dwarvish engineers managed to increase their potency through "
                "a process of coating them in red paint.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.2, 8,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.35, 10,  # Speed
                12,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_220 = Item('Trickster Gauntlets', 'Gloves', 'epic',
                "A pair of gauntlets made out of intricate Elvish tech. "
                "You don't quite fully grasp their functionality but they can be kinda useful.",
                0.1, 5,  # Strength
                0.1, 5,  # Intelligence
                0.1, 5,  # Agility
                0.1, 5,  # Willpower
                0.1, 5,  # Endurance
                0.1, 5,  # Charisma
                0.1, 5,  # Luck
                0.1, 5,  # Speed
                27,  # Armor
                "Multi-tool",  # Enchantment
                "Makes for a good beer keg opener.")  # Enchantment description

item_221 = Item('Vampiric Cowl', 'Headpiece', 'epic',
                "It comes with a mask and a fake pair of longer set of teeth to "
                "help you with your newfound taste for blood.",
                0.0, 0,  # Strength
                0.1, 4,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.2, 8,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                14,  # Armor
                "Lifesteal",  # Enchantment
                "You heal for 20% of your damage done.")  # Enchantment description

# Epic - Weapons

item_250 = Item('Mageslayer Dagger', 'Weapon', 'epic',
                "A skilled fighter can deflect magic missiles with this blade. "
                "It was enchanted to home in onto the mages' throats.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.15, 6,  # Agility
                0.35, 12,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.2, 9,  # Speed
                0,  # Armor
                "Mageslayer",  # Enchantment
                "On weapon strike, deal bonus damage equal to 150% of enemy's intelligence.")  # Enchantment description

item_251 = Item('Firebrand Sword', 'Weapon', 'epic',
                "A two-handed mageblade forged out of meteorite, reinforced with dark iron. "
                "It can withstand a spell and a blade alike.",
                0.35, 12,  # Strength
                0.35, 12,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                -0.25, 0,  # Speed
                0,  # Armor
                "Firebrand",  # Enchantment
                "On weapon strike, deal 45 extra fire damage to the enemy.")  # Enchantment description

item_252 = Item('Dragonwood Wand', 'Weapon', 'epic',
                "Made out of material known by it's arcane conductivity, "
                "this wand let's you cast a barrage of spells in a blink of an eye!",
                0.0, 0,  # Strength
                0.35, 12,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.35, 12,  # Speed
                0,  # Armor
                "Energize",  # Description
                "Gain 3% speed every time you take a turn.")  # Enchantment description

item_253 = Item('"Portable" Cannon', 'Weapon', 'epic',
                "This stunning piece of modern Dwarvish engineering packs a punch like no other weapon!",
                0.85, 18,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.25, 8,  # Charisma
                0.25, 8,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Reload",  # Description
                "It takes two turns to fire this weapon. "
                "This also means that special attacks will happen much less frequently, "
                "although thanks to your over-preparing nature, "
                "first one happens a turn quicker.")  # Enchantment description

item_254 = Item('Grimoire of Shadows', 'Weapon', 'epic',
                "Dark arts used to be a taboo for Dwarves but even taboos can fall victim to the toils of war.",
                0.0, 0,  # Strength
                0.35, 12,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.35, 12,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Dark Arts",  # Description
                "All of your magic spells are replaced with Shadow Bolt. "
                "This forbidden spell penetrates enemy's defences, "
                "ignoring their willpower absorption.")  # Enchantment description

item_255 = Item('Auto Crossbow', 'Weapon', 'epic',
                'Much cooler cousin of its rare "just a crossbow" variant.',
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.45, 16,  # Speed
                0,  # Armor
                "Armor Penetration",  # Enchantment
                "Your physical attacks with a weapon ignore 50% of enemy's armor.")  # Enchantment description

# Epic - Artifacts

item_299 = Item('Mist in a Jar', 'Artifact', 'epic', "It's really just a smoke in a bottle.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Mist",  # Enchantment
                "First four of enemy's attacks will be avoided.")  # Enchantment description

item_298 = Item('Cloak of Avoidance', 'Artifact', 'epic',
                'Elves call it "Cape of Elusiveness", Goblins "Dodge Mantle". Dwarves; however, prefer '
                'to name it by its special ability to make it easier to identify.',
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.1, 4,  # Luck
                0.1, 4,  # Speed
                8,  # Armor
                "Avoidance",  # Enchantment
                "20% chance to avoid enemy attack.")  # Enchantment description

item_297 = Item('Adrenalinium', 'Artifact', 'epic',
                'Potent drug synthesised with the help of some fancy scientific ways. '
                'Though it acts fast and makes you act speedy, it wears off just as quickly, '
                'leaving the user incredibly exhausted.',
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, -6,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Adrenaline",  # Enchantment
                "You start off with a massive 400% speed boost, "
                "but every turn, you lose 15% of your speed till the end of battle.")  # Enchantment description

# LEGENDARY ITEMS

item_301 = Item('Crown of Will', 'Headpiece', 'legendary',
                "Crown of the Archlich - in right hands, it is said to be capable of controlling entire armies...",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                1.5, 0,  # Willpower
                0.0, 0,  # Endurance
                2, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                4,  # Armor
                "Dominion",  # Enchantment
                "1.5x of your charisma and willpower translates into magical damage.")  # Enchantment description

item_302 = Item('Heart of the Mountain', 'Artifact', 'legendary',
                "Legends say that such a crystal lies at the very bottom of every mountain. "
                "Some dwarf clans call it blasphemous to dig in search of them. "
                "Nevertheless, it's aura invigorates you to the very core.",
                0.2, 10,  # Strength
                0.2, 10,  # Intelligence
                0.2, 10,  # Agility
                0.2, 10,  # Willpower
                0.2, 10,  # Endurance
                0.2, 10,  # Charisma
                0.2, 10,  # Luck
                0.2, 10,  # Speed
                20,  # Armor
                "Avatar",  # Enchantment
                "You assume the legendary form of Avatar of the Mountain. "
                "Take 20% less damage from most sources.")  # Enchantment description

item_303 = Item("Tel'lar", 'Weapon', 'legendary',
                "Fabled elvish shield-sword forged as a symbol of union between "
                "Dwarves and Elves many millennia ago during the War of the Ancients. "
                "The peace between us might be long gone, but the blade is still as sharp as ever.",
                0.35, 14,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.45, 16,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                60,  # Armor
                "Earthbound",  # Enchantment
                "The legendary shield-sword Tel'lar protects you from harm. "
                "Every time you are struck in combat, gain 5% armor, agility and willpower.")  # Enchantment description

item_304 = Item("Blessed Aegis", 'Artifact', 'legendary',
                "Mithril shield casted in pearl-rainbow coating, said to be blessed by Goddess Nyure. "
                "It grants significant protection from prismatic forces.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.35, 12,  # Charisma
                0.35, 12,  # Luck
                0.0, 0,  # Speed
                35,  # Armor
                "Aegis",  # Enchantment
                "You take 65% less damage from special attacks.")  # Enchantment description

item_305 = Item("Suspicious Weapon Oil", 'Artifact', 'legendary',
                "Yea, sure, it is dirty and honorless, but think about all the little dwarves "
                "you are going to save from the horrors of war. Tonight the gods will have to look the other way.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, -10,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Neurotoxin",  # Enchantment
                "On first weapon strike, reduce opponent's willpower, agility, "
                "charisma and luck by 35% and deal 500 extra damage.")  # Enchantment description

item_306 = Item("Runeblade of Rivendare", 'Weapon', 'legendary',
                "This dreadful blade cuts not only the body but soul as well.",
                0.35, 12,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.35, 12,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Soulrend",  # Enchantment
                "On weapon strike, deal 5% extra damage based off enemy's total health.")  # Enchantment description

item_307 = Item("Skull of Naz'kar", 'Weapon', 'legendary',
                "Skull of a demon that once terrorized mines of Rinder. "
                "Though the demon has perished many centuries ago, "
                "it still makes for a tremendously powerful magic focus.",
                0.0, 0,  # Strength
                0.35, 12,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.35, 12,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Soul Drain",  # Enchantment
                "On magical hit, steal 3% total health from the enemy.")  # Enchantment description

item_308 = Item("Elixir of Giants", 'Artefact', 'legendary',
                "It's better not to dwell on the ingredients "
                "that are needed to brew one.",
                1.0, 32,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.5, 24,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                -0.75, -18,  # Speed
                30,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

# Special items

item_777 = Item('Lucky Pebble', 'Artifact', 'common', "What is this thing..?",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 2,  # Luck
                0.0, 0,  # Speed
                2,  # Armor
                "Lucky",  # Enchantment
                "What is this thing...? Nevertheless, it's presence "
                "somehow makes you feel a little bit more lucky~")  # Enchantment description

item_555 = Item('White Lotus', 'Artifact', 'legendary', "Mythical flower known to spontaneously bloom on "
                                                        "the graves of great heroes. It bolsters one's vitality.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.3, 25,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                None,  # Enchantment
                None)  # Enchantment description

item_999 = Item('Memento', 'Artifact', 'common',
                "Picture of unknown family, found among stranger's possessions. "
                "For some reason it fills you with unspeakable rage and sense of vengeance, "
                "making you act more reckless.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                -15,  # Armor
                "Goblinbane",
                "Deal 15% more damage to the goblins.")  # Enchantment

item_404 = Item('Cursed Amulet', 'Artifact', 'cursed',
                "An egg-shaped amulet made out of lips and closed eyes. It gives off a sinister aura.",
                -0.33, -20,  # Strength
                -0.33, -20,  # Intelligence
                -0.33, -20,  # Agility
                -0.33, -20,  # Willpower
                -0.33, -20,  # Endurance
                -0.33, -20,  # Charisma
                -0.33, -20,  # Luck
                -0.33, -20,  # Speed
                -20,  # Armor
                "Cursed",  # Enchantment
                "You feel dreadfully compelled to drench it in the blood of your enemies...")  # Enchantment description

item_495 = Item('Warframe', 'Artifact', 'cursed', "Some Gundam or Grendel, idk.",
                1.5, 32,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                1.5, 32,  # Speed
                120,  # Armor
                "Warframe",  # Enchantment
                "You have to get inside first to see what this beauty is capable of.")  # Enchantment description

item_600 = Item('Pipe Bomb', 'Artifact', 'cursed', "You don't like how it stares at you.",
                0.0, 0,  # Strength
                0.0, 0,  # Intelligence
                0.0, 0,  # Agility
                0.0, 0,  # Willpower
                0.0, 0,  # Endurance
                0.0, 0,  # Charisma
                0.0, 0,  # Luck
                0.0, 0,  # Speed
                0,  # Armor
                "Pipe Bomb",  # Enchantment
                "At the start of the battle either you or the enemy "
                "takes 2500 extra damage.")  # Enchantment description

item_list_common = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12,
                    item_13, item_14, item_15, item_16, item_17, item_18, item_50, item_51, item_52, item_99, item_98]
item_list_rare = [item_101, item_102, item_103, item_104, item_105, item_106, item_107, item_108, item_109, item_110,
                  item_111, item_112, item_113, item_114, item_115, item_116, item_117, item_118, item_119, item_150,
                  item_151, item_152, item_153, item_154, item_199, item_198]
item_list_epic = [item_201, item_202, item_203, item_204, item_205, item_206, item_207, item_208, item_209, item_210,
                  item_211, item_212, item_213, item_214, item_215, item_216, item_217, item_218, item_219, item_220,
                  item_221, item_250, item_251, item_252, item_253, item_254, item_255, item_299, item_298, item_297]
item_list_legendary = [item_301, item_302, item_303, item_304, item_305, item_306, item_307, item_308]
item_list_cursed = [item_495, item_600]
item_list_special = [item_999, item_777, item_555, item_404]

item_list_weapon_common = [item_50, item_51, item_52]
item_list_headpiece_common = [item_1, item_7, item_13]
item_list_shoulders_common = [item_2, item_8, item_14]
item_list_chest_common = [item_3, item_9, item_15]
item_list_pants_common = [item_4, item_10, item_16]
item_list_gloves_common = [item_5, item_11, item_17]
item_list_boots_common = [item_6, item_12, item_18]
item_list_artifact_common = [item_99, item_98]

item_list_weapon_rare = [item_150, item_151, item_152, item_153, item_154]
item_list_headpiece_rare = [item_101, item_107, item_113]
item_list_shoulders_rare = [item_102, item_108, item_114]
item_list_chest_rare = [item_103, item_109, item_115]
item_list_pants_rare = [item_104, item_110, item_116]
item_list_gloves_rare = [item_105, item_111, item_117]
item_list_boots_rare = [item_106, item_112, item_118, item_119]
item_list_artifact_rare = [item_199, item_198]

item_list_weapon_epic = [item_250, item_251, item_252, item_253, item_254, item_255]
item_list_headpiece_epic = [item_201, item_207, item_213, item_221]
item_list_shoulders_epic = [item_102, item_108, item_214]
item_list_chest_epic = [item_203, item_209, item_215]
item_list_pants_epic = [item_204, item_210, item_216]
item_list_gloves_epic = [item_205, item_211, item_217, item_220]
item_list_boots_epic = [item_206, item_212, item_218, item_219]
item_list_artifact_epic = [item_299, item_298, item_297]

item_dict = {"Leather Cap": item_1, "Leather Shoulderpads": item_2, "Leather Jacket": item_3,
             "Tight Leather Jeans": item_4, "Leather Gloves": item_5, "Leather Boots": item_6,
             "Rusty Helmet": item_7, "Rusty Pauldrons": item_8, "Rusty Chainmail": item_9, "Rusty Tasset": item_10,
             "Rusty Gauntlets": item_11, "Rusty Greaves": item_12,
             "Tattered Hood": item_13, "Tattered Epaulettes": item_14, "Tattered Robe": item_15,
             "Tattered Pants": item_16, "Tattered Gloves": item_17, "Tattered Shoes": item_18,

             "Leather Whip": item_50, "Bronze Broadsword": item_51, "Oak Staff": item_52,

             "CQC Manual": item_99, "Volatile Flask": item_98,

             "Hardleather Helmet": item_101, "Hardleather Shoulderpads": item_102, "Hardleather Chest": item_103,
             "Hardleather Pants": item_104, "Hardleather Gloves": item_105, "Hardleather Boots": item_106,
             "Iron Helmet": item_107, "Iron Pauldrons": item_108, "Iron Cuirass": item_109, "Iron Legguards": item_110,
             "Iron Handguards": item_111, "Iron Greaves": item_112,
             "Silk Headwrap": item_113, "Silk Shoulderpads": item_114, "Silk Vesture": item_115, "Silk Kilt": item_116,
             "Silk Gloves": item_117, "Silk Slippers": item_118,

             "Boots of Swiftness": item_119,

             "Flintlock Pistol": item_150, "Iron Mace": item_151, "Scrying Orb": item_152, "Crossbow": item_153,
             "Iron-clad Gauntlets": item_154,

             "Shiny Coin": item_199, "Buckler": item_198,

             "Dragonscale Helmet": item_201, "Dragonscale Shoulderguards": item_202, "Dragonscale Chainmail": item_203,
             "Dragonscale Reinforced Kilt": item_204, "Dragonscale Gauntlets": item_205,
             "Dragonscale Wyrm-riders": item_206,
             "Mithril Headguard": item_207, "Mithril Pauldrons": item_208, "Mithril Chestplate": item_209,
             "Mithril Legguards": item_210, "Mithril Gauntlets": item_211, "Mithril Greaves": item_212,
             "Ceremonial Tiara": item_213, "Ceremonial Epaluettes": item_214, "Ceremonial Robe": item_215,
             "Ceremonial Trousers": item_216, "Ceremonial Gloves": item_217, "Ceremonial Shoes": item_218,

             "Red Boots of Swiftness": item_219, "Trickster Gauntlets": item_220, "Vampiric Cowl": item_221,

             "Mageslayer Dagger": item_250, "Firebrand Sword": item_251, "Dragonwood Wand": item_252,
             '"Portable" Cannon': item_253, "Grimoire of Shadows": item_254, "Auto Crossbow": item_255,

             "Mist in a Jar": item_299, "Cloak of Avoidance": item_298, "Adrenalinium": item_297,

             "Crown of Will": item_301, "Heart of the Mountain": item_302, "Tel'lar": item_303,
             "Blessed Aegis": item_304, "Suspicious Weapon Oil": item_305, "Runeblade of Rivendare": item_306,
             "Skull of Naz'kar": item_307, item_308: "Elixir of Giants",

             "Cursed Amulet": item_404, "Memento": item_999, "Warframe": item_495, "Lucky Pebble": item_777,
             "Pipe Bomb": item_600, "White Lotus": item_555}

ability_dict = {
    "Lucky": ["What is this thing...? Nevertheless, it's presence somehow makes you feel a little bit more lucky~",
              "common"],
    "Combat 101": [
        "Dwarf will no longer punch or kick in melee combat during battle but instead opt to strike with his weapon.",
        "common"],
    "Unstable Concoction": ["At the start of the battle either you or the enemy takes 250 extra damage.", "common"],
    "Goblinbane": ["Deal 15% more damage to the goblins.", "common"],
    "Ouch!": ["Your kicks deal 20% more damage.", "common"],

    "Stun Chance": ["On weapon strike, 15% chance to stun the enemy for a turn.", "rare"],
    "Momentum": ["Gain 1% speed every time you take a turn.", "rare"],
    "Hawkeye": ["Your critical attacks deal extra 50 damage.", "rare"],
    "Spiked Boots": ["Your kicks always crit.", "rare"],
    "Armor Penetration": ["Your physical attacks with a weapon ignore 50% of enemy's armor.", "rare"],
    "Static": ["Your electrocute spell deals 50% more damage.", "rare"],
    "Crating": ["Your punches deal 30% more damage. On top of that, everytime "
                "you dodge an attack, you counterattack with a punch.", "rare"],
    "Critical Boost": ["Your critical attacks now deal x2.0 damage instead of x1.5", "rare"],
    "Armor Up!": ["Increase your total armor value by 25%.", "rare"],
    "Mind Sap": ["On magical attack hit, decrease opponent's willpower or intelligence by 5%.", "rare"],

    "Blade Mail": ["You reflect 15% of melee damage taken.", "epic"],
    "Pearl Armor": ["You reflect 15% of magic damage taken.", "epic"],
    "Energize": ["Gain 3% speed every time you take a turn.", "epic"],
    "Lifesteal": ["You heal for 20% of your damage done.", "epic"],
    "Firebrand": ["On weapon strike, deal 45 extra fire damage to the enemy.", "epic"],
    "Smoke Bomb": ["First 4 enemy hits will always miss!", "epic"],
    "Mageslayer": ["On weapon, strike deal bonus damage equal to 150% of enemy's intelligence.", "epic"],
    "Fireproof": ["You take 50% less damage from fire based spells.", "epic"],
    "Anti-magic Zone": ["You take 20% less damage from magical attacks.", "epic"],
    "Authority": ["Steal 35% of your opponent's charisma.", "epic"],
    "Mist": ["First four of enemy attacks will be avoided.", "epic"],
    "Multi-tool": [
        "After a bit of testing, your dwarf managed to figure out their true functionality - on successful attack, "
        "15% chance to blind the enemy. Their next attack will be avoided.",
        "epic"],
    "Reload": [
        "It takes two turns to fire this weapon. This also means that special attacks will happen much less "
        "frequently, although thanks to your over-preparing nature, first one happens a turn quicker.",
        "epic"],
    "Avoidance": ["20% chance to avoid enemy attack.", "epic"],
    "Dark Arts": [
        "All of your magic spells are replaced with Shadow Bolt. This forbidden spell penetrates enemy's defences, "
        "ignoring their willpower absorption.",
        "epic"],
    "Adrenaline": [
        "You start off with a massive 400% speed boost, but every turn, you lose 15% of your speed till the end of "
        "battle.",
        "epic"],
    "Barbed Fists": ["Your punches always crit.", "epic"],

    "Earthbound": [
        "The legendary shield-sword Tel'lar protects you from harm. Every time you are struck in combat, "
        "gain 5% armor, agility and willpower.",
        "legendary"],
    "Soul Drain": ["On magical hit, steal 3% total health from the enemy.", "legendary"],
    "Soulrend": ["On weapon strike, deal 5% extra damage based off enemy's total health.", "legendary"],
    "Avatar": ["You assume the legendary form of Avatar of the Mountain. Take 20% less damage from all sources.",
               "legendary"],
    "Dominion": ["1.5x of your charisma and willpower translates into magical damage.", "legendary"],
    "Aegis": ["You take 65% less damage from special attacks.", "legendary"],
    "Neurotoxin": [
        "On first weapon strike, reduce opponent's willpower, agility, charisma and luck by 35% and deal 500 extra "
        "damage.",
        "legendary"],

    "Cursed": ["Perhaps it would be wiser not to bring it into battle...", "cursed"],
    "Pipe Bomb": ["At the start of the battle either you or the enemy takes 2500 extra damage.", "cursed"],
    "Warframe": [
        "You somehow managed to fit inside... Strength and speed is tremendously increased but you will self-destruct "
        "in 10 turns - may your ashes scatter among the stars well, soldier.",
        "cursed"],
    "Nanomachines": ["You take 50% less damage from physical and magical attacks but 300% more from special attacks.",
                     "cursed"]
}
