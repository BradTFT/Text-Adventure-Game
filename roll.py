


def rollSystem():
    import random
    import time
    attempt = random.randrange(1, 38)
    outcome = random.randrange(1, 38)
    failedattack = 'Your attack failed'
    passedattack = 'Your attack was sucessful'

    print(f'your roll: {attempt}')
    time.sleep(2)
    print(f"outcome: {outcome}")

    if outcome > attempt:
        print(failedattack)
    elif outcome == attempt:
        print(failedattack)
    elif outcome < attempt:
        print(passedattack)