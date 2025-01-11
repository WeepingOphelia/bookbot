def open_file():
  with open("books/frankenstein.txt") as f:
      file_contents = f.read()
      return (file_contents)

def count_words(text):
   words = text.split()
   return len(words)

def character_count(text):
  characters = {}
  for i in text.lower():
    if i in characters:
         characters[i] += 1
    else:
         characters[i] = 1
  return characters

def print_report(n_words, c_dict):
  def sort_on(dict):
    return dict["num"]
  c_list = []
  for key in c_dict:
     c_list.append({"char" : key, "num" : c_dict[key]})
  c_list.sort(reverse=True, key=sort_on)

  print(f"books/frankenstein.txt has {n_words} words.")
  print("")
  print("A character breakdown is as follows:")
  for item in c_list:
    if item["char"].isalpha():
      print(f"The '{item["char"]}' character is present {item["num"]} time(s).")
  print("")
  print("This concludes our exciting report of books/frankenstein.txt")
     
  pass
   

def main():
   text = open_file()
   word_count = count_words(text)
   character_dict = character_count(text)
   print_report(word_count, character_dict)
   pass


main()