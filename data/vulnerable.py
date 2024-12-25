import sqlite3

def create_table_and_insert_data():
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
  cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25)")
  conn.commit()
  return conn

def vulnerable_function(conn, user_input):
  cursor = conn.cursor()
  
  # 脆弱性: ユーザー入力を直接SQLクエリに含めている
  query = f"SELECT * FROM users WHERE name = '{user_input}'"
  cursor.execute(query)

  return cursor.fetchall()

if __name__ == "__main__":
  conn = create_table_and_insert_data()
  user_input = input("Enter a name: ")
  results = vulnerable_function(conn, user_input)
  for row in results:
    print(row)
  conn.close()
