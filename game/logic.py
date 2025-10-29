




def score_guess(secret: str, guess: str) -> tuple[int, int]:
    pass


def is_won(bulls: int, length: int) -> bool:
    pass



def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> dict:
    state = {
        "secret": str,
        "length": int,
        "max_tries": int | None,
        "tries_used": int,
        "unique_digits": bool,
        "allow_leading_zero": bool,
        "history": list[tuple[str, int, int]],  # [(guess, bulls, cows), ...]
        "seen": set[str]  # ניחושים שנעשו
    }
    return state


def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    pass
