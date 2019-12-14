def AskName():
    promptName = input('What is your name:')
    print('Hello ' + promptName)


def PreDie():
    promptDie = input('Would you like to roll a die')

    if promptDie == 'Yes' or 'y' or 'yes' or 'Y':
        print('Not Done')

    elif promptDie == 'no' or 'n' or 'No' or 'N':
        print('Bye')
        
    else:
        print('Please Try Again:')


AskName()
PreDie()
