import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(
    page_title="Anime Recommender",
    layout="wide"
)

# Cache pipeline initialization
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# App title
st.title("🎌 Anime Recommender System")

# User input
query = st.text_input(
    "Enter your anime preferences",
    placeholder="e.g. light-hearted anime with school settings"
)

# Process recommendation
if query:
    with st.spinner("Fetching recommendations for you..."):
        try:
            response = pipeline.recommend(query)

            st.markdown("## 📌 Recommendations")
            st.markdown(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")