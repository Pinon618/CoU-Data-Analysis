"""
In an environment with streamlit, plotly and duckdb installed,
Run with `streamlit run streamlit_app.py`
"""
import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib.patches import Rectangle    

df = pd.read_csv("Coffee_Shop_Sales.csv")
df['total_payment'] = df['unit_price'] * df['transaction_qty']

#######################################
# PAGE SETUP
#######################################



st.set_page_config(page_title="IIUC_Noobies_52", page_icon=":bar_chart:", layout="wide")

def total_sales():
    total_sales = df['total_payment'].sum()

    fig, ax = plt.subplots(figsize=(4,2))
    ax.text(0.5, 0.5, f'Total Sales\n{total_sales}', ha='center', va='center', fontsize=14)
    ax.axis('off')

    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, 
                            color='black', fill=False, linewidth=2)
    ax.add_patch(border_rect)

    st.pyplot(fig)

def avg_daily_sales():
    
    average_sales = df['total_payment'].sum() / 181

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f'Average Daily Sales\n{average_sales:.2f}', ha='center', va='center', fontsize=14)
    ax.axis('off')
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='black', fill=False, linewidth=2)
    ax.add_patch(border_rect)

    st.pyplot(fig)

def total_sell_qty():
    total_sell_qty = df['transaction_qty'].sum()

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f'Total Sales Quantity\n{total_sell_qty:.2f}', ha='center', va='center', fontsize=14)
    ax.axis('off')
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='black', fill=False, linewidth=2)
    ax.add_patch(border_rect)

    st.pyplot(fig)

def monthly_chart():
    
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    monthly_sales = df.groupby([df['transaction_date'].dt.to_period('M'), 'product_type'])['total_payment'].sum().reset_index()
    monthly_sales.columns = ['Month', 'Product Type', 'Total Payment']
    monthly_sales = df.groupby([df['transaction_date'].dt.strftime('%Y-%m'), 'product_type'])['total_payment'].sum().reset_index()

    monthly_sales.columns = ['Month', 'Product Type', 'Total Payment']

    fig = px.bar(
        monthly_sales,
        x='Month',
        y='Total Payment',
        color='Product Type', 
        barmode='group',  
        title='Monthly Sales of All Products',
        labels={'Month': 'Month', 'Total Payment': 'Total Payment', 'Product Type': 'Product Type'},
        text='Total Payment' 
    )
    st.plotly_chart(fig)

def avg_sell_qty():
    avg_sell_qty = df['transaction_qty'].sum()/181

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f'Average Daily Sales Quantity\n{avg_sell_qty:.2f}', ha='center', va='center', fontsize=14)
    ax.axis('off')
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='black', fill=False, linewidth=2)
    ax.add_patch(border_rect)

    st.pyplot(fig)

def avg_sales_per_locations():
    data = {
    'store_location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B', 'Location C'],
    'unit_price': [10, 20, 15, 10, 25, 30],
    'transaction_qty': [3, 2, 5, 4, 6, 1]
    }
    df = pd.DataFrame(data)
    if 'total_payment' not in df.columns:
        df['total_payment'] = df['unit_price'] * df['transaction_qty']
    average_sales_by_location = df.groupby('store_location')['total_payment'].mean()

    st.title('Average Sales per Store Location')
    fig, ax = plt.subplots(figsize=(10, 6))
    average_sales_by_location.plot(kind='bar', ax=ax)
    ax.set_xlabel('Store Location')
    ax.set_ylabel('Average Sales')
    ax.set_title('Average Sales per Store Location')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

def top_product():
    top_product = df.groupby('product_type')['total_payment'].sum().idxmax()
    top_product_sales = df.groupby('product_type')['total_payment'].sum().max()

    top_sales_date = df.groupby('transaction_date')['total_payment'].sum().idxmax()
    top_sales_date_sales = df.groupby('transaction_date')['total_payment'].sum().max()

    top_sales_quantity_product = df.groupby('product_type')['transaction_qty'].sum().idxmax()
    top_sales_quantity = df.groupby('product_type')['transaction_qty'].sum().max()

    least_product = df.groupby('product_type')['total_payment'].sum().idxmin()
    least_product_sales = df.groupby('product_type')['total_payment'].sum().min()

    expensive_product = df.loc[df['unit_price'].idxmax(), 'product_type']
    expensive_product_price = df['unit_price'].max()

    cheap_product = df.loc[df['unit_price'].idxmin(), 'product_type']
    cheap_product_price = df['unit_price'].min()
    st.markdown("""
    <div style="border: 2px solid #007bff; padding: 15px; border-radius: 8px; background-color: #f0f8ff;">
    <h2 style="text-align:center; color:#007bff;">Sales Analysis Summary</h2>
    <p><strong>Top Sales Product:</strong> {0} <br>(Total Sales: {1:.2f})</p>
    <p><strong>Top Sales Date:</strong> {2} <br>(Total Sales: {3:.2f})</p>
    <p><strong>Top Sales Quantity:</strong> {4} <br>(Quantity: {5})</p>
    <p><strong>Least Sales Product:</strong> {6} <br>(Total Sales: {7:.2f})</p>
    <p><strong>Most Expensive Product:</strong> {8} <br>(Price: {9:.2f})</p>
    <p><strong>Least Expensive Product:</strong> {10} <br>(Price: {11:.2f})</p>
    </div>
    """.format(top_product, top_product_sales, 
            top_sales_date.strftime('%Y-%m-%d'), top_sales_date_sales, 
            top_sales_quantity_product, top_sales_quantity,
            least_product, least_product_sales, 
            expensive_product, expensive_product_price,
            cheap_product, cheap_product_price), unsafe_allow_html=True)

def each_product_sales():
    product_sales = df.groupby('product_type')['transaction_qty'].sum().reset_index()
    fig = go.Figure(data=[go.Bar(
        y=product_sales['product_type'],
        x=product_sales['transaction_qty'],
        orientation='h',
        marker=dict(color=product_sales['transaction_qty'], colorscale='Viridis') 
    )])

    fig.update_layout(
        title='Product Sales and Total Transaction Quantity',
        yaxis={'categoryorder': 'total ascending'},
    )
    st.plotly_chart(fig)

def peak_hour():
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])

    df['hour'] = df['transaction_time'].dt.hour

    
    hourly_sales = df.groupby('hour')['total_payment'].sum().reset_index()
    fig = px.line(hourly_sales, x='hour', y='total_payment', title='Hourly Total Sales')
    fig.update_xaxes(title_text='Hour of the Day')
    fig.update_yaxes(title_text='Total Sales')

    
    st.title("Hourly Total Sales")
    #st.write("This chart displays total sales for each hour of the day based on transaction data.")
    st.plotly_chart(fig)

def top_least_product():
    product_sales = df.groupby('product_type')['transaction_qty'].sum()

    top_5_products = product_sales.nlargest(5)

    least_5_products = product_sales.nsmallest(5)

    fig_top_5 = px.pie(top_5_products, values=top_5_products.values, names=top_5_products.index,
                    title='Top 5 Products by Quantity Sold')

    fig_least_5 = px.pie(least_5_products, values=least_5_products.values, names=least_5_products.index,
                        title='Least 5 Products by Quantity Sold')

    st.title("Product Sales Analysis")
    st.write("This app displays the top 5 and least 5 products by quantity sold.")

    st.subheader("Top 5 Products by Quantity Sold")
    st.plotly_chart(fig_top_5)
    st.subheader("Least 5 Products by Quantity Sold")
    st.plotly_chart(fig_least_5)

def product_trend():
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['month_year'] = df['transaction_date'].dt.to_period('M')
    monthly_product_trends = df.groupby(['month_year', 'product_type'])['total_payment'].sum().reset_index()

    monthly_product_trends['month_year'] = monthly_product_trends['month_year'].astype(str)
    st.title('Monthly Product Type Sales Trends')

    # Create the line plot using Plotly
    fig = px.line(
        monthly_product_trends,
        x='month_year',
        y='total_payment',
        color='product_type',
        title='Monthly Product Type Sales Trends',
        labels={'month_year': 'Month', 'total_payment': 'Total Sales', 'product_type': 'Product Type'}
    )
    st.plotly_chart(fig)

def product_dropdown():
    st.title("Product Selection")

    
    product_types = df['product_type'].unique()
    selected_product = st.selectbox("Select a Product Type", product_types)
    filtered_data = df[df['product_type'] == selected_product]
    unique_subcategories = filtered_data[['product_detail', 'unit_price']].drop_duplicates()

    st.subheader(f"Unique Subcategories and Prices for {selected_product}")
    st.write(unique_subcategories)


def overview():
    
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            total_sales()
            avg_daily_sales()

        with subcol2:
            total_sell_qty()
            avg_sell_qty()
    product_trend()
    # Section 1,2 with a chart
    with col2:
        monthly_chart()
        
    col3, col4 = st.columns(2)
    # Section 2,1 with 2 columns
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_product()

        with subcol4:
            each_product_sales()
        product_dropdown()
    # Section 2,2 with 4 rows
    with col4:
        peak_hour()

        top_least_product()

        #product_trend()

        #product_dropdown()

def main():
    st.sidebar.title("Filter")
    level = st.sidebar.radio("Choose One", ['Overview','Location', 'Months', 'Stores'])
    
    if level == 'Overview':
        overview()



if __name__ == "__main__":
    main()

