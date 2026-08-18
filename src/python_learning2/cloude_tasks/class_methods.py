# from itertools import zip_longest
from pathlib import Path

from python_learning2.exceptions.examples import InsufficientFundsError, InvalidAmountError


class BankAccount:
    """Create Bank account and provide functionality for manage
    
    Args:
        owner: account name
        [balance]: start value of balance for new account

    Raises:
        InsufficientFundsError: if not enough balance for operation
        InvalidAmountError: if incorrect value during operation
    """
    bank_name: str = 'PrivatBank'
    
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
        
    def deposit(self, amount: float | str) -> None:
        """Increase account balance

        Args:
            amount (float | str): amount to increase balance
            
        Raises:
            InvalidAmountError: if incorrect value during operation
        """
        amount = BankAccount.validate_amount(amount)
        self.balance += amount
    
    def withdraw(self, amount: float | str) -> None:
        """Decrease account balance

        Args:
            amount (float | str): amount to decrease balance
            
        Raises:
            InsufficientFundsError: if not enough balance 
            InvalidAmountError: if incorrect value during operation
        """
        amount = BankAccount.validate_amount(amount)
        if self.balance < amount:
            raise InsufficientFundsError(self.owner, amount, self.balance)
        else:
            self.balance -= amount
            
    @classmethod
    def from_zero(cls, owner: str) -> 'BankAccount':
        """Create new BankAccount instance with default(0.0) balance

        Args:
            owner (str): account name

        Returns:
            BankAccount: BankAccount instance
        """
        return cls(owner)
    
    @staticmethod
    def validate_amount(amount: float | str) -> float:
        """Validate amount for operation

        Args:
            amount (float | str): Value for validation

        Raises:
            InvalidAmountError: if incorrect value for operation

        Returns:
            float: validated amount
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError) as e:
            raise InvalidAmountError() from e
        if amount <= 0:
            raise InvalidAmountError()

        return amount

def save_accounts(accounts: list[BankAccount], path: Path) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        for account in accounts:
            file.write(f'{','.join([account.owner, str(account.balance)])}\n')
            
def load_accounts(path: Path) -> list[BankAccount]:
    accounts: list[BankAccount] = []
    with open(path, encoding='utf-8') as file:
        for line in file:
            owner, balance = line.strip().split(',')
            accounts.append(BankAccount(owner, float(balance)))
    return accounts     
    
if __name__ == "__main__":
    # BASE_DIR: Path = Path.cwd()
    # TARGET_DIR: Path = BASE_DIR / 'src' / 'python_learning2' / 'cloude_tasks' 
    # TARGET_FILE: Path = TARGET_DIR / 'bank_accounts.txt'

    # account_owner_names: list[str] = ['Sergey', 'Igor', 'Tanya', 'Mikhael', 'Lena', 'Mark']
    # account_owner_balances: list[float] = [26, 34, 76, 23, 65]
    
    # account_owners: list[BankAccount] = []
    
    # # zip_longest об'єднає списки. Якщо елемент відсутній, він підставить None
    # for name, balance in zip_longest(account_owner_names, account_owner_balances, fillvalue=None):
    #     # Спочатку перевіряємо, чи взагалі є ім'я
    #     if name is not None:
    #         if balance is not None:
    #             account_owners.append(BankAccount(name, balance))
    #         else:
    #             account_owners.append(BankAccount.from_zero(name))
    #             print(f'No balance provided for {name}, created with zero balance.')
    #     else:
    #         # Цей блок спрацює, якщо балансів більше, ніж імен
    #         print("Знайдено баланс без власника рахунку!")
            
    
    # save_accounts(account_owners, TARGET_FILE) # will create txt file with records
    
    # account_owners = load_accounts(TARGET_FILE)
    # for account in account_owners:
    #     print(f'{account.owner} - {account.balance}')
    
    first_acc = BankAccount('Roman', 25)
    try:
        first_acc.deposit(25)
        first_acc.withdraw('30')
        first_acc.withdraw('d30')
        first_acc.deposit(5)
        first_acc.withdraw(30)
    except InsufficientFundsError as e:
        print(f'Помилка: {e}')
    except InvalidAmountError as e:
        print(f'Помилка: {e}')
    except RuntimeError as e:
        print(f'Невідома помилка: {e}')
    else:
        print('Операція успішна!')
    finally:
        print('Операція оброблена!')
        
        
    # second_acc = BankAccount.from_zero('Olena')
    # second_acc.deposit(20)
    # try:
    #     second_acc.withdraw(50)
    # except RuntimeError as e:
    #     print(f'Operation(withdraw) was failed. {e}')