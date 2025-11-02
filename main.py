def main():
    import streamlit as st
    from pymongo import MongoClient

    st.title('Period Tracker')

    @st.cache_resource
    def init_connection():
        uri = st.secrets["mongo"]["uri"]
        return MongoClient(uri)
    
    client = init_connection()

if __name__ == "__main__":
    main()
