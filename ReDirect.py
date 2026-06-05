from flask import Flask, redirect, render_template, request
from App import *
from SQL import *
app = Flask(__name__)
@app.route('/')
def home():
    return('''<H1>URL Shortener</H1>
        <form action="/create" method="post">
            <input type="text" name="user_input" placeholder="link" id="url" required/>
            <button type="submit">Create Short Link</button>
        </form>
        <form action="/link" method="post">
            <input type="text" name="user_input" placeholder="hash" id="url" required/>
            <button type="submit">Visit the link</button>
        </form>
        ''')

@app.route('/link/<path:url>', methods=['GET'])
def link_url(url):
    result=get_URL(url)
    if result is None:
        return '<p>link is not found</p>'
    else:
        return redirect('https://'+result)

@app.route("/link", methods=['POST'])
def link():
    url=request.form.get('user_input')
    result=get_URL(url)
    if result is None:
        return '<p>link is not found</p>'
    else:
        return redirect('https://'+result)

@app.route('/create',methods=['POST'])
def create():
    url=request.form.get('user_input')
    found=url_exists(url) != None
    if found:
        return 'link already exists at: '+ url_exists(url)
    else:
        print('1')
        data=hash_link(url)
        print(data)
        outcome=insert_URL(data[0],data[1],data[2],data[3])
        if outcome:
            return 'link has been created at: '+data[0]
        else:
            return 'link couldn\'t be created'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

