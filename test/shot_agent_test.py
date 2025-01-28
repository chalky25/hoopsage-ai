import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.llm_reasoning_agent import LLMReasoningAgent

def shot_agent_test():
    analysis_results = {'player': 'LeBron James', 'season': '2022-23', 'fg_pct': 0.5, 'shot_distribution': {'Restricted Area': 460, 'Above the Break 3': 344, 'Mid-Range': 209, 'In The Paint (Non-RA)': 174, 'Right Corner 3': 19, 'Left Corner 3': 13}, 'shot_efficiency': {'Above the Break 3': 0.3168604651162791, 'In The Paint (Non-RA)': 0.41379310344827586, 'Left Corner 3': 0.23076923076923078, 'Mid-Range': 0.36363636363636365, 'Restricted Area': 0.7434782608695653, 'Right Corner 3': 0.3684210526315789}}
    llm_reasoning_agent = LLMReasoningAgent(os.getenv("DEEPSEEK_API_KEY"))
    #print(llm_reasoning_agent._format_dict(data=analysis_results['shot_distribution']))
    #print(llm_reasoning_agent._create_prompt(data=analysis_results))
    insights = llm_reasoning_agent.generate_insights(analysis_results)
    print(insights)

if __name__ == "__main__":
    shot_agent_test()