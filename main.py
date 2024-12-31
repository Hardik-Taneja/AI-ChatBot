import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the tokens
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# Load the OpenAI API key from an environment variable
openai.api_key = OPEN_API_KEY

def chatbot():
    print("ChatGPT: Hello! Type 'exit' to end the conversation.")
    
    # Initialize conversation messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break

        # Append user's message to the conversation history
        messages.append({"role": "user", "content": user_input})

        try:
            # Call the OpenAI ChatCompletion API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the desired model
                messages=messages,
                max_tokens=100,  # Limit response length
                temperature=0.7  # Adjust creativity
            )

            # Extract and print the assistant's response
            assistant_message = response.choices[0].message.content.strip()
            print(f"ChatGPT: {assistant_message}")

            # Add the assistant's response to the conversation history
            messages.append({"role": "assistant", "content": assistant_message})

        except openai.error.AuthenticationError:
            print("Error: Invalid API key. Please check your API key and try again.")
            break
        except openai.error.RateLimitError:
            print("Error: Rate limit exceeded. Please wait before making more requests.")
            break
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    # Check if the API key is set
    if openai.api_key is None:
        print("Error: OpenAI API key is not set. Please set the 'OPENAI_API_KEY' environment variable.")
    else:
        chatbot()
