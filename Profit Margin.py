# Calculate profit margin based on revenue and cost
def calculate_profit_margin(revenue, cost):
    return ((revenue - cost) / revenue) * 100

# Example usage:
revenue = 5000  # Total revenue
cost = 3000  # Total cost
profit_margin = calculate_profit_margin(revenue, cost)
print("Profit margin:", profit_margin, "%")
