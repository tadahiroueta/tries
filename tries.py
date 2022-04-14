import click
from features import addWord, deleteWord, isValidWord, getAutofill, displayTrie

def exitFailure():
  print('Invalid command')
  exit()

def requireWord(word):
  if word is None:
    print('Missing word argument')
    exit()

@click.command()
@click.argument('call')
@click.argument('word', required=False)
def tries(call, word=None):
  '''
  Carries out the CLI user commands.

  add [word] - add specified word to trie
  
  delete [word] - delete specified word to trie

  search [word] - returns whether the word is valid in the trie

  autofill [word] - returns the possible words that complete [word] in the trie

  display - displays the current state of the trie

  '''
  if call == 'add':
    requireWord(word)
    addWord(word)
    print(f"'{word}' added to trie")

  elif call == 'delete':
    requireWord(word)
    if deleteWord(word):
      print(f"'{word}' deleted from trie")

    else: 
      print(f"'{word}' could not be deleted; it was not present in the trie")

  elif call == 'search':
    requireWord(word)
    print(f"'{word}' is {'valid' if isValidWord(word) else 'invalid'}")

  elif call == 'autofill':
    requireWord(word)
    for autofill in getAutofill(word):
      print(autofill)

  elif call == 'display':
    displayTrie()

  elif call == 'test':
    pass

  else:
    exitFailure()
