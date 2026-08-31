# 🎵 Sound of the Years

A personal music timeline built with Streamlit — scroll through the years, unlock songs one by one, and play their videos directly in the app.

---

## What it does

**Sound of the Years** is an interactive vertical calendar of music memories. Each year from 2004 to 2025 lives in its own capsule. Open a year, and you'll find 5 hidden songs — titles are blurred until you choose to play one. Hit play and the video loads right there in the page.

Key features:
- **Vertical timeline** — one capsule per year, scroll top to bottom through time
- **Era-aware visuals** — each era has its own color accent and background tone that shifts as you scroll
- **Hidden songs** — titles are blurred until you press Play, keeping the discovery feeling alive
- **Inline video player** — YouTube video embeds directly in the app with autoplay
- **Your songs** — the playlist is driven entirely by a CSV file you control

---

## File structure

```
music_timeline/
├── app.py                  # Main Streamlit app
├── songs.csv               # Your original song data
├── songs_with_ids.csv      # The working file: songs + YouTube IDs
├── youtube_id_helper.py    # Helper to generate the lookup template
├── build_app.py            # Rebuilds app.py from songs_with_ids.csv
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## How to run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---

## How to use the app

1. **Scroll** down the timeline to browse years
2. **Click "▼ [year]"** to open a year capsule and see 5 song slots
3. **Click "▶ Play #1"** on any slot — the title reveals and the video starts playing
4. **Click "⏸ Stop"** to stop playback
5. **Click "▲ Close"** to collapse the year back

Only one year can be open at a time. Opening a new year closes the previous one.

---

## How to update the songs

### Step 1 — Edit `songs_with_ids.csv`

This is the master data file. It has one row per song with these columns:

| Column | Description |
|---|---|
| `year` | The year (e.g. `2004`) |
| `title` | Song title shown in the app |
| `artist` | Artist name shown in the app |
| `link_title` | The YouTube video title from your original CSV (for reference) |
| `youtube_id` | **The YouTube video ID** — this is what you need to fill in |
| `search_url` | Auto-generated YouTube search link to help you find the video |

### Step 2 — Get the YouTube ID

For each song, open its YouTube video. The ID is the 11-character code in the URL:

```
https://www.youtube.com/watch?v=Ju8Hr50Ckwk&list=...
                                ^^^^^^^^^^^
                                ID = Ju8Hr50Ckwk
```

Copy everything between `v=` and the first `&` (or end of URL). Paste it into the `youtube_id` column.

You can also use the helper script to auto-generate search links for all songs:
```bash
python3 youtube_id_helper.py
```
This prints each song with a ready-to-click YouTube search URL.

### Step 3 — Rebuild the app

Once all `youtube_id` values are filled in:
```bash
python3 build_app.py
```

This validates the CSV (warns you about any missing IDs) and regenerates `app.py` with your updated songs.

---

## How to customize

### Change the songs for a year

Open `songs_with_ids.csv` and edit any row. You can change the title, artist, and youtube_id freely. Run `build_app.py` afterwards.

### Add or remove a year

- **Add a year**: add 5 rows with the new year value in `songs_with_ids.csv`, then run `build_app.py`.
- **Remove a year**: delete its 5 rows from `songs_with_ids.csv`, then run `build_app.py`.

Then also update the `ERA_THEMES` dictionary in `app.py` (or `build_app.py`) to add/remove the matching theme entry.

### Change the era colors and labels

In `app.py`, find the `ERA_THEMES` dictionary near the top. Each year has:

```python
2004: {
    "bg":     "#0a0a1a",   # Page background tint for this year
    "accent": "#ff6b35",   # Main color: year number, song title, player bar
    "glow":   "#ff4500",   # Glow/shadow color (usually a darker shade of accent)
    "era":    "Early 2000s",  # Small label shown above the vibe text
    "vibe":   "Pop & R&B boom"  # Subtitle line inside the capsule
},
```

Change any of these values to retheme a year.

### Change the number of songs per year

The app supports any number of songs per year — not just 5. Add or remove rows in `songs_with_ids.csv` for that year, then run `build_app.py`.

### Change fonts or layout

All visual styles live in the `CSS` string near the top of `app.py`. The app uses three Google Fonts:
- **Bebas Neue** — year numbers and song titles when playing
- **Space Mono** — small labels, era tags, artist names
- **Rajdhani** — body text and vibe descriptions

To swap a font, change the `@import` URL at the top of the CSS block and update the `font-family` references.

---

## Deploying to Streamlit Cloud

1. Push your project folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set the main file path to `app.py`
4. Deploy — Streamlit Cloud installs `requirements.txt` automatically

> Make sure `songs_with_ids.csv` is committed to the repo (it's needed by `build_app.py` but not by the running app — `app.py` is self-contained).
---
## Requirements
```
streamlit>=1.32.0
```
Python 3.9 or higher recommended.
