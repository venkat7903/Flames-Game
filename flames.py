import streamlit as st
st.title("Welcome to Flames Game")

a=st.text_input("Enter Your Name: ").strip().lower()
b=st.text_input("Enter Your Partner Name: ").strip().lower()
common = set(a) & set(b)
for i in common:
   a.replace(i,'',1)
   b.replace(i,'',1)
if a and b:
    n=len(a) + len(b)
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    while len(flames) > 1:
        n1 = len(flames)
        rem = (n % n1) - 1
        if rem >= 0:
            first_part = flames[:rem]
            sec_part = flames[rem+1:]
            flames = sec_part+first_part
        else:
            flames = flames[: rem]
    res = ''.join(flames)
    st.text(f'Your Relationship is {res}')