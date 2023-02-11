# This is a sample Python script.
import sys

import chessdotcom
from rich import print_json
from chessdotcom import get_player_profile, ChessDotComError

from chees import pgn_lookup
from chees.analyse import game_analyse


def main():
    try:
        # out = get_player_profile("fabianocaruana")
        # player_name = response.json['player']
        #out = get_player_game_archives("fabianocaruana")
        #stats = get_player_stats("fabianocaruana")
        #out = get_player_clubs("fabianocaruana")
        id = 16100246
        pgn = pgn_lookup.get_pgn_by_match_id(id)
        game_analyse(pgn,id)

    except ChessDotComError as e:
        # get the status code
        status_code = e.status_code
        print_json('Error: {}'.format(status_code)+' '+e.text)
        sys.exit()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

#id = "15360860817"
