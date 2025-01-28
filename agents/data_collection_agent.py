from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail, playercareerstats

class DataCollectionAgent:
    def fetch_player_data(self, player_name, season_id):
        """
        Fetches player data from the NBA API.
        
        Args:
            player_name (str): The full name of the player (e.g., "Kyrie Irving").
            season_id (str): The season ID in the format "YYYY-YY" (e.g., "2024-25").
        
        Returns:
            tuple: A tuple containing:
                - player_fg_pct (float): The player's field goal percentage for the season.
                - shotchart_data (pd.DataFrame): Shot chart data for the player.
                - league_avg_data (pd.DataFrame): League average shot chart data.
        """
        # Step 1: Identify the player by name and get their player ID
        all_players = players.get_players()
        player_id = next((player['id'] for player in all_players if player['full_name'] == player_name), None)
        
        if not player_id:
            raise ValueError(f"Player '{player_name}' not found.")
        
        # Step 2: Fetch career statistics for the player
        career_df = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
        
        # Step 3: Get the team ID and FG% for the specified season
        team_id = career_df.loc[career_df['SEASON_ID'] == season_id, 'TEAM_ID'].values[0]
        player_fg_pct = float(career_df[career_df['SEASON_ID'] == season_id]['FG_PCT'].iloc[0])
        
        # Step 4: Fetch shot chart data for the player
        shotchart = shotchartdetail.ShotChartDetail(
            player_id=player_id, 
            team_id=team_id, 
            season_nullable=season_id,
            season_type_all_star='Regular Season',
            context_measure_simple='FGA'
        )
        
        # Step 5: Extract shot chart data and league averages
        shotchart_data = shotchart.get_data_frames()[0]
        league_avg_data = shotchart.get_data_frames()[1]
        
        return player_fg_pct, shotchart_data, league_avg_data