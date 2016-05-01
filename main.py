"""Magic Eight Ball Application.

Author: Alan Fraley
Date: 5/1/2016
"""
from eight_ball import EightBall
# from os import system


def main():
    """This is where the magic happens."""

    # Instantiate an EightBall object.
    mystical_eight_ball = EightBall()

    prompt = '\nEightBall$ '
    answer = '\n\tMagic Eight Ball says:'
    exit_message = '\nExiting the Eight Ball app.'
    art = """
              _.a$$$$$a._
            ,$$$$$$$$$$$$$.
          ,$$$$$$$$$$$$$$$$$.
         d$$$$$$$$$$$$$$$$$$$b
        d$$$$$$$$~'"`~$$$$$$$$b
       ($$$$$$$p   _   q$$$$$$$)
       $$$$$$$$   (_)   $$$$$$$$
       $$$$$$$$   (_)   $$$$$$$$
       ($$$$$$$b       d$$$$$$$)
        q$$$$$$$$a._.a$$$$$$$$p
         q$$$$$$$$$$$$$$$$$$$p
          `$$$$$$$$$$$$$$$$$'
            `$$$$$$$$$$$$$'
              `~$$$$$$$~'"""
    title = """
         ====================
         | Magic Eight Ball |
         ===================="""
    loop_count = 1
    try:
        print(art)
        print(title)
        main_loop = True
        while main_loop:
            if loop_count <= 1:
                # Explain the rules to the user.
                print('\nPlease ask the Eight Ball App a close-ended question, a question that can be answered\
 with a yes or no answers.')
                print('\t<To exit the app at any time enter "exit or x".>')
            else:
                print('\nPlease ask the same question again or ask different question.')
            loop_count += 1

            # Display the user prompt.
            command = str(input(prompt)).lower()

            # Display the EightBall's answers.
            print(answer, mystical_eight_ball.get_answer())

            # Check the mainloop.
            if command == 'x' or command == 'exit':
                main_loop = False
                print(exit_message)
                # system('clear')

    # Handle a keyboard interruption.
    except KeyboardInterrupt:
        print(exit_message)
        # system('clear')
main()
