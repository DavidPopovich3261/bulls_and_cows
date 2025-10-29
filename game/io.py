



def prompt_guess(length: int) -> str:
    guess=input('Please enter a guess')
    return guess


def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(guess,bulls,cows)

def print_status(state: dict) -> None:
    print(state['tries_used'],state['history'])

def print_result(state: dict) -> None:
        print(state['secret'])