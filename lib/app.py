class CLI():
    ''' User interface '''
    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'\nStarting app...')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'\nEnter your Github username: \n')
            if self._user_input == 'exit':
                return self.goodbye()
            print(f'You said: {self._user_input}')
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    @staticmethod
    def goodbye():
        print(f'\nExiting the app :)\n')

if __name__ == '__main__':
    app = CLI()
