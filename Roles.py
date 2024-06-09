"""
Roles.py

This Python script automates the distribution of roles for the game "Werewolf"
(also known as "Mafia"). The script is designed to handle various numbers of
players and assign roles accordingly to ensure a balanced and engaging game.

Here are also defined the order of roles being played. They are based on the
official rules, and should be correct. If you want to modify them, you can
change the "Order" value of your role to change. If you want to add a character

Key Features:
- Supports different player counts, from small groups to large gatherings.
- Includes essential roles such as Werewolves, Villagers, Seer, Witch, Cupid, Hunter, and more.
- Ensures role distribution is fair and random to maintain game integrity and fun.
- Can be easily customized to add or remove roles based on player preferences.

Author: TechnoSpirit
Created: June 5th, 2024, 4:30 PM UTC+2.
Last Updated: June 7th, 2024, 9:14 AM UTC+2
"""


class Roles:
    werewolf = "loup garou"

    villager = "villageois"

    cupid = "cupidon"

    hunter = "chasseur"

    robber = "voleur"

    seer = "voyante"

    mayor = "maire"

    girl = "petite fille"

    witch = "sorcière"

    """
    Nightclub is the list of all characters that wake up during the night at the same time as the werewolves. Consider
    adding your custom wolves here, or it wont work as was made originally.
    """
    nightclub = [werewolf, girl]

    # ==================================================================================================================
    #                             /!\ - Change these values if you are adding custom roles - /!\
    # ==================================================================================================================
    min = 6
    max = 18
    # ==================================================================================================================
    #                             /!\ - Change these values if you are adding custom roles - /!\
    # ==================================================================================================================

    roles = {
        "6": {
            werewolf: 2,
            seer: 1,
            mayor: 1,
            villager: 2,

            cupid: 0,
            hunter: 0,
            robber: 0,
            girl: 0,
            witch: 0,
        },

        "7": {
            werewolf: 2,
            seer: 1,
            mayor: 1,
            villager: 3,

            cupid: 0,
            hunter: 0,
            robber: 0,
            girl: 0,
            witch: 0,
        },

        "8": {
            werewolf: 2,
            seer: 1,
            mayor: 1,
            villager: 4,

            cupid: 0,
            hunter: 0,
            robber: 0,
            girl: 0,
            witch: 0,

        },

        "9": {
            werewolf: 2,
            seer: 1,
            villager: 4,
            cupid: 1,
            hunter: 1,

            robber: 0,
            mayor: 0,
            girl: 0,
            witch: 0,
        },

        "10": {
            werewolf: 2,
            seer: 1,
            villager: 4,
            cupid: 1,
            hunter: 1,
            girl: 1,

            robber: 0,
            mayor: 0,
            witch: 0,
        },

        "11": {
            werewolf: 2,
            seer: 1,
            villager: 5,
            cupid: 1,
            hunter: 1,
            witch: 1,

            robber: 0,
            mayor: 0,
            girl: 0,
        },

        "12": {
            werewolf: 3,
            seer: 1,
            villager: 4,
            cupid: 1,
            hunter: 1,
            girl: 1,
            robber: 1,

            mayor: 0,
            witch: 0,
        },

        "13": {
            werewolf: 3,
            seer: 1,
            villager: 5,
            cupid: 1,
            hunter: 1,
            witch: 1,
            robber: 1,

            mayor: 0,
            girl: 0,
        },

        "14": {
            werewolf: 3,
            seer: 1,
            villager: 6,
            cupid: 1,
            hunter: 1,
            girl: 1,
            robber: 1,

            mayor: 0,
            witch: 0,
        },

        "15": {
            werewolf: 3,
            seer: 1,
            villager: 7,
            cupid: 1,
            hunter: 1,
            witch: 1,
            robber: 1,

            mayor: 0,
            girl: 0,
        },

        "16": {
            werewolf: 3,
            seer: 1,
            villager: 7,
            cupid: 1,
            hunter: 1,
            witch: 1,
            robber: 1,
            girl: 1,

            mayor: 0,
        },

        "17": {
            werewolf: 4,
            seer: 1,
            villager: 7,
            cupid: 1,
            hunter: 1,
            witch: 1,
            robber: 1,
            girl: 1,

            mayor: 0,
        },

        "18": {
            werewolf: 4,
            seer: 1,
            villager: 8,
            cupid: 1,
            hunter: 1,
            witch: 1,
            robber: 1,
            girl: 1,

            mayor: 0,
        },
    }


def GenerateGame(Players):
    _Players = len(Players)

    if Roles.min <= _Players <= Roles.max:
        return Roles.roles.get(str(_Players))

    else:
        return None


"""

----------

for i in range(11):
    testList = []
    for j in range(6+i):
        testList.append(str(j))

    print(str(len(GenerateGame(testList))) + " " + str(6+i))
    
    players = ["a", "b", "c", "d", "e", "f", "g"]
    RolesList = generate_roles_list(players)
    print(RolesList)
    
----------    
    
This is a test script that is used to check if all the roles are being set up properly. This is useful if you have added
custom roles, and want to check is everything is working as it should. Please note that for the generator to work
properly, you HAVE TO set unused roles to zero, and DO NOT ignore them.

If you are using this script to check if your custom roles are set up properly, you will have to change some values in
the given script as follows:

for i in range(Roles.max - Roles.min):
    testList = []
    for j in range(Roles.min + i):
        testList.append(str(j))

    print(str(len(GenerateGame(testList))) + " " + str(6+i))
    
    players = ["a", "b", "c", "d", "e", "f", "g"]
    RolesList = generate_roles_list(players)
    print(RolesList)

You can uncomment or paste the script as is, as the values were showed as placeholders and not as raw values.


########################################################################################################################

Everything below this docstring are test codes that can be safely deleted. But, you should still check to see if they
are used or not, as some test scripts are used in a more permanent way in other files. But I don't really know why you
would even have this idea of deleting some random code...

########################################################################################################################

"""


def generate_roles_list(Players):
    RolesDict = GenerateGame(Players)

    _RolesList = []

    for role, count in RolesDict.items():
        _RolesList.extend([role] * count)

    return _RolesList

# ======================================================================================================================
#                             This file is a part of TechnoSpirit's LunaFur bot. If you want
#                             to modify it, or do your own version, but you are taking parts
#                             of this version, please leave this text at the end of the file
#                                                           ---
#                             Thank you for using LunaFur and I hope it satisfied your needs
#
# ======================================================================================================================
