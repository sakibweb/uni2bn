if 'json' not in globals():
    import json
# Function to convert Unicode Bangla text to Bangla characters
def uni2bn(text):
    # Bangla to Unicode mapping
    maps = {
        '0': '\u09E6', '1': '\u09E7', '2': '\u09E8', '3': '\u09E9', '4': '\u09EA',
        '5': '\u09EB', '6': '\u09EC', '7': '\u09ED', '8': '\u09EE', '9': '\u09EF',
        '+': '+', '-': '-', '*': '*', '/': '/', '%': '%', '=': '=', '<': '<', '>': '>',
        '!': '!', '@': '@', '#': '#', '$': '$', '^': '^', '&': '&', '(': '(', ')': ')',
        '[': '[', ']': ']', '{': '{', '}': '}', '|': '|', '\\': '\\', '`': '`', '~': '~',
        '\'': '\'', '"': '"', ':': ':', ';': ';', ',': ',', '.': '.', '?': '?', '_': '_',
        '৳': '\u09F3',
        '০': '\u09E6', '১': '\u09E7', '২': '\u09E8', '৩': '\u09E9', '৪': '\u09EA',
        '৫': '\u09EB', '৬': '\u09EC', '৭': '\u09ED', '৮': '\u09EE', '৯': '\u09EF',
        'অ': '\u0985', 'আ': '\u0986', 'ই': '\u0987', 'ঈ': '\u0988', 'উ': '\u0989',
        'ঊ': '\u098A', 'ঋ': '\u098B', 'এ': '\u098F', 'ঐ': '\u0990', 'ও': '\u0993',
        'ঔ': '\u0994', 'ক': '\u0995', 'খ': '\u0996', 'গ': '\u0997', 'ঘ': '\u0998',
        'ঙ': '\u0999', 'চ': '\u099A', 'ছ': '\u099B', 'জ': '\u099C', 'ঝ': '\u099D',
        'ঞ': '\u099E', 'ট': '\u099F', 'ঠ': '\u09A0', 'ড': '\u09A1', 'ঢ': '\u09A2',
        'ণ': '\u09A3', 'ত': '\u09A4', 'থ': '\u09A5', 'দ': '\u09A6', 'ধ': '\u09A7',
        'ন': '\u09A8', 'প': '\u09AA', 'ফ': '\u09AB', 'ব': '\u09AC', 'ভ': '\u09AD',
        'ম': '\u09AE', 'য': '\u09AF', 'র': '\u09B0', 'ল': '\u09B2', 'শ': '\u09B6',
        'ষ': '\u09B7', 'স': '\u09B8', 'হ': '\u09B9', 'ড়': '\u09DC', 'ঢ়': '\u09DD',
        'য়': '\u09DF', 'ৎ': '\u09CE', 'ং': '\u0982', 'ঃ': '\u0983', 'ঁ': '\u0981',
        'া': '\u09BE', 'ি': '\u09BF', 'ী': '\u09C0', 'ু': '\u09C1', 'ূ': '\u09C2',
        'ৃ': '\u09C3', 'ৄ': '\u09C4', 'ে': '\u09C7', 'ৈ': '\u09C8', 'ো': '\u09CB',
        ' ্': '\u09CD', 'ৗ': '\u09D7', '়': '\u09BC', 'ঽ': '\u09BD', '্র': '\u09CD\u09B0'
    }
    # List to hold characters to be combined
    combined_chars = []
    # Resulting Bangla text
    result = ""
    for char in text:
        if char in maps:
            # If the character is in the mapping
            converted_char = maps[char]
            # Handle combining characters
            if char == "্":  # Halant
                # Combine with the previous character
                combined_chars[-1] += converted_char
            else:
                # Append the converted character to the result
                result += converted_char
                # If there are any combined characters, add them to the result
                result += "".join(combined_chars)
                # Clear the list of combined characters
                combined_chars = []
        else:
            # If the character is not in the mapping, append it directly to the result
            result += char
    return result