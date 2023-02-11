def match_result_def(result_code):
    result_dict = {
        'win': 'Win',
        'checkmated': 'Checkmated',
        'agreed': 'Draw agreed',
        'repetition': 'Draw by repetition',
        'timeout': 'Timeout',
        'resigned': 'Resigned',
        'stalemate': 'Stalemate',
        'lose': 'Lose',
        'insufficient': 'Insufficient material',
        '50move': 'Draw by 50-move rule',
        'abandoned': 'Abandoned',
        'kingofthehill': 'Opponent king reached the hill',
        'threecheck': 'Checked for the 3rd time',
        'timevsinsufficient': 'Draw by timeout vs insufficient material',
        'bughousepartnerlose': 'Bughouse partner lost',
    }
    return result_dict.get(result_code, "Invalid result code")

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
