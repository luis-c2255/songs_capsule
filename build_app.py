import csv
from collections import defaultdict

INPUT_CSV = "songs_with_ids.csv"
APP_FILE  = "app.py"

ERA_THEMES = {
    2004: {"bg": "#0a0a1a", "accent": "#ff6b35", "glow": "#ff4500", "era": "Early 2000s", "vibe": "Pop & R&B boom"},
    2005: {"bg": "#0d0a1a", "accent": "#ff6b35", "glow": "#ff4500", "era": "Early 2000s", "vibe": "Hip-hop goes mainstream"},
    2006: {"bg": "#0a1a0a", "accent": "#39ff14", "glow": "#00ff41", "era": "Mid-2000s", "vibe": "Dance-pop rises"},
    2007: {"bg": "#0a1a10", "accent": "#39ff14", "glow": "#00ff41", "era": "Mid-2000s", "vibe": "Club anthems era"},
    2008: {"bg": "#1a0a0a", "accent": "#ff073a", "glow": "#ff1744", "era": "Late 2000s", "vibe": "Lady Gaga changes pop"},
    2009: {"bg": "#1a0a10", "accent": "#ff073a", "glow": "#ff1744", "era": "Late 2000s", "vibe": "Electronic explosion"},
    2010: {"bg": "#0a0a1a", "accent": "#00cfff", "glow": "#00bfff", "era": "New Decade", "vibe": "Digital-pop era begins"},
    2011: {"bg": "#0a1020", "accent": "#00cfff", "glow": "#00bfff", "era": "New Decade", "vibe": "Adele rules the world"},
    2012: {"bg": "#10080a", "accent": "#e040fb", "glow": "#ce93d8", "era": "Early 2010s", "vibe": "Gangnam Style goes viral"},
    2013: {"bg": "#080a10", "accent": "#e040fb", "glow": "#ce93d8", "era": "Early 2010s", "vibe": "Indie-pop moment"},
    2014: {"bg": "#0a1008", "accent": "#ffeb3b", "glow": "#ffd600", "era": "Mid-2010s", "vibe": "Happy vibes dominate"},
    2015: {"bg": "#100a08", "accent": "#ffeb3b", "glow": "#ffd600", "era": "Mid-2010s", "vibe": "Uptown era"},
    2016: {"bg": "#08100a", "accent": "#ff4081", "glow": "#f50057", "era": "Mid-2010s", "vibe": "Drake era begins"},
    2017: {"bg": "#100808", "accent": "#ff4081", "glow": "#f50057", "era": "Late 2010s", "vibe": "Trap pop takeover"},
    2018: {"bg": "#080810", "accent": "#64ffda", "glow": "#1de9b6", "era": "Late 2010s", "vibe": "Streaming wars peak"},
    2019: {"bg": "#100810", "accent": "#64ffda", "glow": "#1de9b6", "era": "Late 2010s", "vibe": "Reggaeton era peaks"},
    2020: {"bg": "#0a0a0a", "accent": "#bb86fc", "glow": "#7c4dff", "era": "2020s", "vibe": "Pandemic anthems"},
    2021: {"bg": "#080010", "accent": "#bb86fc", "glow": "#7c4dff", "era": "2020s", "vibe": "Spanish pop takeover"},
    2022: {"bg": "#0a0508", "accent": "#ff80ab", "glow": "#ff4081", "era": "2020s", "vibe": "Electronic revival"},
    2023: {"bg": "#050a08", "accent": "#69ff47", "glow": "#00e676", "era": "2020s", "vibe": "Deep house rules"},
    2024: {"bg": "#080a05", "accent": "#ffd740", "glow": "#ffab00", "era": "2020s", "vibe": "New wave"},
    2025: {"bg": "#050808", "accent": "#40c4ff", "glow": "#0091ea", "era": "Now",   "vibe": "The current soundtrack"},
}

def load_songs():
    songs_by_year = defaultdict(list)
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = int(row["year"])
            songs_by_year[year].append({
                "title":  row["title"],
                "artist": row["artist"],
                "yt":     row["youtube_id"].strip(),
            })
    return dict(songs_by_year)

def validate(songs_by_year):
    issues = []
    for year, songs in sorted(songs_by_year.items()):
        for s in songs:
            if not s["yt"]:
                issues.append(f"  ❌ {year} — '{s['title']}' by {s['artist']} — MISSING youtube_id")
    if issues:
        print("\n⚠️  Missing YouTube IDs — fill these in songs_with_ids.csv first:\n")
        for i in issues:
            print(i)
        print()
        return False
    return True

def build_app(songs_by_year):
    # Build the SONGS_BY_YEAR dict literal
    dict_lines = ["SONGS_BY_YEAR = {\n"]
    for year in sorted(songs_by_year.keys()):
        dict_lines.append(f"    {year}: [\n")
        for s in songs_by_year[year]:
            title  = s["title"].replace('"', '\\"')
            artist = s["artist"].replace('"', '\\"')
            yt     = s["yt"]
            dict_lines.append(f'        {{"title": "{title}", "artist": "{artist}", "yt": "{yt}"}},\n')
        dict_lines.append("    ],\n")
    dict_lines.append("}\n")
    songs_block = "".join(dict_lines)

    # Build ERA_THEMES dict literal
    theme_lines = ["ERA_THEMES = {\n"]
    for year, t in sorted(ERA_THEMES.items()):
        theme_lines.append(
            f'    {year}: {{"bg": "{t["bg"]}", "accent": "{t["accent"]}", '
            f'"glow": "{t["glow"]}", "era": "{t["era"]}", "vibe": "{t["vibe"]}"}},\n'
        )
    theme_lines.append("}\n")
    themes_block = "".join(theme_lines)

    # Read the app template and replace the data blocks
    with open(APP_FILE, "r", encoding="utf-8") as f:
        src = f.read()

    # Replace SONGS_BY_YEAR block
    import re
    src = re.sub(
        r"SONGS_BY_YEAR = \{.*?\n\}\n",
        songs_block,
        src,
        flags=re.DOTALL,
    )
    # Replace ERA_THEMES block
    src = re.sub(
        r"ERA_THEMES = \{.*?\n\}\n",
        themes_block,
        src,
        flags=re.DOTALL,
    )

    with open(APP_FILE, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"✅  {APP_FILE} rebuilt with {sum(len(v) for v in songs_by_year.values())} songs across {len(songs_by_year)} years.")
    print(f"   Run:  streamlit run {APP_FILE}\n")


if __name__ == "__main__":
    songs = load_songs()
    if validate(songs):
        build_app(songs)
    else:
        print("Fix the missing IDs above, then re-run this script.")
