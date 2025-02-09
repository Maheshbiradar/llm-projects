from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

import outputparsers
from thirdparties.linkedin import scrape_linkedin_profile
from agents.linkedinlookupagent import lookup as linkedin_lookup_agent
from outputparsers import summary_parser

def start_with(name: str):
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    print("Hello LangChain")

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    Use this information from Linkedin
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()},
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    start_with(name="NTT Data INC")
