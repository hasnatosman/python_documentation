def argu(prompts, retries=4, reminder='Try again please !'):
    while True:
        ok = input(prompts)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'No'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('Invalid user response!')
        print(reminder)


argu('Do you really want to quit? ')
