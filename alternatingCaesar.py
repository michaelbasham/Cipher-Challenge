#!/usr/bin/env python3
"""Alternating Caesar Cipher encoder and decoder."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def alternating_caesar(text, odd_shift, even_shift, encode=True):
    """Shift letters in text by different shifts for odd and even positions.

    Args:
        text: The string to encode or decode.
        odd_shift: Number of positions to shift for letters in odd positions (1-indexed).
        even_shift: Number of positions to shift for letters in even positions (1-indexed).
        encode: True to shift forward (encode), False to shift backward (decode).

    Returns:
        The transformed string.
    """
    odd_shift = odd_shift % 26
    even_shift = even_shift % 26
    if not encode:
        odd_shift = -odd_shift
        even_shift = -even_shift

    result = []
    for i, ch in enumerate(text):
        if ch.isalpha():
            is_upper = ch.isupper()
            base = ALPHABET.index(ch.upper())

            # Use 1-indexed positions for odd/even determination
            position = i + 1
            if position % 2 == 1:
                shift = odd_shift
            else:
                shift = even_shift

            new_index = (base + shift) % 26
            new_ch = ALPHABET[new_index]
            result.append(new_ch if is_upper else new_ch.lower())
        else:
            # Non-letter characters are left unchanged
            result.append(ch)

    return "".join(result)


def encode(text, odd_shift, even_shift):
    """Encode text using an alternating Caesar cipher with different shifts for odd/even positions."""
    return alternating_caesar(text, odd_shift, even_shift, encode=True)


def decode(text, odd_shift, even_shift):
    """Decode alternating Caesar-ciphered text using different shifts for odd/even positions."""
    return alternating_caesar(text, odd_shift, even_shift, encode=False)


def main():
    print("=== Alternating Caesar Cipher ===")
    mode = input("Encode or Decode? (e/d): ").strip().lower()

    if mode not in ("e", "d", "encode", "decode"):
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    text = input("Enter the text: ")

    try:
        odd_shift = int(input("Shift for odd-positioned letters: "))
        even_shift = int(input("Shift for even-positioned letters: "))
    except ValueError:
        print("Please enter valid integers for shift values.")
        return

    if mode.startswith("e"):
        result = encode(text, odd_shift, even_shift)
        print(f"Encoded: {result}")
    else:
        result = decode(text, odd_shift, even_shift)
        print(f"Decoded: {result}")


if __name__ == "__main__":
    main()