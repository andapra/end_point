from flask import Flask, request, Response, Request, make_response
import os, sys
import json
from xml.etree.ElementTree import Element, SubElement, tostring

def create_xml():
    root = Element('rss')
    root.set("xmlns:atom", "http://www.w3.org/2005/Atom")
    root.set("version", "2.0")

    channel = SubElement(root, 'channel')
    SubElement(channel, 'atom:link', {'rel':"hub", 'href':"//alert-hub.appspot.com"})
    SubElement(channel, 'atom:link', {'rel':"self", 'href':"https://warningcuaca.bmkg.go.id/cap/xml/id/rss.xml"})

    title = SubElement(channel, 'title')
    title.text = 'My Title XML'

    link = SubElement(channel, 'link')
    link.text = 'https://yourmachine.domain.com/cap/xml/id/rss.xml'

    description = SubElement(channel, 'description')
    description.text = 'Your Description XML'

    language = SubElement(channel, 'language')
    language.text = 'En'

    copy_right = SubElement(channel, 'copyright')
    copy_right.text = 'public domain'
    
    return tostring(root)

app = Flask(__name__)
@app.route('/myoutput.xml', methods=['GET'])
def cap_rss(lang):
    if request.method == 'GET':            
        return app.response_class(create_xml(), mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)