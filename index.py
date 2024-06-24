import csv
from datetime import datetime

class Match:
    def __init__(self, match_number, round_number, date, location, home_team, away_team, group, result=None):
        self.match_number = match_number
        self.round_number = round_number
        self.date = datetime.strptime(date, "%d/%m/%Y %H:%M")
        self.location = location
        self.home_team = home_team
        self.away_team = away_team
        self.group = group
        self.result = result  # Tuple (home_goals, away_goals) if result is available

class Team:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.points = 0
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

def read_fixture(file_path):
    matches = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            match = Match(
                match_number=int(row['Match Number']),
                round_number=int(row['Round Number']),
                date=row['Date'],
                location=row['Location'],
                home_team=row['Home Team'],
                away_team=row['Away Team'],
                group=row['Group'],
                result=row['Result'] if row['Result'] else None
            )
            matches.append(match)
    return matches

def read_teams(matches):
    teams = {}
    for match in matches:
        if match.home_team not in teams:
            teams[match.home_team] = Team(name=match.home_team, group=match.group)
        if match.away_team not in teams:
            teams[match.away_team] = Team(name=match.away_team, group=match.group)
    return teams

def update_results(matches, results_file_path):
    with open(results_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        results = {int(row['Match Number']): (int(row['Home Team Goals']), int(row['Away Team Goals'])) for row in reader}
    
    for match in matches:
        if match.match_number in results:
            match.result = results[match.match_number]

def calculate_positions(matches, teams):
    for match in matches:
        if match.result:
            home_goals, away_goals = match.result
            home_team = teams[match.home_team]
            away_team = teams[match.away_team]

            home_team.matches_played += 1
            away_team.matches_played += 1

            home_team.goals_for += home_goals
            home_team.goals_against += away_goals
            away_team.goals_for += away_goals
            away_team.goals_against += home_goals

            if home_goals > away_goals:
                home_team.wins += 1
                home_team.points += 3
                away_team.losses += 1
            elif home_goals < away_goals:
                away_team.wins += 1
                away_team.points += 3
                home_team.losses += 1
            else:
                home_team.draws += 1
                away_team.draws += 1
                home_team.points += 1
                away_team.points += 1

def generate_final_report(teams, output_file_path):
    grouped_teams = {}
    for team in teams.values():
        if team.group not in grouped_teams:
            grouped_teams[team.group] = []
        grouped_teams[team.group].append(team)
    
    with open(output_file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Grupo', 'Equipo', 'Puntos', 'PartidosJugados', 'Victorias', 'Empates', 'Derrotas', 'GolesAFavor', 'GolesEnContra', 'DiferenciaDeGoles'])
        for group, group_teams in grouped_teams.items():
            sorted_teams = sorted(group_teams, key=lambda x: (x.points, x.goal_difference, x.goals_for), reverse=True)
            for team in sorted_teams:
                writer.writerow([group, team.name, team.points, team.matches_played, team.wins, team.draws, team.losses, team.goals_for, team.goals_against, team.goal_difference])

# Paths to the input and output CSV files
fixture_file_path = 'copa-america-2024-UTC.csv'
results_file_path = 'results.csv'
output_file_path = 'final_report.csv'

# Read the fixture and teams
matches = read_fixture(fixture_file_path)
teams = read_teams(matches)

# Update match results
update_results(matches, results_file_path)

# Calculate team positions
calculate_positions(matches, teams)

# Generate the final report
generate_final_report(teams, output_file_path)
