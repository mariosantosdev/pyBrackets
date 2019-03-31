'''
Module usage to remove words and brackets of a string.
'''
import re

def clearString(text, brackets='()[]'):
    count = [0] * (len(brackets) // 2)
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close
                if count[kind] < 0:
                    count[kind] = 0
                else:
                    break
        else:
            if not any(count):
                saved_chars.append(character)
    text = ''.join(saved_chars).strip()
    text = re.sub(' +', ' ', text)
    text = text.lstrip("'")

    return text
