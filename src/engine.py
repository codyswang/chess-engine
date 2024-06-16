"""Chess engine module using UCI to interface."""
from datetime import datetime
from collections import deque
import logging
import time
import chess
import search
logger = logging.getLogger(__name__)


class Engine:

    def __init__(self) -> None:
        self.commands = set([
            "uci", "debug", "isready", "setoption", "register", "ucinewgame",
            "position", "go", "stop", "ponderhit", "quit"
        ])
        self.options = set([

        ])
        self.name = "Anti-Benny Bot"
        self.author = "Cody Wang et al."
        self.board = None

    def uci(self, args):
        assert len(args) == 0
        print(f"id name {self.name}")
        print(f"id author {self.author}")

        # TODO: insert engine prep here, if necessary

        print("uciok")

    def debug(self, args):
        assert len(args) == 1
        raise NotImplementedError

    def isready(self, args):
        assert len(args) == 0

        # TODO: check to make sure engine is ok

        print("readyok")

    def setoption(self, args):
        pass

    def ucinewgame(self, args):
        assert len(args) == 0

    def position(self, args):
        assert len(args) != 0

        position_type = args.popleft()

        if position_type == "startpos":
            self.board = chess.Board()
        elif position_type == "fen":
            assert len(args) >= 2
            self.board = chess.Board(args.popleft())
        else:
            raise ValueError

        while args:
            uci_move = args.popleft()
            if uci_move != "moves":
                move = chess.Move.from_uci(uci_move)
                self.board.push(move)

    def go(self, args):
        turn = "white" if self.board.turn else "black"
        time_start = time.time()
        logger.info("Searching for %s's best move...", turn)
        move, score = search.search(self.board, search.naive_eval_function,
                                    search.alpha_beta_pruning_search_alg,
                                    self.board.turn)
        time_end = time.time()
        logger.info(
            """Best move found in %.2f seconds: %s with an evaluation score of %s.""",
            time_end - time_start, move, score
        )
        print(f"bestmove {move.uci()}")

    def stop(self, args):
        pass

    def ponderhit(self, args):
        pass

    def quit(self, args):
        pass

    def run(self):
        log_name = datetime.now().strftime("chess-engine-%y-%m-%d-%H:%M:%S.log")
        logging.basicConfig(filename=log_name, level=logging.INFO)
        logging.info("Engine start.")
        while True:
            command = input()
            args = deque(command.split())
            while args:
                arg = args.popleft()
                if arg in self.commands:
                    getattr(self, arg)(args)
                    break


if __name__ == "__main__":
    engine = Engine()
    engine.run()
