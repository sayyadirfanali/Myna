import fontforge

font = fontforge.open("Myna-Regular.sfd")

ascent  = font.ascent
descent = font.descent

RATIO = 0.9

# general
font.ascent  = int(font.ascent * RATIO)
font.descent = int(font.descent * RATIO)

# hhea
font.hhea_ascent  = int(font.hhea_ascent * RATIO)
font.hhea_descent = int(font.hhea_descent * RATIO)

# OS/2 typo
font.os2_typoascent  = font.hhea_ascent
font.os2_typodescent = font.hhea_descent

# OS/2 win
font.os2_winascent = ascent # can increase or decrease this if clipped 
font.os2_windescent = descent

font.save("Myna-Regular.sfd")
font.close()
