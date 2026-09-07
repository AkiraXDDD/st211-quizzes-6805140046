from bank import BankAccount

def test_deposit_increase_balance():
    account = BankAccount(balance = 100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_withdraw_decrease_balance():
    account = BankAccount(balance = 150)
    new_balance = account.withdraw(50)
    assert new_balance == 100