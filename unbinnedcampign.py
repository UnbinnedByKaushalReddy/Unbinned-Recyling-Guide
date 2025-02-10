import streamlit as st

recycling_centers = {
    "Frisco": [
        {"name": "Frisco Environmental Collection Center", "address": "6616 Walnut St, Frisco, TX"},
        {"name": "Target Recycling Station", "address": "3201 Preston Rd, Frisco, TX"},
        {"name": "Whole Foods Market", "address": "9280 Dallas Pkwy, Frisco, TX"},
        {"name": "Walmart Plastic Bag Drop-Off", "address": "8555 Preston Rd, Frisco, TX"},
    ],
    "Plano": [
        {"name": "Plano Recycling Drop-Off", "address": "4200 W Plano Pkwy, Plano, TX"},
        {"name": "Kroger Recycling", "address": "Coit Rd, Plano, TX"},
        {"name": "Tom Thumb Bag Drop-Off", "address": "3945 Legacy Dr, Plano, TX"},
        {"name": "Trader Joe’s Recycle Center", "address": "2400 Preston Rd, Plano, TX"},
    ],
    "Dallas": [
        {"name": "Dallas Recycling Center", "address": "123 Green Ave, Dallas, TX"},
        {"name": "EcoDrop Dallas", "address": "789 Blue St, Dallas, TX"},
        {"name": "Sprouts Farmers Market", "address": "11722 Marsh Ln, Dallas, TX"},
        {"name": "Lowe’s Plastic Bag Recycle Bin", "address": "11920 Inwood Rd, Dallas, TX"},
    ],
    "Austin": [
        {"name": "Austin Recycling Center", "address": "2514 Business Center Dr, Austin, TX"},
        {"name": "H-E-B Plastic Bag Recycle Station", "address": "7301 N FM 620, Austin, TX"},
        {"name": "Central Market Drop-Off", "address": "4477 S Lamar Blvd, Austin, TX"},
        {"name": "Whole Foods Market", "address": "525 N Lamar Blvd, Austin, TX"},
    ],
    "Houston": [
        {"name": "Houston Eco Recycling", "address": "5900 Westpark Dr, Houston, TX"},
        {"name": "H-E-B Plastic Bag Drop", "address": "1701 W Alabama St, Houston, TX"},
        {"name": "Walmart Recycle Bin", "address": "2391 S Wayside Dr, Houston, TX"},
        {"name": "Trader Joe’s Recycle Center", "address": "1440 S Voss Rd, Houston, TX"},
    ],
}

st.set_page_config(page_title="Unbinned Recycling Guide", page_icon="♻️", layout="wide")

st.title("♻️ Unbinned: Plastic Bag Recycling Guide 🌍")
st.image("https://images.unsplash.com/photo-1604187351574-c75ca79f5807?q=80&w=3870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
         caption="Stop plastic waste. Recycle responsibly!", use_column_width=True)

st.markdown("### 🧐 Do You Know Where Plastic Bags Should Be Recycled?")
user_recycle = st.radio("Where do plastic bags go?", ("Curbside Bin", "Trash", "Designated Drop-Off Locations"))

if user_recycle == "Curbside Bin":
    st.error("⚠️ Nope! Plastic bags **CANNOT** go in curbside bins. They jam recycling machines.")
elif user_recycle == "Trash":
    st.warning("🚨 Not ideal! Plastic bags should be **recycled properly** at drop-off locations.")
else:
    st.success("✅ Correct! Plastic bags should be taken to **designated drop-off locations**, like grocery stores.")

st.markdown("### 📍 Find a Drop-Off Location Near You")
user_city = st.selectbox("Select your city:", list(recycling_centers.keys()))

st.write("♻️ **Nearest Recycling Centers**:")
for center in recycling_centers[user_city]:
    st.write(f"- **{center['name']}** ({center['address']})")

st.markdown("### 🔢 Don't See Your City? Enter Your ZIP Code")
user_zip = st.text_input("Enter your ZIP code:")
if user_zip:
    st.info(f"🔍 Searching for recycling centers near **ZIP Code {user_zip}**... (Feature Coming Soon!)")

st.markdown("### 🌱 Eco-Friendly Alternatives")
st.write("- **Reusable Tote Bags** 🛍️ – Durable and stylish!")
st.write("- **Paper Bags** 📦 – Recyclable and compostable!")
st.write("- **Biodegradable Bags** 🌿 – A greener option!")

st.markdown("### 🏆 Take the Quick Recycling Quiz!")
quiz_question = st.radio("How long does it take for a plastic bag to decompose?", ("5 years", "50 years", "500+ years"))

if quiz_question == "5 years":
    st.error("❌ Nope! Plastic bags last way longer than that.")
elif quiz_question == "50 years":
    st.warning("⚠️ Close, but plastic bags take even longer to break down!")
else:
    st.success("✅ Correct! Plastic bags take **over 500 years** to decompose.")

st.success("🚀 Thank you for making a difference! Let's keep plastic bags *Unbinned*!")

st.markdown("---")
st.markdown("📍 *Powered by Unbinned – A Sustainability Initiative led by Kaushal Reddy Duddugunta*")
st.markdown("🌍 Follow us on Instagram: [@unbinnedcampaign](#)")
