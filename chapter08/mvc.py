"""MVC模式

>>> main()
Which quote number would you like to see? 2
And the quote is: "Behind a successful man is an exhausted woman."
Which quote number would you like to see? 4
And the quote is: "Facts are stubborn things."
Which quote number would you like to see? 1
And the quote is: "As I said before, I never repeat myself."
Which quote number would you like to see? 6
And the quote is: "Not found!"
Which quote number would you like to see? 3
And the quote is: "Black holes really suck..."
Which quote number would you like to see? 0
And the quote is: "A man is not complete until he is married. Then he is finished."
Which quote number would you like to see?

"""

quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...',
    'Facts are stubborn things.'
)


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:

    def show(self, quote):
        """ print a quote on the screen. """
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        """ used to print an error message on the screen. """
        print(f'Error: {msg}')

    def select_quote(self):
        """ reads the user's selection. """
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        """
        The run() method validates the quoted index given by the user,
        gets the quote from the model, and passes it back to the view
        """
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
