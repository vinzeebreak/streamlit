import streamlit as st


def main():
    current_query_string = st.experimental_get_query_string()
    print(type(current_query_string))
    print(current_query_string)
    st.info("Current query string is: " + str(current_query_string))


if __name__ == "__main__":
    main()
