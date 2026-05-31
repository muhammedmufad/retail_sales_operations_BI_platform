import pandas as pd

df = pd.read_csv("data/customer_shopping_data.csv")

df["revenue"] = df["price"] * df["quantity"]

print("Dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nRevenue by category:")
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue.apply(lambda x: f"{x:,.2f}"))

print("\nRevenue by shopping mall:")
mall_revenue = (
    df.groupby("shopping_mall")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(mall_revenue.apply(lambda x: f"{x:,.2f}"))