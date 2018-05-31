from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import post
import result_util

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('editor.html')


@app.route('/md.html')
def md():
    return render_template('md.html')


@app.route('/publish', methods=['POST'])
def publish():
    data = request.get_json()

    title = data['title']

    tags = data['tags']

    categories = data['categories']

    content = data['content']

    ret = post.publish(title=title, tags=tags, categories=categories, content=content)
    return jsonify(result_util.getSuccessResponse(ret))


if __name__ == '__main__':
    app.run()
