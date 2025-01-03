from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store goals in memory (can be replaced with a database)
vision_board = []

@app.route('/')
def home():
    return render_template('index.html', vision_board=vision_board)

@app.route('/add', methods=['POST'])
def add_goal():
    title = request.form['title']
    description = request.form['description']
    image_url = request.form['image_url']
    vision_board.append({'title': title, 'description': description, 'image_url': image_url})
    return redirect(url_for('home'))

@app.route('/delete/<int:goal_id>')
def delete_goal(goal_id):
    if 0 <= goal_id < len(vision_board):
        vision_board.pop(goal_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
