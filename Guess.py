class Guess(object):
	"""Represents a guess in the game of mastermind."""

	def __init__(self, sequence, num_blacks, num_whites):
		self.sequence = sequence
		self.num_whites = num_whites
		self.num_blacks = num_blacks