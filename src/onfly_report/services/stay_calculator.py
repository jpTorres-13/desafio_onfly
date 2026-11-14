"""Cálculo de noites ocupadas."""

from __future__ import annotations

from datetime import date


def calculate_room_nights(checkin: date, checkout: date, rooms: int) -> int:
    """Calcula noites de quarto: diferença de dias (não inclusiva) vezes quartos."""
    #return (checkout.day - checkin.day) * rooms

    """
    according to README.md, the checkin date is calculated by
    the difference in days between the checkout and checkin dates
    multiplied to the number of rooms.
    
    the calculation above does not consider the possibility of
    checkin and checkout in different months or years.
    """
    return (checkout - checkin).days * rooms
