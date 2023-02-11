import chess


def lost_pieces(fen1, fen2):
    board1 = chess.Board(fen1)
    board2 = chess.Board(fen2)

    lost_pieces = {"white": [], "black": []}
    for piece_type in range(1, 7):
        for square in board1.pieces(piece_type, chess.WHITE):
            if not board2.piece_at(square):
                lost_pieces["white"].append(chess.piece_symbol(piece_type).upper())
        for square in board1.pieces(piece_type, chess.BLACK):
            if not board2.piece_at(square):
                lost_pieces["black"].append(chess.piece_symbol(piece_type).upper())
    return lost_pieces