from game import secret,io,logic,validate



def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret1=secret.generate_secret(length,unique_digits)
    state1=logic.init_state(secret1,length,max_tries,unique_digits,allow_leading_zero)
    flag=True
    while flag:
        goess1=io.prompt_guess(length)
        valid=validate.is_valid_guess(goess1,length,unique_digits)
        if  not valid:
            continue
        if validate.is_new_guess(goess1,state1['seen']):
            bulls_cows=logic.score_guess(secret1,goess1)
            flag=not logic.is_won(bulls_cows[0],length)
            if not flag:
                io.print_result(state1)
                print('wenner')
                continue
            logic.apply_guess(state1,goess1,bulls_cows)
            io.print_feedback(goess1,bulls_cows[0],bulls_cows[1])
            io.print_status(state1)
            if state1['tries_used']==state1['max_tries']:
                print('looser')
                io.print_result(state1)
                flag=False



play()