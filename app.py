from roll import rollSystem #imports a background file running the rolling function

inventory = ['a', 'x', 'b']
#experimenting a little bit
input = input('')


def showInventory():
    #const for printing inventory list
    print('\n')
    print(' \n \n'.join(inventory))
    

if input == 'e' or 'E':
    showInventory()

#basic idea rn