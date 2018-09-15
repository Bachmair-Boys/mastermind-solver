from Guess import Guess
from Colors import Colors as c

guess1 = Guess([c.Y, c.G, c.R, c.Bk],0,2)
guess2 = Guess([c.Bk, c.W, c.Y, c.Bu],1,1)
guess3 = Guess([c.G, c.Bu, c.W, c.R],1,1)
guess4 = Guess([c.W, c.R, c.Bk, c.R],0,1)
guess5 = Guess([c.R, c.R, c.G, c.G],1,1)
guesses = [guess1,guess2,guess3,guess4,guess5]
explanations = []
solutions = []
solution = []
colors = [c.Y,c.G,c.R,c.Bk,c.Bu,c.W]
code = [[c.Y,c.G,c.R,c.Bk,c.Bu,c.W],[c.Y,c.G,c.R,c.Bk,c.Bu,c.W],[c.Y,c.G,c.R,c.Bk,c.Bu,c.W],[c.Y,c.G,c.R,c.Bk,c.Bu,c.W],]
#code[1][2] = c.NONE  

def check_possibilities():
    possibilities = 1
    lengths = [0,0,0,0];
    for x in range(4):
        for y in range(6):
            if not code[x][y].value == 0:
                lengths[x] = lengths[x] + 1
    for x in range(4):
        possibilities = possibilities * lengths[x]
    return possibilities

def must_have_a_color(color): # COULD USE MORE LOGIC THAT WOULD CHECK STUFF IN CODE MATRIX
    for a_guess in guesses:
        num_color = count_instances_of_color_in_guess(color, a_guess.sequence)
        if num_color == 1:
            index = a_guess.sequence.index(color)
            if not a_guess.num_whites == 0 and a_guess.num_blacks == 0:
                a_guess.sequence[index] = c.NONE
                a_guess.num_whites = a_guess.num_whites - 1
                explanations.append(f"took out {color.name} from guess {guesses.index(a_guess)+1} and from num white because we know color is in sequence")
            elif a_guess.num_whites == 0 and not a_guess.num_blacks == 0:
                a_guess.sequence[index] = c.NONE
                a_guess.num_blacks = a_guess.num_blacks - 1
                explanations.append(f"took out {color.name} from guess {guesses.index(a_guess)+1} and from num black because we know color is in sequence")                
                # ADD CALL ELEMENT IS SOLVED LOGIC FROM HERE
                pass
               
def must_not_have_a_color(color): # DONE
    for a_guess in guesses:
        num_color = count_instances_of_color_in_guess(color, a_guess.sequence)
        for x in range(num_color):
            index = a_guess.sequence.index(color)
            a_guess.sequence[index] = c.NONE
            explanations.append(f"took out {color.name} from guess {guesses.index(a_guess)+1} because we know color isn't in sequence")

def from_num_dots_and_colors():
    for a_guess in guesses:
        colors_in_seq = []
        for color in c:
            num_color = count_instances_of_color_in_guess(color, a_guess)
            if num_color >= 1:
                colors_in_seq.append(color)
        if a_guess.num_blacks + a_guess.num_whites >= len(colors_in_seq):
            for color_in_seq in colors_in_seq:
                must_have_a_color(color_in_seq) 
        if a_guess.num_blacks + a_guess.num_whites == 1 and len(colors_in_seq) == 2:
            pass
           
def count_instances_of_color_in_guess(c,guess):
    num_color = 0
    for g in guess:
        if g == c:
            num_color = num_color + 1
    return num_color

def is_solved(position, solvedColor):
	for guess in guesses:
		colorCounter = 0
		for color in guess.sequence:
			if color == solvedColor:
				colorCounter += 1
		
		if colorCounter == 1:
			bool = False
			if guess.sequence.index(solvedColor) == position:
				guess.num_blacks -= 1
				bool = True
				guess.sequence[position] = c.NONE
			if bool == False: 
				guess.num_whites -= 1
				guess.sequence[position] = c.NONE

# def apply_rule1():
#     for guess in guesses:
#         if guess.num_blacks == 0:
#             for color in guess.sequence:
#                 for possibility in possibilities:
#                     if color in possibility:
#                         possibility[possibility.index(color)] = c.NONE


# def print_possibilities():
#     for p in possibilities:
#         print(p)

def main():
#     print(check_possibilities())
#     print(6*5*6*6)
#     print(count_instances_of_color_in_guess(c.Bk, guess1.sequence))
#     must_have_a_color(c.Bk)
#     for a_guess in guesses:
#         print(a_guess.sequence)
    apply_rule1()
    while check_possibilities() > 5:
        from_num_dots_and_colors()
        if check_possibilities <= 5:
            break
        else:
            guess_branch():
    #for g in code    
        
    
        
if __name__ == '__main__':
    main()                
           


