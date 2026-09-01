import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sound of the Years",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SONGS_BY_YEAR = {
    2004: [
        {"title": "If I ain't got you", "artist": "Alicia Keys", "yt": "Ju8Hr50Ckwk"},
        {"title": "My Boo", "artist": "Usher", "yt": "fPgf2meEX1w"},
        {"title": "Yeah", "artist": "Usher", "yt": "GxBSyx85Kp8"},
        {"title": "Numb", "artist": "Linkin Park", "yt": "kXYiU_JCYtU"},
        {"title": "Milkshake", "artist": "Kelis", "yt": "6AwXKJoKJz4"},
    ],
    2005: [
        {"title": "Sun Rising Up", "artist": "Deux", "yt": "IqJ5Y-3qymY"},
        {"title": "We Belong Together", "artist": "Mariah Carey", "yt": "0habxsuXW4g"},
        {"title": "Let Me Love You", "artist": "Mario", "yt": "H64QG4UsrGI"},
        {"title": "Fix You", "artist": "Coldplay", "yt": "k4V3Mo61fJM"},
        {"title": "Lose Control", "artist": "Missy Elliot", "yt": "na7lIb09898"},
    ],
    2006: [
        {"title": "The Cure and The Cause", "artist": "Fish Go Deep", "yt": "ikJCO_FrQQ8"},
        {"title": "Stupid Girls", "artist": "Pink", "yt": "BR4yQFZK9YM"},
        {"title": "My Love", "artist": "Justin Timberlake", "yt": "FqP3-_F0YTs"},
        {"title": "Crazy", "artist": "Gnarls Barkley", "yt": "-N4jf6rtyuw"},
        {"title": "Buttons", "artist": "The Pussycat Dolls", "yt": "VCLxJd1d84s"},
    ],
    2007: [
        {"title": "Deja Vu", "artist": "Beyonce", "yt": "RQ9BWndKEgs"},
        {"title": "Irreplaceable", "artist": "Beyonce", "yt": "2EwViQxSJJQ"},
        {"title": "Big Girls don't cry", "artist": "Fergie", "yt": "agrXgrAgQ0U"},
        {"title": "What goes around comes around", "artist": "Justin Timberlake", "yt": "TOrnUquxtwA"},
        {"title": "U + Ur Hand", "artist": "Pink", "yt": "YUtHjOvPKT0"},
    ],
    2008: [
        {"title": "Bleeding Love", "artist": "Leona Lewis", "yt": "Vzo-EL_62fQ"},
        {"title": "Don’t Stop the Music", "artist": "Rihanna", "yt": "yd8jh9QYfEs"},
        {"title": "Closer", "artist": "Ne-Yo", "yt": "z_aC5xPQ2f4"},
        {"title": "So What", "artist": "Pink", "yt": "FJfFZqTlWrQ"},
        {"title": "No One", "artist": "Alicia Keys", "yt": "rywUS-ohqeE"},
    ],
    2009: [
        {"title": "Sky and Sand", "artist": "Paul Kalkbrenner", "yt": "8ybFb_wKlvQ"},
        {"title": "Deep Fear", "artist": "Sideckick", "yt": "6cch3DYMUmI"},
        {"title": "Empire State of Mind", "artist": "Jay-Z", "yt": "vk6014HuxcE"},
        {"title": "Hey Hey", "artist": "Dennis Ferrer", "yt": "ZqXTtRXDPrw"},
        {"title": "Day n Nite", "artist": "Kid Cudi", "yt": "WSWrepLjTKc"},
    ],
    2010: [
        {"title": "Superman", "artist": "Black Coffee", "yt": "w6-tR3PKCHA"},
        {"title": "Just the way you are", "artist": "Bruno Mars", "yt": "LjhCEhWiKXk"},
        {"title": "Canoa", "artist": "Gregor Salto", "yt": "xC5ECftsajo"},
        {"title": "Love the way you lie", "artist": "Eminem", "yt": "uelHwf8o7_U"},
        {"title": "What’s my name", "artist": "Rihanna", "yt": "3RYhAN8kQoM"},
    ],
    2011: [
        {"title": "Grenade", "artist": "Bruno Mars", "yt": "SR6iYWJxHqs"},
        {"title": "We Found Love", "artist": "Rihanna", "yt": "tg00YEETFzg"},
        {"title": "Rolling in the deep", "artist": "Adele", "yt": "rYEDA3JcQqw"},
        {"title": "Born this way", "artist": "Lady Gaga", "yt": "wV1FrqwZyKw"},
        {"title": "Someone like you", "artist": "Adele", "yt": "hLQl3WQQoQ0"},
    ],
    2012: [
        {"title": "Something Special", "artist": "Miguel Campbell", "yt": "nEJHueJiBvc"},
        {"title": "Diamonds", "artist": "Rihanna", "yt": "lWA2pjMjpBs"},
        {"title": "Set fire to the rain", "artist": "Adele", "yt": "a2giXO6eyuI"},
        {"title": "Locked out of heaven", "artist": "Bruno Mars", "yt": "e-fA-gBCkj0"},
        {"title": "Titanium", "artist": "Sia", "yt": "JRfuAukYTKg"},
    ],
    2013: [
        {"title": "When I was your man", "artist": "Bruno Mars", "yt": "ekzHIouo8Q4"},
        {"title": "Pour It Up", "artist": "Rihanna", "yt": "ehcVomMexkY"},
        {"title": "Get Lucky", "artist": "Daft Punk", "yt": "5NV6Rdv1a3I"},
        {"title": "Your Friend - Original", "artist": "Gregor Salto", "yt": "BzHmGQZFCN0"},
        {"title": "Just give me a reason", "artist": "Pink", "yt": "OpQFFLBMEPI"},
    ],
    2014: [
        {"title": "Happy", "artist": "Pharrel Williams", "yt": "ZbZSe6N_BXs"},
        {"title": "All of Me", "artist": "John Legend", "yt": "450p7goxZqg"},
        {"title": "Latch", "artist": "Disclosure", "yt": "93ASUImTedo"},
        {"title": "Rather Be", "artist": "Clean Bandit", "yt": "m-M1AtrxztU"},
        {"title": "La La La", "artist": "Naughty Boy", "yt": "3O1_3zBUKM8"},
    ],
    2015: [
        {"title": "Earned It", "artist": "The Weekend", "yt": "xe_iCkFsQKE"},
        {"title": "The Hills", "artist": "The Weekend", "yt": "yzTuBuRdAyA"},
        {"title": "How deep is your love", "artist": "Calvin Harris", "yt": "EgqUJOudrcM"},
        {"title": "Thinking out loud", "artist": "Ed Sheeran", "yt": "lp-EO5I60KA"},
        {"title": "Can’t feel my face", "artist": "The Weekend", "yt": "KEI4qSrkPAs"},
    ],
    2016: [
        {"title": "I’m Yours", "artist": "Alessia Cara", "yt": "A3tgV5Uoduo"},
        {"title": "Work", "artist": "Rihanna", "yt": "HL1UzIK-flA"},
        {"title": "Can’t stop the feeling", "artist": "Justin Timberlake", "yt": "ru0K8uYEZWw"},
        {"title": "Pillowtalk", "artist": "ZAYN", "yt": "C_3d6GntKbk"},
        {"title": "Too Good", "artist": "Drake", "yt": "1lbKUiZv1fI"},
    ],
    2017: [
        {"title": "Love on the brain", "artist": "Rihanna", "yt": "QMP-o8WXSPM"},
        {"title": "King of my castle", "artist": "Wamdue Project", "yt": "DXSyQjppqG0"},
        {"title": "There’s nothing holding me back", "artist": "Shawn Mendes", "yt": "dT2owtxkU8k"},
        {"title": "Me rehuso", "artist": "Danny Ocean", "yt": "aDCcLQto5BM"},
        {"title": "Despacito", "artist": "Luis Fonsi", "yt": "kJQP7kiw5Fk"},
    ],
    2018: [
        {"title": "Wish I didn’t miss you", "artist": "Angie Stone", "yt": "9PWz-NubVpM"},
        {"title": "Cola", "artist": "Camelphat", "yt": "LcNXG-6SqWA"},
        {"title": "So hooked on your lovin’", "artist": "Selace", "yt": "9NphyiMh36o"},
        {"title": "Gypsy Woman", "artist": "Crystal Waters", "yt": "_KztNIg4cvE"},
        {"title": "Lola’s Theme", "artist": "The Shapeshifters", "yt": "kIC0aQ56ASE"},
    ],
    2019: [
        {"title": "Pa mi, Cuaderno, Que mas pues", "artist": "Dalex", "yt": "cK8DYOZIsMc"},
        {"title": "Antes de Morirme (feat. Rosalía)", "artist": "C. Tangana", "yt": "RxKVWs_qYBk"},
        {"title": "No voy  a llorar", "artist": "Natti Natasha", "yt": "Y3KiFoZHjFs"},
        {"title": "Callaita", "artist": "Bad Bunny", "yt": "acEOASYioGY"},
        {"title": "Fingias", "artist": "Paloma Mami", "yt": "ltYUH6fEYdE"},
    ],
    2020: [
        {"title": "Rise Up", "artist": "Andra Day", "yt": "lwgr_IMeEgA"},
        {"title": "Ride It", "artist": "Regard", "yt": "ucVUEmjKsko"},
        {"title": "Drive", "artist": "Black Coffee", "yt": "32HANv-bdJs"},
        {"title": "Promises", "artist": "Calvin Harris", "yt": "kkLk2XWMBf8"},
        {"title": "El mismo Aire", "artist": "Camilo", "yt": "ZYDj7bys8jo"},
    ],
    2021: [
        {"title": "Needed Me", "artist": "Rihanna", "yt": "aaOjJWOJPRg"},
        {"title": "Pretty Please", "artist": "Dua Lipa", "yt": "ylzhMn6MlVc"},
        {"title": "La Fama", "artist": "Rosalia", "yt": "e-CEd6xrRQc"},
        {"title": "Demasiadas Mujeres", "artist": "C. Tangana", "yt": "ZlFri4ez_lE"},
        {"title": "No se perdona", "artist": "Rels B", "yt": "ulhF2ARDchU"},
    ],
    2022: [
        {"title": "Buenos Aires", "artist": "Nathy Peluso", "yt": "O8BLUzAxNmQ"},
        {"title": "Todo Contigo", "artist": "Yoli Saa", "yt": "PAwqjTmWnl0"},
        {"title": "Slomo", "artist": "Channel", "yt": "Dwyefl6itpI"},
        {"title": "Linda", "artist": "Rosalia", "yt": "CmmTz3W-JO0"},
        {"title": "Los Tontos", "artist": "C. Tangana", "yt": "vjWyRfnR5CQ"},
    ],
    2023: [
        {"title": "Flowers", "artist": "Miley Cyrus", "yt": "G7KNmW9a75Y"},
        {"title": "The Rapture pt. III", "artist": "Keinemusik", "yt": "MOenJHdj8ro"},
        {"title": "Innerbloom", "artist": "Rufus du Sol", "yt": "Tx9zMFodNtA"},
        {"title": "Prisioner", "artist": "Miley Cyrus", "yt": "0ir1qkPXPVM"},
        {"title": "Watermelon Sugar", "artist": "Shoby", "yt": "yg9omUdKyF0"},
    ],
    2024: [
        {"title": "Move", "artist": "Keinemusik", "yt": "95dB-ObZ7Ho"},
        {"title": "Oh my God", "artist": "Adele", "yt": "niG3YMU6jFk"},
        {"title": "Jump", "artist": "Levi", "yt": "ZkIzfBwxMQo"},
        {"title": "Darling", "artist": "Shimza", "yt": "7EXcGG2krFQ"},
        {"title": "Don’t be so shy", "artist": "Imany", "yt": "b1_B-IKEufg"},
    ],
    2025: [
        {"title": "Crazy for it", "artist": "Keinemusik", "yt": "7q8mnv5uZpQ"},
        {"title": "Una noche", "artist": "HUGEL", "yt": "IJwLS3uBMEk"},
        {"title": "Places", "artist": "Shimza", "yt": "lsQ6JgJfOTM"},
        {"title": "Overthink", "artist": "Naarly", "yt": "o3B3dWYJgJQ"},
        {"title": "I Adore You", "artist": "HUGEL", "yt": "KiIc54yyktw"},
    ],
    2026: [
        {"title": "", "artist": "", "yt": ""},
        {"title": "", "artist": "", "yt": ""},
        {"title": "", "artist": "", "yt": ""},
        {"title": "", "artist": "", "yt": ""},
        {"title": "", "artist": "", "yt": ""},
    ],
}

ERA_THEMES = {
    2004: {"bg": "#0a0a1a", "accent": "#ff6b35", "glow": "#ff4500", "era": "Early 2000s", "vibe": "Ringtone anthems, smooth velvet, and pure radio dominance"},
    2005: {"bg": "#0d0a1a", "accent": "#ff6b35", "glow": "#ff4500", "era": "Early 2000s", "vibe": "Melodrama meets the dancefloor"},
    2006: {"bg": "#0a1a0a", "accent": "#39ff14", "glow": "#00ff41", "era": "Mid-2000s", "vibe": "Peak bloghouse, Timbaland beats, and lipgloss pop"},
    2007: {"bg": "#0a1a10", "accent": "#39ff14", "glow": "#00ff41", "era": "Mid-2000s", "vibe": "Revenge pop, swagger, and the golden era of the breakup track"},
    2008: {"bg": "#1a0a0a", "accent": "#ff073a", "glow": "#ff1744", "era": "Late 2000s", "vibe": "Big heartbreaks, bigger hooks, and maximalist radio"},
    2009: {"bg": "#1a0a10", "accent": "#ff073a", "glow": "#ff1744", "era": "Late 2000s", "vibe": "Rooftop melancholia and sunrise synthlines"},
    2010: {"bg": "#0a0a1a", "accent": "#00cfff", "glow": "#00bfff", "era": "New Decade", "vibe": "Four-on-the-floor euphoria with a side of angst"},
    2011: {"bg": "#0a1020", "accent": "#00cfff", "glow": "#00bfff", "era": "New Decade", "vibe": "Stadium teardrops and peak-era strobe lights"},
    2012: {"bg": "#10080a", "accent": "#e040fb", "glow": "#ce93d8", "era": "Early 2010s", "vibe": "Festival drops, heavy vocal runs, and radio gloss"},
    2013: {"bg": "#080a10", "accent": "#e040fb", "glow": "#ce93d8", "era": "Early 2010s", "vibe": "Nu-disco funk, club swagger, and arena belts"},
    2014: {"bg": "#0a1008", "accent": "#ffeb3b", "glow": "#ffd600", "era": "Mid-2010s", "vibe": "Garage swing goes prime-time pop"},
    2015: {"bg": "#100a08", "accent": "#ffeb3b", "glow": "#ffd600", "era": "Mid-2010s", "vibe": "Dark pop royalty and sleek synth-funk"},
    2016: {"bg": "#08100a", "accent": "#ff4081", "glow": "#f50057", "era": "Mid-2010s", "vibe": "Tropical rhythms, smooth falsettos, and summer haze"},
    2017: {"bg": "#100808", "accent": "#ff4081", "glow": "#f50057", "era": "Late 2010s", "vibe": "Global rhythm shakeup and sultry earworms"},
    2018: {"bg": "#080810", "accent": "#64ffda", "glow": "#1de9b6", "era": "Late 2010s", "vibe": "Vocal-heavy cuts, warehouse basslines, and classic groove revivals"},
    2019: {"bg": "#100810", "accent": "#64ffda", "glow": "#1de9b6", "era": "Late 2010s", "vibe": "Neo-perreo, Madrid cool, and effortless swagger"},
    2020: {"bg": "#0a0a0a", "accent": "#bb86fc", "glow": "#7c4dff", "era": "2020s", "vibe": "Late-night escapism and four-to-the-floor healing"},
    2021: {"bg": "#080010", "accent": "#bb86fc", "glow": "#7c4dff", "era": "2020s", "vibe": "Spanish avant-garde, bass-heavy pop, and sleek melancholy"},
    2022: {"bg": "#0a0508", "accent": "#ff80ab", "glow": "#ff4081", "era": "2020s", "vibe": "Club-kid flair, neo-folklore, and runway energy"},
    2023: {"bg": "#050a08", "accent": "#69ff47", "glow": "#00e676", "era": "2020s", "vibe": "Deep desert melodies, sunset grooves, and stadium liberation"},
    2024: {"bg": "#080a05", "accent": "#ffd740", "glow": "#ffab00", "era": "2020s", "vibe": "High-roller afro house and 4 AM sunrise tension"},
    2025: {"bg": "#050808", "accent": "#40c4ff", "glow": "#0091ea", "era": "2020s",   "vibe": "Tulum-to-Ibiza swing, sultry drops, and afro-latin heat"},
    2026: {"bg": "#050808", "accent": "#40c4ff", "glow": "#0091ea", "era": "Now", "vibe": ""},
}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Mono:wght@400;700&family=Rajdhani:wght@300;400;600;700&display=swap');
*{box-sizing:border-box}
html,body,[data-testid="stAppViewContainer"]{background:#080808!important;color:#e0e0e0;font-family:'Rajdhani',sans-serif}
[data-testid="stAppViewContainer"]>.main{background:transparent!important}
[data-testid="stHeader"],[data-testid="stToolbar"],.stDeployButton,footer,#MainMenu,section[data-testid="stSidebar"]{display:none!important}
[data-testid="block-container"],.main .block-container{padding:0!important;max-width:100%!important}
.hero{text-align:center;padding:60px 20px 20px;background:linear-gradient(180deg,#000 0%,transparent 100%)}
.hero h1{font-family:'Bebas Neue',sans-serif;font-size:clamp(3rem,8vw,7rem);letter-spacing:.12em;margin:0;background:linear-gradient(135deg,#fff,#aaa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{font-family:'Space Mono',monospace;font-size:.75rem;color:#666;letter-spacing:.3em;text-transform:uppercase;margin-top:8px}
.ysec{width:100%;padding:12px 5vw}
.ycap{border:1px solid rgba(255,255,255,.08);border-radius:20px;overflow:hidden;background:rgba(255,255,255,.02);transition:all .4s}
.ycap:hover{border-color:rgba(255,255,255,.2);background:rgba(255,255,255,.04)}
.yhdr{display:flex;align-items:center;justify-content:space-between;padding:20px 32px;gap:16px}
.ynum{font-family:'Bebas Neue',sans-serif;font-size:clamp(2.5rem,5vw,4.5rem);line-height:1;letter-spacing:.05em;min-width:120px}
.ymeta{flex:1}
.yera{font-family:'Space Mono',monospace;font-size:.65rem;letter-spacing:.25em;text-transform:uppercase;opacity:.5;margin-bottom:4px}
.yvibe{font-size:1.1rem;font-weight:600;opacity:.8}
.ychev{font-size:1.5rem;opacity:.4}
.sgrid{padding:8px 32px 24px;display:flex;flex-direction:column;gap:10px}
.srow{display:flex;align-items:center;gap:16px;padding:14px 18px;border-radius:12px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);transition:all .3s}
.srow:hover{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.15);transform:translateX(4px)}
.snum{font-family:'Space Mono',monospace;font-size:.7rem;opacity:.3;min-width:20px}
.sinfo{flex:1}
.stit{font-size:1rem;font-weight:700;letter-spacing:.03em;transition:filter .5s}
.stit.blur{filter:blur(6px);user-select:none}
.sart{font-size:.8rem;opacity:.5;font-family:'Space Mono',monospace;transition:filter .5s}
.sart.blur{filter:blur(5px)}
.spbtn{font-size:1.2rem;opacity:.5}
.srow:hover .spbtn{opacity:1}
.player{margin:0 32px 24px;border-radius:16px;overflow:hidden;background:rgba(0,0,0,.6);border:1px solid rgba(255,255,255,.1)}
.tvframe{padding:20px;background:#0a0a0a}
.tvbody{background:#111;border-radius:12px;padding:14px;box-shadow:0 0 40px rgba(0,0,0,.9),0 0 0 2px #1a1a1a}
.tvscr{background:#000;border-radius:6px;overflow:hidden;aspect-ratio:16/9;box-shadow:inset 0 0 20px rgba(0,0,0,.8)}
.tvscr iframe{width:100%;height:100%;border:none;display:block}
.tvdots{display:flex;justify-content:center;gap:8px;padding-top:10px}
.tvdot{width:8px;height:8px;border-radius:50%;background:#222}
.tvlegs{display:flex;justify-content:center;gap:60px;padding-top:8px}
.tvleg{width:8px;height:20px;background:linear-gradient(to bottom,#1a1a1a,#111);border-radius:0 0 4px 4px}
.tline{width:2px;height:40px;background:linear-gradient(to bottom,transparent,rgba(255,255,255,.15),transparent);margin:0 auto}
.stButton>button{background:transparent!important;border:1px solid rgba(255,255,255,.15)!important;color:#fff!important;border-radius:8px!important;font-family:'Space Mono',monospace!important;font-size:.7rem!important;letter-spacing:.15em!important;padding:6px 16px!important;transition:all .2s!important}
.stButton>button:hover{background:rgba(255,255,255,.08)!important;border-color:rgba(255,255,255,.4)!important}
</style>
"""

if "open_year" not in st.session_state:
    st.session_state.open_year = None
if "revealed" not in st.session_state:
    st.session_state.revealed = {}
if "playing" not in st.session_state:
    st.session_state.playing = {}

st.markdown(CSS, unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>Sound of the Years</h1><p>scroll through time &mdash; click to unlock &mdash; play the anthem</p></div>',
           unsafe_allow_html=True)

years = sorted(SONGS_BY_YEAR.keys())

for i, year in enumerate(years):
    theme = ERA_THEMES[year]
    songs = SONGS_BY_YEAR[year]
    is_open = st.session_state.open_year == year
    revealed = st.session_state.revealed.get(year, set())
    playing_idx = st.session_state.playing.get(year, None)
    accent, glow = theme['accent'], theme['glow']

    if i > 0:
        st.markdown('<div class="tline"></div>', unsafe_allow_html=True)

    bg = theme["bg"]
    html = f'''<div class="ysec" style="background:linear-gradient(135deg, {bg}cc,rgba(0,0,0,0.95))">
    <div class="ycap"><div class="yhdr">
    <div class="ynum" style="color:{accent};text-shadow:0 0 30px {glow}88">{year}</div>
    <div class="ymeta"><div class="yera" style="color:{accent}99">{theme["era"]}</div><div class="yvibe">{theme["vibe"]}</div></div>
    <div class="ychev">{"▲" if is_open else "▼"}</div>
    </div>'''

    if is_open:
        html += '<div class="sgrid">'
        for j, s in enumerate(songs):
            pl = playing_idx == j
            glow_s = f"box-shadow:0 0 20px {glow}44;border-color:{accent}55" if pl else ""
            # Only show title/artist if currently playing, otherwise show "???"
            if pl:
                title_html  = f'<div class="stit" style="color:{accent}">{s["title"]}</div>'
                artist_html = f'<div class="sart">{s["artist"]}</div>'
                icon = "⏸"
            else:
                title_html  = '<div class="stit" style="filter:blur(7px);user-select:none;pointer-events:none">????????????</div>'
                artist_html = '<div class="sart" style="filter:blur(5px);user-select:none;pointer-events:none">??????????</div>'
                icon = "▶"
            html += f'''<div class="srow" style="{glow_s}">
<div class="snum">0{j+1}</div>
<div class="sinfo">{title_html}{artist_html}</div>
<div class="spbtn">{icon}</div></div>'''
        html += '</div>'

    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)

    if not is_open:
        c1, _ = st.columns([1, 6])
        with c1:
            if st.button(f"▼  {year}", key=f"o_{year}"):
                st.session_state.open_year = year
                st.rerun()
    else:
        c1, _ = st.columns([1, 6])
        with c1:
            if st.button("▲  Close", key=f"c_{year}"):
                st.session_state.open_year = None
                st.session_state.playing.pop(year, None)
                st.rerun()

        # One play button per song — clicking reveals AND plays it
        for j, s in enumerate(songs):
            pl = playing_idx == j
            _, c1, _r = st.columns([0.2, 1.2, 4])
            with c1:
                if st.button("⏸ Stop" if pl else f"▶ Play #{j+1}", key=f"pl_{year}_{j}"):
                    if pl:
                        st.session_state.playing.pop(year, None)
                    else:
                        st.session_state.playing[year] = j
                    st.rerun()

        if playing_idx is not None:
            s = songs[playing_idx]
            embed = f"https://www.youtube-nocookie.com/embed/{s['yt']}?autoplay=1&rel=0&modestbranding=1"
            watch = f"https://www.youtube.com/watch?v={s['yt']}"
            components.html(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:100%;background:#0a0a0a}}
.wrap{{width:100%;background:#0a0a0a;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.1)}}
.screen{{width:100%;aspect-ratio:16/9;background:#000;display:block}}
.screen iframe{{width:100%;height:100%;border:none;display:block}}
.meta{{padding:10px 20px;display:flex;align-items:center;justify-content:space-between}}
.left .mtit{{font-family:'Bebas Neue',cursive;font-size:1.2rem;color:{accent};letter-spacing:.06em}}
.left .mart{{font-size:.6rem;color:rgba(255,255,255,.4);letter-spacing:.1em;margin-top:2px}}
.mlink{{font-size:.6rem;color:{accent}88;text-decoration:none;letter-spacing:.12em;border-bottom:1px solid {accent}44;white-space:nowrap}}
</style>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Mono:wght@400&display=swap" rel="stylesheet">
</head><body>
<div class="wrap">
  <div class="screen">
    <iframe src="{embed}"
      allow="autoplay; encrypted-media; fullscreen; picture-in-picture"
      allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
  </div>
  <div class="meta">
    <div class="left">
      <div class="mtit">{s["title"]}</div>
      <div class="mart">{s["artist"]}</div>
    </div>
    <a class="mlink" href="{watch}" target="_blank">↗ OPEN IN YOUTUBE</a>
  </div>
</div>
</body></html>""", height=600, scrolling=False)

st.markdown('<div style="text-align:center;padding:60px 20px;opacity:.2"><div style="font-family:\'Space Mono\',monospace;font-size:.65rem;letter-spacing:.3em">2004 — 2026 · ALL YEARS LOADED</div></div>', unsafe_allow_html=True)
