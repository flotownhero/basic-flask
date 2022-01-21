from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_plate():
    text = '''
    https://rnacentral.org/help/public-database

    In addition to downloadable files, an API, and the text search, RNAcentral provides a public Postgres database that can be used to query the data using SQL syntax. The database is updated with every RNAcentral release and contains a copy of the data available through the RNAcentral website.
    '''
    return text

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=42042, debug=True)
    app.run(host='0.0.0.0', debug=True)