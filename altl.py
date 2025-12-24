import fontforge
import math
import psMat

def mkFont(name, weight):
    font = fontforge.open(name + ".sfd")

    font.selection.select("alt_l")
    font.copy()
    font.selection.select("l")
    font.paste()

    font.generate(name + ".otf")

    font.close()

mkFont("Myna-Regular", "Regular")
mkFont("Myna-Bold", "Bold")
