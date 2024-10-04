from typing import Any
from crewai_tools import BaseTool

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentimental Analysis Tool"
    description: str = ("Analyzes the sentiment of text "
         "to ensure positive and engaging communication.")
    
    def _run(self, text: str) -> str:
        return "positive"
