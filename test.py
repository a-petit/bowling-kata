from game import Game


def test_gutter_game():
    game = Game()
    _roll_many(game, 20, 0)
    assert game.score() == 0


def test_all_ones():
    game = Game()
    _roll_many(game, 20, 1)
    assert game.score() == 20


def test_game_with_a_spare():
    game = Game()
    game.roll(6)
    game.roll(4)
    game.roll(3)
    _roll_many(game, 17, 0)
    assert game.score() == 16


def test_game_with_a_strike():
    game = Game()
    game.roll(10)
    game.roll(7)
    game.roll(2)
    _roll_many(game, 17, 0)
    assert game.score() == 28


def test_perfect_game():
    game = Game()
    _roll_many(game, 12, 10)
    assert game.score() == 300


def _roll_many(game, n, pins):
    for i in range(n):
        game.roll(pins)
