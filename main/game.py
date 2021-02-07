import random


class Game:
    def __init__(self, characters, players):
        """
        *
        characters: list of characters
        players: list of players
        """
        self.characters = random.sample(characters, len(characters))
        self.players = random.sample(players, len(players))
        self.assignment = dict(zip(self.players, self.characters))

    def player_count_check(self):
        if len(self.characters) >= len(self.players):
            self.player_check = True
        else:
            self.player_check = False

    def play(self):
        if self.player_check:
            for player, character in self.assignment.items():
                if character == "Werewolf":
                    print("Werewolf")

            playing = True
            while playing:
                pass

    # 1 Werewolf role
    class Werewolf:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 2 Civillian role
    class Civillian:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 3 Robber role
    class Robber:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 4 TroubleMaker role
    class TroubleMaker:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 5 Seer role
    class Seer:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 6 Drunk role
    class Drunk:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 7 Insomniac
    class Insomniac:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 8 Tanner
    class Tanner:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """

    # 9 Hunter
    class Hunter:
        def __init__(self, player):
            self.player = player

        def action(self, player):
            """
            Action happening at night time, voting for the player
            """

        def vote(self):
            """
            Voting in the day time in the public
            """
