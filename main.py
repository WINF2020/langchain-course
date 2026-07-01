import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")


def main():
    print("Hello from langchain-course!")

    if api_key:
        print(f"{api_key[:8]}...{api_key[-4:]}")
    else:
        print("OPENAI_API_KEY nicht gesetzt")


if __name__ == "__main__":
    main()
