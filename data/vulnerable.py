import sqlite3

def vulnerable_function(user_input):
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
  cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25)")

  # 脆弱性: ユーザー入力を直接SQLクエリに含めている
  query = f"SELECT * FROM users WHERE name = '{user_input}'"
  cursor.execute(query)
  rows = cursor.fetchall()

  for row in rows:
    print(row)

  conn.close()

if __name__ == "__main__":
  user_input = input("Enter a name: ")
  vulnerable_function(user_input)
