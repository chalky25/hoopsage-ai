import matplotlib.pyplot as plt
import os
import make_court

import pandas as pd

class DataAnalysisAgent:
    def __init__(self):
        pass

    def analyze_player_data(self, player_fg_pct, shotchart_data, player_name, season_id):
        # Generate visualizations (unchanged)
        plt.figure(figsize=(8, 7))
        make_court.shot_chart(shotchart_data, player_fg_pct, title=f"{player_name} Shot Chart {season_id}")
        output_dir = 'static'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'shot_chart.png')
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()

        # Calculate shot distribution and efficiency
        shot_distribution = shotchart_data['SHOT_ZONE_BASIC'].value_counts().to_dict()
        shot_efficiency = shotchart_data.groupby('SHOT_ZONE_BASIC')['SHOT_MADE_FLAG'].mean().to_dict()

        #Returns data        
        return {
            'player': player_name,
            'season': season_id,
            'fg_pct': player_fg_pct,
            'shot_distribution': shot_distribution,
            'shot_efficiency': shot_efficiency,
        }