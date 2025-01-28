from openai import OpenAI
import json

class LLMReasoningAgent:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("DeepSeek API key is required")
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

    def generate_insights(self, data):
        """
        Generates insights about a player's shooting performance using the DeepSeek API.
        """
        prompt = self._create_prompt(data)
        
        try:
            print("Making API request with following parameters:")
            print(f"Model: deepseek-reasoner")
            print(f"Base URL: {self.client.base_url}")
            
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an expert NBA analyst specializing in player performance analysis."},
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )
            
            

            """for chunk in response:
                if chunk.choices[0].delta.reasoning_content:
                    reasoning_content += chunk.choices[0].delta.reasoning_content
                else:
                    content += chunk.choices[0].delta.content
            # Add debug print"""

            #print(f"Raw API Response: {response.choices[0].message.content}")
            
            return (response.choices[0].message.content)

        except Exception as e:
            print(f"Full error details: {str(e)}")
            if hasattr(e, 'response'):
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.content}")
            raise Exception(f"Error calling DeepSeek API: {str(e)}")

    def _create_prompt(self, data):
        return f"""
        Please analyze the following basketball statistics for {data['player']} in the {data['season']} season:

        1. Field Goal Percentage: {data['fg_pct']:.2%}

        2. Shot Distribution by Zone:
{self._format_dict(data['shot_distribution'])}

        3. Shot Efficiency by Zone:
{self._format_dict(data['shot_efficiency'], percentage=True)}

        Please provide:
            1. A summary of the player's shooting performance
            2. Key strengths and weaknesses based on the data
            3. Specific areas for improvement
            4. Actionable recommendations for enhancing their shooting efficiency
        """

    def _format_dict(self, data, percentage=False):
        # Find the longest key for proper alignment
        max_key_length = max(len(key) for key in data.keys())
        
        formatted = []
        for key, value in data.items():
            # Pad the key with spaces for alignment
            padded_key = key.ljust(max_key_length)
            if percentage:
                formatted.append(f"\t- {padded_key}: {value:.2%}")
            else:
                formatted.append(f"\t- {padded_key}: {value}")
        return "\n".join(formatted)