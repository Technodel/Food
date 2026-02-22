import streamlit as st
import random
from PIL import Image

# --- Page Config for Mobile ---
st.set_page_config(page_title="شو بدنا ناكل؟", page_icon="🍴")

# CSS for Mobile Optimization and Right-to-Left (RTL) Support
st.markdown("""
    <style>
    /* Make buttons bigger for phone thumbs */
    div.stButton > button:first-child {
        height: 3.5em;
        width: 100%;
        font-size: 22px;
        font-weight: bold;
        border-radius: 12px;
        background-color: #f04f43;
        color: white;
    }
    /* Right to Left for Arabic text and Alignment */
    .stMarkdown, .stAlert, h1, h2, h3 {
        direction: rtl;
        text-align: right;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        font-size: 14px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Image ---
try:
    image = Image.open("food.png")
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.warning("image 'food.png' not found in directory.")

def load_meals():
    try:
        with open("food.txt", "r", encoding="utf-8") as f:
            content = f.read()
        
        if "APP section" in content:
            parts = content.split("APP section")
            plates = [p.strip() for p in parts[0].split('\n') if p.strip()]
            apps = [a.strip() for a in parts[1].split('\n') if a.strip()]
        else:
            plates = [p.strip() for p in content.split('\n') if p.strip()]
            apps = []
        return plates, apps
    except FileNotFoundError:
        return ["ملف food.txt غير موجود!"], []

# --- Logic ---
plates, apps = load_meals()

st.title("🍴 شو بدنا ناكل اليوم؟")

# Session State
if 'current_plate' not in st.session_state:
    st.session_state.current_plate = None
if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

# Interaction Area
st.subheader("تفضلي ستنا")
if st.button("🎲 اقترحي طبخة"):
    st.session_state.current_plate = random.choice(plates)
    st.session_state.confirmed = False

# Display Selection
if st.session_state.current_plate:
    st.markdown("---")
    st.markdown(f"### شو رأيك بـ:")
    st.info(f"## **{st.session_state.current_plate}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ تمام"):
            st.session_state.confirmed = True
            
    with col2:
        if st.button("❌ لا، غيريها"):
            st.session_state.current_plate = random.choice(plates)
            st.session_state.confirmed = False
            st.rerun()

# Appetizer Reveal
if st.session_state.confirmed:
    st.balloons()
    if apps:
        app_choice = random.choice(apps)
        st.success(f"**ألف صحة!** فيكي تعملي حدّها: \n\n ### 🥗 {app_choice}")
    else:
        st.success("**ألف صحة!**")

# --- Footer ---
st.markdown("""
    <div class="footer">
        By Galaxy<br>
        03659872
    </div>
    """, unsafe_allow_html=True)
