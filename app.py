from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Global game state (reset on server restart)
state = {
    'board': [''] * 9,
    'current_player': 'X',
    'history': []
}

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/state")
def get_state():
    winner = check_winner(state['board'])
    draw = '' not in state['board'] and not winner
    return jsonify({
        'board': state['board'],
        'current_player': state['current_player'],
        'winner': winner,
        'draw': draw
    })

@app.route("/move", methods=['POST'])
def move():
    index = int(request.json['index'])
    if state['board'][index] == '' and not check_winner(state['board']):
        state['board'][index] = state['current_player']
        state['history'].append(index)
        state['current_player'] = 'O' if state['current_player'] == 'X' else 'X'
    return get_state()

@app.route("/undo", methods=['POST'])
def undo():
    if state['history']:
        last_move = state['history'].pop()
        state['board'][last_move] = ''
        state['current_player'] = 'O' if state['current_player'] == 'X' else 'X'
    return get_state()

@app.route("/restart", methods=['POST'])
def restart():
    state['board'] = [''] * 9
    state['current_player'] = 'X'
    state['history'] = []
    return get_state()

if __name__ == "__main__":
    app.run(debug=True)
