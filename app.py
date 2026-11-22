import streamlit as st

st.set_page_config(
    page_title="StructGuard AI",
    page_icon="SG",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
[data-testid="stSidebar"] { background: #12263A; }
[data-testid="stSidebar"] * { color: #F5F8FB; }
[data-testid="stMetric"] { background: #F4F7FA; border: 1px solid #DDE7EF; border-radius: 10px; padding: 12px; }
.block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

overview = st.Page("pages/overview.py", title="Overview", icon="🏠", default=True)
cracks = st.Page("pages/crack_analytics.py", title="Crack Analytics", icon="🔍")
setup = st.Page("pages/material_setup.py", title="Material & Specimen", icon="⚙️")
som = st.Page("pages/som_analysis.py", title="SOM Analysis", icon="📐")
reports = st.Page("pages/reports.py", title="Reports", icon="📄")

pg = st.navigation([overview, cracks, setup, som, reports])
pg.run()
