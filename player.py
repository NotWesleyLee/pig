"""Program for entities"""

class Player():
    """Class function for players"""
    def __init__(self, name, total, turn, is_bot):
        self.name = name
        self.total = total
        self.turn = turn
        self.is_bot = is_bot

    def failure(self):
        """Program to display failure state"""
        print('Oh No! {} rolled a 1'.format(self.name))
        print("{}'s total points: {}\n".format(self.name, self.total))

    def display_stats(self):
        """Program to display stats"""
        print("{} ended their turn for a total of {} points\n"
              .format(self.name, self.total))
