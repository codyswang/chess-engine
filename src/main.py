from pathlib import Path
import chess
import chess.engine
import engine

def main():
	engine_path = str(Path.cwd() / "engine.sh")
	engine = chess.engine.SimpleEngine.popen_uci(engine_path)

	board = chess.Board()
	while not board.is_game_over():
		result = engine.play(board, chess.engine.Limit(time=0.1))
		board.push(result.move)
	
	engine.quit()

if __name__ == "__main__":
	main()
