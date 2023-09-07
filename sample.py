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

