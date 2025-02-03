from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import os

information= """Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and political figure known for his key roles in the automotive company Tesla, Inc. and the space company SpaceX. He is also known for his ownership of the technology company X Corp. and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI. Musk is the wealthiest individual in the world; as of January 2025, Forbes estimates his net worth to be US$426 billion."""
 
def main():
    print("Hello, World!")
    load_dotenv()

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})
    print (res)

if __name__ == "__main__":
    main()
