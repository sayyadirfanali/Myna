#!/usr/bin/env python3
import fontforge

font = fontforge.open("Myna.sfd")
font.generate("Myna.otf")

if "alt_l" in font:
    font.selection.select("alt_l")
    font.copy()
    font.selection.select("l")
    font.paste()

font.generate("Myna-alt_l.otf")
font.close()
