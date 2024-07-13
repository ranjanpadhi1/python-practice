import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

def save_user(user):
    try:    
      mydb.cursor().execute('insert into test.user values(%(id)s, %(name)s, %(age)s)', user)
      mydb.commit()
      return True, f"User '{user['id']}' inserted successfully"
    except:
       return False, f'Error while inserting user {user['id']}'
    
def delete_user(id):
    try:
      mydb.cursor().execute(f'delete from test.user where id={id}')
      mydb.commit()
      return True, f"User '{id}' deleted successfully"
    except:
      return False, f"Error while deleting user '{id}'"
