from mysql import connector

database = connector.connect(
  host="trie-db.c6ymrxybsj2r.us-east-2.rds.amazonaws.com",
  user="admin",
  password="trie-db-admin-password271828",
  database="trie-schema"
)

def query(command):
  cursor = database.cursor()
  cursor.execute(command)
  return cursor.fetchall()

def commit(command):
  cursor = database.cursor()
  cursor.execute(command)
  database.commit()

def fetchNode(id):
  return query(f"SELECT * FROM `trie-schema`.nodes WHERE id = {id};")[0]

def fetchChildren(parentId):
  return query(f"SELECT * FROM `trie-schema`.nodes WHERE parent_id = {parentId};")

def fetchChild(parentId, character):
  return query(f"SELECT * FROM `trie-schema`.nodes WHERE parent_id = {parentId} AND `character` = '{character}';")[0]

def insertNode(character, parentId, isValidWord):
  commit(f"INSERT INTO `trie-schema`.nodes (`character`, `parent_id`, `valid_word`) VALUES ('{character}', {parentId}, {isValidWord});")

def deleteNode(id):
  commit(f"DELETE FROM `trie-schema`.nodes WHERE id = {id};")

def makeNodeValidWord(id):
  commit(f"UPDATE `trie-schema`.nodes SET valid_word = 1 WHERE id = {id};")

def makeNodeInvalidWord(id):
  commit(f"UPDATE `trie-schema`.nodes SET valid_word = 0 WHERE id = {id};")
