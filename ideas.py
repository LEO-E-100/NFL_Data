# Setup
df_players = 0 # Read in a CSV of players, teams and positions in the NFL - outside the function perhaps??
df_fixtures = 0 # Read in a CSV of the fixtures for each team
df_ratings = 0 # Read in a CSV of the team ratings for each team


def find_player(player):

    df = df_players

    player_frame = df[df['player_name'].str.contains(player)]
    player_team = player_frame['team']
    player_position = player_frame['position']

    return player_team, player_position

def find_opposition(player_team):

    df = df_fixtures

    home_team = df[df['TEAM_1'].str.contains(player_team)]
    away_team = home_team['TEAM_2']

    if player_team == home_team:
        return away_team
    else:
        return home_team

def opposition_rating(opposition):

    df = df_ratings

    rating = df[df['rating'].str.contains(opposition)]

    return rating

def player_choice(player_1, player_2):

    team_1 = find_player(player_1)
    team_2 = find_player(player_2)

    oppo_1 = find_opposition(team_1)
    oppo_2 = find_opposition(team_2)

    oppo_rating_1 = opposition_rating(oppo_1)
    oppo_rating_2 = opposition_rating(oppo_2)

    if oppo_rating_1 < oppo_rating_2:
        return oppo_rating_1
    else:
        return oppo_rating_2
