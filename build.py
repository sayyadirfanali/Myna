import fontforge
import math
import psMat

def mkFont(name, weight):
    font = fontforge.open(name + ".sfd")
    font.mergeFeature("features.fea")
    font.generate("./fonts/" + name + ".otf")
    font.generate("./fonts/" + name + ".ttf")

    font.selection.all()
    angle = 12
    font.transform(psMat.skew(angle * math.pi / 180))

    font.fontname   = name + "Italic"
    font.familyname = "Myna"
    font.fullname   = "Myna " + weight + " Italic"
    font.weight     = weight

    font.italicangle = angle

    font.os2_stylemap |= 0x01
    panoseL = list(font.os2_panose)
    panoseL[7] = 1
    font.os2_panose = tuple(panoseL)

    font.appendSFNTName("English (US)", "SubFamily", "Italic")

    font.generate("./fonts/" + name + "Italic.otf")
    font.generate("./fonts/" + name + "Italic.ttf")
    font.close()

mkFont("Myna-Regular", "Regular")
mkFont("Myna-Bold", "Bold")
