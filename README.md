Function: sort(width, height, length, mass) -> str
Returns: "STANDARD", "SPECIAL", or "REJECTED".
Rules (inclusive)
Bulky if:
width * height * length >= 1_000_000 cm³, or
any dimension >= 150 cm
Heavy if: mass >= 20 kg

Dispatch:
both bulky & heavy -> REJECTED
either bulky or heavy -> SPECIAL
neither -> STANDARD

Use
from sort import sort

print(sort(10, 10, 10, 1))        # STANDARD
print(sort(150, 10, 10, 1))       # SPECIAL (bulky by dimension)
print(sort(100, 100, 100, 1))     # SPECIAL (bulky by volume)
print(sort(50, 50, 50, 20))       # SPECIAL (heavy)
print(sort(150, 150, 1, 20))      # REJECTED (both)

Tests
pytest -q
# or
python sort.py  # runs smoke tests, prints "All tests passed."
