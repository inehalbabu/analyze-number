from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'My First API'

@app.route('/analyze_number/<int:n>')
def analyze_number(n):
    sum = 0
    order = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    is_armstrong = sum == n

    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    is_palindrome = original == reverse

    result = {
        'number': original,
        'armstrong': is_armstrong,
        'palindrome': is_palindrome,
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
