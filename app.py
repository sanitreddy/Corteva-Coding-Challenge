from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Establishing Database Connection
app.config['MYSQL_HOST'] = '**Local Connection HostName**'
app.config['MYSQL_USER'] = '**Local Connection UserName**'
app.config['MYSQL_PASSWORD'] = '**Local Connection Password**'
app.config['MYSQL_DB'] = '**Local Database Name**'
 
mysql = MySQL(app)

#To check default route
@app.route('/')
def check():
    return 'Flask is working'

@app.route('/api/weather', methods=['GET'])
def weather():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
 
    #Executing SQL Statement
    cursor.execute(" SELECT * FROM weatherStation ")
    
    #Fetching all records
    query = cursor.fetchall()
    
    #Closing the cursor
    cursor.close()

    response=[]
    for item in list(query):
        response.append({"year": item[0], 
            "maxTemp": item[1], 
            "minTemp": item[2], 
            "precipitation": item[3]})
    return response

@app.route('/api/weather/stats', methods=['GET'])
def weatherStats():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Extract the parameters from the request
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
 
    #Executing SQL Statement
    cursor.execute(" SELECT * FROM weatherStation WHERE year BETWEEN '{}' AND '{}' LIMIT {} OFFSET {} ".format(start_date, end_date, limit, offset))

    #Fetching all records
    query = cursor.fetchall()
    
    #Closing the cursor
    cursor.close()

    response=[]
    for item in list(query):
        response.append({"year": item[0], 
            "maxTemp": item[1], 
            "minTemp": item[2], 
            "precipitation": item[3]})
    return response


if __name__ == '__main__':
    app.run()