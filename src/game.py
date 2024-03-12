class MoveError(Exception):
    def __init__(self, message="Invalid move; space is occupied"):
        self.message = message
        super().__init__(self.message)

class Game:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def make_move(self, x: int, y: int):
        if self.board[y][x] == 0:
            self.board[y][x] = self.current_player
            self.current_player *= -1
        else:
            raise MoveError()
    
    def is_winner(self, player: int) -> bool:
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
            
        for _ in range(2):
            if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
                return True
            if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
                return True
        
        return False
    
    def is_full(self) -> bool:
        for row in self.board:
            if 0 in row:
                return False
        return True
    
    def getReward(self) -> int:
        if self.is_winner(1):
            return 1
        if self.is_winner(-1):
            return -1
        return 0
    
    def get_possible_moves(self) -> list[list[int]]:
        out = []
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 0:
                    out.append([x, y])

        # go through each cell in the board, if 0 append [x, y] to out
        # range of y range x check if == 0 add xy to the list

        return out
    
    def clone(self):
        new_game = Game()
        new_game.board = [row.copy() for row in self.board]
        new_game.current_player = self.current_player
        return new_game

    def __str__(self):
        out = ""
        for row in self.board:
            out += " ".join(["x" if cell == 1 else "o" if cell == -1 else "-" for cell in row]) + "\n"

        return out