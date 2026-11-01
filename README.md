# Gambling777

A terminal-based 3-reel slot machine written in Python. Reels are modelled as NumPy arrays that are rotated with `numpy.roll`, rendered as an in-place animated 3x3 grid using ANSI escape codes, and accompanied by sound effects through `pygame.mixer`. A persistent high score is stored in a text file.

Learning goals of the project: NumPy arrays, a basic game loop and state tracking, file handling, and first use of `pygame` for audio.

## Features

- Three reels that spin simultaneously and stop one after another (reel 1, then reel 2, then reel 3).
- Randomised spin length per reel, so every spin ends differently.
- Spin animation drawn in place in the terminal (`\033[3F` moves the cursor up three lines, so the grid is redrawn rather than scrolled).
- Looping spin sound during the spin, and a sound cue on completion.
- Balance tracking with a fixed stake per spin.
- Persistent high score in `highscore.txt`, with an option to reset it.

## How it works

**Reels**

Each reel is a 4-element array of the symbols `$`, `&`, `7`, `N`. The three reels start at different offsets, so the initial grid is not uniform.

```python
column_1 = array(['$','&','7','N'])
column_2 = array(['&','7','N','$'])
column_3 = array(['7','N','$','&'])
```

**Spin logic**

```
l = randint(20, 25)   # reel 1 stops after l+1 rolls
m = randint(32, 37)   # reel 2 stops after m+1 rolls
n = randint(40, 50)   # total frames; reel 3 rolls every frame
```

For each frame `i in range(n)`, reel 1 rolls while `i <= l`, reel 2 rolls while `i <= m`, and reel 3 always rolls. Since `l < m < n` always holds, the reels stop in order. Each frame is printed as a 3x3 grid and delayed with `time.sleep(0.2)`.

```
[['$' '&' '7']
 ['&' '7' 'N']
 ['7' 'N' '$']]
```

**Payline**

Only the middle row (index `[1]` of each reel) is evaluated.

**Payouts**

The stake of 10 is deducted before the spin; the payout is then added back. Net values match the in-game rules text.

| Middle row | Payout added | Net result |
|---|---|---|
| `7 7 7` | +110 | **+100** (jackpot) |
| `$ $ $` | +80 | +70 |
| `& & &` | +70 | +60 |
| `N N N` | +0 | -10 (stake lost) |
| Any two matching | +30 | +20 |
| No match | +0 | -10 |

**Game loop**

- Starts with a balance of `100` and a spin cost of `10`.
- Press Enter to spin, or type anything to cash out.
- The game ends when the balance reaches `0` or the player cashes out.
- The final balance is the score and is compared with the stored high score.

**High score**

`highscore.txt` is read with `open(..., "r")`; a missing file is handled with `FileNotFoundError` and defaults to `0`. A new high score overwrites the file and plays a looping victory track. Otherwise, the current high score is shown and the player may reset it.

## Requirements

- Python 3.x
- [`numpy`](https://pypi.org/project/numpy/)
- [`pygame`](https://pypi.org/project/pygame/)
- Three audio files (not included): a spin loop, a spin-over/win sound, and a high-score track
- A terminal that supports ANSI escape codes (Windows Terminal, VS Code terminal, or any Linux/macOS terminal)

```bash
pip install numpy pygame
```

## Setup

The audio paths are hard-coded absolute Windows paths. Edit these three variables to point at your own files:

```python
spin     = r"...\slot machine spin sound.mp3"   # looped during the spin
spinover = r"...\winsound.mp3"                  # played when the reels stop
high     = r"...\W.mp3"                         # looped on a new high score
```

A relative path such as `os.path.join(os.path.dirname(__file__), "sounds", "winsound.mp3")` is recommended for portability.

## Run

```bash
python Gambling777.py
```

Enter `r` at the first prompt to see the rules. The game then loops until you cash out or go broke.

## Project structure

```
Gambling777.py     # entire application (single file)
highscore.txt      # created automatically on the first new high score
```

## Known limitations

- **Case check bug:** `r == ("r" or 'R')` and `input() == ("y" or "Y")` both evaluate to a comparison against only the first string, so `R` and `Y` are not accepted. Use `r.lower() == "r"` or `r in ("r", "R")`.
- `from numpy import *` pollutes the namespace and can shadow built-ins such as `sum`, `max`, `min`, `all` and `any`. Prefer `import numpy as np`.
- The spin-over sound is played after every spin, including losing ones.
- Audio paths are hard-coded, so the program fails to start on any other machine without edits (`pygame.error` on load).
- `highscore.txt` is resolved relative to the current working directory, not the script's location, and a corrupted file raises an unhandled `ValueError`.
- The reel is a fixed 4-symbol cycle, so symbol frequency is uniform and the odds are not tunable independently of the layout.
- The spin loop uses blocking `time.sleep` calls, so input cannot be interrupted mid-animation.

## Possible improvements

- Replace the copy-pasted `if/elif` payout chain with a dict lookup, e.g. `PAYOUTS = {"7": 110, "$": 80, "&": 70, "N": 0}`.
- Use `np.random.default_rng()` and weighted symbols to control the house edge.
- Wrap the main flow in `main()` and add `if __name__ == "__main__":`.
- Store the high score as JSON together with the player name and date.
- Add input validation and a configurable stake.

---
*Virtual currency only. Built as a learning project.*
