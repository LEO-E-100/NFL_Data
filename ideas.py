"""
The ideas for using the pro-football-reference data set.

The website doesn't appear to have an API to use.

The data can be used for fantasy football to check match ups.

For example: If you have a choice of two running backs a function that returns the right player to play that week,
this is on the basis of which will be facing a team that gives more yards on running plays that week.

This will require parsing the pro-football-reference as CSV as well as the fixture list for football matches.

In this way the function can return the right player to choose each week.

Take two players as an arguments. These can be tested for team and position.

With this data, the correct opposition for the players can be identified and the opposition stats in that position can
be identified. The function will return the right player to choose based on the ranking of the opposition.

https://www.pro-football-reference.com/years/2017/opp.htm

Datasets required and sub-functions to be used:

Dataset_1 = Defence rankings
Dataset_2 = Fixture list
Dataset_3 = Players set

Function_1 = find_team
Function_2 = find_position - sub-function of Function_1 -> Actually need separate return statements so maybe separate?
Function_3 = find_opposition
Function_4 = player_choice

Still to do:

- make this apply to positional ratings and not base ratings
- find correct CSVs and update column headings
- ensure return statements are correct
- Begin program in jupyter or pycharm

"""

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

    home_team = df[df['home'].str.contains(player_team)]
    away_team = home_team['away']

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
