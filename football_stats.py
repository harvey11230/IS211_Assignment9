from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def main():
    PlayerName = []
    PlayerPosition = []
    Team = []
    Touchdown = []
    url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    for item in soup.find_all('span', class_='CellPlayerName--long'):
    # players = item.find('a').contents[0]
        players = item.find('a')
        for l in players:
            PlayerName.append(l)
    Top20_players = PlayerName[:20]

    player_position = soup.find_all('span', class_='CellPlayerName-position')

    for i in player_position:
        player_position = i.text.replace(' ', '')
        player_position = player_position.replace('\n','')
        PlayerPosition.append(player_position)

    Top20_players_position = PlayerPosition[:20]

    team = soup.find_all('span', class_='CellPlayerName-team')

    for i in team:
        team = i.text.replace(' ', '')
        team = team.replace('\n', '')
        Team.append(team)

    Team = Team[::2]
    Top20_teams = Team[:20]

    touch_down = soup.find_all('td', class_='TableBase-bodyTd TableBase-bodyTd--number')

    for i in touch_down:
        touch_down = i.text.replace(' ', '')
        touch_down = touch_down.replace('\n', '')
        Touchdown.append(touch_down)

    Touchdown = Touchdown[7::12]
    Top20_touchdown = Touchdown[:20]

    result = pd.DataFrame({'Player Name':Top20_players, 'Position':Top20_players_position, 'Team':Top20_teams, 'Touch Down':Top20_touchdown})
    print(result)

if __name__ == '__main__':
    main()















