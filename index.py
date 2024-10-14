class Skin:
    def __init__(self):
        champion = ""
        cor = ""
        conjunto = ""

    def __eq__(self, other):
        return self.champion == other.champion and self.conjunto == other.conjunto

