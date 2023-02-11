from io import StringIO

import chess.engine
import chess.pgn

from chees.lost_pieces import lost_pieces
from chees.pivotal_moves import sort_by_score_diff

# Start the Stockfish engine
engine = chess.engine.SimpleEngine.popen_uci("stockfish")


# Load the PGN file

import chess
import chess.engine
import json
from io import StringIO

def game_analyse(pgn,id):
    pgn_string = StringIO(pgn)
    game = chess.pgn.read_game(pgn_string)
    board = game.board()
    analysis = []
    previous_score = 0
    for move in game.mainline_moves():
        if board.is_game_over():
            break
        score = engine.analyse(board, chess.engine.Limit(time=0.100))["score"]
        # make number positive
        capture = board.is_capture(move)
        if capture:
            captured_piece_type = chess.piece_name(board.piece_type_at(move.to_square))
        else:
            captured_piece_type = None
        if board.turn == True:
            player = "white"
            score_diff = score.relative.score(mate_score=10000) - previous_score
            previous_score = score.relative.score(mate_score=10000)
        else:
            player = "black"
            score_diff = (score.relative.score(mate_score=10000) * -1) - previous_score
            previous_score = score.relative.score(mate_score=10000) * -1
        analysis.append({
            "fullmove_number": board.fullmove_number,
            "color": player,
            "score": score.relative.score(mate_score=10000),
            "score_diff": score_diff,
            "mate": score.relative.mate(),
            "fen": board.fen(),
            "move": move.uci(),
            "check": board.is_check(),
            "checkmate": board.is_checkmate(),
            "capture": capture,
            "captured_piece_type": captured_piece_type,
            "castling": board.is_castling(move)
        })
        board.push(move)
    engine.quit()
    print(json.dumps(analysis, indent=2))
    score_sort = sort_by_score_diff(analysis)
    print(json.dumps(score_sort, indent=2))
    return analysis, score_sort





