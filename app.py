from flask import Flask, request

app = Flask(__name__)

events = []

@app.route('/')
def home():
    return '''
    <h1>Event Registration System</h1>

    <form action="/register" method="post">
        <input type="text" name="name" placeholder="Enter Your Name" required>
        <input type="text" name="event" placeholder="Enter Event Name" required>
        <button type="submit">Register</button>
    </form>
    '''

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    event = request.form['event']

    events.append({
        'name': name,
        'event': event
    })

    return f'''
    <h2>Registration Successful!</h2>

    <p>Name: {name}</p>
    <p>Event: {event}</p>

    <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)