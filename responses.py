from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == ' ':
        return 'Well, you are awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    else:
        return choice(['i dont understand...',
                       'What are you talking about?',
                       'Do you mind repharsing that?'])

    #raise NotImplementedError('Code is missing...')
