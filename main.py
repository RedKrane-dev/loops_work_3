import string

def main():
    text = input("Введите текст:\n")
    text_low = text.lower()

    vowels = "аеёиоуыэюя"
    simbols = string.punctuation

    cleaned_chars = []
    for char in text_low:
        if char in simbols:
            cleaned_chars.append(" ")
        else:
            cleaned_chars.append(char)
    cleaned_text = "".join(cleaned_chars)
    # 1
    words = cleaned_text.split()
    word_count = len(words)

    # 2
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # 3
    vowel_count = 0
    for char in text_low:
        if char in vowels:
            vowel_count += 1

    # 4
    words_count_dict = {}
    for word in words:
        if word in words_count_dict:
            words_count_dict[word] += 1
        else:
            words_count_dict[word] = 1

    print(
        f'Количество слов в тексте: {word_count}',
        f'Самое длинное слово: {longest_word if longest_word else "(нет слов)"}',
        f'Количество гласных букв в тексте: {vowel_count}',
        f'Частота слов в тексте:',
        sep='\n'
    )
    for word, count in words_count_dict.items():
        print(f"\t{word}: {count}")

if __name__ == "__main__":
    main()
