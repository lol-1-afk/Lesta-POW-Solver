from dataclasses import dataclass


@dataclass
class Algorithm:
    extension: str
    name: str
    resourse: str
    version: int


@dataclass
class Challenge:
    algorithm: Algorithm
    complexity: int
    random_string: str
    timestamp: int
    type: str
