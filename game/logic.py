




def score_guess(secret: str, guess: str,) -> tuple[int, int]:
    bulls=0
    cows=0
    for i,y in enumerate(guess):
        if y in secret:
            if guess[i]==secret[i]:
                bulls+=1
            else:
                cows+=1
    return bulls,cows


def is_won(bulls: int, length: int) -> bool:
    if bulls==length:
        return True
    return False



def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> dict:
    state = {
        "secret": secret,
        "length": length,
        "max_tries": max_tries,
        "tries_used": 0,
        "unique_digits": unique_digits,
        "allow_leading_zero": bool,
        "history": [],  # [(guess, bulls, cows), ...]
        "seen": []  # ניחושים שנעשו
    }
    return state


def apply_guess(state: dict, guess: str,bulls_cows:tuple[int, int]):
    history=[guess,bulls_cows[0],bulls_cows[1]]
    state['history'].append(history)
    state['tries_used']+=1
    state['seen'].append(guess)
