from datetime import datetime
from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_details: str) -> str | None:
    """Обработка данных карты или счета"""
    if (
        "Visa" in payment_details
        or "Maestro" in payment_details
        or "MasterCard" in payment_details
    ):
        card_details = get_mask_card_number(payment_details[-16:])
        return f"{payment_details[:-17]} {card_details}"
    elif "Счет" in payment_details:
        account_details = get_mask_account(payment_details[-20:])
        return f"{payment_details[:-21]} {account_details}"
    else:
        return None


print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(date_info: str) -> Any | None:
    """Преобразование даты в формат dd.mm.YYYY"""
    parsed_date = datetime.strptime(date_info[:10], "%Y-%m-%d").date()
    formated_date = parsed_date.strftime("%m.%d.%Y")
    return formated_date


print(get_date("2024-03-11T02:26:18.671407"))
