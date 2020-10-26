def start():
    print('H A N G M A N')
    print('The game will be available soon.')


def ask(check_answer):
    if check_answer == input('> '):
        print('You survived!')
    else:
        print('You lost!')


correct_answer = 'python'
start()
ask(correct_answer)
