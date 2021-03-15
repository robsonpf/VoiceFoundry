import vanitynumber

def is_valid_word(word: str) -> bool:
  with open('dictionary.txt', 'r') as file:
    dict_words = file.read().splitlines()
    if word in dict_words:
      return True

    else:
      return False

def is_acronym(word: str) -> bool:
  vowels = ['a', 'e', 'i', 'o', 'u']

  if word[1] in vowels:
    return False

  return True

wordifications = vanitynumber.all_wordifications('1-407-522-8994')
# print(wordifications)

best_results = []

for vanity_number in wordifications:
  word = vanity_number[6:].lower()

  if is_valid_word(word):
    # print(word)
    best_results.append(vanity_number)
  else:
    first_word = word[0:3]
    second_word = word[3:]

    if (is_valid_word(first_word) and (not is_acronym(first_word))) and is_valid_word(second_word):
      best_results.append(vanity_number)

print(best_results)
