def gen_sequence(deposit_1, deposit_2):
    bal_1 = deposit_1
    bal_2 = deposit_1 + deposit_2
    new_bal = bal_1 + bal_2
    day = 3
    while new_bal < 1000000:
        old_bal = new_bal
        new_bal += bal_2
        bal_2 = old_bal
        day += 1
        if new_bal == 1000000:
            winning_balance = {'Deposit 1': deposit_1,
                               'Deposit 2': deposit_2,
                               'Days': day}
            return winning_balance


def check_balances(end_num):
    winners = []
    for i in range(1, end_num):
        for j in range(1, end_num):
            deposit_1 = i
            deposit_2 = j
            if gen_sequence(deposit_1, deposit_2) != None:
                winners.append(gen_sequence(deposit_1, deposit_2))
    return winners


if __name__ == '__main__':
    winners = check_balances(10000)
    max_days = 0
    for entry in winners:
        if entry['Days'] > max_days:
            max_days = entry['Days']
            winner = entry
    print(winner)
