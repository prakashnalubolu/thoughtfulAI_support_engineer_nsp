from typing import Union

Number = Union[int, float]

def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    """
    Return which stack a package should go to based on dimensions (cm) and mass (kg).
    Rules:
    - Bulky: volume ≥ 1_000_000 cm³ OR any dimension ≥ 150 cm
    - Heavy: mass ≥ 20 kg
    - DISPATCH:
        * "REJECTED" if both bulky and heavy
        * "SPECIAL"  if either bulky or heavy (but not both)
        * "STANDARD" otherwise
    """
    #Basic input validation (non-negative numbers)
    dims = (width, height, length)
    if any(d < 0 for d in dims) or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative numbers.")

    volume = width * height * length
    bulky = volume >= 1_000_000 or any(d >= 150 for d in dims)
    heavy = mass >= 20

    return "REJECTED" if (bulky and heavy) else ("SPECIAL" if (bulky or heavy) else "STANDARD")


# ------------ Simple tests ------------
def _run_smoke_tests():
    tests = [
        # STANDARD
        ((10, 10, 10, 1), "STANDARD"),
        ((149.9, 149.9, 149.9, 19.99), "STANDARD"),

        # SPECIAL by bulky (dimension)
        ((150, 10, 10, 1), "SPECIAL"),
        # SPECIAL by bulky (volume)
        ((100, 100, 100, 1), "SPECIAL"),  # 1_000_000 cm³ exactly
        # SPECIAL by heavy
        ((50, 50, 50, 20), "SPECIAL"),     # heavy threshold

        # REJECTED (both)
        ((150, 150, 1, 20), "REJECTED"),
        ((100, 100, 100, 20), "REJECTED"), # bulky by volume + heavy
    ]

    for (args, expected) in tests:
        out = sort(*args)
        assert out == expected, f"Input {args}: expected {expected}, got {out}"

if __name__ == "__main__":
    _run_smoke_tests()
    print("All tests passed.")
