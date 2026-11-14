"""Conversão de valores para BRL."""

from __future__ import annotations

from decimal import Decimal


def convert_to_brl(amount: Decimal, currency: str, rates: dict[str, Decimal]) -> Decimal:
    """Converte um valor na moeda informada para BRL usando a taxa da tabela."""
    rate = rates[currency]
    # return Decimal(str(float(amount) / float(rate)))

    """
    once receiving N DLR, the BLR conversion consists in
    N * (rate[DLR] / rate[BLR]). since rate[BLR] is always 1,
    this can also simplify to N * rate[DLR].

    for handling a possible case where rate[BLR] is not 1,
    the formula is kept as N * (rate[DLR] / rate[BLR]).
    """
    return Decimal(str(float(amount) * float(rate) / float(rates["BRL"])))
