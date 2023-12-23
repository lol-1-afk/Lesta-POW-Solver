Lesta Proof of Work Solver
This Python script, pow_solver.py, provides a solution to the POW challenge presented by the Lesta web service. The challenge is obtained through an API call to "https://lesta.ru/id/signin/challenge/?type=pow". The solution involves repeatedly hashing a combination of challenge parameters until a valid prefix is found.

Original JS script: https://pastebin.com/tRETy3yZ

Usage example:
```python
from models import Challenge, Algorithm
from pow_solver import LestaPowSolver
import requests

# Make an API call to get the PoW challenge
# Referer must be this one, site doesnt accept any other
HEADERS = {
    "Referer": "https://lesta.ru/id/signin/"
}

response = requests.get("https://lesta.ru/id/signin/challenge/?type=pow", headers=HEADERS).json()

# Create a Challenge object
POW = Challenge(
    algorithm=Algorithm(**response["pow"]["algorithm"]),
    complexity=response["pow"]["complexity"],
    random_string=response["pow"]["random_string"],
    timestamp=response["pow"]["timestamp"],
    type=response["pow"]["type"]
)

# Initialize the solver and solve the challenge
solver = LestaPowSolver(POW)
solution = solver.solve_challenge()
print(solution)
```
