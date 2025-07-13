from flask import Flask, render_template, request
import language_tool_python

app = Flask(__name__, static_url_path='/static', static_folder='static')
tool = language_tool_python.LanguageTool('en-US')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    text = request.form['text']
    matches = tool.check(text)
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
