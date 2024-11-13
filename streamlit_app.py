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
    ax.text(0.5, 0.5, f'Total Sales\n{total_sales:.2f}', ha='center', va='center', fontsize=14)
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

def location():
    
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

def astoria_total_qty():
    df['total_payment'] = df['unit_price'] * df['transaction_qty']
    total_transaction_qty_astoria = df[df['store_location'] == 'Astoria']['transaction_qty'].sum()

    fig = go.Figure(
        go.Indicator(
            mode="number",
            value=total_transaction_qty_astoria,
            title={"text": "<span style='font-size:20px;'>Total Quantity</span>"},
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
            title={"text": "<span style='font-size:20px;'>AVERAGE SELLS</span>"},
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
            title={"text": "<span style='font-size:20px;'>Total Sales</span>"},
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
            title={"text": "<span style='font-size:20px;'>Total Sales</span>"},
            number={'font': {'size': 30}},
            domain={'x': [0, 1], 'y': [0, 1]}
        )
    )
    fig.update_layout(
        paper_bgcolor='white',
        font_color='black',
        width=120,  # Adjust width as needed
        height=120  # Adjust height as needed
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
 
    # Update the layout for the bar chart
    fig.update_layout(
        title='Monthly Sales for Astoria',
        xaxis_title='Month',
        yaxis_title='Total Sales',
        plot_bgcolor='white',
        font_color='black'
    )
 
    # Display the Streamlit app title
    #st.title("Monthly Total Sales for Astoria")
 
    # Display the figure in the Streamlit app
    st.plotly_chart(fig)
def Percentage_and_Quantity_of_Product_Types_Sold_in_Astoria():
    
    df_astoria = df[df['store_location'] == 'Astoria']
    product_type_sales = df_astoria.groupby('product_type').agg({'total_payment': 'sum', 'transaction_qty': 'sum'})
    product_type_sales = product_type_sales.sort_values('total_payment', ascending=False)
    # Calculate percentage of total sales for each product type
    product_type_sales['percentage_of_total_sales'] = (product_type_sales['total_payment'] / product_type_sales[
        'total_payment'].sum()) * 100
 
    # Create a scrollable bar chart with product types sorted by total sales
    fig = px.bar(
        product_type_sales,
        x='percentage_of_total_sales',
        y=product_type_sales.index,
        orientation='h',
        labels={'percentage_of_total_sales': 'Percentage of Total Sales', 'index': 'Product Type'},
        title='Percentage and Quantity of Product Types Sold in Astoria',
        text='transaction_qty'
    )
 
    # Update layout for the bar chart
    fig.update_layout(
        xaxis_title='Percentage of Total Sales',
        yaxis_title='Product Type',
        plot_bgcolor='white',
        font_color='black',
        yaxis=dict(
            title='Product Type',
            automargin=True,
            categoryorder='total ascending'  # Ensures the most sold product is at the top
        )
    )
 
    # Adjust height to make the chart scrollable if many product types are present
    fig.update_layout(height=600)
 
    # Set up the Streamlit app title
    #st.title("Coffee Shop Sales Dashboard")
 
    # Display the figure in the Streamlit app
    st.plotly_chart(fig)
def Top_Sold_Product_Category():
    df_astoria = df[df['store_location'] == 'Astoria']
    top_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmax()
    top_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmax()
    # Find the date with the maximum overall quantity sold
    max_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmax()
    # Find the overall quantity sold on that date
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
def Lowest_Sold_Product_Category():
    
    df_astoria = df[df['store_location'] == 'Astoria']

    lowest_product_category = df_astoria.groupby('product_category')['transaction_qty'].sum().idxmin()
 
    # Find the lowest-selling product type
    lowest_product_type = df_astoria.groupby('product_type')['transaction_qty'].sum().idxmin()
 
    # Find the date with the minimum overall quantity sold
    min_selling_date = df_astoria.groupby(df_astoria['transaction_date'].dt.date)['transaction_qty'].sum().idxmin()
 
    # Find the overall quantity sold on that date
    overall_quantity_on_min_date = df_astoria[df_astoria['transaction_date'].dt.date == min_selling_date][
        'transaction_qty'].sum()
 
    # Display the results in Streamlit with HTML styling
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
    df_astoria = df[df['store_location'] == 'Astoria']
 
    # Group by product type and calculate average price and total quantity
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )
 
    # Sort by average price in descending order to find the most expensive
    expensive_product = product_type_analysis.sort_values('unit_price', ascending=False).iloc[0]
    # Sort by average price in ascending order to find the cheapest
    cheapest_product = product_type_analysis.sort_values('unit_price').iloc[0]
 
    # Display results in Streamlit with styled HTML
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
 
    # Group data by unit_price and sum transaction_qty
    price_quantity = df_astoria.groupby('unit_price')['transaction_qty'].sum().reset_index()
 
    # Create the line diagram
    fig = px.line(price_quantity, x='unit_price', y='transaction_qty',
                  title='Astoria: Price vs Sell Quantity')
    fig.update_layout(
        xaxis_title='Price',
        yaxis_title='Sell Quantity',
        plot_bgcolor='white',  # Set background color to white
        font_color='black',  # Set font color to black
    )
 
    # Display the plot in Streamlit
    st.plotly_chart(fig)
def Hourly_Sales_in_Astoria():
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['hour'] = df['transaction_time'].dt.hour
 
    # Filter data for Astoria location
    df_astoria = df[df['store_location'] == 'Astoria']
 
    # Group by hour and calculate the total quantity sold
    hourly_sales_astoria = df_astoria.groupby('hour')['transaction_qty'].sum()
 
    # Create a bar chart
    fig = px.bar(
        x=hourly_sales_astoria.index,
        y=hourly_sales_astoria.values,
        labels={'x': 'Hour', 'y': 'Total Quantity Sold'},
        title='Hourly Sales in Astoria'
    )
 
    fig.update_layout(
        plot_bgcolor='white',  # Set background color to white
        font_color='black',  # Set font color to black
        xaxis_title='Hour',
        yaxis_title='Total Quantity Sold'
    )
 
    # Display the plot in Streamlit
    st.plotly_chart(fig)
def Astoria_Sales_Analysis():
    # Filter data for Astoria location
    df_astoria = df[df['store_location'] == 'Astoria']
 
    # Group by product type and sum transaction quantity for the top 5 sold products
    top_products_astoria = df_astoria.groupby('product_type')['transaction_qty'].sum().nlargest(5)
 
    # Create a pie chart for the top 5 product types sold by quantity
    fig1 = px.pie(
        values=top_products_astoria.values,
        names=top_products_astoria.index,
        title='Top 5 Product Types Sold in Astoria by Quantity'
    )
    fig1.update_layout(plot_bgcolor='white', font_color='black')
 
    # Group by transaction quantity and count the number of transactions
    transaction_qty_counts = df_astoria['transaction_qty'].value_counts()
 
    # Filter for the specified transaction quantities
    specified_quantities = [1, 2, 4, 6, 8]
    filtered_counts = transaction_qty_counts[transaction_qty_counts.index.isin(specified_quantities)]
 
    # Create a pie chart for the specified transaction quantities
    fig2 = px.pie(
        values=filtered_counts.values,
        names=filtered_counts.index,
        title='Percentage of Quantity of Items Bought at a Time in Astoria'
    )
    fig2.update_layout(plot_bgcolor='white', font_color='black')
 
    # Display the charts in Streamlit
    st.title("Astoria Sales Analysis")
 
    # Display the first pie chart
    st.plotly_chart(fig1)
 
    # Display the second pie chart
    st.plotly_chart(fig2)
def Increasing_Demand_of_Product_Types_in_Astoria():
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
 
    # Filter data for Astoria location
    df_astoria = df[df['store_location'] == 'Astoria']
 
    # Group by product type and transaction date, then sum transaction quantity
    product_demand = df_astoria.groupby(['product_type', 'transaction_date'])['transaction_qty'].sum().reset_index()
 
    # Pivot the table to have product types as columns and transaction dates as rows
    product_demand_pivot = product_demand.pivot(index='transaction_date', columns='product_type',
                                                values='transaction_qty').fillna(0)
 
    # Calculate the cumulative sum for each product type to show increasing demand
    product_demand_cumulative = product_demand_pivot.cumsum()
 
    # Create the line chart for cumulative demand
    fig = go.Figure()
    for product_type in product_demand_cumulative.columns:
        fig.add_trace(go.Scatter(x=product_demand_cumulative.index, y=product_demand_cumulative[product_type],
                                 mode='lines', name=product_type))
 
    # Update layout for the chart
    fig.update_layout(
        title='Increasing Demand of Product Types in Astoria',
        xaxis_title='Transaction Date',
        yaxis_title='Cumulative Transaction Quantity',
        plot_bgcolor='white',
        font_color='black'
    )
 
    # Display the title and the plot in Streamlit
    #st.title("Astoria Product Demand Analysis")
    st.plotly_chart(fig)
def Top_5_Most_Expensive_Product_Types_in_Astoria_by_Unit_Price():
    df['total_payment'] = df['unit_price'] * df['transaction_qty']
 
    # Filter data for Astoria location
    df_astoria = df[df['store_location'] == 'Astoria']
 
    # Group by product type and calculate average price and total quantity
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )
 
    # Sort by average price in descending order to find the top 5 most expensive
    top_5_expensive_products = product_type_analysis.sort_values('unit_price', ascending=False).head(5)
 
    
    fig = px.bar(
        top_5_expensive_products,
        x='transaction_qty',
        y=top_5_expensive_products.index,
        orientation='h',
        labels={'transaction_qty': 'Total Quantity Sold', 'index': 'Product Type'},
        title='Top 5 Most Expensive Product Types in Astoria',
        text='transaction_qty'  # Display total quantity on the bars
    )

    fig.update_layout(
        plot_bgcolor='white',  # Background color
        font_color='black',  # Text color
        xaxis_title='Total Quantity Sold',
        yaxis_title='Product Type',
        height=600  # Chart height for visibility
    )
 
    # Display title and the plot in Streamlit
    #st.title("Astoria's Top 5 Expensive Product Types by Unit Price")
    st.plotly_chart(fig)
def Top_5_Cheapest_Product_Types_in_Astoria():
    df_astoria = df[df['store_location'] == 'Astoria']

    # Group by product type and calculate average price and total quantity
    product_type_analysis = df_astoria.groupby('product_type').agg(
        {'unit_price': 'mean', 'transaction_qty': 'sum'}
    )

    # Sort by average price in ascending order and get top 5 cheapest products
    top_5_cheapest_products = product_type_analysis.sort_values('unit_price').head(5)

    # Create a bar chart with a reddish color and quantity labels on top of bars
    fig = px.bar(
        top_5_cheapest_products,
        x=top_5_cheapest_products.index,
        y='unit_price',
        text='transaction_qty',  # Display total quantity on the bars
        labels={'x': 'Product Type', 'unit_price': 'Average Unit Price'},
        title='Top 5 Cheapest Product Types in Astoria',
        color_discrete_sequence=['#CD5C5C']  # Set bars to a reddish color
    )
    fig.update_layout(
        plot_bgcolor='white',  # Background color
        font_color='black',  # Text color
        xaxis_title='Product Type',
        yaxis_title='Average Unit Price',
        height=600  # Chart height for visibility
    )
    #st.title("Astoria's Top 5 Cheapest Product Types by Unit Price")
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
            
    
    # Section 1,2 with a chart
    with col2:
        Monthly_Sales_for_Astoria()
        
    col3, col4 = st.columns(2)
    # Section 2,1 with 2 columns
    with col3:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            Top_Sold_Product_Category()
            Expensive_Product()
            Lowest_Sold_Product_Category()


        with subcol4:
            Percentage_and_Quantity_of_Product_Types_Sold_in_Astoria()
        Astoria_Price_vs_Sell_Quantity()
    # Section 2,2 with 4 rows
    with col4:
        Hourly_Sales_in_Astoria()

        Increasing_Demand_of_Product_Types_in_Astoria()

        Top_5_Most_Expensive_Product_Types_in_Astoria_by_Unit_Price()

        Top_5_Cheapest_Product_Types_in_Astoria()

        


def hellkitchen():
    st.write()

def manhattan():
    st.write()
    
def january():
    st.write()
    
def february():
    st.write()
    
def march():
    st.write()
    
def april():
    st.write()
    
def may():
    st.write()
    
def june():
    st.write()
    

    
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
            manhattan()

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

