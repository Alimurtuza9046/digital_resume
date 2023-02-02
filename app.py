from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
#profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Murtuza Syed Ali"
PAGE_ICON = ":wave:"
NAME = "Murtuza Syed Ali"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "murtuza.syedali@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
#with col1:
    #st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Regional Sales Manager, Western Region | Reichle & De-Massari AG**")
st.write("January 2020 – July 2021")
st.write(
    """
- Implemented risk-price strategy for project bidding which increased the winning probability by 30% annually.
- Developed and monitored annual and multi-year client strategy work plans, resulting in increased revenue by 8%.
- Provided revisions to strategy and execution plans depending on business initiatives, aided in meeting yearly targets.
- Collaborated with product management teams to identify potential new product offerings.
- Executed function/area objectives that supported continuous quarterly improvements
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Developer, Legrand Data Center Solutions | Legrand Saudi Arabia**")
st.write("January 2016 – December 2019")
st.write(
    """
- Implemented warranty claim validation system using avoidance method by assessing various data points from SQL database, resulting in 50% reduction in erroneous claims, a 5% rise in yearly revenue.
- Developed a Python based quote tool that offered specific logistic costs, custom duty for the product category, and currency conversion rates, allowing for more precise offers resulting in a 10% boost in revenue.
- Created dynamic dashboards in Salesforce and PowerBI, which were utilized by top executives to track the new and current businesses, increased staff productivity by 25%.
- Improved demand forecasting by tracking macroeconomic factors such as GDP, stock market performance, employment statistics, and home sales data, which decreased short-term forecast errors by up to 38% and increased inventory accuracy by up to 15%.
- Conducted exploratory data analysis of customer environments using Python to recommend and drive technical solutions that address their business needs and pain points.
- Successfully increased revenue by up to 20% by providing expert level technical guidance on Legrand Data Center Solutions during the sales process.
- Delivered on-site or remote proof of concepts for potential customers, translating complex technical problems into tangible business value.
- Collaborated with senior engineers in designing of building automation system that monitored and gathered operational data for all machinery in the facility.
- Implemented rigorous supply chain partner pre-screening procedure to minimize bribery, product counterfeiting, and bogus warranty certification, resulting in stronger brand confidence.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Pre-Sales Engineer, Legrand Data Center Solutions | Legrand Saudi Arabia**")
st.write("June 2013 – December 2015")
st.write(
    """
- Conducted exploratory data analysis of customer environments using Python to recommend and drive technical solutions that address their business needs and pain points.
- Successfully increased revenue by up to 20% by providing expert level technical guidance on Legrand Data Center Solutions during the sales process.
- Delivered on-site or remote proof of concepts for potential customers, translating complex technical problems into tangible business value.
- Coordinated with marketing team to develop marketing campaigns for new products. 
"""
)

