python build.py \
&& cp Myna-alt_l.otf ~/.fonts/. \
&& fontforge -script ~/bin/fontpatcher/font-patcher --complete Myna.otf && mv MynaNerdFont-Regular.otf Myna-NerdFont.otf \
&& fontforge -script ~/bin/fontpatcher/font-patcher --complete Myna-alt_l.otf && mv MynaNerdFont-Regular.otf Myna-NerdFont-alt_l.otf
