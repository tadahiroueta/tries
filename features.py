from nodes import *

rootNode = fetchNode(12)

def getId(node):
  (id, character, parentId, validWord) = node
  return id

def getCharacter(node):
  (id, character, parentId, validWord) = node
  return character

def getParentId(node):
  (id, character, parentId, validWord) = node
  return parentId

def isLastCharacter(node):
  (id, character, parentId, validWord) = node
  return validWord

def fetchParent(childId):
  (id, character, parentId, validWord) = fetchNode(childId)
  return fetchNode(parentId)

def hasChildren(parentId):
  return len(fetchChildren(parentId)) > 0

def getLastNode(word):
  wordSnip = word
  node = rootNode
  while len(wordSnip) > 0:
    firstLetter = wordSnip[0]
    if not hasChildren(getId(node)):
      return False
    node = fetchChild(getId(node), firstLetter)

    wordSnip = wordSnip[1:]
  return node

def getWord(node, wordSnip):
  character = getCharacter(node)
  if character is None:
    return wordSnip

  return getWord(fetchParent(getId(node)), character + wordSnip)

def getWords(node, words):
  newWords = words.copy()
  if isLastCharacter(node):
    newWords.append(getWord(node, ''))

  for child in fetchChildren(getId(node)):
    newWords += getWords(child, [])

  return newWords

def displayChildren(parentId, prefix):
  for child in fetchChildren(parentId):
    print(prefix + "└──" + getCharacter(child))
    displayChildren(getId(child), prefix + "   ")

def addWord(word):
  wordSnip = word
  node = rootNode
  while len(wordSnip) > 0:
    firstLetter = wordSnip[0]
    try:
      node = fetchChild(getId(node), firstLetter)

    except IndexError:
      insertNode(firstLetter, getId(node), False)
      node = fetchChild(getId(node), firstLetter)

    wordSnip = wordSnip[1:]

  makeNodeValidWord(getId(node))

def deleteWord(word):
  if not isValidWord(word):
    return False

  node = getLastNode(word)
  makeNodeInvalidWord(getId(node))
  parentNode = None
  while getCharacter(node) != '':
    if hasChildren(getId(node)):
      return True

    parentNode = fetchParent(getId(node))
    deleteNode(getId(node))
    node = parentNode

def isValidWord(word):
  wordSnip = word
  node = rootNode
  while len(wordSnip) > 0:
    firstCharacter = wordSnip[0]
    if not hasChildren(getId(node)):
      return False
   
    try:
      node = fetchChild(getId(node), firstCharacter)
    
    except IndexError:
      return False
      
    wordSnip = wordSnip[1:]

  return isLastCharacter(node)

def getAutofill(word):
  return getWords(getLastNode(word), [])

def displayTrie():
  displayChildren(getId(rootNode), '')
