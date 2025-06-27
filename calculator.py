import streamlit as st


st.title("Simple Calculator")
st.write("This is a simple calculator built with streamlit")

c1,c2=st.columns(2) #to create columns to input a value


fnum=c1.number_input("Enter the  first number",value=0)
snum=c2.number_input("Enter the  second number",value=0)

options=["Add","Subtract","Multiply","Division"]
choice=st.radio("Select operations",options) #in radioonly one option is selected at a time
button=st.button("Calculate")
result=0
if button:
    if choice=="Add":
        result=fnum+snum
    if choice=="Subtract":
        result=fnum-snum
    if choice=="Multiply":
        result=fnum*snum
    if choice=="Add":
        result=fnum//snum
st.success(f"Result:{result}")   
st.balloons()        
