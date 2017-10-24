# NFL Fantasy Football Selector

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

| Required      | Name             | Type     |
| ------------- |------------------| ---------|
| Dataset_1     | Defence rankings | Data     |
| NFL_Fixtures.csv     | Fixture list     | Data     |
| Dataset_3     | Players set      | Data     |
| Function_1    | find_team        | function |
| Function_2    | find_position    | function |
| Function_3    | find_opposition  | function |
| Function_4    | player_choice    | function |


The final script will be written as `final_script.py`. This can then be published with a GUI or WebApp interface.
Initially however this will be a simple command line python script.


Still to do:

- Make this apply to positional ratings and not base ratings
- Find correct CSVs and update column headings
- Ensure return statements are correct
- ~~Begin program in jupyter or pycharm~~
