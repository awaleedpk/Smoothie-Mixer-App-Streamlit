
# Import necessary libraries
import streamlit as st
import requests
import pandas as pd

# FruityVice API URL
fruityvice_api_url = "https://fruityvice.com/api/fruit/"

# Function to fetch fruit data from FruityVice API
def get_fruit_data(fruit_choice):
    response = requests.get(fruityvice_api_url + fruit_choice)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data for {fruit_choice} from FruityVice API")
        st.stop()

# Function to fetch fruit image from FruityVice API
def get_fruit_image(fruit_choice):
    response = requests.get(fruityvice_api_url + fruit_choice)
    if response.status_code == 200:
        return response.json().get("image", None)
    return None

# Function to display nutritional information using a bar chart
def display_nutritional_chart(selected_fruits):
    st.subheader("Nutritional Information (Bar Chart):")
    nutrition_data = {
        "Fruit": [],
        "Calories": [],
        "Fat": [],
        "Sugar": [],
        "Carbohydrates": [],
        "Protein": [],
    }

    # Loop through selected fruits to retrieve nutritional data
    for fruit in selected_fruits:
        fruit_data = get_fruit_data(fruit)
        nutrition_data["Fruit"].append(fruit.capitalize())
        nutrition_data["Calories"].append(fruit_data["nutritions"]["calories"])
        nutrition_data["Fat"].append(fruit_data["nutritions"]["fat"])
        nutrition_data["Sugar"].append(fruit_data["nutritions"]["sugar"])
        nutrition_data["Carbohydrates"].append(fruit_data["nutritions"]["carbohydrates"])
        nutrition_data["Protein"].append(fruit_data["nutritions"]["protein"])

    df = pd.DataFrame(nutrition_data)
    st.bar_chart(df.set_index("Fruit"))

# Set Streamlit page configuration
st.set_page_config(page_title="Smoothie Mixer App ", page_icon="🥤")

# Main function to create the Smoothie Mixer app
def main():
    st.title("Smoothie Mixer App 🥤")
    st.write("Create custom smoothie recipes with your favorite fruits!")

    # List of available fruits
    available_fruits = [
        "Persimmon", "Strawberry", "Banana", "Tomato", "Pear", "Durian", "Blackberry", "Lingonberry",
        "Kiwi", "Lychee", "Pineapple", "Fig", "Gooseberry", "Passionfruit", "Plum", "Orange",
        "GreenApple", "Raspberry", "Watermelon", "Lemon", "Mango", "Blueberry", "Apple", "Guava",
        "Apricot", "Papaya", "Melon", "Tangerine", "Pitahaya", "Lime", "Pomegranate", "Dragonfruit",
        "Grape", "Morus", "Feijoa", "Avocado", "Kiwifruit", "Cranberry", "Cherry", "Peach",
        "Jackfruit", "Horned Melon", "Hazelnut", "Pomelo", "Mangosteen"
    ]

    # Allow user to select fruits for the smoothie
    selected_fruits = st.multiselect("Select Fruits for Your Smoothie", available_fruits)

    # Check if at least two fruits are selected
    if not selected_fruits:
        st.warning("Please select at least two fruit.")
        st.stop()

    st.subheader("Selected Fruits:")
    for fruit in selected_fruits:
        st.write("- " + fruit + " 🍓")

    # Display nutritional information using a bar chart
    display_nutritional_chart(selected_fruits)

    # Button to generate and display the smoothie recipe
    if st.button("Generate Smoothie Recipe"):
        smoothie_recipe = generate_smoothie_recipe(selected_fruits)
        st.success("Smoothie Recipe:")
        st.write(smoothie_recipe)

# Function to generate a simple smoothie recipe
def generate_smoothie_recipe(selected_fruits):
    smoothie_recipe = "**Simple Smoothie Recipe**\n\n"
    smoothie_recipe += "Ingredients: 🥣\n"

    # Include selected fruits in the recipe
    for fruit in selected_fruits:
        smoothie_recipe += f"- {fruit}\n"

    # Add preparation instructions
    smoothie_recipe += "\nInstructions: 📋\n"
    smoothie_recipe += "1. Wash the fruits thoroughly.\n"
    smoothie_recipe += "2. Peel and chop the fruits into small pieces.\n"
    smoothie_recipe += "3. Blend all the fruits together until smooth.\n"
    smoothie_recipe += "4. Pour the smoothie into a glass and enjoy!\n"

    return smoothie_recipe

# Run the app
if __name__ == "__main__":
    main()