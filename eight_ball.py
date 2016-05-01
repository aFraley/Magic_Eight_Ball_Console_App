"""A Magic Eight Ball module."""
from random import choice


class EightBall():
    """A class to create an EightBall object."""
    def __init__(self):
        """Initialize an EightBall's attributes."""
        self.__answers = (
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes, definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        )

    def get_answer(self):
        """Grab an answer from answers tuple."""
        return choice(self.__answers)