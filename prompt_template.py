
def mock_persona(tweet_examples, task):
    def get_authors_tone_description(tweet_examples):

        template = f"""
            You are an AI Bot skilled in extracting political stances from writing examples.
            Please analyze the examples provided and determine the political stance conveyed in the writing.

            % START OF EXAMPLES
            {tweet_examples}
            % END OF EXAMPLES

            Describe the political stance of the example above.
        """
        final_prompt = template.format(tweet_examples=tweet_examples)
        return llm.predict(final_prompt)
    
    template = \
        """
        % INSTRUCTIONS
        - You are an AI Bot that is very good at mimicking an author writing style.
        - Your goal is to write content with the political stance tone that is described below.
        - You're a smart AI. You can determine from the examples below whether the user is a supporter of Trump, Biden, or neither.
        - Do not go outside the tone instructions below

        % Description of the authors political stance tone:
        {authors_tone_description}

        % START OF EXAMPLES
        {tweet_examples}
        % END OF EXAMPLES

        % YOUR TASK
        1. Answering the question "{task}" using author writing style and mock author political persona
    """
    
    authors_tone_description = get_authors_tone_description(tweet_examples)
    prompt_template = \
        template.format(authors_tone_description=authors_tone_description,tweet_examples=tweet_examples, task=task)
    return prompt_template