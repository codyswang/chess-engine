"""Driver module for testing engine functionality."""
from pathlib import Path
import logging
import platform
import chess
import chess.engine
import chess.svg
logger = logging.getLogger(__name__)


def main():
    """
    Driver function.

    Loads the specified engine and runs self-play.
    """
    cwd = Path.cwd()
    if platform.system() == "Windows":
        engine_path = cwd / r"src/engine/engine.exe"
    else:
        engine_path = cwd / "engine.sh"
    engine = chess.engine.SimpleEngine.popen_uci(str(engine_path))

    board = chess.Board()
    while not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=30))
        board.push(result.move)
        chess.svg.board(board, size=350)
    engine.quit()


if __name__ == "__main__":
    main()
