import json

import requests
import chessdotcom

def _get_pgn_headers_by_match_id(id):
    response = requests.get(f"https://www.chess.com/callback/live/game/{id}")
    if response.status_code == 200:
        data = json.loads(response.text)
        pgn_headers = data["game"]["pgnHeaders"]
        return pgn_headers
    else:
        return None

def _get_players_matches(pgn_headers):
    white = pgn_headers["White"]
    black = pgn_headers["Black"]
    month = pgn_headers["Date"].split(".")[1]
    year = pgn_headers["Date"].split(".")[0]
    matches = chessdotcom.get_player_games_by_month(white, year, month)
    return matches

def get_pgn_by_match_id(id):
    pgn_headers = _get_pgn_headers_by_match_id(id)
    matches = _get_players_matches(pgn_headers)
    matches = json.loads(matches.text)
    for match in matches["games"]:
        if match["url"] == f"https://www.chess.com/game/live/{id}":
            return match["pgn"]
    return None