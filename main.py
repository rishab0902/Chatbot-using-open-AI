# Import the OpenAI library to interact with OpenAI's GPT models
import openai

# Set the API key to access OpenAI's services
#openai.api_key = "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"

# Define a function to interact with the GPT model
def chat_with_gpt(prompt):
    # Create a response using the GPT model with the provided prompt
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Specify the model to use
        messages=[{"role": "user", "content": prompt}]  # Set the message content and role
    )

    # Return the response content from the model
    return response.choices[0].message['content'].strip()

# Main block to keep the conversation going
if __name__ == "__main__":
    while True:
        # Prompt the user for input
        user_input = input("You: ")
        # Break the loop if the user types 'quit', 'exit', or 'bye'
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        # Get the response from the GPT model
        response = chat_with_gpt(user_input)
        # Print the chatbot's response
        print("Chatbot: ", response)
