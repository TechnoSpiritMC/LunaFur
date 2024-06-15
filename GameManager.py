import random
import Roles
from threading import Lock

import UUIDgen


class CGU:

    """
    This class is the class that is responsible for game turns, and play orders. It allows different lobbys to have
    different timelines and different games. I do not suggest to try to modify it, because you may break the entire game
    engine.
    """

    def __init__(self, lst):
        self.lst = lst
        self.positions = {}
        self.lock = Lock()

    def get_next(self, id_hex):
        with self.lock:
            if id_hex not in self.positions:
                self.positions[id_hex] = 0
            else:
                self.positions[id_hex] = (self.positions[id_hex] + 1) % len(self.lst)
            return self.lst[self.positions[id_hex]]

    def clear(self, id_hex):
        with self.lock:
            if id_hex in self.positions:
                del self.positions[id_hex]

    def get_all_ids(self):
        with self.lock:
            return list(self.positions.keys())

    def view_all_positions(self):
        with self.lock:
            return {id_hex: self.lst[pos] for id_hex, pos in self.positions.items()}


class GameManager:
    """
    Greetings to GameManager. This file's main purpose is managing current games, and allowing them to work. It does so by
    having multiple functions to create, delete, manage and play games, but also functionalities that allow people to vote
    for each other, add, delete, and manage lobbies, and making them work.

    Some methods of this file use Roles.py content. If you run into some random errors, please consider checking if
    Roles.py exists before going into some overcomplicated computer exorcism.

    This file's content will be described in depth here:

    CreateGame:
    CreateGame is the method responsible for creating new games, and referencing them in the central game unit (or CGU as it
    will be referenced further). If you are making your own version of this game, you should consider using CreateGame, and
    if you want to modify it, you will have to modify the entire CGU after that.
    """

    def __init__(self):
        self.games = []
        self.players = []


    def GetGame(self, GameID):

        """"""

        keys : list[str] = []
        ID = -1

        for i in range(len(self.games)):
            hello = self.games[i-1]

            for key in hello.keys():
                keys.append(str(key))

                if GameID == str(key):
                    print(str(key))
                    ID = i - 1

        return keys, ID


    @staticmethod
    def GenerateRolesList(players):
        roles_dict = Roles.GenerateGame(players)

        roles_list = []

        for role, count in roles_dict.items():
            roles_list.extend([role] * count)

        return roles_list

    @staticmethod
    def CreateGame(Players, GameID):
        LocalPlayers = Players[:]
        LocalGame = {}
        LocalRolesList = GameManager.GenerateRolesList(Players)

        while len(LocalPlayers) > 0 and len(LocalRolesList) > 0:
            Player = random.choice(LocalPlayers)
            Role = random.choice(LocalRolesList)
            LocalGame[str(Player)] = str(Role)

            LocalPlayers.remove(Player)
            LocalRolesList.remove(Role)

        print("[GAME] → " + str({GameID: LocalGame}))
        return {GameID: LocalGame}

    def AddGame(self, Players, GameID):
        game = self.CreateGame(Players, GameID)
        self.games.append(game)
        print(">>> " + str(self.games))


    def ViewGames(self):
        return self.games


    def ViewGame(self, GameID):

        game = self.GetGame(GameID)

        if GameID in game[0]:
            return self.games[game[1]]


    def SetPlayerRoles(self, GameID, Player, RolePrivateID):

        PlayerLobby = self.GetGame(GameID)

        lobby = self.games[PlayerLobby[1]]


if __name__ == "__main__":

    GM = GameManager()

    print(GM.GenerateRolesList(["Denis", "Martin", "Sebastian", "Joshua", "Alexis", "Nathan", "Romain"]))

    GM.AddGame(["Denis", "Martin", "Sebastian", "Joshua", "Alexis", "Nathan", "Romain"], "abcdefg")
    print("Games: " + str(GM.ViewGames()))

    print(GM.ViewGame("abcdefg").get("abcdefg"))

# ======================================================================================================================
#                             This file is a part of TechnoSpirit's LunaFur bot. If you want
#                             to modify it, or make your own version, but you are taking parts
#                             of this version, please leave this text at the end of the file
#                                                           ---
#                             Thank you for using LunaFur and I hope it satisfied your needs
# ======================================================================================================================
