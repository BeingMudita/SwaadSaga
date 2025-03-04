# Food Recommendations App

## Description

The **Food Recommendations App** provides personalized food recommendations based on your cuisine, diet, and course preferences. The app offers a collection of food items from a database and allows users to explore detailed information about each dish, including ingredients, prep time, and instructions.

## Features

- **Filter by Cuisine**: Select your preferred cuisine (e.g., Indian, Chinese, etc.).
- **Diet Preferences**: Choose between vegetarian or non-vegetarian options.
- **Course Selection**: Filter dishes based on the course (e.g., Lunch, Dinner, Snacks).
- **Detailed Information**: View the ingredients, prep time, and detailed instructions for each recipe.

## Technologies Used

- **Streamlit**: For building the user interface and handling user interactions.
- **SQLite**: For managing the food data and storing recipes.
- **Python**: For backend logic and database interactions.
- **Pandas**: For loading and processing data from CSV files into the database.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Streamlit
- SQLite
- Pandas

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/food-recommendations-app.git
    cd food-recommendations-app
    ```

2. **Set up a Virtual Environment** (optional, but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App**:
    ```bash
    streamlit run app.py
    ```

### Note
The app uses a database (`food_recommendations.db`) that is populated with data from the `indian_food_recipes.csv` file. Make sure that the dataset file is present in the root directory.

## Database Schema

The app uses an SQLite database to store food recommendations. The database contains a `food` table with the following columns:

- `id`: Unique identifier for each food item.
- `name`: Name of the food item.
- `image_url`: URL of the food image.
- `description`: Description of the food item.
- `cuisine`: Cuisine type (e.g., Indian, Chinese).
- `course`: Meal course (e.g., Lunch, Dinner).
- `diet`: Diet preference (e.g., Vegetarian, Non-Vegetarian).
- `prep_time`: Preparation time for the recipe.
- `ingredients`: Ingredients required for the recipe.
- `instructions`: Instructions for preparing the dish.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The food data is sourced from the "Indian Food and Its Recipes" dataset on Kaggle.
- Streamlit for providing a simple and powerful interface for building web apps.

