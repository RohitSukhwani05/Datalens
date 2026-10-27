
import streamlit as st
import pandas as pd

st.title("DataLens")


uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(data)

    st.subheader("Dataset Information")
    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])
    
    st.subheader("Data Quality Report")

    # Count missing values in each column
    missing_values = data.isnull().sum()

    st.write("Missing values in each column:")
    st.dataframe(missing_values)

    # Count duplicate rows
    duplicate_count = data.duplicated().sum()

    st.write("Number of duplicate rows:", int(duplicate_count))
    st.subheader("Data Cleaning")

    remove_missing = st.checkbox("Remove rows with missing values")
    remove_duplicates = st.checkbox("Remove duplicate rows")

    cleaned_data = data.copy()

    if remove_missing:
        cleaned_data = cleaned_data.dropna()

    if remove_duplicates:
        cleaned_data = cleaned_data.drop_duplicates()

    st.write("Rows after cleaning:", cleaned_data.shape[0])

    st.subheader("Cleaned Data Preview")
    st.dataframe(cleaned_data)

    csv_file = cleaned_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv_file,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
    st.subheader("Data Visualization")


    numeric_columns = cleaned_data.select_dtypes(include="number").columns

    if len(numeric_columns) > 0 and not cleaned_data.empty:

        selected_column = st.selectbox(
            "Choose a column to visualize",
            numeric_columns
        )

        if "Name" in cleaned_data.columns:
            st.bar_chart(cleaned_data, x="Name", y=selected_column)
        else:
            st.bar_chart(cleaned_data, y=selected_column)

    else:
        st.info("No numerical data available for charts after cleaning.")