def agent_q2(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    # Your code here: Amend the agent!
    my_mark = obs.mark
    opp_mark = 1 if obs.mark==2 else 2
    for col in valid_moves:
        if(check_winning_move(obs, config, col, piece=obs.mark)):
            return col
        elif(check_winning_move(obs, config, col, piece=opp_mark)):
            return col
    return random.choice(valid_moves)
def agent_q2(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    # Your code here: Amend the agent!
    my_mark = obs.mark
    opp_mark = 1 if obs.mark==2 else 2
    for col in valid_moves:
        if(check_winning_move(obs, config, col, piece=obs.mark)):
            return col
        elif(check_winning_move(obs, config, col, piece=opp_mark)):
            return col
    return random.choice(valid_moves)
