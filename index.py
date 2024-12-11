import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"],
    "Product_A_Sales": [230, 220, 250, 275, 300, 280, 290, 310, 320, 330, 340, 360],
    "Product_B_Sales": [450, 430, 460, 480, 500, 490, 510, 520, 540, 550, 560, 580]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the Sales Data
print("Sales Data for Product A and Product B over a year: ")
print(df)

# Calculating percentiles for Product A Sales
percentiles = df["Product_A_Sales"].quantile([0.25, 0.5, 0.75])
print("\nPercentiles for Product A Sales:")
print({
    '25th Percentile': float(percentiles[0.25]),
    '50th Percentile (Median)': float(percentiles[0.5]),
    '75th Percentile': float(percentiles[0.75]) 
})

# Calculating Standard Deviation and Variance for both products
std_dev_product_a = df["Product_A_Sales"].std()
variance_product_a = df["Product_A_Sales"].var()   
std_dev_product_b = df["Product_B_Sales"].std()
variance_product_b = df["Product_B_Sales"].var()

print("\nStandard Deviation and Variance:")
print(f"Product A - Std Dev: {std_dev_product_a:.2f}, Variance: {variance_product_a:.2f}")
print(f"Product B - Std Dev: {std_dev_product_b:.2f}, Variance: {variance_product_b:.2f}")

# Calculating the correlation between Product A and Product B sales
correlation = df["Product_A_Sales"].corr(df["Product_B_Sales"])
print("\nCorrelation between Product A and Product B sales:", round(correlation, 2))

# Generating the correlation matrix
correlation_matrix = df[["Product_A_Sales", "Product_B_Sales"]].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Correlation vs. Causality explanation
print("\nCorrelation vs. Causality:")
print("""
Correlation measures the strength of the relationship between two variables.
However, it does not imply causality. For instance, while Product A and Product B
sales show a strong positive correlation, other factors such as seasonal trends
affecting both products rather than one causing an increase in the other's sales.
""")

plt.figure(figsize=(10, 6))
plt.plot(df["Month"], df["Product_A_Sales"], marker='o', label='Product A Sales', color='blue')
plt.plot(df["Month"], df["Product_B_Sales"], marker='o', label='Product B Sales', color='green')
plt.title("Monthly Sales Data for Product A and Product B", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Product_A_Sales", y="Product_B_Sales", data=df, color="purple", s=100)
plt.title("Scatter Plot: Product A Sales vs. Product B Sales", fontsize=14)
plt.xlabel("Product A Sales", fontsize=12)
plt.ylabel("Product B Sales", fontsize=12)
plt.grid()
plt.show()