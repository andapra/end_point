from flask import Flask, request, Response, Request, make_response
import os, sys
import json

app = Flask(__name__)
@app.route('/myoutput.json', methods=['GET'])
def cap_rss(lang):
    if request.method == 'GET':
        create_json = {
            'key_1': 'value_1',
            'key_2': {
                'subkey_1': 'key_2_subkey2_value1',
                'subkey_2': 'key_2_subkey2_value2'
            }

        }            
    return json.dumps(create_json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)