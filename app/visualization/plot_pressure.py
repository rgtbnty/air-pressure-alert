import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pressure_data = pd.read_csv("../storage/output.csv", parse_dates=["date"])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.lineplot(x="date", y="pressure", data=pressure_data)
plt.title("Pressure Over Time")
plt.show()