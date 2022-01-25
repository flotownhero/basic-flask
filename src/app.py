from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_plate():
    text = '''
    https://rnacentral.org/help/public-database

    In addition to downloadable files, an API, and the text search, RNAcentral provides a public Postgres database that can be used to query the data using SQL syntax. The database is updated with every RNAcentral release and contains a copy of the data available through the RNAcentral website.
    '''
    return text

@app.route('/washington', methods=['GET', 'POST'])
def gw():
    text = '''
Friends and Fellow Citizens:

The period for a new election of a citizen to administer the executive government of the United States being not far distant, and the time actually arrived when your thoughts must be employed in designating the person who is to be clothed with that important trust, it appears to me proper, especially as it may conduce to a more distinct expression of the public voice, that I should now apprise you of the resolution I have formed, to decline being considered among the number of those out of whom a choice is to be made.

I beg you, at the same time, to do me the justice to be assured that this resolution has not been taken without a strict regard to all the considerations appertaining to the relation which binds a dutiful citizen to his country; and that in withdrawing the tender of service, which silence in my situation might imply, I am influenced by no diminution of zeal for your future interest, no deficiency of grateful respect for your past kindness, but am supported by a full conviction that the step is compatible with both.
    '''
    return text


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=42042, debug=True)
    # app.run(host='0.0.0.0', debug=True)
    app.run()