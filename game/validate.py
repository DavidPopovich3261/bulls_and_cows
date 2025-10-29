

def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    flag=True
    if len(guess)==length:
        if not guess.isdigit():
            flag=False
            print()
        elif unique_digits:
            guess2=''
            for i in guess:
                if i in guess2:
                    flag =False
                    print()
                else:
                    guess2+=i
    return flag ,guess



def is_new_guess(guess: str, history: set[str]) -> bool:
    if guess in history:
        return False
    return True