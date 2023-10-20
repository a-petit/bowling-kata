class Game:
    TOTAL_FRAMES = 10
    PINS_PER_FRAME = 10

    def __init__(self):
        self._rolls = [0] * 21
        self._currentRoll = 0

    def roll(self, pins):
        self._rolls[self._currentRoll] = pins
        self._currentRoll += 1

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(self.TOTAL_FRAMES):
            if self._is_strike(frame_index):
                score += self.PINS_PER_FRAME + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += self.PINS_PER_FRAME + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == self.PINS_PER_FRAME

    def _spare_bonus(self, frame_index):
        return self._rolls[frame_index + 2]

    def _is_strike(self, frame_index):
        return self._rolls[frame_index] == self.PINS_PER_FRAME

    def _strike_bonus(self, frame_index):
        return self._rolls[frame_index + 1] + self._rolls[frame_index + 2]
