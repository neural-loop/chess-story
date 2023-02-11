{
  "avatar": "https://images.chesscomfiles.com/uploads/v1/user/11177810.9dfc8d31.200x200o.9a9eccebc07c.png",
  "player_id": 11177810,
  "@id": "https://api.chess.com/pub/player/fabianocaruana",
  "url": "https://www.chess.com/member/FabianoCaruana",
  "name": "Fabiano Caruana",
  "username": "fabianocaruana",
  "title": "GM",
  "followers": 13330,
  "country": "https://api.chess.com/pub/country/US",
  "last_online": 1675461007,
  "joined": 1363533272,
  "status": "premium",
  "is_streamer": false,
  "verified": false,
  "league": "Silver"
}

def title_def(title_code):
    title_dict = {
        'GM': 'Grandmaster',
        'WGM': 'Woman Grandmaster',
        'IM': 'International Master',
        'WIM': 'Woman International Master',
        'FM': 'FIDE Master',
        'WFM': 'Woman FIDE Master',
        'NM': 'National Master',
        'WNM': 'Woman National Master',
        'CM': 'Candidate Master',
        'WCM': 'Woman Candidate Master',
    }
    return title_dict.get(title_code, "Invalid title code")
