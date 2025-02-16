import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Load the dataset
df = pd.read_csv("collection.csv")

# Convert pub_date to numeric, handling errors
df["pub_date"] = pd.to_numeric(df["pub_date"], errors="coerce")

# Drop NaN values (if any)
df = df.dropna(subset=["pub_date"])

# Convert to integer (after dropping NaNs)
df["pub_date"] = df["pub_date"].astype(int)

# Set figure size
plt.figure(figsize=(10, 5))

# Plot histogram with Seaborn
sns.histplot(df["pub_date"], bins=50, kde=True, color="royalblue")

# Customize X-axis ticks
plt.xticks(rotation=45)  # Rotate for better readability
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))  # Show ticks every 10 years

# Customize plot
plt.xlabel("Veröffentlichungsdatum", fontsize=12)
plt.ylabel("Anzahl", fontsize=12)
plt.title("Verteilung der Veröffentlichungsdaten (1562-1742)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)

# Show plot
plt.show()
