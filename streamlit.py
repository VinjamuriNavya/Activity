import pickle
import streamlit as st 


pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)


def predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard):
    prediction=model.predict([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard]])
    print(prediction)
    return prediction

def main():
    st.title("Personal Loan")
    Age = st.text_input("Age Value")
    Experience = st.text_input("Number of years")
    Family = st.text_input("Number of persons")
    Income = st.text_input("Income Value")
    CCAvg = st.text_input("CC Avg Value ")
    Education = st.text_input("Education Value")
    Mortgage = st.text_input("Mortgage Value")
    SecuritiesAccount = st.text_input("Number of accounts")
    CDAccount = st.text_input("CDAccount Value")
    Online = st.text_input("Online Value")
    CreditCard = st.text_input("CreditCard Value")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
