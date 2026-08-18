
class InsufficientFundsError(Exception):
    """Raise if not enough balance for operation

    Args:
        owner: account name
        requested: requested amount for description of issue
        available: available amount for description of issue
    """
    def __init__(self, owner: str, requested: float, available: float) -> None:
        self.owner = owner
        self.requested = requested
        self.available = available
        super().__init__(
            f"{owner}: недостатньо коштів (потрібно {requested}, є {available})"
        )

class InvalidAmountError(Exception):
    """Raise if value type is not number or number <= 0  
    """
    def __init__(self) -> None:
        super().__init__("Сума ≤ 0")


if __name__ == "__main__":
    def divide_10_on_value(value: int) -> float:
        try:
            result = 10 / value
            print('TRY block')
            return result
        except ZeroDivisionError:
            print('Ділити на нуль заборонено')
            print('EXCEPT block')
            return 0
        else:
            # else виконується, ТІЛЬКИ якщо try пройшов без винятку і без return
            print(f'Result: {result}')
            print('ELSE block')
            return result
        finally:
            # finally виконується завжди
            print('FINALLY block')
            print('Operation completed')

    print(divide_10_on_value(0))
    print('#' * 12)
    print(divide_10_on_value(5))

    # raw_input: str = input('Input your age:\n')
    # try:
    #     age = int(raw_input)
    # except ValueError as e:
    #     raise ValueError(f"Некоректний вік: {raw_input!r}") from e