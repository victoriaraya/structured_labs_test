from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

text("# Fruit Prices 🍒")

connect() 
df = get_df('fruit_prices')

sql = '''SELECT Fruit, RetailPrice FROM fruit_prices WHERE RetailPriceUnit = 'per pound' '''
filtered_df = query(sql, "fruit_prices")

text("### USA Fruit Prices per Pound")
table(filtered_df, title="🍎🍐🍊🍌🍉🍇🫐🥭🍍")

filtered_df["item"] = filtered_df["Fruit"].apply(lambda x: x.split(",")[0].split("(")[0].strip())
fig = px.scatter(
    filtered_df, 
    x="item", 
    y="RetailPrice", 
    text="item",
    title="📈 Fruit Price per Pound 📈 ",
    labels={"item": "Fruit", "RetailPrice": "Price"}
)
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightpink'))
fig.update_layout(template='plotly_white')
plotly(fig)