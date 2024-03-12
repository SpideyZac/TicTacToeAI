from game import Game

def get_best_move(game: Game) -> list[int]:
    best_move = None
    best_score = float("-inf")
    for move in game.get_possible_moves():
        new_game = game.clone()
        new_game.make_move(move[0], move[1])
        score = minimax(new_game, 8, False, game.current_player == 1)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move # type: ignore

def minimax(game: Game, depth: int, maximizing: bool, started_player_1: bool) -> int:
    if game.is_winner(1):
        if started_player_1:
            return 1
        else:
            return -1
    if game.is_winner(-1):
        if started_player_1:
            return -1
        else:
            return 1
    if game.is_full():
        return 0
    
    if depth == 0:
        if started_player_1:
            return game.getReward()
        else:
            return -game.getReward()
        
    if maximizing:
        best_score = float("-inf")
        for move in game.get_possible_moves():
            new_game = game.clone()
            new_game.make_move(move[0], move[1])
            score = minimax(new_game, depth - 1, False, started_player_1)
            best_score = max(score, best_score)
        return best_score # type: ignore
    else:
        best_score = float("inf")
        for move in game.get_possible_moves():
            new_game = game.clone()
            new_game.make_move(move[0], move[1])
            score = minimax(new_game, depth - 1, True, started_player_1)
            best_score = min(score, best_score)
        return best_score # type: ignore
    
g = Game()
player_turn = 1

print(g)

while True:
    if g.current_player == player_turn:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        g.make_move(x - 1, y - 1)
    else:
        move = get_best_move(g)
        g.make_move(move[0], move[1])

    print(g)

    if g.is_winner(1):
        print("Player 1 wins!")
        break
    if g.is_winner(-1):
        print("Player -1 wins!")
        break
    if g.is_full():
        print("Draw!")
        break