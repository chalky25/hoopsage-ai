import os
from dotenv import load_dotenv
from agents.data_collection_agent import DataCollectionAgent
from agents.data_analysis_agent import DataAnalysisAgent
from agents.llm_reasoning_agent import LLMReasoningAgent

def analyze_player_shooting(player_name, season_id):
    """
    Complete pipeline to analyze a player's shooting performance.
    
    Args:
        player_name (str): Full name of the player (e.g., "LeBron James")
        season_id (str): Season in format "YYYY-YY" (e.g., "2022-23")
    
    Returns:
        dict: Complete analysis including statistics and AI insights
    """
    # Load environment variables
    load_dotenv()
    
    try:
        # Initialize agents
        data_collection_agent = DataCollectionAgent()
        data_analysis_agent = DataAnalysisAgent()
        llm_agent = LLMReasoningAgent(os.getenv("DEEPSEEK_API_KEY"))
        
        # Step 1: Collect raw data
        print(f"\nFetching data for {player_name} ({season_id})...")
        player_fg_pct, shotchart_data, league_avg_data = data_collection_agent.fetch_player_data(
            player_name, 
            season_id
        )
        
        # Step 2: Analyze shooting patterns
        print("Analyzing shooting patterns...")
        analysis_results = data_analysis_agent.analyze_player_data(
            player_fg_pct,
            shotchart_data,
            player_name,
            season_id
        )
        
        # Step 3: Generate AI insights
        print("Generating insights...")
        insights = llm_agent.generate_insights(analysis_results)
        
        # Step 4: Combine all results
        final_results = {
            **analysis_results,
            'ai_insights': insights
        }
        
        # Print summary
        print("\n=== Analysis Complete ===")
        print(f"\nPlayer: {final_results['player']}")
        print(f"Season: {final_results['season']}")
        print(f"Field Goal %: {final_results['fg_pct']:.2%}")
        
        print("\nShot Distribution:")
        for zone, count in final_results['shot_distribution'].items():
            print(f"  {zone}: {count}")
        
        print("\nShot Efficiency by Zone:")
        for zone, pct in final_results['shot_efficiency'].items():
            print(f"  {zone}: {pct:.2%}")
        
        print("\nAI Analysis:")
        print(final_results['ai_insights'])
        
        return final_results
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    player_name = "Anthony Edwards"
    season_id = "2024-25"
    
    analyze_player_shooting(player_name, season_id)
