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

    font.familyname = "Myna"
    font.weight     = weight
    font.italicangle = -angle
    
    if weight == "Bold":
        subfamily = "Bold Italic"
        # 0x01 (Italic) + 0x20 (Bold) = 0x21
        font.os2_stylemap = 0x21 
        full_name = "Myna Bold Oblique"
    else:
        subfamily = "Italic"
        font.os2_stylemap = 0x01
        full_name = "Myna Regular Oblique"

    font.fullname = full_name
    font.fontname = full_name.replace(" ", "")

    # This is the critical part for app recognition:
    font.appendSFNTName("English (US)", "SubFamily", subfamily)

    # Preferred Style
    # font.appendSFNTName("English (US)", "Preferred Style", weight + " Oblique")

    # 7th is Letterform where 9 = Oblique and 2 = Italic
    panoseL = list(font.os2_panose)
    panoseL[7] = 9 
    font.os2_panose = tuple(panoseL)

    font.generate("./fonts/" + name + "Oblique.otf")
    font.generate("./fonts/" + name + "Oblique.ttf") 
    font.close()


mkFont("Myna-Regular", "Regular")
mkFont("Myna-Bold", "Bold")
