import csv
import urllib.parse
import webbrowser
import time

INPUT_CSV = "songs.csv"
OUTPUT_CSV = "songs_with_ids.csv"

def make_search_url(query: str) -> str:
  return "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)

def main():
  rows = []
  with open(INPUT_CSV, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row.get("Song Title"):
        rows.append(row)

print(f"Found {len(rows)} songs in {INPUT_CSV\n")
print("=" * 80)
print(f"{'#':<4} {'YEAR':<6} {'TITLE':<35} {'ARTIST':<25} SEARCH URL")
print("=" * 80)

for i, row in enumerate(rows, 1):
  title = row["Song Title"].strip()
  artist = row["Artist"].strip()
  link = row["Link"].strip()   # This is already the YouTube video title!
  year = row["Year"].strip()
  
  # Use the Link field first (it's the video title), fall back to title+artist
  search_query = link if link and link != "#VALUE!" else f"{title} {artist} official video"
  url = make_search_url(search_query)
  
  print(f"{i:<4} {year:<6} {title:<35} {artist:<25}")
  print(f"     🔗 {url}\n")

# Write the template CSV
with open(OUPUT_CSV, "w", newline="", encoding="utf-8") as f:
  fieldnames = ["year", "title", "artist", "link_title", "youtube_id", "search_url"]
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  for row in rows:
    title = row["Song Title"].strip()
    artist = row["Artist"].strip()
    link   = row["Link"].strip()
    year   = row["Year"].strip()
    search_query = link if link and link != "#VALUE!" else f"{title} {artist} official video"
            writer.writerow({
                "year":       year,
                "title":      title,
                "artist":     artist,
                "link_title": link,
                "youtube_id": "",          # ← YOU FILL THIS IN
                "search_url": make_search_url(search_query),
            })

print(f"\n✅  Template saved to: {OUTPUT_CSV}")
print("   Open it in Excel / Google Sheets.")
print("   For each row: click the search_url, find your video, copy the ID")
print("   (the part after ?v= in the YouTube URL), paste into youtube_id column.")
print("\n   Then run:  python3 build_app.py  to regenerate the Streamlit app.\n")

# Optional: open all search URLs in your browser automatically 
def open_all_in_browser(delay=1.5):
  """
  Uncomment the call at the bottom if you want every video to auto-open
  in your browser so you just copy the ID from the address bar.
  Be careful — this will open 110 tabs!
  """
  rows = []
    with open(INPUT_CSV, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Song Title"):
                rows.append(row)
    for row in rows:
        link = row["Link"].strip()
        title  = row["Song Title"].strip()
        artist = row["Artist"].strip()
        q = link if link and link != "#VALUE!" else f"{title} {artist} official"
        url = make_search_url(q)
        print(f"Opening: {title} — {artist}")
        webbrowser.open(url)
        time.sleep(delay)


if __name__ == "__main__":
    main()
    # Uncomment the line below to auto-open ALL searches in your browser (110 tabs!):
    # open_all_in_browser(delay=1.5)
  
