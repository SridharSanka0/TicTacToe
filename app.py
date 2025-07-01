import streamlit as st

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.history = []

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def restart_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.history = []

def undo_move():
    if st.session_state.history:
        last = st.session_state.history.pop()
        st.session_state.board[last] = ""
        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

st.title("🎮 Tic Tac Toe")

# Board
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            if st.session_state.board[idx] == "":
                if st.button(" ", key=idx):
                    st.session_state.board[idx] = st.session_state.current_player
                    st.session_state.history.append(idx)
                    if not check_winner(st.session_state.board):
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            else:
                st.button(st.session_state.board[idx], key=idx, disabled=True)

# Winner or Turn
winner = check_winner(st.session_state.board)
if winner:
    st.success(f"🎉 Player {winner} wins!")
elif "" not in st.session_state.board:
    st.info("🤝 It's a draw!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

# Controls
col1, col2 = st.columns(2)
with col1:
    if st.button("🔁 Restart"):
        restart_game()
with col2:
    if st.button("↩️ Undo"):
        undo_move()

