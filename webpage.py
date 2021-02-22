import streamlit as st
import pickle
import numpy as np
model1234=pickle.load(open('model1234.pkl','rb'))


def predict_sales(Item_Type_Combined,Item_Fat_Content,Item_Visibility,Item_MRP,
               Item_Type,Outlet_Establishment_Year,Outlet_Type,Item_Weight,Outlet_Identifier,Outlet_Size,Outlet_Location_Type):

    input=np.array([[Item_Type_Combined,Item_Fat_Content,Item_Visibility,Item_MRP,
               Item_Type,Outlet_Establishment_Year,Outlet_Type,Item_Weight,Outlet_Identifier,Outlet_Size,Outlet_Location_Type]]).astype(np.float64)
               
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Big Mart Sales Predictor")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Big Mart Sales Prediction Web App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Item_Type_Combined = st.text_input("Item_Type_Combined","Type Here")
    Item_Fat_Content = st.text_input("Item_Fat_Content","Type Here")
    Item_Visibility = st.text_input("Item_Visibility","Type Here")
    Item_MRP = st.text_input("Item_MRP","Type Here")
    Item_Type = st.text_input("Item_Type","Type Here")
    Outlet_Establishment_Year = st.text_input("Outlet_Establishment_Year","Type Here")
    Outlet_Type = st.text_input("Outlet_Type","Type Here")
    Item_Weight = st.text_input("Item_Weight","Type Here")
    Outlet_Identifier = st.text_input("Outlet_Identifier","Type Here")
    Outlet_Size = st.text_input("Outlet_Size","Type Here")
    Outlet_Location_Type = st.text_input("Outlet_Location_Type","Type Here")




    '''safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """'''
    sales_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your Sales </h2>
       </div>
    """
    if Item_Fat_Content is 'LowFat': 
        Item_Fat_Content=0
    else:
        Item_Fat_Content=1

    if Outlet_Size is 'Small': 
        Outlet_Size=0
    elif Outlet_Size is 'Medium':
        Outlet_Size=1
    else:
        Outlet_Size=2

    if Outlet_Location_Type is 'Tier 1': 
        Outlet_Location_Type=0
    elif Outlet_Size is 'Tier 2':
        Outlet_Location_Type=1
    else:
        Outlet_Location_Type=2
    
    if Outlet_Type is 'Grocery Store': 
        Outlet_Type=0
    elif Outlet_Type is 'Supermarket Type1	':
        Outlet_Type=1
    elif Outlet_Type is 'Supermarket Type2	':
        Outlet_Type=2
    else:
        Outlet_Type=3

    if Item_Type_Combined is 'Drinks': 
        Item_Type_Combined=0
    elif Item_Type_Combined is 'Food':
        Outlet_Type=1
    else:
        Item_Type_Combined=2
    
    if Item_Type is 'Dairy':
	    Item_Type=4
    elif Item_Type is 'Soft Drinks':
	    Item_Type=14
    elif Item_Type is 'Meat':
	    Item_Type=10
    elif Item_Type is 'Fruits and Vegetables':
	    Item_Type=6
    elif Item_Type is 'Household':
	    Item_Type=9
    elif Item_Type is 'Snack Foods':
	    Item_Type=0
    elif Item_Type is 'Baking Goods':
	    Item_Type=13
    elif Item_Type is 'Health and Hygiene':
	    Item_Type=5
    elif Item_Type is 'Hard Drinks':
	    Item_Type=4
    elif Item_Type is 'Frozen Foods':
	    Item_Type=2
    elif Item_Type is 'Breakfast':
	    Item_Type=8
    elif Item_Type is 'Canned':
	    Item_Type=7
    elif Item_Type is 'Breads':
	    Item_Type=3
    elif Item_Type is 'Starchy Foods':
	    Item_Type=1
    else:
	    Item_Type=11
    


    
    
    if st.button("Predict"):
        output=predict_forest(Item_Type_Combined,Item_Fat_Content,Item_Visibility,Item_MRP,
               Item_Type,Outlet_Establishment_Year,Outlet_Type,Item_Weight,Outlet_Identifier,Outlet_Size,Outlet_Location_Type)
        st.success('The Outlet Sales of Big Mart will be  {}'.format(output))
        st.markdown(sales_html,unsafe_allow_html=True)
    

if __name__=='__main__':
    main()
