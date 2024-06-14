from collections import deque
import logging
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
        assert(len(args) == 0)
        print(f"id name {self.name}")
        print(f"id author {self.author}")

        # TODO: add proper engine option modifications
        print("option name Nullmove type check default true")

        # TODO: insert engine prep here, if necessary

        print("uciok")

    def debug(self, args):
        assert(len(args) == 1)
        raise NotImplementedError

    def isready(self, args):
        assert(len(args) == 0)
        
        # TODO: check to make sure engine is ok

        print("readyok")

    def setoption(self, args):
        pass

    def ucinewgame(self, args):
        assert(len(args) == 0)

    def position(self, args):
        assert(len(args) != 0)

        position_type = args.popleft()

        if position_type == "startpos":
            self.board = chess.Board()
        elif position_type == "fen":
            assert(len(args) >= 2)
            self.board = chess.Board(args.popleft())
        else:
            raise ValueError

        while args:
            uci_move = args.popleft()
            if uci_move != "moves":
                move = chess.Move.from_uci(uci_move)
                self.board.push(move)

    def go(self, args):
        with open("log.txt", mode="a+", encoding="utf-8") as f:
            f.write(f"{self.board.turn == chess.WHITE}\n")
        move, eval = search.search(self.board, search.naive_eval_function, search.alpha_beta_pruning_search_alg, self.board.turn == chess.WHITE)
        print(f"bestmove {move.uci()}")

    def stop(self, args):
        pass

    def ponderhit(self, args):
        pass

    def quit(self, args):
        pass
	
    def run(self):
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
