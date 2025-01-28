import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.data_collection_agent import DataCollectionAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.llm_reasoning_agent import LLMReasoningAgent

def run_analysis_pipeline(player_name, season_id):
    # Initialize agents
    data_collection_agent = DataCollectionAgent()
    data_analysis_agent = DataAnalysisAgent()
    
    try:
        # Step 1: Collect data using DataCollectionAgent
        print(f"Fetching data for {player_name} ({season_id})")
        player_fg_pct, shotchart_data, league_avg_data = data_collection_agent.fetch_player_data(player_name, season_id)
        
        # Step 2: Analyze data using DataAnalysisAgent
        print("Analyzing player data and generating insights...")
        analysis_results = data_analysis_agent.analyze_player_data(
            player_fg_pct,
            shotchart_data,
            player_name,
            season_id
        )
        
        # Step 3: Print results
        print("\nAnalysis Results:")
        print(f"Player: {analysis_results['player']}")
        print(f"Season: {analysis_results['season']}")
        print(f"Field Goal %: {analysis_results['fg_pct']:.2%}")
        print("\nShot Distribution:")
        for zone, pct in analysis_results['shot_distribution'].items():
            print(f"  {zone}: {pct}")
        print("\nShot Efficiency by Zone:")
        for zone, pct in analysis_results['shot_efficiency'].items():
            print(f"  {zone}: {pct:.2%}")
        
        return analysis_results

    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    player_name = "LeBron James"
    season_id = "2022-23"  # Using a past season as 2024-25 won't have data yet
    
    analysis_results = run_analysis_pipeline(player_name, season_id) 
    print(analysis_results)