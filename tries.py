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
  This carries out the CLI user commands.
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
