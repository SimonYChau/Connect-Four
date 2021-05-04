import pygame
import sys

# DISPLAY_SIZE = 800
DISPLAY_SIZE = 700
BOARD_DIMENSION = 7
display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
pygame.display.set_caption("Connect Four")

BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
SLATEGRAY4 = (108,123,139)

class Checker:
	# checker constructor
	def __init__(self, row, col, blockSize):
		self.row = row
		self.col = col
		self.x = col * blockSize
		self.y = row * blockSize
		self.blockSize = blockSize
		self.circleColour = SLATEGRAY4
		if row == 0:
			self.boarderColour = SLATEGRAY4
		else:
			self.boarderColour = BLUE

	def isFilled(self):
		return self.circleColour != SLATEGRAY4

	def isNotFilled(self):
		return self.circleColour == SLATEGRAY4

	def setCircleColour(self, colour):
		self.circleColour = colour

	# we will only redraw what needs to be redrawn(not the whole display)
	def drawChecker(self, display):
		# fill the rectangle with the boarder colour
		rect = pygame.Rect(self.x, self.y, self.blockSize, self.blockSize)
		pygame.draw.rect(display, self.boarderColour, rect)
		# draw the circle
		centre = (self.x + self.blockSize // 2, self.y + self.blockSize // 2)
		pygame.draw.circle(display, self.circleColour, centre, self.blockSize // 2.25)
		pygame.display.update(rect)

	def isGameWinningChecker(self, board):
		checkerColour = self.circleColour
		checkerRow = self.row
		checkerCol = self.col
		if checkerColour == SLATEGRAY4:
			return False
		# horizontal case
		if checkerCol + 3 < BOARD_DIMENSION:
			if (board[checkerRow][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow][checkerCol + 2].circleColour == checkerColour and
				board[checkerRow][checkerCol + 3].circleColour == checkerColour):
				return True
		if checkerCol + 2 < BOARD_DIMENSION and checkerCol - 1 >= 0:
			if (board[checkerRow][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow][checkerCol + 2].circleColour == checkerColour):
				return True
		if checkerCol + 1 < BOARD_DIMENSION and checkerCol - 2 >= 0:
			if (board[checkerRow][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow][checkerCol + 1].circleColour == checkerColour):
				return True
		if checkerCol - 3 >= 0:
			if (board[checkerRow][checkerCol - 3].circleColour == checkerColour and
				board[checkerRow][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow][checkerCol - 1].circleColour == checkerColour):
				return True
		# vertical case
		if checkerRow + 3 < BOARD_DIMENSION:
			if (board[checkerRow + 1][checkerCol].circleColour == checkerColour and
				board[checkerRow + 2][checkerCol].circleColour == checkerColour and
				board[checkerRow + 3][checkerCol].circleColour == checkerColour):
				return True
		# diagonal (positive slope)
		if checkerRow - 3 >= 0 and checkerCol + 3 < BOARD_DIMENSION:
			if (board[checkerRow - 1][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow - 2][checkerCol + 2].circleColour == checkerColour and
				board[checkerRow - 3][checkerCol + 3].circleColour == checkerColour):
				return True
		if (checkerRow - 2 >= 0 and checkerCol + 2 < BOARD_DIMENSION and
			checkerRow + 1 < BOARD_DIMENSION and checkerCol - 1 >= 0):
			if (board[checkerRow + 1][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow - 1][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow - 2][checkerCol + 2].circleColour == checkerColour):
				return True
		if (checkerRow - 1 >= 0 and checkerCol + 1 < BOARD_DIMENSION and
			checkerRow + 2 < BOARD_DIMENSION and checkerCol - 2 >= 0):
			if (board[checkerRow + 2][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow + 1][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow - 1][checkerCol + 1].circleColour == checkerColour):
				return True
		if checkerRow + 3 < BOARD_DIMENSION and checkerCol - 3 >= 0:
			if (board[checkerRow + 3][checkerCol - 3].circleColour == checkerColour and
				board[checkerRow + 2][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow + 1][checkerCol - 1].circleColour == checkerColour):
				return True
		# diagonal (negative slope)
		if checkerRow + 3 < BOARD_DIMENSION and checkerCol + 3 < BOARD_DIMENSION:
			if (board[checkerRow + 1][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow + 2][checkerCol + 2].circleColour == checkerColour and
				board[checkerRow + 3][checkerCol + 3].circleColour == checkerColour):
				return True
		if (checkerRow + 2 < BOARD_DIMENSION and checkerCol + 2 < BOARD_DIMENSION and
			checkerRow - 1 >= 0 and checkerCol - 1 >= 0):
			if (board[checkerRow - 1][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow + 1][checkerCol + 1].circleColour == checkerColour and
				board[checkerRow + 2][checkerCol + 2].circleColour == checkerColour):
				return True
		if (checkerRow + 1 < BOARD_DIMENSION and checkerCol + 1 < BOARD_DIMENSION and
			checkerRow - 2 >= 0 and checkerCol - 2 >= 0):
			if (board[checkerRow - 2][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow - 1][checkerCol - 1].circleColour == checkerColour and
				board[checkerRow + 1][checkerCol + 1].circleColour == checkerColour):
				return True
		if checkerRow - 3 >= 0 and checkerCol - 3 >= 0:
			if (board[checkerRow - 3][checkerCol - 3].circleColour == checkerColour and
				board[checkerRow - 2][checkerCol - 2].circleColour == checkerColour and
				board[checkerRow - 1][checkerCol - 1].circleColour == checkerColour):
				return True
		return False

def makeBoard(display, size, width):
	board = []
	blockSize = size // width
	for i in range(width):
		board.append([])
		for j in range(width):
			checker = Checker(i, j, blockSize)
			checker.drawChecker(display)
			board[i].append(checker)
	return board

def getMouseColumn(position, size, width):
	blockSize = size // width
	x, y = position
	return x // blockSize

def insertChecker(display, board, col, colour):
	if board[1][col].isFilled():
		return None

	for i in range(1, BOARD_DIMENSION):
		checker = board[i][col]
		if i == BOARD_DIMENSION - 1 and checker.isNotFilled():
			checker.setCircleColour(colour)
			checker.drawChecker(display)
			return checker
		checkerAbove = board[i - 1][col]
		checkerAbove.setCircleColour(colour)
		checkerAbove.drawChecker(display)
		pygame.time.wait(35)
		if checker.isNotFilled():
			if i == 1:
				pygame.time.wait(500)
			checkerAbove.setCircleColour(SLATEGRAY4)
			checkerAbove.drawChecker(display)
		else:
			return checkerAbove

def resetBoard(display, board):
	for row in board:
		for checker in row:
			checker.setCircleColour(SLATEGRAY4)
			checker.drawChecker(display)

def main(display, size, width):
	pygame.init()
	board = makeBoard(display, size, width)
	clock = pygame.time.Clock()
	colour = RED
	end = False
	checkersInBoard = 0
	while True:

		if checkersInBoard == 42:
			font = pygame.font.Font(None, 40)
			text = font.render("Draw!", False, BLACK)
			display.blit(text, (0, 0))
			rect = pygame.Rect(0, 0, size, size // width)
			pygame.display.update(rect)
			end = True

		for event in pygame.event.get():
			# check if the user exits the pygame display
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			# check if the user clicks enter key
			if event.type == pygame.KEYDOWN:
				# reset the display
				if event.key == pygame.K_r:
					for row in board:
						for checker in row:
							resetBoard(display, board)
							colour = RED
							end = False
							checkersInBoard = 0
			
			# check if the user left clicks
			if pygame.mouse.get_pressed()[0] and not end:
				position = pygame.mouse.get_pos()
				col = getMouseColumn(position, size, width)
				checker = insertChecker(display, board, col, colour)
				# check if there is a win
				if checker is not None and checker.isGameWinningChecker(board):
					font = pygame.font.Font(None, 40)
					if colour == RED:
						text = font.render("Red wins!", False, BLACK)
					else:
						text = font.render("Yellow wins!", False, BLACK)
					display.blit(text, (0, 0))
					rect = pygame.Rect(0, 0, size, size // width)
					pygame.display.update(rect)
					end = True
				# change the colour if we were able to insert
				if checker is not None:
					if colour == RED:
						colour = YELLOW
					else:
						colour = RED
					checkersInBoard += 1

		clock.tick(60)

if __name__ == "__main__":
	main(display, DISPLAY_SIZE, BOARD_DIMENSION)
