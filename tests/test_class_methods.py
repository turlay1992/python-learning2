import pytest

from python_learning2.cloude_tasks.class_methods import BankAccount
from python_learning2.exceptions.examples import InsufficientFundsError, InvalidAmountError


def test_validate_amount_rejects_negative() -> None:
    with pytest.raises(InvalidAmountError):
        BankAccount.validate_amount(-5)


def test_insufficient_funds_rejects_negative() -> None:
    with pytest.raises(InsufficientFundsError):
        account: BankAccount = BankAccount.from_zero("Roman")
        account.withdraw(20)
