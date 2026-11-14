"""Política de status das reservas."""

from __future__ import annotations


def is_billable(status: str) -> bool:
    """Indica se a reserva entra nos totais financeiros e de noites."""
    #return status != "CANCELLED"

    """
    since, according to README.md, the only billable status is
    "CONFIRMED", this shall return True only for that status.
    """
    return status == "CONFIRMED"
