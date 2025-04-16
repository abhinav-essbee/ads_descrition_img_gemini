from google import generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load environment variables
load_dotenv()

# Get the API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the genai client
genai.configure(api_key=gemini_api_key)

# Load the Gemini Pro Vision model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Load the image using Pillow
image = Image.open("download.jpg")


# Create the prompt with the image
contents = [
    image,
    "Using this image, find the product in it and format a description and title for the product for posting in an e-commerce ad page."
]

# Generate the response
try:
    response = model.generate_content(contents)
    print(response.text)
except Exception as e:
    print("Error generating content:", e)

