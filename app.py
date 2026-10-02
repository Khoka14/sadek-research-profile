
import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Sadek Hossain Khoka | Research Profile",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
.block-container {max-width: 1150px; padding-top: 2rem;}
.hero {padding: 2.2rem; border-radius: 18px; background: linear-gradient(135deg,#f4f7fb,#eef3f8); margin-bottom: 1.5rem;}
.hero h1 {font-size: 2.8rem; margin-bottom: .25rem;}
.tag {display:inline-block; padding:.35rem .7rem; margin:.2rem; border-radius:999px; background:#e8eef5;}
.card {padding:1.2rem; border:1px solid #e4e8ed; border-radius:15px; height:100%;}
.small {color:#667085;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Research Profile")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Research", "Data & Analytics", "Sales Data Explorer", "CV & Contact"]
)

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Sadek Hossain Khoka</h1>
        <h3>Sales & Business Analytics | Applied Research</h3>
        <p>
        Business professional with experience in Modern Trade, E-commerce and
        Key Account Management, developing an academic and applied research
        portfolio in Business Analytics, Sales Analytics and emerging-market research.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><h3>Research</h3><p>Applied research in business analytics, financial markets and emerging economies.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h3>Analytics</h3><p>Python, data analysis, visualization and Power BI dashboard development.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><h3>Professional</h3><p>Modern Trade, E-commerce, Key Accounts, sales performance and commercial analytics.</p></div>', unsafe_allow_html=True)

    st.subheader("Research Interests")
    for x in ["Business Analytics", "Sales Analytics", "Emerging Markets",
              "Financial Markets", "Applied Economics", "Data Visualization"]:
        st.markdown(f'<span class="tag">{x}</span>', unsafe_allow_html=True)

elif page == "About":
    st.title("About Me")
    st.write("""
    I am a business professional working in Modern Trade and E-commerce,
    with professional experience in sales, key account management and commercial
    operations. Alongside my professional career, I am building research and
    analytical capabilities in Python, data visualization and business analytics.

    My long-term academic interest is to develop evidence-based research that
    connects business decisions with quantitative analysis, particularly in
    emerging-market contexts.
    """)
    st.subheader("Academic Background")
    st.write("- BBA — Management Studies")
    st.write("- MBA — Human Resource Management")
    st.subheader("Current Analytics Skills")
    st.write("Python • Pandas • NumPy • Data Cleaning • Data Visualization • Power BI • Excel")

elif page == "Research":
    st.title("Research")
    projects = [
        ("Oil Price, Exchange Rate & Stock Market Volatility",
         "Examining how oil-price and exchange-rate shocks may transmit into stock-market risk in emerging markets.",
         "Applied Economics / Financial Markets"),
        ("Sales Analytics & Customer Performance",
         "Using transaction-level sales data to examine customer, brand, sales-force and business-unit performance.",
         "Business Analytics / Sales Analytics"),
        ("Business Analytics Applications in FMCG",
         "Exploring how data-driven performance measurement can support commercial decision-making in FMCG environments.",
         "Business Analytics / Commercial Strategy"),
    ]
    for title, desc, area in projects:
        st.markdown(f"""
        <div class="card" style="margin-bottom:1rem;">
        <h3>{title}</h3><p>{desc}</p><p class="small"><b>Area:</b> {area}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Data & Analytics":
    st.title("Data & Analytics Portfolio")
    st.subheader("Tools")
    st.write("Python • Pandas • NumPy • Matplotlib • Power BI • Microsoft Excel")

    st.subheader("Planned Portfolio Projects")
    st.markdown("""
    1. **2025 Sales Performance Dashboard** — customer, brand, SE and monthly analysis.
    2. **Customer Risk & Outstanding Analysis** — identify commercial risk indicators.
    3. **Oil Price + Exchange Rate + Stock Market Risk** — research-oriented time-series analysis.
    4. **Python Business Analytics Projects** — reproducible data cleaning and visualization.
    """)

elif page == "Sales Data Explorer":
    st.title("Sales Data Explorer")
    data_path = Path("data/Sales Data Jan to Dec-2025.xls.xlsx")

    if not data_path.exists():
        st.info("Place the Excel file inside the project's data folder to activate this page.")
    else:
        try:
            df = pd.read_excel(data_path, sheet_name="Sales Data Jan to Dec-2025")
            st.caption(f"{len(df):,} rows loaded")

            cols = st.columns(3)
            with cols[0]:
                st.metric("Total Sales", f"৳{df['Sales Amount'].sum()/1e7:,.2f} Cr")
            with cols[1]:
                st.metric("Customers", f"{df['Customer ID'].nunique():,}")
            with cols[2]:
                st.metric("Brands", f"{df['Brand'].nunique():,}")

            if "Challan Date" in df.columns:
                df["Challan Date"] = pd.to_datetime(df["Challan Date"], errors="coerce")
                monthly = df.groupby(df["Challan Date"].dt.to_period("M"))["Sales Amount"].sum()
                monthly.index = monthly.index.astype(str)
                st.subheader("Monthly Sales")
                st.line_chart(monthly)

            if "Brand" in df.columns:
                st.subheader("Sales by Brand")
                brand_sales = df.groupby("Brand")["Sales Amount"].sum().sort_values(ascending=False)
                st.bar_chart(brand_sales)

            st.subheader("Raw Data Preview")
            st.dataframe(df.head(500), use_container_width=True)
        except Exception as e:
            st.error(f"Could not read the Excel file: {e}")

elif page == "CV & Contact":
    st.title("CV & Contact")
    st.subheader("Professional Profile")
    st.write("Senior Key Account Executive — Modern Trade & E-commerce")
    st.write("Transcom Beverages Limited")
    st.write("Dhaka, Bangladesh")

    st.subheader("Links to add")
    st.write("• LinkedIn")
    st.write("• GitHub")
    st.write("• Google Scholar")
    st.write("• Email")

    st.info("Replace the placeholder links above with your actual profiles before publishing.")

st.sidebar.markdown("---")
st.sidebar.caption("Research portfolio — built with Python & Streamlit")
