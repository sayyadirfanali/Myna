#!/usr/bin/env python3
import fontforge

font = fontforge.open("Myna.sfd")
font.mergeFeature("Myna.fea")

font.generate("fonts/Myna.otf")
font.generate("fonts/Myna.ttf")

if "alt_l" in font:
    font.selection.select("alt_l")
    font.copy()
    font.selection.select("l")
    font.paste()

font.generate("fonts/Myna-AltL.otf")
font.generate("fonts/Myna-AltL.ttf")
font.close()
