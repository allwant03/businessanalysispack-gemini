import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
MODEL = os.getenv("WAFERPACK_MODEL", "gemini-3.6-flash")
ADMIN_CODE = os.getenv("ADMIN_CODE", "")
DART_API_KEY = os.getenv("DART_API_KEY", "")


def is_configured() -> bool:
    return bool(GEMINI_API_KEY and TAVILY_API_KEY)
