from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def example():
    text_param = request.args.get('text', None)
    int_param = request.args.get('number', None)

    if text_param is None or int_param is None:
        return "Please provide both 'text' and 'number' parameters.", 400

    try:
        int_param = int(int_param)
    except ValueError:
        return "The 'number' parameter must be an integer.", 400

    return f"Received parameters: text = {text_param}, number = {int_param}"

if __name__ == '__main__':
    app.run()

#try this in the browser http://127.0.0.1:5000/example?text=hello&number=42
#curl "http://127.0.0.1:5000/example?text=hello&number=42
