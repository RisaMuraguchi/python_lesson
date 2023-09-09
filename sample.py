from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#DB
stores = [
  {
    'name': 'my_store',
    'items': [
      {
        'name': 'chocolate',
        'price': 120
      }
    ]
  }
]

# GET /store/<string:name>
@app.route('/stores/<string:name>')
def get_store(name):
  for store in stores:
    if store["name"] == name:
      return jsonify(store)
  return jsonify({"message": "no store named {} found.".format(name)})  