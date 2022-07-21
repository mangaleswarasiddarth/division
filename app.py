import streamlit as st


st.header("Divsion")
a=st.number_input("enter first number")
b=st.number_input("enter second number or divisor")

st.write("Division of 2 given numbers")
if b==0:
	st.write("error")
else:
	c=a/b
	st.write(c)
