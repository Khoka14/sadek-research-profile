import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Sadek Hossain Khoka | Research Profile",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

# Current GitHub file name
PROFILE_IMAGE = BASE_DIR / "profile.jpg.jpg"

# If you later rename it to profile.jpg, this will also work
if not PROFILE_IMAGE.exists():
    PROFILE_IMAGE = BASE_DIR / "profile.jpg"

# Possible sales data locations
SALES_FILE_1 = BASE_DIR / "Sales Data Jan to Dec-2025.xls.xlsx"
SALES_FILE_2 = BASE_DIR / "data" / "Sales Data Jan to Dec-2025.xls.xlsx"


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Research Profile")

st.sidebar.markdown(
    """
    **Sadek Hossain Khoka**

    Researcher  
    Business Analytics & Consumer Behavior
    """
)

st.sidebar.divider()

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

st.sidebar.divider()

st.sidebar.caption(
    "Research interests: Business Analytics • Consumer Behavior • Behavioral Analytics"
)


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.title("Sadek Hossain Khoka")

    st.subheader("Researcher | Business Analytics & Consumer Behavior")

    st.write(
        "I am interested in understanding consumer behavior, consumer psychology, "
        "behavioral analytics, and data-driven decision making through applied "
        "business analytics."
    )

    st.divider()

    # Profile section
    col1, col2 = st.columns([1, 2])

    with col1:

        if PROFILE_IMAGE.exists():
            st.image(
                str(PROFILE_IMAGE),
                width=180
            )
        else:
            st.info("Profile photo will appear here.")

    with col2:

        st.markdown("### Research Interests")

        interests = [
            "Business Analytics",
            "Consumer Behavior",
            "Consumer Psychology",
            "Behavioral Analytics",
            "Data-Driven Decision Making",
            "Consumer Analytics"
        ]

        for interest in interests:
            st.write(f"• {interest}")

    st.divider()

    st.markdown("### Academic Background")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
            **BBA – Management Studies**

            Academic foundation in management, business operations,
            marketing and organizational studies.
            """
        )

    with col2:
        st.info(
            """
            **MBA – Human Resource Management**

            Graduate-level study covering organizational behavior,
            management and human resource practices.
            """
        )

    st.divider()

    st.markdown("### Current Research Direction")

    st.write(
        "My research interests focus on how data and behavioral insights "
        "can be used to understand consumers and support better business decisions."
    )

    st.write(
        "I am particularly interested in the intersection of consumer psychology, "
        "behavioral analytics and business data."
    )


# =========================================================
# ABOUT
# =========================================================

elif page == "About":

    st.title("About Me")

    st.write(
        "I am an emerging researcher interested in Business Analytics, "
        "Consumer Behavior and Consumer Psychology."
    )

    st.write(
        "My academic background combines management studies and human resource "
        "management, while my current learning path is increasingly focused on "
        "data analytics and research."
    )

    st.write(
        "I am developing practical skills in Python, Pandas, NumPy, Matplotlib, "
        "Microsoft Power BI and Microsoft Excel to support data-driven research."
    )

    st.divider()

    st.subheader("Academic Background")

    st.markdown(
        """
        **BBA – Management Studies**

        Focus areas include management, business operations,
        marketing and organizational studies.
        """
    )

    st.markdown(
        """
        **MBA – Human Resource Management**

        Graduate-level academic background in human resource management,
        organizational behavior and management.
        """
    )

    st.divider()

    st.subheader("Research Approach")

    st.write(
        "My approach is to combine business knowledge with quantitative and "
        "data-analytic methods to investigate practical business and consumer problems."
    )


# =========================================================
# RESEARCH
# =========================================================

elif page == "Research":

    st.title("Research")

    st.subheader("Research Interests")

    research_topics = [
        "Business Analytics",
        "Consumer Behavior",
        "Consumer Psychology",
        "Behavioral Analytics",
        "Consumer Analytics",
        "Data-Driven Decision Making"
    ]

    for topic in research_topics:
        st.write(f"• {topic}")

    st.divider()

    st.subheader("Research Projects & Directions")

    with st.container(border=True):

        st.markdown("### 1. Consumer Behavior and Consumer Psychology")

        st.write(
            "Exploring how consumer attitudes, perceptions, motivations and "
            "decision-making processes influence purchasing behavior."
        )

    with st.container(border=True):

        st.markdown("### 2. Behavioral Analytics")

        st.write(
            "Using behavioral data and analytical techniques to identify "
            "patterns that can support consumer and business insights."
        )

    with st.container(border=True):

        st.markdown("### 3. Data-Driven Consumer Insights")

        st.write(
            "Applying business analytics to understand customer behavior, "
            "purchase patterns and consumer preferences."
        )

    with st.container(border=True):

        st.markdown("### 4. Applied Business Analytics")

        st.write(
            "Using Python, Pandas, NumPy, Excel and Power BI to clean, "
            "analyze and visualize business data."
        )

    st.divider()

    st.subheader("Future Research Development")

    st.write(
        "Future research work may involve statistical analysis, regression "
        "methods, econometric techniques and advanced analytical methods as "
        "these skills are developed further."
    )


# =========================================================
# DATA & ANALYTICS
# =========================================================

elif page == "Data & Analytics":

    st.title("Data & Analytics")

    st.write(
        "I am developing practical data analytics skills for business research "
        "and decision-making."
    )

    st.divider()

    st.subheader("Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🐍 Python")
        st.write("Python programming for business analytics.")

        st.markdown("### 🐼 Pandas")
        st.write("Data manipulation and analysis.")

        st.markdown("### 🔢 NumPy")
        st.write("Numerical computing and analytical operations.")

    with col2:
        st.markdown("### 📈 Matplotlib")
        st.write("Data visualization and analytical charts.")

        st.markdown("### 📊 Power BI")
        st.write("Interactive business dashboards and reporting.")

        st.markdown("### 📗 Excel")
        st.write("Business reporting, analysis and data preparation.")

    with col3:
        st.markdown("### 🧹 Data Cleaning")
        st.write("Preparing and validating datasets.")

        st.markdown("### 🔎 Exploratory Data Analysis")
        st.write("Identifying patterns and trends in data.")

        st.markdown("### 💡 Business Analytics")
        st.write("Turning business data into actionable insights.")

    st.divider()

    st.subheader("Analytics Workflow")

    workflow = [
        "Data Collection",
        "Data Cleaning",
        "Data Validation",
        "Exploratory Data Analysis",
        "Data Visualization",
        "Business Interpretation",
        "Research Insight"
    ]

    for i, step in enumerate(workflow, start=1):
        st.write(f"**{i}.** {step}")


# =========================================================
# SALES DATA EXPLORER
# =========================================================

elif page == "Sales Data Explorer":

    st.title("Sales Data Explorer")

    st.write(
        "This section demonstrates practical business analytics using a sales dataset."
    )

    # Find available sales file
    if SALES_FILE_1.exists():
        sales_file = SALES_FILE_1
    elif SALES_FILE_2.exists():
        sales_file = SALES_FILE_2
    else:
        sales_file = None

    if sales_file is None:

        st.info(
            "Sales dataset is not currently available in the repository. "
            "The Sales Data Explorer will become active when the dataset is uploaded."
        )

    else:

        try:

            df = pd.read_excel(sales_file)

            st.success("Sales dataset loaded successfully.")

            st.subheader("Dataset Preview")

            st.dataframe(
                df,
                use_container_width=True
            )

            st.divider()

            st.subheader("Dataset Summary")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Rows",
                    df.shape[0]
                )

            with col2:
                st.metric(
                    "Columns",
                    df.shape[1]
                )

            with col3:
                st.metric(
                    "Missing Values",
                    int(df.isnull().sum().sum())
                )

            with col4:
                st.metric(
                    "Duplicate Rows",
                    int(df.duplicated().sum())
                )

            st.divider()

            # Identify numerical columns
            numeric_columns = df.select_dtypes(
                include="number"
            ).columns.tolist()

            if numeric_columns:

                st.subheader("Numerical Analysis")

                selected_column = st.selectbox(
                    "Select a numerical variable",
                    numeric_columns
                )

                st.write(
                    f"Analysis of **{selected_column}**"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Total",
                        f"{df[selected_column].sum():,.2f}"
                    )

                with col2:
                    st.metric(
                        "Average",
                        f"{df[selected_column].mean():,.2f}"
                    )

                with col3:
                    st.metric(
                        "Maximum",
                        f"{df[selected_column].max():,.2f}"
                    )

                st.divider()

                st.subheader("Visualization")

                fig, ax = plt.subplots()

                df[selected_column].plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_title(
                    f"{selected_column} Analysis"
                )

                ax.set_ylabel(
                    selected_column
                )

                st.pyplot(fig)

            else:

                st.info(
                    "No numerical columns were detected in the dataset."
                )

        except Exception as e:

            st.error(
                "The dataset could not be loaded."
            )

            st.write(
                f"Error: {e}"
            )


# =========================================================
# CV & CONTACT
# =========================================================

elif page == "CV & Contact":

    st.title("CV & Contact")

    st.subheader("Research Profile")

    st.write(
        "Sadek Hossain Khoka"
    )

    st.write(
        "Researcher | Business Analytics & Consumer Behavior"
    )

    st.divider()

    st.subheader("Academic Background")

    st.write("• BBA – Management Studies")
    st.write("• MBA – Human Resource Management")

    st.divider()

    st.subheader("Research Interests")

    st.write("• Business Analytics")
    st.write("• Consumer Behavior")
    st.write("• Consumer Psychology")
    st.write("• Behavioral Analytics")
    st.write("• Consumer Analytics")
    st.write("• Data-Driven Decision Making")

    st.divider()

    st.subheader("Technical Skills")

    st.write(
        "Python • Pandas • NumPy • Matplotlib • Power BI • Excel • "
        "Data Cleaning • Exploratory Data Analysis • Data Visualization"
    )

    st.divider()

    st.subheader("Research & Professional Links")

    st.write(
        "LinkedIn: Add your LinkedIn profile link here"
    )

    st.write(
        "GitHub: Add your GitHub profile link here"
    )

    st.write(
        "Google Scholar: Add your Google Scholar profile link here"
    )

    st.write(
        "Email: Add your academic/research email here"
    )

    st.divider()

    st.caption(
        "Research Profile | Business Analytics & Consumer Behavior"
    )
