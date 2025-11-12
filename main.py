def main():
    import streamlit as st
    import pandas as pd

    st.title("Period Tracker")

    st.header("Cycles History")
    data = pd.read_parquet("./data/historical-data.parquet")

    st.table(data)


if __name__ == "__main__":
    main()
