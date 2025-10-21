from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Assembler:
    @classmethod
    def create(cls) -> Assembler:
        return cls()

    def assemble(self, _assembly: Iterable[str]) -> Iterable[str]:
        return []  # TODO: your work for Project 6 starts here
