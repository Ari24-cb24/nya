class Nya:
    def __init__(self):
        self.chars = {
                "n": ("n", "m"),
                "y": ("y", "e", "i"),
                "a": ("a"),
                "u": ("o"),
                "d": ("t")
            }

    def replace_char(self, c):
        for keys in self.chars.keys():
            if c in self.chars[keys]:
                return keys

        return c
    
    def nyaifier(self, text):
        return "".join(self.replace_char(c) for c in text)
