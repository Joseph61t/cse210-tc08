from batter_template.batter.game import point
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
        brick = cast["brick"][0] # there's only one
        # artifacts = cast["artifact"]
        brick.set_text("")
        #for artifact in artifacts:


        # the if statements the cover when a ball hits a brick
        # covers if the ball hits a brick from bellow
        if ball.get_y(ball.get_position()) - 1 == brick.get_y(ball.get_position()) and ball.get_x(ball.get_position()) == brick.get_x(ball.get_position()):
            point = Point(ball.get_x(), (ball.get_y() * -1))
            ball.set_velocity(point)
        # covers if the ball hits a brick from above
        if ball.get_y(ball.get_position()) + 1 == brick.get_y(ball.get_position()) and ball.get_x(ball.get_position()) == brick.get_x(ball.get_position()):
            point = Point(ball.get_x(), (ball.get_y() * -1))
            ball.set_velocity(point)
        # covers if the ball hits a brick from the left
        if ball.get_x(ball.get_position()) - 1 == brick.get_x(ball.get_position()) and ball.get_y(ball.get_position()) == brick.get_y(ball.get_position()):
            point = Point((ball.get_x() * -1), ball.get_y())
            ball.set_velocity(point) 
        # covers if the ball hits a brick from the right
        if ball.get_x(ball.get_position()) + 1 == brick.get_x(ball.get_position()) and ball.get_y(ball.get_position()) == brick.get_y(ball.get_position()):
            point = Point((ball.get_x() * -1), ball.get_y())
            ball.set_velocity(point)