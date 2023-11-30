from flask import Flask, render_template, request, jsonify
from language_tool_python import LanguageTool

app = Flask(__name__)

def check_grammar(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    return matches

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        try:
            matches = check_grammar(text)
            return jsonify(html=render_template('result_partial.html', text=text, matches=matches))
        except Exception as e:
            return jsonify(error=str(e))
    return render_template('index.html', matches=None)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
