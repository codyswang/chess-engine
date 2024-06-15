
import chess


def search(board, eval_function, search_alg, is_white_player):
    return search_alg(board, eval_function, 3, is_white_player)


def get_moved_board(move, board):
    new_board = board.copy()
    new_board.push(move)
    return new_board


def alpha_beta_pruning_search_alg(board, eval_function, depth=3, is_maximizing=True, alpha=float('-inf'), beta=float('inf')):
    game_ended = board.is_checkmate() or board.is_stalemate(
    ) or board.is_insufficient_material()

    if depth == 0 or game_ended:
        return (None, eval_function(board))

    if is_maximizing:
        max_child_eval = float('-inf')
        for child_move in board.legal_moves:
            best_child_move, eval = alpha_beta_pruning_search_alg(
                get_moved_board(child_move, board), eval_function, depth-1, not is_maximizing)
            if eval > max_child_eval:
                max_child_eval = eval
                best_move = child_move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return (best_move, max_child_eval)
    else:
        min_child_eval = float('inf')
        for child_move in board.legal_moves:
            best_child_move, eval = alpha_beta_pruning_search_alg(get_moved_board(
                child_move, board), eval_function, depth-1, not is_maximizing)
            if eval < min_child_eval:
                min_child_eval = eval
                best_move = child_move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return (best_move, min_child_eval)


def naive_eval_function(board):
    chess_piece_values = {
        'P': 10,
        'N': 30,
        'B': 30,
        'R': 50,
        'Q': 90,
        'K': 900,
        'p': -10,
        'n': -30,
        'b': -30,
        'r': -50,
        'q': -90,
        'k': -900
    }
    eval_score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            eval_score += chess_piece_values[str(piece)]

    return eval_score


if __name__ == "__main__":
    board = chess.Board()
    move, _ = search(board, naive_eval_function,
                     alpha_beta_pruning_search_alg, True)
    print(move.uci())
