"""Simple processing functions for the starter package."""

from collections.abc import Iterable


def total_count(counts: Iterable[int]) -> int:
    """Return the sum of a sequence of example counts."""
    return sum(counts)
