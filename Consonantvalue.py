def solve(s):
    vowels = 'aeiou'
    consonant_values = {char: ord(char) - ord('a') + 1 for char in 'bcdfghjklmnpqrstvwxyz'}

    consonant_substrings = []
    current_substring = ""
    highest_value = 0

    for char in s:
        if char in consonant_values:
            current_substring += char
        else:
            if current_substring:
                value = sum(consonant_values[c] for c in current_substring)
                consonant_substrings.append(value)
                highest_value = max(highest_value, value)
                current_substring = ""

    if current_substring:
        value = sum(consonant_values[c] for c in current_substring)
        consonant_substrings.append(value)
        highest_value = max(highest_value, value)

    return highest_value

# Test cases
print(solve("zodiacs"))   #26
print(solve("strength"))  #57
