import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

st.title("📊 Employee Attrition Dashboard")
st.markdown("This dashboard offers comprehensive HR insights into employee attrition patterns using filters, charts, and key metrics.")

@st.cache_data
def load_data():
    df = pd.read_csv("EA.csv")
    df.drop(columns=["EmployeeCount", "EmployeeNumber", "StandardHours"], inplace=True)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
dept = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
job_role = st.sidebar.multiselect("Job Role", df["JobRole"].unique(), default=df["JobRole"].unique())

filtered_df = df[(df["Department"].isin(dept)) & (df["Gender"].isin(gender)) & (df["JobRole"].isin(job_role))]

st.markdown("### 🧾 Filtered Dataset Preview")
st.dataframe(filtered_df.head())

# Tabs for analysis
tab1, tab2, tab3 = st.tabs(["📈 Macro Insights", "🔬 Micro Insights", "📚 Attrition Specific"])

with tab1:
    st.markdown("#### Attrition Distribution by Department")
    st.write("This chart shows how attrition is spread across departments.")
    fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("#### Gender-wise Attrition Rate")
    st.write("Understand gender differences in attrition.")
    fig2 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("#### Monthly Income Distribution")
    fig3 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("#### Education Field vs Attrition")
    fig4 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("#### Correlation Heatmap")
    corr = filtered_df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=False, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

with tab2:
    st.markdown("#### Age vs Monthly Income")
    st.write("This scatter plot helps examine if age impacts salary.")
    fig5 = px.scatter(filtered_df, x="Age", y="MonthlyIncome", color="Attrition", size="TotalWorkingYears")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("#### Job Level vs Job Satisfaction")
    fig6 = px.box(filtered_df, x="JobLevel", y="JobSatisfaction", color="Attrition")
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("#### Work-Life Balance Analysis")
    fig7 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("#### Training Times vs Performance")
    fig8 = px.scatter(filtered_df, x="TrainingTimesLastYear", y="PerformanceRating", color="Attrition")
    st.plotly_chart(fig8, use_container_width=True)

    st.markdown("#### Years at Company vs Job Role")
    fig9 = px.box(filtered_df, x="JobRole", y="YearsAtCompany", color="Attrition")
    st.plotly_chart(fig9, use_container_width=True)

with tab3:
    st.markdown("#### Attrition Count")
    st.write("Quick view of overall attrition numbers.")
    st.bar_chart(filtered_df["Attrition"].value_counts())

    st.markdown("#### Attrition by Marital Status")
    fig10 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig10, use_container_width=True)

    st.markdown("#### Attrition by Business Travel")
    fig11 = px.histogram(filtered_df, x="BusinessTravel", color="Attrition", barmode="group")
    st.plotly_chart(fig11, use_container_width=True)

    st.markdown("#### Percent Salary Hike Distribution")
    fig12 = px.box(filtered_df, x="Attrition", y="PercentSalaryHike", color="Attrition")
    st.plotly_chart(fig12, use_container_width=True)

    st.markdown("#### Years with Current Manager vs Attrition")
    fig13 = px.violin(filtered_df, y="YearsWithCurrManager", x="Attrition", color="Attrition", box=True)
    st.plotly_chart(fig13, use_container_width=True)

st.markdown("---")
st.caption("Developed for HR strategic insights using Streamlit.")
