import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unbinned Guide", page_icon="♻️", layout="wide")

# Header Section
st.title("♻️ Unbinned Guide: Plastic Bag Recycling Made Easy 🌍")
st.markdown("### Helping you find the right way to recycle plastic bags and adopt eco-friendly habits.")

# Header Image
st.image(
    "https://images.unsplash.com/photo-1604187351574-c75ca79f5807?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    caption="Stop plastic waste. Recycle responsibly!",
    use_column_width=True
)

# Split Layout for Interaction
col1, col2 = st.columns(2)

# Recycling Knowledge Check
with col1:
    st.subheader("🧐 Are You Recycling Plastic Bags Correctly?")
    user_recycle = st.radio(
        "Where do plastic bags go?",
        ("Curbside Bin", "Trash", "Designated Drop-Off Locations"),
        index=None
    )

    if user_recycle == "Curbside Bin":
        st.error("⚠️ Incorrect! Plastic bags **CANNOT** go in curbside bins as they jam recycling machines.")
    elif user_recycle == "Trash":
        st.warning("🚨 Not ideal! Plastic bags should be **recycled at designated drop-off locations**.")
    elif user_recycle == "Designated Drop-Off Locations":
        st.success("✅ Correct! Plastic bags should be taken to **grocery store drop-off points or special collection centers**.")

# Drop-off Location Finder
with col2:
    st.subheader("📍 Find a Drop-Off Location Near You")
    recycling_centers = {
        "Frisco": ["Frisco Environmental Collection Center", "Target Recycling Station", "Whole Foods Market"],
        "Plano": ["Plano Recycling Drop-Off", "Kroger Recycling", "Trader Joe’s Recycle Center"],
        "Dallas": ["Dallas Recycling Center", "Sprouts Farmers Market", "Lowe’s Plastic Bag Recycle Bin"],
        "Austin": ["Austin Recycling Center", "H-E-B Plastic Bag Recycle Station", "Whole Foods Market"],
        "Houston": ["Houston Eco Recycling", "H-E-B Plastic Bag Drop", "Trader Joe’s Recycle Center"]
    }

    user_city = st.selectbox("Select your city:", list(recycling_centers.keys()))

    st.write(f"**♻️ Nearest Recycling Centers in {user_city}:**")
    for center in recycling_centers[user_city]:
        st.write(f"- {center}")

# Alternative Entry for ZIP Code
st.subheader("🔢 Enter Your ZIP Code for More Locations")
user_zip = st.text_input("Enter your ZIP code:")
if user_zip:
    st.info(f"🔍 Searching for recycling centers near **ZIP Code {user_zip}**... (Feature Coming Soon!)")

# Eco-Friendly Alternatives
st.markdown("---")
st.subheader("🌱 Eco-Friendly Alternatives to Plastic Bags")
col3, col4 = st.columns(2)

with col3:
    st.write("✅ **Reusable Tote Bags** – Durable, stylish, and sustainable!")
    st.write("✅ **Paper Bags** – Recyclable and biodegradable.")
    
with col4:
    st.write("✅ **Biodegradable Bags** – Break down naturally, reducing waste.")
    st.write("✅ **Mesh Bags** – Great for groceries and reusable for years.")

# Quick Recycling Quiz
st.markdown("---")
st.subheader("🏆 Quick Recycling Quiz")
quiz_question = st.radio(
    "How long does it take for a plastic bag to decompose?",
    ("5 years", "50 years", "500+ years"),
    index=None
)

if quiz_question == "5 years":
    st.error("❌ Nope! Plastic bags last way longer than that.")
elif quiz_question == "50 years":
    st.warning("⚠️ Close, but plastic bags take even longer to break down!")
elif quiz_question == "500+ years":
    st.success("✅ Correct! Plastic bags take **over 500 years** to decompose.")

# Call to Action
st.success("🚀 Thank you for making a difference! Let's keep plastic bags *Unbinned*!")

# Footer
st.markdown("---")
st.markdown("📍 *Powered by Unbinned – A Student-Led Sustainability Initiative*")
st.markdown("🌍 Follow us on Instagram: [@Unbinned](#)")
