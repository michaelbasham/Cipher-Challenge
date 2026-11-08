#!/usr/bin/env python3
"""Simple Caesar Cipher encoder and decoder."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar(text, shift, encode=True):
    """Shift letters in text by shift positions.

    Args:
        text: The string to encode or decode.
        shift: Number of positions to shift (0-25).
        encode: True to shift forward (encode), False to shift backward (decode).

    Returns:
        The transformed string.
    """
    shift = shift % 26
    if not encode:
        shift = -shift

    result = []
    for ch in text:
        if ch.isalpha():
            is_upper = ch.isupper()
            base = ALPHABET.index(ch.upper())
            new_index = (base + shift) % 26
            new_ch = ALPHABET[new_index]
            result.append(new_ch if is_upper else new_ch.lower())
        else:
            # Non-letter characters are left unchanged
            result.append(ch)

    return "".join(result)


def encode(text, shift):
    """Encode text using a Caesar cipher with the given shift."""
    return caesar(text, shift, encode=True)


def decode(text, shift):
    """Decode Caesar-ciphered text using the given shift."""
    return caesar(text, shift, encode=False)


def letter_to_shift(letter):
    """Return the shift amount implied by mapping 'A' to the given letter.

    For example, mapping A->B gives shift 1, and A->F gives shift 5.
    """
    letter = letter.strip().upper()
    if len(letter) != 1 or letter not in ALPHABET:
        raise ValueError("Please enter a single letter A-Z.")
    return ALPHABET.index(letter)  # A -> 0, B -> 1, ..., F -> 5, ...


def main():
    print("=== Caesar Cipher ===")
    mode = input("Encode or Decode? (e/d): ").strip().lower()

    if mode not in ("e", "d", "encode", "decode"):
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    text = input("Enter the text: ")

    try:
        if mode.startswith("e"):
            mapping = input("Which letter does A map to? (e.g. B for shift 1): ")
            shift = letter_to_shift(mapping)
        else:
            mapping = input("Which ciphertext letter corresponds to A? (e.g. B): ")
            shift = letter_to_shift(mapping)
    except ValueError as exc:
        print(exc)
        return

    if mode.startswith("e"):
        result = encode(text, shift)
        print(f"Encoded: {result}")
    else:
        result = decode(text, shift)
        print(f"Decoded: {result}")


if __name__ == "__main__":
    main()
