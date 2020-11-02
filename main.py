from flask import Flask, jsonify, request, make_response
import jwt 
import datetime
import pymysql, json
import psycopg2
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/route?token=generated_token_goes_here

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected', methods=['GET'])
@token_required
def protected():
    token = request.args.get('token')
    data_token = jwt.decode(token, app.config['SECRET_KEY'])
    user = data_token['user']
    return jsonify({'user' : user, 'message' : 'Your token is valid.'})

@app.route('/protected', methods=['POST'])
@token_required
def insert():
    token = request.args.get('token')
    data_token = jwt.decode(token, app.config['SECRET_KEY'])
    user = data_token['user']
    req = request.get_json()
    data = req['contacts']
    
    fields = [
        'name',
        'cellphone'
    ]
    
    if user == 'macapa':

        
        # connect to MySQL
        conn = pymysql.connect(host='localhost', user='admin', password='', db='admin')
        cur = conn.cursor()
        # create a table with one column per field
        cur.execute(
            """CREATE table IF NOT EXISTS contacts (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR ( 200 ) NOT NULL,
            celular VARCHAR ( 20 ) NOT NULL,
            PRIMARY KEY (id)
        );"""
        )

        for item in data:
            for field in fields:
                if field == 'name':
                    n_nome = item[field]
                    nomeformatado = n_nome.upper()
                    item[field] = nomeformatado
                if field == 'cellphone':
                    n_celular = item[field]
                    celularformatado = '+{} ({}) {}-{}'.format(n_celular[0:2],n_celular[2:4] ,n_celular[4:9], n_celular[9:])
                    item[field] = celularformatado
        
        for item in data:
            my_data = [item[field] for field in fields]
            cur.execute("INSERT INTO contacts (nome, celular) VALUES (%s,%s)", tuple(my_data))        

    if user == 'varejao':
    
        # connect to PostgreSQL
        conn = psycopg2.connect(host='localhost', user='admin', password='adminpassword', database='admin', port='5432')
        cur = conn.cursor()
        conn.autocommit = True

        cur.execute(
            "CREATE table IF NOT EXISTS contacts (id serial PRIMARY KEY, nome VARCHAR ( 100 ) NOT NULL, celular VARCHAR ( 13 ) NOT NULL);"
        )

        for item in data:
            my_data = [item[field] for field in fields]
            cur.execute("INSERT INTO contacts (nome, celular) VALUES (%s,%s)", tuple(my_data))

    # commit changes
    conn.commit()
    # close the connection
    conn.close()

    return jsonify({'user' : user, 'message' : 'The data was inserted at client database.'})


@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.username == 'macapa' and auth.password == 'senhamacapa':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])

        return jsonify({'user' : auth.username, 'token' : token.decode('UTF-8')})

    if auth and auth.username == 'varejao' and auth.password == 'senhavarejao':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])

        return jsonify({'user' : auth.username, 'token' : token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/logout')
def logout():
        return jsonify({'message' : 'You are now logged out.'}), 401

if __name__ == '__main__':
    app.run(debug=True)