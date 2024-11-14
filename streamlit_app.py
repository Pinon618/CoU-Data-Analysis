"""
In an environment with streamlit, plotly and duckdb installed,
Run with `streamlit run streamlit_app.py`
"""
import random
import numpy as np
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
df['transaction_date'] = pd.to_datetime(df['transaction_date'])






st.set_page_config(page_title="IIUC_Noobies_52", page_icon=":bar_chart:", layout="wide")

def total_sales():
    total_sales = df['total_payment'].sum()

    fig, ax = plt.subplots(figsize=(4,2))
    ax.text(0.5, 0.5, f'Total Sales\n{total_sales:.2f}', ha='center', va='center', fontsize=14)
    ax.axis('off')

    filled_rect = Rectangle((0, 0), 1,1, transform=ax.transAxes,
                        color='white', zorder=1)  
    ax.add_patch(filled_rect)
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
    
    filled_rect = Rectangle((0, 0), 1,1, transform=ax.transAxes,
                        color='white', zorder=1)  
    ax.add_patch(filled_rect)
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, 
                            color='black', fill=False, linewidth=2)
    ax.add_patch(border_rect)
    
    st.pyplot(fig)

def total_sell_qty():
    total_sell_qty = df['transaction_qty'].sum()

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.text(0.5, 0.5, f'Total Sales Quantity\n{total_sell_qty:.2f}', ha='center', va='center', fontsize=14)
    ax.axis('off')
    
    filled_rect = Rectangle((0, 0), 1,1, transform=ax.transAxes,
                        color='white', zorder=1)  
    ax.add_patch(filled_rect)
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, 
                            color='black', fill=False, linewidth=2)
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
    
    filled_rect = Rectangle((0, 0), 1,1, transform=ax.transAxes,
                        color='white', zorder=1)  
    ax.add_patch(filled_rect)
    fig.patch.set_visible(False) 
    border_rect = Rectangle((0, 0), 1, 1, transform=ax.transAxes, 
                            color='black', fill=False, linewidth=2)
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
    <div style="border: 2px solid 
    <h2 style="text-align:center; color:
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
        title='Total Transaction',
        yaxis={'categoryorder': 'total ascending'},
    )
    st.plotly_chart(fig)

def peak_hour():
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])

    df['hour'] = df['transaction_time'].dt.hour

    
    hourly_sales = df.groupby('hour')['total_payment'].sum().reset_index()
    fig = px.line(hourly_sales, x='hour', y='total_payment')
    fig.update_xaxes(title_text='Hour of the Day')
    fig.update_yaxes(title_text='Total Sales')

    
    st.title("Overall Product Demands")
    
    st.plotly_chart(fig)

def top_least_product():
    product_sales = df.groupby('product_type')['transaction_qty'].sum()

    top_5_products = product_sales.nlargest(5)

    least_5_products = product_sales.nsmallest(5)

    fig_top_5 = px.pie(top_5_products, values=top_5_products.values, names=top_5_products.index)

    fig_least_5 = px.pie(least_5_products, values=least_5_products.values, names=least_5_products.index)

    st.title("Product Sales Analysis")
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

    
    fig = px.line(
        monthly_product_trends,
        x='month_year',
        y='total_payment',
        color='product_type',
        #title='Monthly Product Type Sales Trends',
        labels={'month_year': 'Month', 'total_payment': 'Total Sales', 'product_type': 'Product Type'}
    )
    st.plotly_chart(fig)

def product_dropdown():
    st.title("Product Selection")

    
    product_types = df['product_type'].unique()
    selected_product = st.selectbox("Select a Product Type", product_types)
    filtered_data = df[df['product_type'] == selected_product]
    unique_subcategories = filtered_data.groupby(['product_detail', 'unit_price']).size().reset_index(name='count')

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
    
    with col2:
        monthly_chart()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_product()

        with subcol4:
            each_product_sales()
        product_dropdown()
    
    with col4:
        peak_hour()

        top_least_product()

        

        



def astoria_total_qty():
    df['total_payment'] = df['unit_price'] * df['transaction_qty']
    total_transaction_qty_astoria = df[df['store_location'] == 'Astoria']['transaction_qty'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=total_transaction_qty_astoria,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Total Quantity</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )
    st.plotly_chart(fig)

def avg_daily_income():
    
    df['total_payment'] = df['unit_price'] * df['transaction_qty']

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    df_astoria = df[df['store_location'] == 'Astoria']

    average_sell_per_day_astoria = df_astoria.groupby(df_astoria['transaction_date'].dt.date)[
        'total_payment'].sum().mean()
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=average_sell_per_day_astoria,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Average Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )

    st.plotly_chart(fig)

def astoria_total():
    astoria_sales = df[df['store_location'] == 'Astoria']['total_payment'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value= astoria_sales,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Total Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )
    st.plotly_chart(fig)


def astoria_sell_quantity():

    df_astoria = df[df['store_location'] == 'Astoria']
    average_transaction_qty_per_day_astoria = df_astoria.groupby(df_astoria['transaction_date'].dt.date)[
        'transaction_qty'].sum().mean()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=average_transaction_qty_per_day_astoria,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Average Quantity</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,  
        height=120  
    )

    st.plotly_chart(fig)

def Monthly_Sales_for_Astoria():
    df['month'] = df['transaction_date'].dt.month

    df_astoria = df[df['store_location'] == 'Astoria']

    monthly_sales_astoria = df_astoria.groupby('month')['total_payment'].sum()

    colors = ['#800000', '#A52A2A', '#CD5C5C', '#F08080', '#FFA07A', '#FA8072',
              '#E9967A', '#F08080', '#DC143C', '#B22222', '#FF6347', '#FF4500']
 

    fig = go.Figure(data=[go.Bar(
        x=monthly_sales_astoria.index,
        y=monthly_sales_astoria.values,
        marker_color=colors
    )])
 
    
    fig.update_layout(
        title='Monthly Sales for Astoria',
        xaxis_title='Month',
        yaxis_title='Total Sales',
        plot_bgcolor='white',
        font_color='black'
    )
 
    
    
 
    
    st.plotly_chart(fig)
def Percentage_and_Quantity_of_Product_Types_Sold_in_Astoria():
    
    df_astoria = df[df['store_location'] == 'Astoria']
    product_type_sales = df_astoria.groupby('product_type').agg({'total_payment': 'sum', 'transaction_qty': 'sum'})
    product_type_sales = product_type_sales.sort_values('total_payment', ascending=False)
    
    product_type_sales['percentage_of_total_sales'] = (product_type_sales['total_payment'] / product_type_sales[
        'total_payment'].sum()) * 100
 
    
    fig = px.bar(
        product_type_sales,
        x='percentage_of_total_sales',
        y=product_type_sales.index,
        orientation='h',
        labels={'percentage_of_total_sales': 'Percentage of Total Sales', 'index': 'Product Type'},
        title='Sold Product Type',
        text='transaction_qty'
    )
 
    
    fig.update_layout(
        xaxis_title='Percentage of Total Sales',
        yaxis_title='Product Type',
        plot_bgcolor='white',
        font_color='black',
        yaxis=dict(
            title='Product Type',
            automargin=True,
            categoryorder='total ascending'  
        )
    )
 
    
    fig.update_layout(height=600)
 
    
    
 
    
    st.plotly_chart(fig)
def Top_Sold_Product_Category():
    df_astoria = df[df['store_location'] == 'Astoria']
    top_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmax()
    top_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmax()
    
    max_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmax()
    
    overall_quantity_on_max_date = df_astoria[df_astoria['transaction_date'].dt.date == max_selling_date][
        'transaction_qty'].sum()
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'> 
            <br>
            <b>Top Sold Product Category:</b> {top_product_category}<br>
            <b>Top Sold Product Type:</b> {top_product_type}<br>
            <b>Overall Max Selling Date:</b> {max_selling_date}<br>
            <b>Overall Quantity on Max Date:</b> {overall_quantity_on_max_date}
            <br>
        </div>
        """,
        unsafe_allow_html=True
    )

def pie_chart_astoria():
    df_astoria = df[df['store_location'] == 'Astoria']
    top_products_astoria = df_astoria.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    fig1 = px.pie(
        values=top_products_astoria.values,
        names=top_products_astoria.index,
        title='Top 5 Product Types Sold in Astoria by Quantity',
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')

    transaction_qty_counts = df_astoria.groupby('transaction_qty')['transaction_qty'].count()
    specified_quantities = [1, 2, 3, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]

    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title='Percentage of Quantity of Items Bought at a Time in Lower Manhattan',
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_products_astoria.index, values=top_products_astoria.values, title="Top 5 Products"), 1, 1)
    fig.add_trace(go.Pie(labels=filtered_counts.index, values=filtered_counts.values, title="Specified Quantities"), 1, 2)
    fig.update_layout(height=600, width=1000, title_text="Astoria Sales Analysis")
    st.plotly_chart(fig)

def Lowest_Sold_Product_Category():
    
    df_astoria = df[df['store_location'] == 'Astoria']

    lowest_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmin()
 
    
    lowest_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmin()
 
    
    min_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmin()
 
    
    overall_quantity_on_min_date = df_astoria[df_astoria['transaction_date'].dt.date == min_selling_date][
        'transaction_qty'].sum()
 
    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'> 
            <b>Lowest Sold Product Category:</b> {lowest_product_category}<br>
            <b>Lowest Sold Product Type:</b> {lowest_product_type}<br>
            <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
            <b>Overall Quantity on Lowest Date:</b> {overall_quantity_on_min_date}
        </div>
        """,
        unsafe_allow_html=True
    )
def Expensive_lower_Product():
    df_astoria = df[df['store_location'] == 'Astoria']
 
    
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )
 
    
    expensive_product = product_type_analysis.sort_values('unit_price', ascending=False).iloc[0]
    
    cheapest_product = product_type_analysis.sort_values('unit_price').iloc[0]
 
    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'> 
            <b>Expensive Product:</b> {expensive_product.name}<br>
            <b>Average Price:</b> ${expensive_product['unit_price']:.2f}<br>
            <b>Total Quantity:</b> {expensive_product['transaction_qty']}<br><br>
            <b>Cheapest Product:</b> {cheapest_product.name}<br>
            <b>Average Price:</b> ${cheapest_product['unit_price']:.2f}<br>
            <b>Total Quantity:</b> {cheapest_product['transaction_qty']}
        </div>
        """,
        unsafe_allow_html=True
    )
def Astoria_Price_vs_Sell_Quantity():

    df_astoria = df[df['store_location'] == 'Astoria']
 
    
    price_quantity = df_astoria.groupby('unit_price')['transaction_qty'].sum().reset_index()
 
    
    fig = px.line(price_quantity, x='unit_price', y='transaction_qty',
                  title='Astoria: Price vs Sell Quantity')
    fig.update_layout(
        xaxis_title='Price',
        yaxis_title='Sell Quantity',
        plot_bgcolor='white',  
        font_color='black',  
    )
 
    
    st.plotly_chart(fig)
def Hourly_Sales_in_Astoria():
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['hour'] = df['transaction_time'].dt.hour
 
    
    df_astoria = df[df['store_location'] == 'Astoria']
 
    
    hourly_sales_astoria = df_astoria.groupby('hour')['transaction_qty'].sum()
 
    
    fig = px.bar(
        x=hourly_sales_astoria.index,
        y=hourly_sales_astoria.values,
        labels={'x': 'Hour', 'y': 'Total Quantity Sold'},
        title='Hourly Sales in Astoria'
    )
 
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Hour',
        yaxis_title='Total Quantity Sold'
    )
 
    
    st.plotly_chart(fig)
def Astoria_Sales_Analysis():
    
    df_astoria = df[df['store_location'] == 'Astoria']
 
    
    top_products_astoria = df_astoria.groupby('product_type')['transaction_qty'].sum().nlargest(5)
 
    
    fig1 = px.pie(
        values=top_products_astoria.values,
        names=top_products_astoria.index,
        title='Top 5 Product Types Sold in Astoria by Quantity'
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')
 
    
    transaction_qty_counts = df_astoria['transaction_qty'].value_counts()
 
    
    specified_quantities = [1, 2, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]
 
    
    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title='Percentage of Quantity of Items Bought at a Time in Astoria'
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')
 
    
    st.title("Astoria Sales Analysis")
 
    
    st.plotly_chart(fig1)
 
    
    st.plotly_chart(fig2)
def Increasing_Demand_of_Product_Types_in_Astoria():
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
 
    
    df_astoria = df[df['store_location'] == 'Astoria']
 
    
    product_demand = df_astoria.groupby(['product_type', 'transaction_date'])['transaction_qty'].sum().reset_index()
 
    
    product_demand_pivot = product_demand.pivot(index='transaction_date', columns='product_type',
                                                values='transaction_qty').fillna(0)
 
    
    product_demand_cumulative = product_demand_pivot.cumsum()
 
    
    fig = go.Figure()
    for product_type in product_demand_cumulative.columns:
        fig.add_trace(go.Scatter(x=product_demand_cumulative.index, y=product_demand_cumulative[product_type],
                                 mode='lines', name=product_type))
 
    
    fig.update_layout(
        title='Increasing Demand of Product Types in Astoria',
        xaxis_title='Transaction Date',
        yaxis_title='Cumulative Transaction Quantity',
        plot_bgcolor='white',
        font_color='black'
    )
 
    
    
    st.plotly_chart(fig)
def Top_5_Most_Expensive_Product_Types_in_Astoria_by_Unit_Price():
    df_astoria = df[df['store_location'] == 'Astoria']
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )
    top_5_expensive_products = product_type_analysis.sort_values('unit_price', ascending=False).head(5)

    fig = px.bar(
        x=top_5_expensive_products.index,
        y=top_5_expensive_products['unit_price'],
        text=top_5_expensive_products['transaction_qty'], 
        labels={'x': 'Product Type', 'y': 'Average Unit Price', 'text': 'Total Quantity'},
        title='Top 5 Most Expensive Product Types in Astoria',
    )

    fig.update_layout(
        plot_bgcolor='white',
        font_color='black', 
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600,
    )
    st.plotly_chart(fig)

def Top_5_Cheapest_Product_Types_in_Astoria():
    df_astoria = df[df['store_location'] == 'Astoria']

    
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    top_5_cheapest_products = product_type_analysis.sort_values('unit_price').head(5)

    
    fig = px.bar(
        top_5_cheapest_products,
        x=top_5_cheapest_products.index,
        y='unit_price',
        text='transaction_qty',  
        labels={'x': 'Product Type', 'unit_price': 'Average Unit Price'},
        title='Top 5 Cheapest Product Types in Astoria',
        color_discrete_sequence=['#CD5C5C']
    )
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600  
    )
    
    st.plotly_chart(fig)

def astoria():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            astoria_total()
            avg_daily_income()

        with subcol2:
            astoria_total_qty()
            astoria_sell_quantity()
            
    
    
    with col2:
        Monthly_Sales_for_Astoria()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            Top_Sold_Product_Category()
            Expensive_lower_Product()
            Lowest_Sold_Product_Category()


        with subcol4:
            Percentage_and_Quantity_of_Product_Types_Sold_in_Astoria()
        Astoria_Price_vs_Sell_Quantity()
        Top_5_Most_Expensive_Product_Types_in_Astoria_by_Unit_Price()
        
    
    with col4:
        Hourly_Sales_in_Astoria()

        Increasing_Demand_of_Product_Types_in_Astoria()
        pie_chart_astoria()
        Top_5_Cheapest_Product_Types_in_Astoria()

        


def Total_Sell_Kitchen():
    
    total_payment_astoria = df[df['store_location'] == "Hell's Kitchen"]['total_payment'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=total_payment_astoria,
            title={"text": "<span style='font-size:20px;font-weight:bold;'>Total Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',  
        font_color='black',  
        width=120,  
        height=120
    )

    
    st.plotly_chart(fig)
def avg_daily_sale_kitchen():
    total_transaction_qty_astoria = df[df['store_location'] == "Hell's Kitchen"]['transaction_qty'].sum()
    daily_kitchen = total_transaction_qty_astoria/181
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=daily_kitchen,
            title={"text": "<span style='font-size:20px;font-weight:bold;'>Average Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    
    fig.update_layout(
        paper_bgcolor='white',  
        font_color='black',  
        
        
        width=120,  
        height=120
    )

    
    st.plotly_chart(fig)

def avg_daily_income_kitchen():

    
    total_transaction_qty_astoria = df[df['store_location'] == "Hell's Kitchen"]['transaction_qty'].sum()

    
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=total_transaction_qty_astoria,
            title={"text": "<span style='font-size:20px;font-weight:bold;'>Total Quantity</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    
    fig.update_layout(
        paper_bgcolor='white',  
        font_color='black',  
        
        
        width=120,  
        height=120
    )

    
    st.plotly_chart(fig)
def AVG_Sell_Quantity_kitchen():
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df_kitchen = df[df['store_location'] == "Hell's Kitchen"]  
    average_transaction_qty_per_day_kitchen = df_kitchen.groupby(df_kitchen['transaction_date'].dt.date)[
        'transaction_qty'].sum().mean()

    
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=average_transaction_qty_per_day_kitchen,
            title={"text": "<span style='font-size:20px;font-weight:bold;'>Average Quantity</span>"},  
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    
    fig.update_layout(
        paper_bgcolor='white',  
        font_color='black',  
        
        
        width=120,  
        height=120
    )

    
    st.plotly_chart(fig)
def Monthly_Sales_for_Kitchen():

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['month'] = df['transaction_date'].dt.month

    
    df_kitchen = df[df['store_location'] == "Hell's Kitchen"]

    
    monthly_sales_kitchen = df_kitchen.groupby('month')['total_payment'].sum()

    
    colors = ['#800000', '#A52A2A', '#CD5C5C', '#F08080', '#FFA07A', '#FA8072',
              '#E9967A', '#F08080', '#DC143C', '#B22222', '#FF6347', '#FF4500']  # Darker red shades

    
    fig = go.Figure(data=[go.Bar(
        x=monthly_sales_kitchen.index,
        y=monthly_sales_kitchen.values,
        marker_color=colors
    )])

    
    fig.update_layout(
        title="Monthly Sales for Hell's Kitchen",
        xaxis_title='Month',
        yaxis_title='Total Sales',
        plot_bgcolor='white',
        font_color='black'
    )

    
    st.plotly_chart(fig)
def Quantity_of_Each_Product_Type_Sold_in_Kitchen():
    
    df_kitchen = df[df['store_location'] == "Hell's Kitchen"]
    product_type_sales = df_kitchen.groupby('product_type')['transaction_qty'].sum()

    
    product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        x=product_type_sales.index,
        y=product_type_sales.values,
        labels={'x': 'Product Type', 'y': 'Total Quantity Sold'},
        title="Sold Product Type",
    )

    
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Total Quantity Sold',
        height=800,  
        margin={"t": 50, "b": 100}  
    )

    
    st.plotly_chart(fig)
def top_product_category_kitchen():
    
    df_astoria = df[df['store_location'] == "Astoria"]

    
    top_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmax()

    
    top_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmax()

    
    max_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmax()

    
    overall_quantity_on_max_date = df_astoria[df_astoria['transaction_date'].dt.date == max_selling_date][
        'transaction_qty'].sum()

    
    output_string = f"""
    <b>Top Sold Product Category:</b> {top_product_category}<br>
    <b>Top Sold Product Type:</b> {top_product_type}<br>
    <b>Overall Max Selling Date:</b> {max_selling_date}<br>
    <b>Overall Quantity on Max Date:</b> {overall_quantity_on_max_date}
    """

    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px;'>
            {output_string}
        </div>
        """,
        unsafe_allow_html=True
    )

def lowest_selling_product_category_kitchen():

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    lowest_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmin()

    
    lowest_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmin()

    
    min_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmin()

    
    overall_quantity_on_min_date = df_astoria[df_astoria['transaction_date'].dt.date == min_selling_date][
        'transaction_qty'].sum()

    
    output_string = f"""
    <b>Lowest Sold Product Category:</b> {lowest_product_category}<br>
    <b>Lowest Sold Product Type:</b> {lowest_product_type}<br>
    <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
    <b>Overall Quantity on Lowest Date:</b> {overall_quantity_on_min_date}
    """

    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px;'>
            {output_string}
        </div>
        """,
        unsafe_allow_html=True
    )
def expensive_product_kitchen():

    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    expensive_product = product_type_analysis.sort_values('unit_price', ascending=False).iloc[0]
    
    cheapest_product = product_type_analysis.sort_values('unit_price').iloc[0]

    
    output_string = f"""
    **Expensive Product:** {expensive_product.name}  
    **Average Price:** ${expensive_product['unit_price']:.2f}  
    **Total Quantity:** {expensive_product['transaction_qty']}  

    <br><br>

    **Cheapest Product:** {cheapest_product.name}  
    **Average Price:** ${cheapest_product['unit_price']:.2f}  
    **Total Quantity:** {cheapest_product['transaction_qty']}
    """

    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 20px;'>
            {output_string}
        </div>
        """,
        unsafe_allow_html=True
    )
def Kitchen_Price_vs_Sell_Quantity():

    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    price_quantity = df_astoria.groupby('unit_price')['transaction_qty'].sum().reset_index()

    
    fig = px.line(price_quantity, x='unit_price', y='transaction_qty',
                  title="Hell's Kitchen: Price vs Sell Quantity")

    
    fig.update_layout(
        xaxis_title='Price',
        yaxis_title='Sell Quantity',
        plot_bgcolor='white',  
        font_color='black',  
    )

    
    st.plotly_chart(fig)
def Hourly_Sales_in_Kitchen():

    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['hour'] = df['transaction_time'].dt.hour

    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    hourly_sales_astoria = df_astoria.groupby('hour')['transaction_qty'].sum()

    
    fig = px.bar(
        x=hourly_sales_astoria.index,
        y=hourly_sales_astoria.values,
        labels={'x': 'Hour', 'y': 'Total Quantity Sold'},
        title="Hourly Sales in Hell's Kitchen"
    )

    
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Hour of Day',
        yaxis_title='Total Quantity Sold'
    )

    
    
    st.plotly_chart(fig)
def Kitchen_Sales_Analysis():
    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    top_products_astoria = df_astoria.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        values=top_products_astoria.values,
        names=top_products_astoria.index,
        title='Top 5 Product Types Sold in Astoria by Quantity',
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')

    
    transaction_qty_counts = df_astoria.groupby('transaction_qty')['transaction_qty'].count()

    
    specified_quantities = [1, 2, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]

    
    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title="Percentage of Quantity of Items Bought at a Time in Astoria",
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_products_astoria.index, values=top_products_astoria.values), 1, 1)
    fig.add_trace(go.Pie(labels=filtered_counts.index, values=filtered_counts.values), 1, 2)

    
    fig.update_layout(
        height=600,
        width=1000,
        title_text="Hell's Kitchen Sales Analysis"
    )

    
    
    st.plotly_chart(fig)
def Increasing_Demand_of_Product_Types_in_Kitchen():
    
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    product_demand = df_astoria.groupby(['product_type', 'transaction_date'])['transaction_qty'].sum().reset_index()

    
    product_demand_pivot = product_demand.pivot(index='transaction_date', columns='product_type',
                                                values='transaction_qty').fillna(0)

    
    product_demand_cumulative = product_demand_pivot.cumsum()

    
    fig = go.Figure()
    for product_type in product_demand_cumulative.columns:
        fig.add_trace(
            go.Scatter(x=product_demand_cumulative.index, y=product_demand_cumulative[product_type], mode='lines',
                       name=product_type))

    
    fig.update_layout(
        title="Increasing Demand of Product Types in Hell's Kitchen",
        xaxis_title='Transaction Date',
        yaxis_title='Cumulative Transaction Quantity',
        plot_bgcolor='white',
        font_color='black'
    )

    
    
    st.plotly_chart(fig)
def Top_5_Most_Expensive_Product_Types_in_Kitchen():
    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    top_5_expensive_products = product_type_analysis.sort_values('unit_price', ascending=False).head(5)

    
    fig = px.bar(
        x=top_5_expensive_products.index,
        y=top_5_expensive_products['unit_price'],
        text=top_5_expensive_products['transaction_qty'],  
        labels={'x': 'Product Type', 'y': 'Average Unit Price', 'text': 'Total Quantity'},
        title="Top 5 Most Expensive Product Types in Hell's Kitchen",
    )

    
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600,  
        showlegend=False  
    )

    
    
    st.plotly_chart(fig)
def Top_5_Cheapest_Product_Types_in_Kitchen():
    
    df_astoria = df[df['store_location'] == "Hell's Kitchen"]

    
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    top_5_cheapest_products = product_type_analysis.sort_values('unit_price').head(5)

    
    fig = px.bar(
        x=top_5_cheapest_products.index,
        y=top_5_cheapest_products['unit_price'],
        text=top_5_cheapest_products['transaction_qty'],  
        labels={'x': 'Product Type', 'y': 'Average Unit Price', 'text': 'Total Quantity'},
        title="Top 5 Cheapest Product Types in Hell's Kitchen",
        color_discrete_sequence=['#CD5C5C']
    )

    
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600,  
        showlegend=False  
    )

    
    
    st.plotly_chart(fig)


def hellkitchen():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sell_Kitchen()
            avg_daily_sale_kitchen()

        with subcol2:
            
            avg_daily_income_kitchen()
            AVG_Sell_Quantity_kitchen()
            
    
    
    with col2:
        Monthly_Sales_for_Kitchen()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_product_category_kitchen()
            expensive_product_kitchen()
            lowest_selling_product_category_kitchen()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_Kitchen()
        Kitchen_Price_vs_Sell_Quantity()
        Top_5_Most_Expensive_Product_Types_in_Kitchen()

        
    
    with col4:
        Hourly_Sales_in_Kitchen()

        Increasing_Demand_of_Product_Types_in_Kitchen()
        Kitchen_Sales_Analysis()
        Top_5_Cheapest_Product_Types_in_Kitchen()


def lower_total_qty():
    df['total_payment'] = df['unit_price'] * df['transaction_qty']
    total_transaction_qty_lower = df[df['store_location'] == 'Lower Manhattan']['transaction_qty'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=total_transaction_qty_lower,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Total Quantity</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )
    st.plotly_chart(fig)

def avg_lower_income():
    
    df['total_payment'] = df['unit_price'] * df['transaction_qty']

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    df_lower = df[df['store_location'] == 'Lower Manhattan']

    average_sell_per_day_lower = df_lower.groupby(df_lower['transaction_date'].dt.date)[
        'total_payment'].sum().mean()
    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=average_sell_per_day_lower,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Average Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )

    st.plotly_chart(fig)

def lower_total():
    lower_sales = df[df['store_location'] == 'Lower Manhattan']['total_payment'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value= lower_sales,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Total Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )

    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,
        height=120
    )
    st.plotly_chart(fig)

def pie_chart_lower():
    df_astoria = df[df['store_location'] == 'Lower Manhattan']
    top_products_astoria = df_astoria.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    fig1 = px.pie(
        values=top_products_astoria.values,
        names=top_products_astoria.index,
        title='Top 5 Product Types Sold in Lower Manhattan by Quantity',
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')

    transaction_qty_counts = df_astoria.groupby('transaction_qty')['transaction_qty'].count()
    specified_quantities = [1, 2, 3, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]

    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title='Percentage of Quantity of Items Bought at a Time in Lower Manhattan',
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_products_astoria.index, values=top_products_astoria.values, title="Top 5 Products"), 1, 1)
    fig.add_trace(go.Pie(labels=filtered_counts.index, values=filtered_counts.values, title="Specified Quantities"), 1, 2)
    fig.update_layout(height=600, width=1000, title_text="Lower Manhattan Sales Analysis")
    st.plotly_chart(fig)

def lower_sell_quantity():

    df_lower = df[df['store_location'] == 'Lower Manhattan']
    average_transaction_qty_per_day_lower = df_lower.groupby(df_lower['transaction_date'].dt.date)[
        'transaction_qty'].sum().mean()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=average_transaction_qty_per_day_lower,
            title={"text": "<span style='font-size:20px; font-weight:bold;'>Total Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,  
        height=120  
    )

    st.plotly_chart(fig)

def Monthly_Sales_for_Lower_Manhattan():
    df['month'] = df['transaction_date'].dt.month

    df_lower = df[df['store_location'] == 'Lower Manhattan']

    monthly_sales_lower = df_lower.groupby('month')['total_payment'].sum()

    colors = ['#800000', '#A52A2A', '#CD5C5C', '#F08080', '#FFA07A', '#FA8072',
              '#E9967A', '#F08080', '#DC143C', '#B22222', '#FF6347', '#FF4500']
 
    fig = go.Figure(data=[go.Bar(
        x=monthly_sales_lower.index,
        y=monthly_sales_lower.values,
        marker_color=colors
    )])
 
    
    fig.update_layout(
        title='Monthly Sales for Lower Manhattan',
        xaxis_title='Month',
        yaxis_title='Total Sales',
        plot_bgcolor='white',
        font_color='black'
    )
 
    
    
 
    
    st.plotly_chart(fig)
def Percentage_and_Quantity_of_Product_Types_Sold_in_Lower_Manhattan():
    
    df_lower = df[df['store_location'] == 'Lower Manhattan']
    product_type_sales = df_lower.groupby('product_type').agg({'total_payment': 'sum', 'transaction_qty': 'sum'})
    product_type_sales = product_type_sales.sort_values('total_payment', ascending=False)
    
    product_type_sales['percentage_of_total_sales'] = (product_type_sales['total_payment'] / product_type_sales[
        'total_payment'].sum()) * 100
 
    
    fig = px.bar(
        product_type_sales,
        x='percentage_of_total_sales',
        y=product_type_sales.index,
        orientation='h',
        labels={'percentage_of_total_sales': 'Percentage of Total Sales', 'index': 'Product Type'},
        title='Sold Product Type',
        text='transaction_qty'
    )
 
    
    fig.update_layout(
        xaxis_title='Percentage of Total Sales',
        yaxis_title='Product Type',
        plot_bgcolor='white',
        font_color='black',
        yaxis=dict(
            title='Product Type',
            automargin=True,
            categoryorder='total ascending'  
        )
    )
 
    
    fig.update_layout(height=600)
 
    
    
 
    
    st.plotly_chart(fig)
def Top_Sold_Product_lower():
    df_lower = df[df['store_location'] == 'Lower Manhattan']
    top_product_category = df_lower.groupby('product_category')['transaction_qty'].sum().idxmax()
    top_product_type = df_lower.groupby('product_type')['transaction_qty'].sum().idxmax()
    
    max_selling_date = df_lower.groupby(df_lower['transaction_date'].dt.date)['transaction_qty'].sum().idxmax()
    
    overall_quantity_on_max_date = df_lower[df_lower['transaction_date'].dt.date == max_selling_date][
        'transaction_qty'].sum()
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'> 
            <br>
            <b>Top Sold Product Category:</b> {top_product_category}<br>
            <b>Top Sold Product Type:</b> {top_product_type}<br>
            <b>Overall Max Selling Date:</b> {max_selling_date}<br>
            <b>Overall Quantity on Max Date:</b> {overall_quantity_on_max_date}
            <br>
        </div>
        """,
        unsafe_allow_html=True
    )
def Lowest_Sold_Product_lower():
    
    df_lower = df[df['store_location'] == 'Lower Manhattan']

    lowest_product_category = df_lower.groupby('product_category')['transaction_qty'].sum().idxmin()
 
    
    lowest_product_type = df_lower.groupby('product_type')['transaction_qty'].sum().idxmin()
 
    
    min_selling_date = df_lower.groupby(df_lower['transaction_date'].dt.date)['transaction_qty'].sum().idxmin()
 
    
    overall_quantity_on_min_date = df_lower[df_lower['transaction_date'].dt.date == min_selling_date][
        'transaction_qty'].sum()
 
    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'>
            <b>Lowest Sold Product Category:</b> {lowest_product_category}<br>
            <b>Lowest Sold Product Type:</b> {lowest_product_type}<br>
            <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
            <b>Overall Quantity on Lowest Date:</b> {overall_quantity_on_min_date}
        </div>
        """,
        unsafe_allow_html=True
    )
def Expensive_Product():
    df_lower = df[df['store_location'] == 'Lower Manhattan']
 
    
    product_type_analysis = df_lower.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )
 
    
    expensive_product = product_type_analysis.sort_values('unit_price', ascending=False).iloc[0]
    
    cheapest_product = product_type_analysis.sort_values('unit_price').iloc[0]
 
    
    st.markdown(
        f"""
        <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content; border: 1px solid #ccc;'> 
            <b>Expensive Product:</b> {expensive_product.name}<br>
            <b>Average Price:</b> ${expensive_product['unit_price']:.2f}<br>
            <b>Total Quantity:</b> {expensive_product['transaction_qty']}<br><br>
            <b>Cheapest Product:</b> {cheapest_product.name}<br>
            <b>Average Price:</b> ${cheapest_product['unit_price']:.2f}<br>
            <b>Total Quantity:</b> {cheapest_product['transaction_qty']}
        </div>
        """,
        unsafe_allow_html=True
    )
def Lower_Manhattan_Price_vs_Sell_Quantity():

    df_lower = df[df['store_location'] == 'Lower Manhattan']
 
    
    price_quantity = df_lower.groupby('unit_price')['transaction_qty'].sum().reset_index()
 
    
    fig = px.line(price_quantity, x='unit_price', y='transaction_qty',
                  title='Lower Manhattan: Price vs Sell Quantity')
    fig.update_layout(
        xaxis_title='Price',
        yaxis_title='Sell Quantity',
        plot_bgcolor='white',  
        font_color='black',  
    )
 
    
    st.plotly_chart(fig)
def Hourly_Sales_in_Lower_Manhattan():
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['hour'] = df['transaction_time'].dt.hour
 
    
    df_lower = df[df['store_location'] == 'Lower Manhattan']
 
    
    hourly_sales_lower = df_lower.groupby('hour')['transaction_qty'].sum()
 
    
    fig = px.bar(
        x=hourly_sales_lower.index,
        y=hourly_sales_lower.values,
        labels={'x': 'Hour', 'y': 'Total Quantity Sold'},
        title='Hourly Sales in Lower Manhattan'
    )
 
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Hour',
        yaxis_title='Total Quantity Sold'
    )
 
    
    st.plotly_chart(fig)
def Lower_Manhattan_Sales_Analysis():
    
    df_lower = df[df['store_location'] == 'Lower Manhattan']
 
    
    top_products_lower = df_lower.groupby('product_type')['transaction_qty'].sum().nlargest(5)
 
    
    fig1 = px.pie(
        values=top_products_lower.values,
        names=top_products_lower.index,
        title='Top 5 Product Types Sold in Lower Manhattan by Quantity'
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')
 
    
    transaction_qty_counts = df_lower['transaction_qty'].value_counts()
 
    
    specified_quantities = [1, 2, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]
 
    
    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title='Percentage of Quantity of Items Bought at a Time in Lower Manhattan'
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')
 
    
    st.title("Lower Manhattan Sales Analysis")
 
    
    st.plotly_chart(fig1)
 
    
    st.plotly_chart(fig2)
def Increasing_Demand_of_Product_Types_in_Lower_Manhattan():
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
 
    
    df_lower = df[df['store_location'] == 'Lower Manhattan']
 
    
    product_demand = df_lower.groupby(['product_type', 'transaction_date'])['transaction_qty'].sum().reset_index()
 
    
    product_demand_pivot = product_demand.pivot(index='transaction_date', columns='product_type',
                                                values='transaction_qty').fillna(0)
 
    
    product_demand_cumulative = product_demand_pivot.cumsum()
 
    
    fig = go.Figure()
    for product_type in product_demand_cumulative.columns:
        fig.add_trace(go.Scatter(x=product_demand_cumulative.index, y=product_demand_cumulative[product_type],
                                 mode='lines', name=product_type))
 
    
    fig.update_layout(
        title='Increasing Demand of Product Types in Lower Manhattan',
        xaxis_title='Transaction Date',
        yaxis_title='Cumulative Transaction Quantity',
        plot_bgcolor='white',
        font_color='black'
    )
 
    
    
    st.plotly_chart(fig)
def Top_5_Most_Expensive_Product_Types_in_Lower_Manhattan_by_Unit_Price():
    
    df_lower = df[df['store_location'] == "Lower Manhattan"]

    
    product_type_analysis = df_lower.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    top_5_expensive_products = product_type_analysis.sort_values('unit_price', ascending=False).head(5)

    
    fig = px.bar(
        x=top_5_expensive_products.index,
        y=top_5_expensive_products['unit_price'],
        text=top_5_expensive_products['transaction_qty'],  
        labels={'x': 'Product Type', 'y': 'Average Unit Price', 'text': 'Total Quantity'},
        title="Top 5 Most Expensive Product Types in Lower Manhattan",
    )

    
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600,  
        showlegend=False  
    )

    
    
    st.plotly_chart(fig)
def Top_5_Cheapest_Product_Types_in_Lower_Manhattan():
    df_lower = df[df['store_location'] == 'Lower Manhattan']

    
    product_type_analysis = df_lower.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    
    top_5_cheapest_products = product_type_analysis.sort_values('unit_price').head(5)

    
    fig = px.bar(
        top_5_cheapest_products,
        x=top_5_cheapest_products.index,
        y='unit_price',
        text='transaction_qty',  
        labels={'x': 'Product Type', 'unit_price': 'Average Unit Price'},
        title='Top 5 Cheapest Product Types in Lower Manhattan',
        color_discrete_sequence=['#CD5C5C']
    )
    fig.update_layout(
        plot_bgcolor='white',  
        font_color='black',  
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600  
    )
    
    st.plotly_chart(fig)

def lower():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            lower_total()
            avg_lower_income()

        with subcol2:
            lower_total_qty()
            lower_sell_quantity()
            
    
    
    with col2:
        Monthly_Sales_for_Lower_Manhattan()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            Top_Sold_Product_lower()
            Expensive_Product()
            Lowest_Sold_Product_lower()


        with subcol4:
            Percentage_and_Quantity_of_Product_Types_Sold_in_Lower_Manhattan()
        Lower_Manhattan_Price_vs_Sell_Quantity()
        Top_5_Most_Expensive_Product_Types_in_Lower_Manhattan_by_Unit_Price()

    
    with col4:
        Hourly_Sales_in_Lower_Manhattan()

        Increasing_Demand_of_Product_Types_in_Lower_Manhattan()

        pie_chart_lower()

        
        Top_5_Cheapest_Product_Types_in_Lower_Manhattan()

def Total_Sales_january():

    january_sales = df[df['transaction_date'].dt.month == 1]
    total_january_payment = january_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_january_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
    )

    
    st.plotly_chart(fig)

def Total_Quantity_january():
    january_sales = df[df['transaction_date'].dt.month == 1]
    total_january_qty = january_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_january_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Average_qty_january():
    january_sales = df[df['transaction_date'].dt.month == 1]
    total_january_qty = january_sales['transaction_qty'].sum()
    average_january_qty = total_january_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_january_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  

def Average_Sales_january():
    january_sales = df[df['transaction_date'].dt.month == 1]
    total_january_payment = january_sales['total_payment'].sum()

    
    avg_sales_january = total_january_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_january,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)

def Daily_Sales_in_January():
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    daily_sales = january_sales.groupby(january_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in January')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_january():

    january_sales = df[df['transaction_date'].dt.month == 1]
    top_sold_product = january_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = january_sales.groupby(january_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = january_sales.groupby(january_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_january():
    

    
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    lowest_sold_product = january_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = january_sales.groupby(january_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = january_sales.groupby(january_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_january():

    
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    top_selling_store = january_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_january():
    
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    store_sales = january_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_January():
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    product_type_sales = january_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:January',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_January():
    
    
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    location_payment = january_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in January',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def January_Sales_Analysis():
    
    january_sales = df[df['transaction_date'].dt.month == 1]

    
    top_5_products = january_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in January by Quantity'
    )

    
    january_sales['transaction_qty_category'] = pd.cut(january_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = january_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in January'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="January Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_January():

    january_sales = df[df['transaction_date'].dt.month == 1]

    
    product_type_daily_sales = january_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in January')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)

def january():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_january()
            Average_Sales_january()

        with subcol2:
            Total_Quantity_january()
            Average_qty_january()
            
    
    
    with col2:
        Daily_Sales_in_January()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_january()
            lowest_sold_product_category_january()
            top_selling_store_location_january()
            Lowest_selling_store_location_january()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_January()
        Total_Sales_by_Location_in_January()
    
    with col4:
        January_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_January()
        

    
def Total_Sales_february():

    february_sales = df[df['transaction_date'].dt.month == 2]
    total_february_payment = february_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_february_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)
def Total_Quantity_february():
    february_sales = df[df['transaction_date'].dt.month == 2]
    total_february_qty = february_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_february_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)
def Average_qty_february():
    february_sales = df[df['transaction_date'].dt.month == 2]
    total_february_qty = february_sales['transaction_qty'].sum()
    average_february_qty = total_february_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_february_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  
def Average_Sales_february():

    february_sales = df[df['transaction_date'].dt.month == 2]
    total_february_payment = february_sales['total_payment'].sum()

    
    avg_sales_february = total_february_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_february,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)
def Daily_Sales_in_February():
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    daily_sales = february_sales.groupby(february_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in February')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_february():

    february_sales = df[df['transaction_date'].dt.month == 2]
    top_sold_product = february_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = february_sales.groupby(february_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = february_sales.groupby(february_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_february():
    

    
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    lowest_sold_product = february_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = february_sales.groupby(february_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = february_sales.groupby(february_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_february():

    
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    top_selling_store = february_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_february():
    
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    store_sales = february_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_February():
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    product_type_sales = february_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:February',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_February():
    
    
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    location_payment = february_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in February',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def February_Sales_Analysis():
    
    february_sales = df[df['transaction_date'].dt.month == 2]

    
    top_5_products = february_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in February by Quantity'
    )

    
    february_sales['transaction_qty_category'] = pd.cut(february_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = february_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in February'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="February Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_February():

    february_sales = df[df['transaction_date'].dt.month == 2]

    
    product_type_daily_sales = february_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in February')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)

def february():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_february()
            Average_Sales_february()

        with subcol2:
            Total_Quantity_february()
            Average_qty_february()
            
    
    
    with col2:
        Daily_Sales_in_February()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_february()
            lowest_sold_product_category_february()
            top_selling_store_location_february()
            Lowest_selling_store_location_february()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_February()
        Total_Sales_by_Location_in_February()
    
    with col4:
        February_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_February()
        
def Total_Sales_march():

    march_sales = df[df['transaction_date'].dt.month == 3]
    total_march_payment = march_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_march_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)
def Total_Quantity_march():
    march_sales = df[df['transaction_date'].dt.month == 3]
    total_march_qty = march_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_march_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Average_qty_march():
    march_sales = df[df['transaction_date'].dt.month == 3]
    total_march_qty = march_sales['transaction_qty'].sum()
    average_march_qty = total_march_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_march_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  

def Average_Sales_march():
    march_sales = df[df['transaction_date'].dt.month == 3]
    total_march_payment = march_sales['total_payment'].sum()

    
    avg_sales_march = total_march_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_march,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)

def Daily_Sales_in_March():
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    daily_sales = march_sales.groupby(march_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in March')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_march():

    march_sales = df[df['transaction_date'].dt.month == 3]
    top_sold_product = march_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = march_sales.groupby(march_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = march_sales.groupby(march_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_march():
    

    
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    lowest_sold_product = march_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = march_sales.groupby(march_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = march_sales.groupby(march_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_march():

    
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    top_selling_store = march_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_march():
    
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    store_sales = march_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_March():
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    product_type_sales = march_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:March',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_March():
    
    
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    location_payment = march_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in March',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def March_Sales_Analysis():
    
    march_sales = df[df['transaction_date'].dt.month == 3]

    
    top_5_products = march_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in March by Quantity'
    )

    
    march_sales['transaction_qty_category'] = pd.cut(march_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = march_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in March'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="March Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_March():

    march_sales = df[df['transaction_date'].dt.month == 3]

    
    product_type_daily_sales = march_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in March')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)

def march():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_march()
            Average_Sales_march()

        with subcol2:
            Total_Quantity_march()
            Average_qty_march()
            
    
    
    with col2:
        Daily_Sales_in_March()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_march()
            lowest_sold_product_category_march()
            top_selling_store_location_march()
            Lowest_selling_store_location_march()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_March()
        Total_Sales_by_Location_in_March()
    
    with col4:
        March_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_March()
        
def Total_Sales_april():

    april_sales = df[df['transaction_date'].dt.month == 4]
    total_april_payment = april_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_april_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Total_Quantity_april():
    april_sales = df[df['transaction_date'].dt.month == 4]
    total_april_qty = april_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_april_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Average_qty_april():
    april_sales = df[df['transaction_date'].dt.month == 4]
    total_april_qty = april_sales['transaction_qty'].sum()
    average_april_qty = total_april_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_april_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  

def Average_Sales_april():
    april_sales = df[df['transaction_date'].dt.month == 4]
    total_april_payment = april_sales['total_payment'].sum()

    
    avg_sales_april = total_april_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_april,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)

def Daily_Sales_in_April():
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    daily_sales = april_sales.groupby(april_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in April')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_april():

    april_sales = df[df['transaction_date'].dt.month == 4]
    top_sold_product = april_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = april_sales.groupby(april_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = april_sales.groupby(april_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_april():
    

    
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    lowest_sold_product = april_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = april_sales.groupby(april_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = april_sales.groupby(april_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_april():

    
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    top_selling_store = april_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_april():
    
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    store_sales = april_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_April():
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    product_type_sales = april_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:April',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_April():
    
    
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    location_payment = april_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in April',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def April_Sales_Analysis():
    
    april_sales = df[df['transaction_date'].dt.month == 4]

    
    top_5_products = april_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in April by Quantity'
    )

    
    april_sales['transaction_qty_category'] = pd.cut(april_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = april_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in April'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="April Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_April():

    april_sales = df[df['transaction_date'].dt.month == 4]

    
    product_type_daily_sales = april_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in April')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)

def april():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_april()
            Average_Sales_april()

        with subcol2:
            Total_Quantity_april()
            Average_qty_april()
            
    
    
    with col2:
        Daily_Sales_in_April()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_april()
            lowest_sold_product_category_april()
            top_selling_store_location_april()
            Lowest_selling_store_location_april()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_April()
        Total_Sales_by_Location_in_April()
    
    with col4:
        April_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_April()
        
    
def Total_Sales_may():

    may_sales = df[df['transaction_date'].dt.month == 5]
    total_may_payment = may_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_may_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Total_Quantity_may():
    may_sales = df[df['transaction_date'].dt.month == 5]
    total_may_qty = may_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_may_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Average_qty_may():
    may_sales = df[df['transaction_date'].dt.month == 5]
    total_may_qty = may_sales['transaction_qty'].sum()
    average_may_qty = total_may_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_may_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  

def Average_Sales_may():
    may_sales = df[df['transaction_date'].dt.month == 5]
    total_may_payment = may_sales['total_payment'].sum()

    
    avg_sales_may = total_may_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_may,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)

def Daily_Sales_in_May():
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    daily_sales = may_sales.groupby(may_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in May')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_may():

    may_sales = df[df['transaction_date'].dt.month == 5]
    top_sold_product = may_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = may_sales.groupby(may_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = may_sales.groupby(may_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_may():
    

    
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    lowest_sold_product = may_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = may_sales.groupby(may_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = may_sales.groupby(may_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_may():

    
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    top_selling_store = may_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_may():
    
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    store_sales = may_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_May():
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    product_type_sales = may_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:May',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_May():
    
    
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    location_payment = may_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in May',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def May_Sales_Analysis():
    
    may_sales = df[df['transaction_date'].dt.month == 5]

    
    top_5_products = may_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in May by Quantity'
    )

    
    may_sales['transaction_qty_category'] = pd.cut(may_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = may_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in May'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="May Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_May():

    may_sales = df[df['transaction_date'].dt.month == 5]

    
    product_type_daily_sales = may_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in May')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)

def may():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_may()
            Average_Sales_may()

        with subcol2:
            Total_Quantity_may()
            Average_qty_may()
            
    
    
    with col2:
        Daily_Sales_in_May()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_may()
            lowest_sold_product_category_may()
            top_selling_store_location_may()
            Lowest_selling_store_location_may()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_May()
        Total_Sales_by_Location_in_May()
    
    with col4:
        May_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_May()
        
def Total_Sales_june():

    june_sales = df[df['transaction_date'].dt.month == 6]
    total_june_payment = june_sales['total_payment'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_june_payment,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Total_Quantity_june():
    june_sales = df[df['transaction_date'].dt.month == 6]
    total_june_qty = june_sales['transaction_qty'].sum()

    
    fig = go.Figure(go.Indicator(
        mode="number",
        value=total_june_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Total Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        
        
        
        
        
        
    )

    
    st.plotly_chart(fig)

def Average_qty_june():
    june_sales = df[df['transaction_date'].dt.month == 6]
    total_june_qty = june_sales['transaction_qty'].sum()
    average_june_qty = total_june_qty / 31

    fig_qty = go.Figure(go.Indicator(
        mode="number",
        value=average_june_qty,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Quantity</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    fig_qty.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ))

    st.plotly_chart(fig_qty)  

def Average_Sales_june():
    june_sales = df[df['transaction_date'].dt.month == 6]
    total_june_payment = june_sales['total_payment'].sum()

    
    avg_sales_june = total_june_payment / 31


    
    fig_sales = go.Figure(go.Indicator(
        mode="number",
        value=avg_sales_june,
        title={"text": "<span style='font-size:20px; font-weight:bold; font-weight:bold;'>Average Sales</span>"},
        domain={'x': [0, 1], 'y': [0, 1]},
    ))

    fig_sales.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=200,
        height=200,
        font=dict(
            family="Arial",
            size=18,
            color="black"
        )
    )

    
    
    
    st.plotly_chart(fig_sales)

def Daily_Sales_in_June():
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    daily_sales = june_sales.groupby(june_sales['transaction_date'].dt.date)['total_payment'].sum().reset_index()
    daily_sales.columns = ['transaction_date', 'total_payment']  

    
    fig = px.line(daily_sales, x='transaction_date', y='total_payment', title='Daily Sales in June')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales')

    
    st.plotly_chart(fig)

def top_sold_product_category_june():

    june_sales = df[df['transaction_date'].dt.month == 6]
    top_sold_product = june_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmax()

    
    max_selling_date = june_sales.groupby(june_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmax()
    overall_max_qty = june_sales.groupby(june_sales['transaction_date'].dt.date)['transaction_qty'].sum().max()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Sold Product Category:</b> {top_sold_product[0]}<br>
      <b>Top Sold Product Type:</b> {top_sold_product[1]}<br>
      <b>Overall Max Selling Date:</b> {max_selling_date}<br>
      <b>Overall Quantity on Max Date:</b> {overall_max_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def lowest_sold_product_category_june():
    

    
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    lowest_sold_product = june_sales.groupby(['product_category', 'product_type'])['transaction_qty'].sum().idxmin()

    
    min_selling_date = june_sales.groupby(june_sales['transaction_date'].dt.date)[
        'transaction_qty'].sum().idxmin()
    overall_min_qty = june_sales.groupby(june_sales['transaction_date'].dt.date)['transaction_qty'].sum().min()

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Sold Product Category:</b> {lowest_sold_product[0]}<br>
      <b>Lowest Sold Product Type:</b> {lowest_sold_product[1]}<br>
      <b>Overall Lowest Selling Date:</b> {min_selling_date}<br>
      <b>Overall Quantity on Lowest Date:</b> {overall_min_qty}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def top_selling_store_location_june():

    
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    top_selling_store = june_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    top_store_location = top_selling_store['total_payment'].idxmax()

    
    sold_quantity = top_selling_store.loc[top_store_location, 'transaction_qty']
    total_payment = top_selling_store.loc[top_store_location, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Top Selling Store Location:</b> {top_store_location}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Lowest_selling_store_location_june():
    
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    store_sales = june_sales.groupby('store_location').agg({'transaction_qty': 'sum', 'total_payment': 'sum'})

    
    lowest_selling_store = store_sales['total_payment'].idxmin()

    
    sold_quantity = store_sales.loc[lowest_selling_store, 'transaction_qty']
    total_payment = store_sales.loc[lowest_selling_store, 'total_payment']

    
    output_string = f"""
    <div style='background-color: white; text-align: left; color: black; padding: 10px; width: fit-content;'>
      <b>Lowest Selling Store Location:</b> {lowest_selling_store}<br>
      <b>Sold Quantity:</b> {sold_quantity}<br>
      <b>Total Payment:</b> ${total_payment:.2f}
    </div>
    """

    
    st.markdown(output_string, unsafe_allow_html=True)
def Quantity_of_Each_Product_Type_Sold_in_June():
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    product_type_sales = june_sales.groupby('product_type')['transaction_qty'].sum()

    
    sorted_product_type_sales = product_type_sales.sort_values(ascending=False)

    
    fig = px.bar(
        sorted_product_type_sales,
        x=sorted_product_type_sales.values,
        y=sorted_product_type_sales.index,
        orientation='h',
        title='Sold Quantity of Each Product:June',
        labels={'x': 'Total Quantity', 'y': 'Product Type'},
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  
        height=800,  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def Total_Sales_by_Location_in_June():
    
    
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    location_payment = june_sales.groupby('store_location')['total_payment'].sum()

    
    fig = px.bar(
        location_payment,
        x=location_payment.index,
        y=location_payment.values,
        title='Total Sales by Location in June',
        labels={'x': 'Store Location', 'y': 'Total Payment'},
        color=location_payment.index  
    )

    
    st.plotly_chart(fig, use_container_width=True)
def June_Sales_Analysis():
    
    june_sales = df[df['transaction_date'].dt.month == 6]

    
    top_5_products = june_sales.groupby('product_type')['transaction_qty'].sum().nlargest(5)

    
    fig1 = px.pie(
        top_5_products,
        values=top_5_products.values,
        names=top_5_products.index,
        title='Top 5 Sold Product Types in June by Quantity'
    )

    
    june_sales['transaction_qty_category'] = pd.cut(june_sales['transaction_qty'],
                                                       bins=[1, 2, 3, 4, 6, 8, float('inf')],
                                                       labels=['1 item', '2 items', '3 items', '4 items', '6 items',
                                                               '8 items'])

    quantity_distribution = june_sales.groupby('transaction_qty_category')['transaction_qty'].count()

    fig2 = px.pie(
        quantity_distribution,
        values=quantity_distribution.values,
        names=quantity_distribution.index,
        title='Quantity of Items Bought at a Time in June'
    )

    
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=top_5_products.index, values=top_5_products.values), 1, 1)
    fig.add_trace(go.Pie(labels=quantity_distribution.index, values=quantity_distribution.values), 1, 2)

    fig.update_layout(height=600, width=1000, title_text="June Sales Analysis")

    
    st.plotly_chart(fig, use_container_width=True)
def Increasing_Demand_for_Each_Product_Type_in_June():

    june_sales = df[df['transaction_date'].dt.month == 6]

    
    product_type_daily_sales = june_sales.groupby(['product_type', 'transaction_date'])[
        'transaction_qty'].sum().reset_index()

    
    fig = px.line(product_type_daily_sales, x='transaction_date', y='transaction_qty', color='product_type',
                  title='Increasing Demand for Each Product Type in June')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total Quantity Sold')

    
    st.plotly_chart(fig, use_container_width=True)
def june():
    col1, col2 = st.columns(2)
    with col1:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            Total_Sales_june()
            Average_Sales_june()

        with subcol2:
            Total_Quantity_june()
            Average_qty_june()
            
    
    
    with col2:
        Daily_Sales_in_June()
        
    col3, col4 = st.columns(2)
    
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            top_sold_product_category_june()
            lowest_sold_product_category_june()
            top_selling_store_location_june()
            Lowest_selling_store_location_june()


        with subcol4:
            Quantity_of_Each_Product_Type_Sold_in_June()
        Total_Sales_by_Location_in_June()
    
    with col4:
        June_Sales_Analysis()
        Increasing_Demand_for_Each_Product_Type_in_June()
        

def main():
    st.sidebar.title("Filter")
    level = st.sidebar.radio("Choose One", ['Overview','Location', 'Months'])
    

    if level == 'Overview':
        overview()

    elif level == 'Location':

        location_type = st.sidebar.selectbox("Select Location Type", ['Astoria', 'Hells Kitchen', 'Lower Manhattan'])
        if location_type == 'Astoria':
            astoria()
        elif location_type == 'Hells Kitchen':
            hellkitchen()
        elif location_type == 'Lower Manhattan':
            lower()

    elif level == 'Months':
        month_type = st.sidebar.selectbox("Select Months Type", ['January', 'February', 'March', 'April', 'May', 'June'])
        if month_type == 'January':
            january()
        elif month_type == 'February':
            february()
        elif month_type == 'March':
            march()
        elif month_type == 'April':
            april()
        elif month_type == 'May':
            may()
        elif month_type == 'June':
            june()



if __name__ == "__main__":
    main()

