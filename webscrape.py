import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, abort

app = Flask(__name__)
search_url = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183'
page = requests.get(search_url)
if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')
    review = bs.findAll(class_='col-xs-12 mainReviews')
    review = bs.findAll(class_='col-xs-12 mainReviews hiddenReviews')


@app.route('/', methods=['GET'])
def get_reviews():
    Reviews = []
    for reviews in review:
        review1 = {
            'title': reviews.find(class_='reviewTitle').text,
            'text': reviews.find(class_='reviewText').text,
            'author': reviews.find(class_='consumerName').text,
            'date': reviews.find(class_='consumerReviewDate').text,
            'rating': reviews.find(class_='numRec').text,
        }

        Reviews.append(review1)

    return jsonify('Reviews', Reviews)


@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "Method not allowed", 405


@app.route("/")
def crash_post():
    raise Exception


if __name__ == '__main__':
    app.run(host='127.10.0.0', port='9000', debug=True)
