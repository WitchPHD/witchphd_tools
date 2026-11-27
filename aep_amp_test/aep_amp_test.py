# Test AEP's AMP program over random numbers
import random

use_history = []
cum_saving = 0
default = 109

class monat:
    def __init__(self, dollars):
        usage = 200
        payment = 200
        avg_payment = 200
        cum_payment = 200
        cum_avg_payment = 200
        

print ('AMP (Average Monthly Payments) is a program provided by AEP to reduce bill volatility.\n')
print ('It keeps a 12 month history of your usage and averages them to determine your bill.\n')
print ('This script is designed to test if that saves or loses you money over time using RNG.\n')
print ('With insufficient history, AEP uses {:} as the usage amount.\n'.format(default))

for i in range(12):
    use_history.append(default)

months = int(input('\nPlease enter the number of months you wish to simulate:'))

for month in range(months):
    payment = default + random.randrange(-40, 60, 1)
    use_history.append(payment)
    use_history.pop(0)
    amp_payment = sum(use_history) / len(use_history)
    amp_saving = payment - amp_payment
    cum_saving += amp_saving
    print('Month {:}: \n\t Regular Payment: {:.02f} \n\t AMP Payment: {:.02f} \n\t AMP Saving: {:.02f} \n\t - Cumulative AMP Saving: {:.02f}'.format(month+1, payment, amp_payment, amp_saving, cum_saving))

input('\nHIT ENTER TO TERMINATE THE PROGRAM.')


