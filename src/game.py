class Game:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def make_move(self, x: int, y: int):
        raise NotImplementedError
    
    def is_winner(self, player: int) -> bool:
        raise NotImplementedError
    
    def is_full(self) -> bool:
        # Check if draw
        raise NotImplementedError