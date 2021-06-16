from game.constants import MAX_X
from game import point
import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        bricks = cast["bricks"] # there's only one
        # artifacts = cast["artifact"]
        #brick.set_text("")
        #for artifact in artifacts:

        if ball.get_position().get_x == MAX_X:
            point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
            ball.set_velocity(point) 

        # the if statements the cover when a ball hits a brick
        # covers if the ball hits a brick from bellow
        for brick in bricks:
            if ball.get_position().get_y() - 1 == brick.get_position().get_y() and ball.get_position().get_x() == brick.get_position().get_x():
                point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
                ball.set_velocity(point)
            # covers if the ball hits a brick from above
            if ball.get_position().get_y() + 1 == brick.get_position().get_y() and ball.get_position().get_x() == brick.get_position().get_x():
                point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
                ball.set_velocity(point)
            # covers if the ball hits a brick from the left
            if ball.get_position().get_x() - 1 == brick.get_position().get_x() and ball.get_position().get_y() == brick.get_position().get_y():
                point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
                ball.set_velocity(point) 
            # covers if the ball hits a brick from the right
            if ball.get_position().get_x() + 1 == brick.get_position().get_x() and ball.get_position().get_y() == brick.get_position().get_y():
                point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
                ball.set_velocity(point)