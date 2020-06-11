#imports from A4:
import random
from time import sleep
from IPython.display import clear_output

#The following function was given in A4 and is not mine
#I have changed/added a couple things, all of which are noted with code comments
#removed spacing around keyword argument assignment for code style usng pylint
#tweaked grid size to be default size 8 (instead of 5)
def play_board(bots, n_iter=25, grid_size=8, sleep_time=0.3):
    """Run a bot across a board.

    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5 (Must be at least 5)
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    
    This code is external code from A4.
    """

    # Wrote this conditional to require a grid size that is at least 5
    if grid_size < 5:
        raise ValueError('Please input grid size greater than or equal to 5')

    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]

    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    for iteration in range(n_iter):

        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]

        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()

#This code is from A4 and is not mine
def add_lists(list1, list2):
    """Add lists together.

    Parameters
    ----------
    list1 = list
        The first list to be added
    list2 = list
        The second list to be added

    Returns
    -------
    output = list
        The resulting list from the addition
    
    This code is external code from A4.
    """

    output = []
    for element1, element2 in zip(list1, list2):
        output.append(element1 + element2)

    return output

#This function was written for A4 and is not mine
def check_bounds(position, size):
    """Check that a point is within bounds.
    Parameters
    ----------
    position = list
        An ordered pair
    size = int
        The size of the grid

    Returns
    -------
    boolean = bool
        True if the position is within bounds, False if not
    
    This code is external code from A4.
    """

    boolean = bool

    #for each position, if out of bounds return false. if within bounds, returns True.
    for item in position:
        if item < 0:
            boolean = False

        elif item >= size:
            boolean = False

    return boolean
    boolean = True

#This class was written in A4 and is not mine
class Bot():
    """Initializes a bot

    Parameters
    -----------
    position = list
        The ordered pair reflecting the position in the grid
    moves = list
        Ordered pairs of the bot's movements
    grid_size = int, optional
        The size of the grid
        Slightly modified from assignment to equal grid_size instead of None
    character = string
    
    This code is external code from A4.

"""
    def __init__(self, character=8982, grid_size=7): #usually gridsize not here
        self.position = [0, 0]
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.grid_size = grid_size
        self.character = chr(character)

#The following bots all inherit the Bot class created in A4
#some methods borrow from the methods created in A4, and are all noted.

#initializes a class that inherits from Bot that does not move
class Obstacle(Bot):
    """Creates a stationary bot.
    Parameters
    ----------
    character = string
    position = list
        ordered pair reflecting position of the bot
    """

    def __init__(self, character=8982, position=[1, 2]):
        super().__init__(character=8982)
        self.position = position

    def stationary(self):
        """Implements bot's next move to the same position.
        Returns
        -------
        move = list
            ordered pair of the next move of the bot
        """

        #Returns the same postion as the next move to keep bot still
        move = self.position
        return move

    def move(self):
        """Uses the (lack of) movement to make bot stay at same position
        Returns
        -------
        self.position = list
            ordered pair of the next position of the bot, which remains the same
        """

        self.position = self.stationary()
        return self.position

#imagine this bot like a self-operating machine that has to avoid obstacles in the path
class DiagonalBot(Bot):
    """Creates a bot that can only move diagonally. Inherits from Bot Class.

    Parameters
    ----------
    character = string

    Attributes
    ----------
    moves = list
        List of ordered pairs that reflect the bot's movements
    position = list
        Ordered pair reflecting the bot's position

    """

    def __init__(self, character=8982):
        super().__init__(character=8982)
        self.moves = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        self.position = random.choice([[0, 0], [1, 1], [2, 2]])

    def diagonal_move(self):
        """Creates the diagonal movements of the bot

        Returns
        -------
        new_diagonal_position = list
            Ordered pair of the bot's next movement
            
        This code is external code adapted from A4.
        """

        #This method was adapted from A4's wander method.
        has_new_position = False
        while not has_new_position:
            move = random.choice(self.moves)
            new_diagonal_position = add_lists(move, self.position)
            has_new_position = check_bounds(new_diagonal_position, self.grid_size)

        return new_diagonal_position

    def move(self):
        """Uses the diagonal movement created to move

        Returns
        -------
        self.position = list
            Ordered pair of the position that the bot ends up in
        """

        #If the next move of the bot will take the same place of the obstacle, move to avoid it.
        if self.diagonal_move() == Obstacle.stationary(self):
            move = random.choice(self.moves)
            self.position = add_lists(self.diagonal_move(), move)
            return self.position
        #If not, continue with the original intended move.
        else:
            self.position = self.diagonal_move()
            return self.position

#imagine this bot like a self-operating machine that has to avoid obstacles in the path
class HorizontalBot(Bot):
    """Inherits from Bot class and creates a bot that can only move directly to the right or left

    Parameters
    ----------
    character = string

    Attributes
    ----------
    self.moves = list
        Ordered pairs that give the bot's possible movements
    self.position = list
        Ordered pairs that give the possible starting positions for the bot
    """

    def __init__(self, character=8982):
        #restricted movements one step to the left or right
        #can randomly start in the first, second, or third rows of the grid
        super().__init__(character=8982)
        self.moves = [[0, 1], [0, -1]]
        self.position = random.choice([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]])

    #This method is adapted from A4's wander method.
    def sideways_move(self):
        """Creates the horizontal movements of the bot
        Returns
        -------
        new_horizontal_position = list
            Ordered pair of the new movement of the bot
            
        This code is external code adapted from A4.
        """

        has_new_position = False
        while not has_new_position:
            move = random.choice(self.moves)
            new_horizontal_position = add_lists(move, self.position)
            has_new_position = check_bounds(new_horizontal_position, self.grid_size)

        return new_horizontal_position

    def move(self):
        """Moves the bot according to the new horizontal position
        Returns
        -------
        self.position = list
            The current position of the bot after moving
        """

        #if bot's new movement intereferes with the obstacle, it moves down to avoid it
        if self.sideways_move() == Obstacle.stationary(self):
            self.position = add_lists(self.sideways_move(), [1, 0])
            return self.position
        #if not, bot continues
        else:
            self.position = self.sideways_move()
            return self.position

#initializes a class that inherits from Bot that has restricted vertical movements
#imagine this bot like a self-operating machine that has to avoid obstacles in the path
class VerticalBot(Bot):
    """Initializes a bot that can only move directly up or down
    Parameters
    ----------
    character = string

    Attributes
    ----------
    moves = list
        ordered pairs that represent possible movements of the bot
    position = list
        ordered pairs that represent possible starting positions of the bot
    """

    def __init__(self, character=8982):
        super().__init__(character=8982)
        self.moves = [[1, 0], [-1, 0]]
        self.position = random.choice([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]])

    #This method is adapted from A4's wander method.
    def updown_move(self):
        """Method that creates the next move for the bot by creating a new position
        Returns
        -------
        new_vertical_position = list
            ordered pair of the new position of the bot
            
        This code is external code adapted from A4.
        """

        has_new_position = False
        while not has_new_position:
            move = random.choice(self.moves)
            new_vertical_position = add_lists(move, self.position)
            has_new_position = check_bounds(new_vertical_position, self.grid_size)

        return new_vertical_position

    def move(self):
        """Method that moves the bot to its new position
        Returns
        -------
        self.position = list
            ordered pair of the current position of the bot after moving
        """

        #if the new position interferes with the obstacle, bot moves over to avoid
        if self.updown_move() == Obstacle.stationary(self):
            self.position = add_lists(self.updown_move(), [0, 1])
            return self.position
        #if not, the bot will continue on
        else:
            self.position = self.updown_move()
            return self.position

#This class creates a bot that imitates a Pedestrian who has full range of motion
#the last step however, determines the next step.
#As a 'pedestrian', this bot can walk over obstacles, unlike the bots preceding

class PedestrianBot(Bot):
    """Class that initializes a PedestrianBot that takes steps depending on the step preceding
    Parameters
    ----------
    character = string

    Attributes
    ----------
    self.moves = list
        list of ordered pairs of possible movements
    self.position = list
        list of ordered pairs of possible starting positions
    self.last_step = list or None
        list of ordered pairs of the last step that the bot took
    """

    def __init__(self, character=8982):
        super().__init__(character=8982)
        self.moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.position = random.choice([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]])
        self.last_step = None

    def choose_step(self):
        """Method that takes last step into account to choose next step

        Returns
        -------
        move = list
            ordered pair of the next step of the bot
        
        The second if statement is adapted from A4.
        """

        move = None
        if self.last_step is not None:
            if self.last_step == [1, 0]:
                move = [0, 1]
            elif self.last_step == [0, 1]:
                move = [-1, 0]
            elif self.last_step == [-1, 0]:
                move = [0, -1]
            elif self.last_step == [0, -1]:
                move = [1, 0]
        #This if statement inspired by A4's ExploreBot if statement in biased_choice
        if self.last_step is None:
            move = random.choice(self.moves)

        return move

    def walk(self):
        """Method that creates new position based on last step
        Returns
        -------
        has_new_step = list
            ordered pair of the current position of the bot after taking next step
        
        This code is external code adapted from A4.
        """

        #This method is adapted from A4's wander method.
        took_new_step = False
        while not took_new_step:
            move = self.choose_step()
            has_new_step = add_lists(move, self.position)
            took_new_step = check_bounds(has_new_step, self.grid_size)

        return has_new_step

    def move(self):
        """Method that moves bot to the new position
        Returns
        -------
        self.position = list
            Ordered pair of the new position of the bot
        """

        self.position = self.walk()
        return self.position

#Inspired by the is_question function in A3
def answer(answer_string):
    """Function to check for answers to a yes/no question
    Parameters
    ----------
    answer_string = string
        The answer to the yes/no question

    Returns
    -------
    output = bool
        If yes, returns True. If not, returns False
    """

    if 'Yes' in answer_string:
        output = True
    elif 'yes' in answer_string:
        output = True
    else:
        output = False

    return output

def chat_to_start():
    """This function starts the simple chat bot.

    Returns
    -------
    chat = bool
        Always returns False to end the chat bot

    """
    print('Hi! Thanks for coming. Are you ready to see some bots? Please answer "yes" or "no"!')
    chat = True
    while chat:
        #Implements a input field for users to use
        start_message = input()
        #If they say yes, the play_board plays!
        if answer(start_message) == True:
            play_board(bots=[Obstacle(), DiagonalBot(), HorizontalBot(), VerticalBot(), PedestrianBot()])
            print('Thanks for watching!')
            chat = False
        #If they say no, the chat bot ends and they do not see the bots.
        elif answer(start_message) == False:
            print('Sorry to hear that. Have a good day!')
            chat = False