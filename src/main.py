from time import sleep
from pathlib import Path
import chess
import chess.engine
from chessboard import display
import chess.svg
import engine

def main():
	engine_path = str(Path.cwd() / "engine.sh")
	engine = chess.engine.SimpleEngine.popen_uci(engine_path)

	board = chess.Board()
	while not board.is_game_over():
		result = engine.play(board, chess.engine.Limit(time=30))
		board.push(result.move)
	engine.quit()

if __name__ == "__main__":
	main()
