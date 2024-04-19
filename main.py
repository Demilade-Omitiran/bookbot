def count_words(string):
  return len(string.split())

def count_letters(string):
  letter_count_dict = {}

  for character in string:
    if character.lower() in letter_count_dict:
      letter_count_dict[character.lower()] += 1
    elif character.isalpha():
      letter_count_dict[character.lower()] = 1

  return letter_count_dict

def print_report(string):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{count_words(string)} words found in the document\n")

  letter_count_dict = {k: v for k, v in sorted(count_letters(string).items(), key=lambda x: x[1], reverse = True)}
  
  for key in letter_count_dict:
    print(f"The '{key}' character was found {letter_count_dict[key]} times")
  
  print("--- End report ---")

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print_report(file_contents)

main()