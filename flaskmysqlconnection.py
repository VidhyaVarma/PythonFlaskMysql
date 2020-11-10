from flask import Flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="spikey9967",
  database="testdatabase"
)

mycursor = mydb.cursor()
@app.route('/')
def index():
  output = []
  mycursor.execute("select * from users")
  data=mycursor.fetchall()
  header = [i[0] for i in mycursor.description]
  for i in data:
    output.append(dict(zip(header, i)))
  return((json.dumps({'items':output})))


if __name__ == '__main__':
   app.run()
