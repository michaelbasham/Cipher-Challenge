#!/usr/bin/env python3
"""Letter frequency analysis for a piece of text."""

import os
import sys

import matplotlib.pyplot as plt

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Text file bundled with the project, used by default when the user answers yes.
TEXT_FILE = "textFA.txt"


def clear_terminal():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def read_text_from_file(path):
    """Return the contents of the text file at path."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# Approximate letter frequencies in English (as percentages, 2 decimal places).
ENGLISH_FREQUENCIES = {
    "A": 8.20,
    "B": 1.50,
    "C": 2.80,
    "D": 4.30,
    "E": 12.70,
    "F": 2.20,
    "G": 2.00,
    "H": 6.10,
    "I": 7.00,
    "J": 0.15,
    "K": 0.77,
    "L": 4.00,
    "M": 2.40,
    "N": 6.70,
    "O": 7.50,
    "P": 1.90,
    "Q": 0.10,
    "R": 6.00,
    "S": 6.30,
    "T": 9.10,
    "U": 2.80,
    "V": 0.98,
    "W": 2.40,
    "X": 0.15,
    "Y": 2.00,
    "Z": 0.07,
}


def analyze_frequency(text):
    """Count how many times each letter A-Z appears in text.

    Returns a dict mapping each letter to its count.
    """
    counts = {letter: 0 for letter in ALPHABET}
    total = 0

    for ch in text.upper():
        if ch in ALPHABET:
            counts[ch] += 1
            total += 1

    return counts, total


def plot_frequency(counts, total):
    """Display side-by-side bars comparing text frequency vs English frequency.

    For each letter there are two adjacent bars:
      * blue = percentage in the entered text
      * red  = expected frequency in the English language
    """
    letters = list(counts.keys())
    text_percents = [
        (counts[letter] / total * 100) if total > 0 else 0.0 for letter in letters
    ]
    english_percents = [ENGLISH_FREQUENCIES[letter] for letter in letters]

    x = range(len(letters))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 6))

    bars_text = ax.bar(
        [pos - width / 2 for pos in x],
        text_percents,
        width,
        label="Your text",
        color="steelblue",
        edgecolor="black",
    )
    bars_english = ax.bar(
        [pos + width / 2 for pos in x],
        english_percents,
        width,
        label="English",
        color="indianred",
        edgecolor="black",
        alpha=0.8,
    )

    # Label each text bar with its percentage (only when count > 0)
    for bar in bars_text:
        height = bar.get_height()
        if height > 0:
            ax.annotate(
                f"{height:.2f}%",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=7,
            )

    ax.set_xticks(list(x))
    ax.set_xticklabels(letters)
    ax.set_ylabel("Frequency (%)")
    ax.set_title("Letter Frequency: Your Text vs English")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    highest = max(max(text_percents), max(english_percents))
    ax.set_ylim(0, highest * 1.25 if highest > 0 else 15)
    plt.tight_layout()
    plt.show()


def main():
    clear_terminal()
    print("=== Letter Frequency Analysis ===")

    # Prefer the text file bundled with the project.
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), TEXT_FILE)

    answer = input(f"Use the text from '{TEXT_FILE}'? (y/n): ").strip().lower()

    if answer in ("y", "yes"):
        try:
            text = read_text_from_file(default_path)
        except OSError as exc:
            print(f"Could not read '{TEXT_FILE}': {exc}")
            return
    else:
        # Read from stdin until EOF (Ctrl-D, or Ctrl-Z then Enter on Windows)
        # so text can be typed or pasted directly.
        print("Type or paste your text, then press Ctrl-D (Ctrl-Z on Windows) to finish:")
        text = sys.stdin.read()

    counts, total = analyze_frequency(text)

    print("\nLetter frequencies:")
    print(f"{'Letter':<8} {'Count':<8} {'Percent':<8}")
    print("-" * 24)

    for letter in ALPHABET:
        count = counts[letter]
        percent = (count / total * 100) if total > 0 else 0.0
        print(f"{letter:<8} {count:<8} {percent:<8.2f}%")

    print(f"\nTotal letters counted: {total}")

    plot_frequency(counts, total)


if __name__ == "__main__":
    main()
