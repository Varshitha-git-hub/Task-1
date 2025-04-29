import requests
from bs4 import BeautifulSoup

# Function to get topic details from W3Schools
def get_info_from_w3schools(topic):
    url = f'https://www.w3schools.com/python/{topic}.asp'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to get the definition
        try:
            definition = soup.find('div', class_='w3-panel w3-light-grey w3-round').get_text(strip=True)
        except:
            definition = "Definition not found."

        # Try to get example code
        try:
            example = soup.find('div', class_='w3-code').get_text(strip=True)
        except:
            example = "Example not found."

        return definition, example
    else:
        return None, None

# Main program
def main():
    print("Welcome to W3Schools Python Topic Viewer!\n")

    while True:
        topic = input("Enter a Python topic (like 'ifelse', 'for_loops') or type 'exit' to quit: ").lower()
        if topic == "exit":
            print("Goodbye!")
            break

        definition, example = get_info_from_w3schools(topic)

        if definition:
            print(f"\n--- {topic.upper()} ---")
            print(f"\nDefinition:\n{definition}")
            print(f"\nExample:\n{example}")
        else:
            print("Topic not found or error loading data.\n")

# Run the program
if name == "main":
    main()