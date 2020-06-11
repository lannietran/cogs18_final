import random
from time import sleep
from IPython.display import clear_output
from my_module.my_functions import *

#Test that add_lists works
def test_add_lists():
    """Tests the 'add_lists' function"""
    #Test adding integers
    assert [2, 2] == add_lists ([0, 1], [2, 1])
    
    #Test adding floats
    assert [1.5, 2.0] == add_lists([1.0, 1.5], [0.5, 0.5])
    
    #Test adding strings
    assert ['red apple', 'yellow banana'] == add_lists(['red ', 'yellow '], ['apple', 'banana'])
    
    #Test adding negative numbers
    assert [-4, -9] == add_lists([5, -4], [-9, -5])
    
    #Test the function returns a list
    assert isinstance(add_lists([0, 1], [2, 1]), list)
    
test_add_lists()

def test_check_bounds():
    """Tests 'check_bounds' function"""
    
    #Test an out-of-bounds position will return false when less than 0
    assert not check_bounds([-2, -2], 1 )
    
    #Test an out-of_bounds position will return false when item is greater than size but still greater than 0
    assert not check_bounds([4, 4], 2)
    
    #Test an in-bound position will return as True when it is within bounds
    assert check_bounds ([3, 3], 5)

test_check_bounds()

#Test the ObstacleBot
def test_obstacle():
    assert Obstacle()
    o_bot = Obstacle()
    assert o_bot

    #Test that ObstacleBot has default position
    assert o_bot.position == [1, 2]
    
    #Test that ObstacleBot's stationary position is an ordered pair
    assert o_bot.stationary()
    assert isinstance(o_bot.stationary(), list)
    
    #Test that ObstacleBot's move is an ordered pair
    assert o_bot.move()
    assert isinstance(o_bot.move(), list)

    #Test the Obstacle. The obstacle should not move.
    play_board(o_bot)

test_obstacle()

#Test out the DiagonalBot
def test_diagonal_bot():
    
    #Test that the Diagonal Bot class and functions work
    assert DiagonalBot
    d_bot = DiagonalBot()
    assert d_bot
    
    d_bot.grid_size = 5
    
    #Test that diagonal_move method correctly implements a new diagonal position
    assert d_bot.diagonal_move()
    
    #Test that DiagonalBot has restricted movements
    assert d_bot.moves == [[1, 1], [1, -1], [-1, -1], [-1, 1]]

    #Test that DiagonalBot's next move is an ordered pair (list)
    assert d_bot.diagonal_move()
    assert isinstance(d_bot.diagonal_move(), list)
    
    #Test that DiaongalBot's next position is an ordered pair (list)
    assert d_bot.move()
    assert isinstance(d_bot.move(), list)
    
    # Test out the DiagonalBot. The bot should only be moving around the grid in diagonal movements.
    play_board(d_bot)
    
test_diagonal_bot()

def test_horizontal_bot():
    assert HorizontalBot()
    h_bot = HorizontalBot()
    assert h_bot
    
    #Set a grid size to test
    h_bot.grid_size = 5
    
    #Test that HorizontalBot has restricted horizontal movements
    assert h_bot.moves == [[0, 1], [0, -1]]
    
    #Test that HorizontalBot will initialize at one of the random choices
    assert h_bot.position == [0, 0] or [1, 0] or [2, 0] or [3, 0] or [4, 0]
    
    #Test that HorizontalBot's next move is an ordered pair (a list)
    assert h_bot.sideways_move()
    assert isinstance(h_bot.sideways_move(), list)
    
    #Test that HorizontalBot's next position is an ordered pair (a list)
    assert h_bot.move()
    assert isinstance(h_bot.move(), list)

    #Test out the HorizontalBot. The bot should only be moving around the grid in horizontal movements. 
    play_board(h_bot)
    
test_horizontal_bot()

#Test the VerticalBot
def test_vertical_bot():

    assert VerticalBot()
    v_bot = VerticalBot()
    assert v_bot
    
    #Set a grid size to test
    v_bot.grid_size = 5
    
    #Test that VerticalBot has restricted vertical movements
    assert v_bot.moves == [[1, 0], [-1, 0]]
    
    #Test that VerticalBot will begin at one of the random vertical positions
    assert v_bot.position == [0, 0] or [0, 1] or [0, 2] or [0, 3] or [0, 4]

    #Test that VerticalBot's next movement is an ordered pair (list)
    assert v_bot.updown_move()
    assert isinstance(v_bot.updown_move(), list)
    
    #Test that VerticalBot's next position is an ordered pair (list)
    assert v_bot.move()
    assert isinstance(v_bot.move(), list)
    
    #Test out the VerticalBot. The bot should only be moving around the grid in vertical (up or down) movements. 
    play_board(v_bot)
    
test_vertical_bot()

#Test Pedestrian Bot
def test_pedestrian_bot():
    assert PedestrianBot()
    p_bot = PedestrianBot()
    assert p_bot
    
    #Set a grid size to test the bot on
    p_bot.grid_size = 5
    
    #Check that the next step given is an ordered pair (a list)
    assert isinstance(p_bot.choose_step(), list)
    
    #Check that last_step is originally None as it hasn't moved yet
    assert p_bot.last_step == None
    
    #Check that bot only has the four requested movements
    assert p_bot.choose_step == [0, 1] or [0, -1] or [1, 0] or [-1, 0]
    
    #Test that PedestrianBot's next move is an ordered pair (a list)
    assert p_bot.choose_step()
    assert isinstance(p_bot.choose_step(), list)
    
    #Test that PedestrianBot's next step is an ordered pair (a list)
    assert p_bot.walk()
    assert isinstance(p_bot.walk(), list)
    
    #Test that PedestrianBot's next position is an ordered pair (a list)
    assert p_bot.move()
    assert isinstance(p_bot.move(), list)
    
    #Test out the PedestrianBot. You should see a bot that takes "steps" around the grid.
    play_board(p_bot)

#Should see a bot that moves around the grid with its next step depending on where it was last    
test_pedestrian_bot() 

#Test the answer function
def test_answer():
    #Test that it returns a boolean
    assert isinstance (answer('yes'), bool)
    #Tests that it returns True if the answer is yes
    assert answer('yes') == True
    #Tests that for any other answer, the answer is no
    assert answer('eh') == False
    assert answer('no') == False

test_answer()

def test_all():
    test_add_lists()
    test_check_bounds()
    test_obstacle()
    test_diagonal_bot()
    test_horizontal_bot()
    test_vertical_bot()
    test_pedestrian_bot()
    test_answer()
    
test_all()