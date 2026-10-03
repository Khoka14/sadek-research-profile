import streamlit as st
from pathlib import Path
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Sadek Hossain Khoka | Research Profile",
    page_icon="📊",
    layout="wide",
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

.hero {
    padding: 2.2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #f4f7fb, #eef3f8);
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-size: 2.8rem;
    margin-bottom: .25rem;
}

.hero h3 {
    margin-top: 0;
    font-weight: 500;
}

.tag {
    display: inline-block;
    padding: .35rem .7rem;
    margin: .2rem;
    border-radius: 999px;
    background: #e8eef5;
}

.card {
    padding: 1.2rem;
    border: 1px solid #e4e8ed;
    border-radius: 15px;
    height: 100%;
}

.small {
    color: #667085;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("Research Profile")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "About",
        "Research",
        "Data & Analytics",
        "Sales Data Explorer",
        "CV & Contact"
    ]
)


# =========================================================
# HOME
# =========================================================
if page == "Home":

    image_path = Path("profile.jpg")

    col1, col2 = st.columns([1, 3])

    with col1:

        if image_path.exists():
            st.image(
                str(image_path),
                width=170
            )
        else:
            st.info("Profile photo not found.")

    with col2:

        st.markdown("""
        <div class="hero">

            <h1>Sadek Hossain Khoka</h1>

            <h3>
            Researcher | Business Analytics & Consumer Behavior
            </h3>

            <p>
            Developing an academic and applied research portfolio focused
            on business analytics, consumer behavior, behavioral insights
            and data-driven decision making.
            </p>

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # MAIN AREAS
    # -----------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card">

            <h3>Research</h3>

            <p>
            Exploring consumer behavior, consumer psychology,
            behavioral insights and evidence-based business research.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with c2:

        st.markdown("""
        <div class="card">

            <h3>Analytics</h3>

            <p>
            Using Python, Pandas, NumPy, Power BI and Excel
            for data analysis and visualization.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with c3:

        st.markdown("""
        <div class="card">

            <h3>Data-Driven Insights</h3>

            <p>
            Connecting analytical findings with consumer insights
            and evidence-based business decisions.
            </p>

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # RESEARCH INTERESTS
    # -----------------------------------------------------

    st.subheader("Research Interests")

    interests = [
        "Business Analytics",
        "Consumer Behavior",
        "Consumer Psychology",
        "Behavioral Analytics",
        "Data-Driven Decision Making"
    ]

    for interest in interests:

        st.markdown(
            f'<span class="tag">{interest}</span>',
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # RESEARCH FOCUS
    # -----------------------------------------------------

    st.subheader("Research Focus")

    st.write("""
    My research interests focus on understanding consumer behavior
    and decision-making through data-driven analytical approaches.
    I am particularly interested in how behavioral and psychological
    factors influence consumer choices and how business analytics
    can generate actionable insights from consumer and business data.
    """)


# =========================================================
# ABOUT
# =========================================================
elif page == "About":

    st.title("About Me")

    st.write("""
    I am a business professional developing an academic and applied
    research profile in Business Analytics and Consumer Behavior.

    My research interests center on using data and analytical methods
    to understand consumer behavior, decision-making and behavioral
    patterns. I am particularly interested in connecting quantitative
    business analysis with consumer and behavioral insights.
    """)


    st.subheader("Academic Background")

    st.write("- BBA — Management Studies")
    st.write("- MBA — Human Resource Management")


    st.subheader("Technical Skills")

    skills = [
        "Python",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Microsoft Power BI",
        "Microsoft Excel",
        "Data Cleaning",
        "Exploratory Data Analysis",
        "Data Visualization",
        "Business Analytics",
        "Consumer Analytics"
    ]

    for skill in skills:

        st.markdown(
            f'<span class="tag">{skill}</span>',
            unsafe_allow_html=True
        )


# =========================================================
# RESEARCH
# =========================================================
elif page == "Research":

    st.title("Research")


    projects = [

        (
            "Consumer Behavior & Business Analytics",

            "Exploring how analytical methods can be used to understand "
            "consumer preferences, purchasing patterns and decision-making.",

            "Business Analytics / Consumer Behavior"
        ),

        (
            "Consumer Psychology & Behavioral Analytics",

            "Examining behavioral and psychological factors that may "
            "influence consumer attitudes, preferences and choices.",

            "Consumer Psychology / Behavioral Analytics"
        ),

        (
            "Data-Driven Consumer Insights",

            "Using structured business and consumer data to identify "
            "patterns, trends and actionable insights for decision-making.",

            "Business Analytics / Consumer Analytics"
        ),

        (
            "Applied Business Analytics",

            "Developing practical analytical projects using Python, "
            "Power BI and Excel to transform business data into insights.",

            "Business Analytics / Data Visualization"
        ),
    ]


    for title, description, area in projects:

        st.markdown(f"""
        <div class="card" style="margin-bottom:1rem;">

            <h3>{title}</h3>

            <p>{description}</p>

            <p class="small">
                <b>Area:</b> {area}
            </p>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# DATA & ANALYTICS
# =========================================================
elif page == "Data & Analytics":

    st.title("Data & Analytics Portfolio")


    st.subheader("Tools & Technologies")

    tools = [
        "Python",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Power BI",
        "Microsoft Excel"
    ]

    for tool in tools:

        st.markdown(
            f'<span class="tag">{tool}</span>',
            unsafe_allow_html=True
        )


    st.subheader("Analytical Areas")

    st.markdown("""
    - **Data Cleaning & Preparation**
    - **Exploratory Data Analysis (EDA)**
    - **Business Analytics**
    - **Consumer Analytics**
    - **Data Visualization**
    - **Dashboard Development**
    - **Sales & Performance Analytics**
    """)


    st.subheader("Portfolio Projects")

    st.markdown("""
    1. **Sales Performance Dashboard**
       — customer, brand and monthly performance analysis.

    2. **Customer Risk & Outstanding Analysis**
       — identifying commercial risk indicators from business data.

    3. **Consumer Analytics Projects**
       — exploring consumer patterns and behavioral insights.

    4. **Python Business Analytics Projects**
       — reproducible data cleaning, analysis and visualization.
    """)


# =========================================================
# SALES DATA EXPLORER
# =========================================================
elif page == "Sales Data Explorer":

    st.title("Sales Data Explorer")


    data_path = Path(
        "data/Sales Data Jan to Dec-2025.xls.xlsx"
    )


    if not data_path.exists():

        st.info(
            "Place the Excel file inside the project's data folder "
            "to activate this page."
        )


    else:

        try:

            df = pd.read_excel(
                data_path,
                sheet_name="Sales Data Jan to Dec-2025"
            )


            st.caption(
                f"{len(df):,} rows loaded"
            )


            # -------------------------------------------------
            # METRICS
            # -------------------------------------------------

            cols = st.columns(3)


            with cols[0]:

                st.metric(
                    "Total Sales",
                    f"৳{df['Sales Amount'].sum()/1e7:,.2f} Cr"
                )


            with cols[1]:

                st.metric(
                    "Customers",
                    f"{df['Customer ID'].nunique():,}"
                )


            with cols[2]:

                st.metric(
                    "Brands",
                    f"{df['Brand'].nunique():,}"
                )


            # -------------------------------------------------
            # MONTHLY SALES
            # -------------------------------------------------

            if "Challan Date" in df.columns:

                df["Challan Date"] = pd.to_datetime(
                    df["Challan Date"],
                    errors="coerce"
                )


                monthly = (
                    df.groupby(
                        df["Challan Date"].dt.to_period("M")
                    )["Sales Amount"]
                    .sum()
                )


                monthly.index = monthly.index.astype(str)


                st.subheader("Monthly Sales")

                st.line_chart(monthly)


            # -------------------------------------------------
            # BRAND SALES
            # -------------------------------------------------

            if "Brand" in df.columns:

                st.subheader("Sales by Brand")


                brand_sales = (
                    df.groupby("Brand")["Sales Amount"]
                    .sum()
                    .sort_values(ascending=False)
                )


                st.bar_chart(brand_sales)


            # -------------------------------------------------
            # RAW DATA
            # -------------------------------------------------

            st.subheader("Raw Data Preview")

            st.dataframe(
                df.head(500),
                use_container_width=True
            )


        except Exception as e:

            st.error(
                f"Could not read the Excel file: {e}"
            )


# =========================================================
# CV & CONTACT
# =========================================================
elif page == "CV & Contact":

    st.title("CV & Contact")


    st.subheader("Academic & Research Profile")

    st.write("""
    Researcher interested in Business Analytics, Consumer Behavior,
    Consumer Psychology and Data-Driven Decision Making.
    """)


    st.subheader("Education")

    st.write("- BBA — Management Studies")
    st.write("- MBA — Human Resource Management")


    st.subheader("Technical Skills")

    st.write("""
    Python • Pandas • NumPy • Matplotlib • Power BI •
    Microsoft Excel • Data Cleaning • Data Visualization
    """)


    st.subheader("Links")

    st.write("• LinkedIn — Add your profile link")
    st.write("• GitHub — Add your GitHub link")
    st.write("• Google Scholar — Add your profile link")
    st.write("• Email — Add your professional email")


    st.info(
        "Update the links above with your actual profiles before sharing."
    )


# =========================================================
# SIDEBAR FOOTER
# =========================================================
st.sidebar.markdown("---")

st.sidebar.caption(
    "Research portfolio — built with Python & Streamlit"
)
