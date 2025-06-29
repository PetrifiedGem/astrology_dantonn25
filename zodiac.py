from datetime import datetime

ZODIAC_DATES = [
    ("Capricorn", (1, 1), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
    ("Capricorn", (12, 22), (12, 31))
]

def get_zodiac_sign(birth_date_str: str) -> str:
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    for sign, start, end in ZODIAC_DATES:
        start_date = datetime(birth_date.year, *start)
        end_date = datetime(birth_date.year, *end)
        if start_date <= birth_date <= end_date:
            return sign
    return "Unknown"
