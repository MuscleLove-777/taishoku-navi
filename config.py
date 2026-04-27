"""退職代行ナビ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "退職代行ナビ"
BLOG_DESCRIPTION = "退職代行サービスの徹底比較・体験談・トラブル防止策まで網羅。弁護士法人・労働組合・民間業者の違い、料金相場、有給消化の交渉まで完全ガイド。"
BLOG_URL = "https://musclelove-777.github.io/taishoku-navi/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/taishoku-navi"

TARGET_CATEGORIES = [
    "退職代行サービス比較",
    "退職代行の選び方",
    "退職時のトラブル対処",
    "パワハラ・ブラック企業対策",
    "退職金・有給休暇",
    "退職後の手続き",
    "失業保険・再就職",
]

THEME = {
    "primary": "#2c3e50",
    "accent": "#e74c3c",
    "gradient_start": "#2c3e50",
    "gradient_end": "#e74c3c",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
