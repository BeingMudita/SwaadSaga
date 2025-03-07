import streamlit as st
import sqlite3
import os

# Database connection
db_path = os.path.join(os.path.dirname(__file__), 'food_recommendations.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Streamlit page configuration
st.set_page_config(page_title="SwaadSaga - A journey through the taste of India 🍛", layout="centered")
st.title("🍛 SwaadSaga - A journey through the taste of India 🍛")

# Sidebar filters
st.sidebar.header("Filter Your Preferences")
cuisine = st.sidebar.selectbox("Choose a cuisine:", options=["Any"] + [row[0] for row in cursor.execute("SELECT DISTINCT cuisine FROM food")])
diet = st.sidebar.selectbox("Choose your diet preference:", options=["Any"] + [row[0] for row in cursor.execute("SELECT DISTINCT diet FROM food")])
course = st.sidebar.selectbox("Choose the course:", options=["Any"] + [row[0] for row in cursor.execute("SELECT DISTINCT course FROM food")])

# Build query based on filters
query = "SELECT * FROM food WHERE 1=1"
params = []

if cuisine != "Any":
    query += " AND cuisine = ?"
    params.append(cuisine)
if diet != "Any":
    query += " AND diet = ?"
    params.append(diet)
if course != "Any":
    query += " AND course = ?"
    params.append(course)

# Fetch and store recommendations
if st.button("Get Recommendations"):
    cursor.execute(query, tuple(params))
    items = cursor.fetchall()
    st.session_state["items"] = items

items = st.session_state.get("items", [])

# Display recommendations
if items:
    st.subheader("Here are some recommendations for you:")
    for item in items[:10]:  # Show first 10 items
        st.markdown("---")
        col1, col2 = st.columns([1, 3])
        with col1:
            if item[2]:  # Check if image URL exists
                st.image(item[2], width=120)
        with col2:
            st.write(f"**{item[1]}**")  # Food name
            st.write(item[3])  # Description
            food_id = item[0]  # Food ID

            # Display "See Details" button for each food item
            if st.button(f"See Details of {item[1]}", key=f"details_{food_id}"):
                # Fetch detailed information based on the food_id
                cursor.execute("SELECT * FROM food WHERE id=?", (food_id,))
                food = cursor.fetchone()

                if food:
                    st.image(food[2])  # Image URL
                    st.subheader(food[1])  # Food name
                    st.write(food[3])  # Description
                    st.write(f"Cuisine: {food[4]}")
                    st.write(f"Course: {food[5]}")
                    st.write(f"Diet: {food[6]}")

                    # Ingredients, Prep Time, and Instructions
                    st.markdown(f"**Preparation Time**: {food[7]}")
                    st.markdown(f"**Ingredients**: {food[8]}")
                    st.markdown(f"**Instructions**:\n{food[9]}")
                else:
                    st.write("Details not available for this food.")
else:
    st.write("No recommendations found. Please adjust your filters.")

# Close the connection to the database
conn.close()
