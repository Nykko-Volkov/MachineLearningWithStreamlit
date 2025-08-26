import streamlit as st

x = st.text_input("Enter your name", max_chars=10)
if st.button("Submit"):
    st.write(f"Hello, {x}!")

primary_button = st.button("Primary Button")
if primary_button:
    st.write("Primary Button Clicked!")





select = st.selectbox("Select a number", options=[1, 2, 3, 4, 5])
st.write(f"You selected: {select}")


radio = st.radio("Select a color", options=["Red", "Blue", "Green"])
st.write(f"You selected: {radio}")



# make a form for school admissiona dna save tersult as csv file
with    st.form("admission_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    department = st.selectbox("Department", options=["CSE", "ECE", "MECH", "CIVIL"])
    submit = st.form_submit_button("Submit")
    if submit:
        st.write("Form Submitted")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Department: {department}")
        
        # save the data to a csv file
        import pandas as pd
        df = pd.DataFrame({"Name": [name], "Age": [age], "Department": [department]})
        df.to_csv("admission_data.csv", mode='a', header=False, index=False)
        st.success("Data saved to admission_data.csv")