import chess.engine
import stockfish

# Start the Stockfish engine
# engine = chess.engine.SimpleEngine.popen_uci("stockfish")
# Load the PGN file
pgn = open("/path/to/game.pgn")
games = chess.pgn.read_game(pgn)

# Keep track of player strengths
player_strengths = {}

# Loop through each game in the PGN file
for game in games:
    board = game.board()

    # Keep track of the current player's strength
    player = None
    strength = 0

    # Loop through each move in the game
    for move in game.mainline_moves():
        # Update the board with the next move
        board.push(move)

        # If it's the first move of the game, start tracking the player's strength
        if player is None:
            player = board.turn
            info = engine.analyse(board, chess.engine.Limit(time=0.100))
            strength = info["score"].relative.cp

        # If it's the other player's turn, update their strength
        elif board.turn != player:
            info = engine.analyse(board, chess.engine.Limit(time=0.100))
            player_strengths[player] = player_strengths.get(player, 0) + info["score"].relative.cp
            player = board.turn
            strength = info["score"].relative.cp
        else:
            strength = info["score"].relative.cp + strength

    # Add the final player's strength to the total
    player_strengths[player] = player_strengths.get(player, 0) + strength

# Average the player strengths
for player, strength in player_strengths.items():
    player_strengths[player] = strength / len(games)

# Print the results
print(player_strengths)

# Close the Stockfish engine
engine.quit()