"""Your Human in One Word — entrypoint.

Reads the single word from entry.txt and prints it.
"""

from pathlib import Path


def load_word(path: Path) -> str:
    word = path.read_text(encoding="utf-8").strip()
    if not word:
        raise ValueError("entry.txt is empty — one word is required")
    return word


def main() -> None:
    word = load_word(Path(__file__).with_name("entry.txt"))
    print(word)


if __name__ == "__main__":
    main()
