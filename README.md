![Myna](./images/hero.png)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-OFL-success.svg?style=for-the-badge)

Do you ever feel like your programmign font treats symbols as second-class glyphs? Are you frustrated that your `->` looks nothing like an arrow, or `$`, `@`, `%` seem ever mismatched?
Want to experience the beauty of ligatures without losing the simplicity of ASCII.

**Myna** (*Gracula religiosa* 🐦‍⬛) is a monospace font which aims to bring harmony to your editor by treating symbols as first-class glyphs alongside alphanumeric characters.

## Why Myna?
Here is why Myna stands apart from other fonts:
- **Symbol-First Design**: clear emphasis on ASCII symbols which are ubiquitous in programming languages
- **Near-Perfect Alignment**: multi-character symbols like `->`, `>>=`, `=~`, `::` align seamlessly
- **Balanced Weight**: symbols have just the right visual weight against your code
- **Minimalist Forms**: geometric shapes for quotes and commas
- **Clear Distinction**: no more confusing `1 l I |` or `0 O o`
- **Language-Aware Design**: clean sigils for Perl + elegant operators for Haskell + clear symbols for C

NB: Myna is a very simple font. It does **not** feature ligatures, or separate bold/italic styles currently.

## Showcase
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="images/Perl_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="images/Perl_light.png">
  <img alt="Perl" src="https://example.com/Perl_light.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="images/Haskell_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="images/Haskell_light.png">
  <img alt="Haskell" src="https://example.com/Haskell_light.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="images/C_dark.png">
  <source media="(prefers-color-scheme: light)" srcset="images/C_light.png">
  <img alt="C" src="https://example.com/C_light.png">
</picture>


| Language | Light | Dark |
|----------|-------|------|
|  **Perl**     |  <img  src="images/Perl_light.png"     width="500">  |  <img  src="images/Perl_dark.png"     width="500">  |
|  **Haskell**  |  <img  src="images/Haskell_light.png"  width="500">  |  <img  src="images/Haskell_dark.png"  width="500">  |
|  **C**        |  <img  src="images/C_light.png"        width="500">  |  <img  src="images/C_dark.png"        width="500">  |
|  **Bash**     |  <img  src="images/Bash_light.png"     width="500">  |  <img  src="images/Bash_dark.png"     width="500">  |
|  **Clojure**  |  <img  src="images/Clojure_light.png"  width="500">  |  <img  src="images/Clojure_dark.png"  width="500">  |
|  **Erlang**   |  <img  src="images/Erlang_light.png"   width="500">  |  <img  src="images/Erlang_dark.png"   width="500">  |
|  **OCaml**    |  <img  src="images/OCaml_light.png"    width="500">  |  <img  src="images/OCaml_dark.png"    width="500">  |
|  **Ruby**     |  <img  src="images/Ruby_light.png"     width="500">  |  <img  src="images/Ruby_dark.png"     width="500">  |
|  **Rust**     |  <img  src="images/Rust_light.png"     width="500">  |  <img  src="images/Rust_dark.png"     width="500">  |
|  **LaTeX**    |  <img  src="images/LaTeX_light.png"    width="500">  |  <img  src="images/LaTeX_dark.png"    width="500">  |
|  **HTML**     |  <img  src="images/HTML_light.png"     width="500">  |  <img  src="images/HTML_dark.png"     width="500">  |
|  **SQL**      |  <img  src="images/SQL_light.png"      width="500">  |  <img  src="images/SQL_dark.png"      width="500">  |

## Installation
### macOS
```bash
git clone https://github.com/sayyadirfanali/Myna.git
cd Myna
cp Myna.otf ~/Library/Fonts/
```

### Linux
```bash
git clone https://github.com/sayyadirfanali/Myna.git
cd Myna
cp Myna.otf ~/.local/share/fonts/
fc-cache -v
```

### Windows
1. Download the release
2. Right-click `Myna.otf` and select "Install for all users"

## License
SIL Open Font License

## Credits
Myna started out as [Hera](https://github.com/sayyadirfanali/Hera.git) which was a customised version of Source Code Pro but now has come a long way after stealing many beautiful designs from Fira Mono, Inconsolata, Plex Mono, Office Code Pro, Anonymous Pro.

## Contributions
Myna is designed to be used in every terminal primarily with ASCII text. If you want the shape of some glyph to be changed or find Myna lacking in some non-ASCII glyph and want it to be added, please feel free to open issues. You can also contact me at irfan@irfanali.org.
