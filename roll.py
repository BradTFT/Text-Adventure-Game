


def rollSystem():
    import random
    attack = input('you need to attack this spider')
    attempt = random.randrange(1, 38)
    outcome = random.randrange(1, 38)
    failedattack = 'Your attack failed'
    passedattack = 'Your attack was sucessful'

    print(f'your roll: {attempt}')
    print(f"outcome: {outcome}")

    if outcome > attempt:
        print(failedattack)
    elif outcome == attempt:
        print(failedattack)
    elif outcome < attempt:
        print(passedattack)