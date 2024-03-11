import streamlit as st

# Set page configuration
st.set_page_config(page_title="NutriLens")
st.header("NutriLens")



# Navigation menu
page = st.sidebar.radio("Navigation", ["Home", "About Us", "Contact Us"])

def parse_gemini_response(response):
    # Parse the response here to extract numerical data for plotting
    # For example, split the response and extract numerical values
    numerical_data = [float(item.split('-')[-1].strip()) for item in response.split('\n')]
    return numerical_data

# Define the content for each page
if page == "Home":
    st.header("Let's Begin")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
        #  image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    submit = st.button("Tell me about the total calories")
    clear = st.button("Delete the uploaded image")
    graph = st.button("Generate Graph")


    input_prompt = """
    You are an expert in nutritionist where you need to see the food items from the image
    and
    calculate the total calories, also provide the details of every food items with calories intake in below format
    1. Item 1 - no of calories
    2. Item - no of calories
    - - --
    Finally you can also mention whether the food is healthy or not and also mention the
    percentage split of the ratio of carbohydrates, fats, fibers, sugar and other things required in our diet.
    Suggest alternate recipes with better nutrition for the same.
    """
 
    # Button to generate graph
    if graph:
        if uploaded_file is not None:
            # Get Gemini response
            prompt = """
            Generate statistical data suitable for plotting based on the image of the food items. Include information such as calories, nutrients, or any other relevant numerical data. Please provide data in a format suitable for creating a graph using Plotly."""
            # gemini_response = get_gemini_response(prompt, uploaded_file)

            # Parse Gemini response to extract numerical data
            # numerical_data = parse_gemini_response(gemini_response)

            # Create plotly graph
            fig = go.Figure(data=[go.Histogram(x=numerical_data)])
            fig.update_layout(title='Histogram of Numerical Data', xaxis_title='Value', yaxis_title='Frequency')

            # Display the plot
            st.plotly_chart(fig)
    else:
        st.error("Please upload an image first.")

    if clear:
        uploaded_file =None

    if submit:
        # image_data= input_image_setup(uploaded_file)
        # response = get_gemini_response(input_prompt,image_data)
        st.header("The Response is")
        # st.write(response)

if page == "About Us":
    st.header("About Us")  
    st.write("""
    NutriLens is a nutritionist tool developed to analyze food items from images and provide detailed information about their nutritional content. 
    Our team is passionate about helping individuals make healthier food choices by providing accurate and insightful data about their diet.
    
    *Key Features:*
    
    - *Food Recognition:* NutriLens uses advanced image recognition technology to identify various food items in an image.
    
    - *Calorie Calculation:* It calculates the total calories of the food items detected in the image.
    
    - *Nutritional Details:* NutriLens provides detailed information about the nutritional content of each food item, including the breakdown of carbohydrates, fats, fibers, sugar, and other nutrients.
    
    - *Health Assessment:* Based on the nutritional information, NutriLens assesses whether the food is healthy or not and suggests alternate recipes with better nutrition.
    
    *Meet the Team:*
    
    - *Awnish Ranjan:* [LinkedIn](https://www.linkedin.com/in/awnish-ranjan-93a725251/)
    
    - *Swati Swapna:* [LinkedIn](https://www.linkedin.com/in/swati-swapna/)
    
    - *Animesh Jha:* [LinkedIn](https://www.linkedin.com/in/animesh-jha-6bb9721b4/)
    
    - *Ujjawal Kantt:* [LinkedIn](https://www.linkedin.com/in/ujjawal-kantt-069aba269/)
    
    We are committed to providing users with a valuable tool to improve their nutritional habits and overall health.
    """)
    
elif page == "Contact Us":
    st.header("Contact Us")
    st.write("""
    Thank you for your interest in NutriLens! If you have any questions, feedback, or suggestions, please feel free to reach out to us.
    
    *Email:* contact@nutrilens.com
    
    *Phone:* +91 (...........)
    
    *Address:* 
    NutriLens Headquarters
    123 Nutrition Street
    Healthyville, NutriLand
    
    We look forward to hearing from you!
    """)

# Add a footer with hyperlinks
st.markdown(
    """
    <style>
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0E1117;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
    </style>
    <footer>
        <a href='https://www.linkedin.com/in/awnish-ranjan-93a725251/'>Awnish Ranjan</a> ⚡
        <a href='https://www.linkedin.com/in/swati-swapna/'>Swati Swapna</a> ⚡
        <a href='https://www.linkedin.com/in/animesh-jha-6bb9721b4/'>Animesh Jha</a> ⚡
        <a href='https://www.linkedin.com/in/ujjawal-kantt-069aba269/'>Ujjawal Kantt</a>
        <br>
        © Tema Buddha 2024
    </footer>
    """,
    unsafe_allow_html=True
)