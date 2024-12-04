from flask import Flask, jsonify,request,jsonify
from amazon_search import search_amazon
import os

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    
    results = search_amazon(keyword)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
