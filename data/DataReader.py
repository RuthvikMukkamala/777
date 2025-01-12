"""
Web Scraping all of Berkshire's Shareholder Letter
"""

from langchain_openai import ChatOpenAI
from browser_use import Agent, AgentHistoryList
import asyncio


class WebAgentDataScraping():
    ...


"""
    Example of a data scraper using a pure LLM based approach
"""
class BerskhireScraper():
    def __init__(self):
        self.prompt = ''' 
        Your going to scrape all of the data from the Berkshire Hathaway website an give me a formatted 
        JSON file to read from. 
        
        Go to: https://www.berkshirehathaway.com/letters/letters.html
        Read all the years of data, and give it to me in a formatted response
        . Extract: Retrieve all relevant information and data from the webpage by going into all the years of data and 
        retrieving the shareholder information. 
        Transform to JSON: Convert the extracted data into a valid JSON structure, preserving meaningful hierarchies 
        and relationships in the data. Return result: Provide the JSON as your final output.

        Ensure the JSON you provide contains all the important content or data fields from the page. If the page has 
        multiple sections or nested data, keep the JSON structure clean and well-organized. If you encounter dynamic 
        or paginated sections, iterate or simulate the required actions to capture all data.
        
        '''

        self.llm = ChatOpenAI(model="gpt-4o")

    async def run_agent(self):
        agent = Agent(
            task=self.prompt,
            llm=self.llm,
        )
        result = await agent.run()
        return result

    def result_analysis(self, result: AgentHistoryList):
        print(result.final_result())
