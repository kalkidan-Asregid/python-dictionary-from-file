# Read file and create the dictionary
fruits_color = open('word.txt', 'r')
fruits_dict = {}

for line in fruits_color:
    line = line.strip()
    if ':' in line:
        key, value = line.split(':', 1)  # Split into key and value
        fruits_dict[key] = value         # Add to dictionary
        print(f"{key}: {value}")         # Print each key-value pair

fruits_color.close()

print('\n')

# Define the function to invert the dictionary and format the output
def invert_dict(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)  # Append if value already exists
        else:
            inverted_dict[value] = [key]      # Initialize list with first key
    
    # Print each inverted key-value pair in the desired format
    for color, fruits in inverted_dict.items():
        print(f"{color}: {', '.join(fruits)}")

# Invert the fruits_dict
invert_dict(fruits_dict)
