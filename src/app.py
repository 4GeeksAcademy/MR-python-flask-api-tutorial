from flask import Flask, jsonify, request

app = Flask(__name__)

todos= [ { "label": "My first task", "done": True } ]

@app.route('/todos', methods= ['GET'])
def todos_list():
  return jsonify(todos)

@app.route('/todos', methods=["POST"])
def add_new_todo():
  request_body = request.get_json(force=True)
  if request_body:
    todos.append(request_body)
  print("Incoming request with the following body", request_body)
  return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo()
    print("This is the position to delete: ",position)
    return todos

@app.route('/todos', methods=['GET'])
def hello_world():
  return "<h1>Hello!</h1>"









# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)