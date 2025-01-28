import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.data_collection_agent import DataCollectionAgent

# Initialize the Data Collection Agent
data_collection_agent = DataCollectionAgent()

# Fetch data for a player (e.g., Kyrie Irving for the 2024-25 season)
player_name = "LeBron James"
season_id = "2024-25"

try:
    print(f"Fetching data for {player_name} ({season_id})")
    player_fg_pct, shotchart_data, league_avg_data = data_collection_agent.fetch_player_data(player_name, season_id)
    print(f"Fetched data for {player_name} ({season_id}):")
    print(f"FG%: {player_fg_pct:.2%}")
    print(f"Shot Chart Data: {shotchart_data.head()}")
    print(f"League Averages: {league_avg_data.head()}")
except ValueError as e:
    print(f"Error: {e}")