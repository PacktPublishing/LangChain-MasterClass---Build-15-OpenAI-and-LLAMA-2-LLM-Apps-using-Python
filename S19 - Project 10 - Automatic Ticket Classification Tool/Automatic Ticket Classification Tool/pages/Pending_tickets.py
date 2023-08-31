import streamlit as st
 
st.title('Departments')
 
# Create tabs
tab_titles = ['HR Support', 'IT Support', 'Transportation Support']
tabs = st.tabs(tab_titles)
 
# Add content to each tab
with tabs[0]:
    st.header('HR Support tickets')
    for ticket in st.session_state['HR_tickets']:
        st.write(str(st.session_state['HR_tickets'].index(ticket)+1)+" : "+ticket)
    
 
with tabs[1]:
    st.header('IT Support tickets')
    for ticket in st.session_state['IT_tickets']:
        st.write(str(st.session_state['IT_tickets'].index(ticket)+1)+" : "+ticket)
 
with tabs[2]:
    st.header('Transportation Support tickets')
    for ticket in st.session_state['Transport_tickets']:
        st.write(str(st.session_state['Transport_tickets'].index(ticket)+1)+" : "+ticket)
    
 