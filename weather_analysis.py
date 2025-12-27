import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

avg_temp = df["Temperature"].mean()
hottest_day = df.loc[df["Temperature"].idxmax()]  #index of max ele
coldest_day = df.loc[df["Temperature"].idxmin()]   # index of min ele 
rainy_days = df[df["Rainfall"] > 0]


print("\n--- Weather Analysis Report ---")
print("Average Temperature:", round(avg_temp, 2))
print("Hottest Day:", hottest_day["Date"], "-", hottest_day["Temperature"], "°C")
print("Coldest Day:", coldest_day["Date"], "-", coldest_day["Temperature"], "°C")
print("Total Rainy Days:", len(rainy_days))

plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.title("Temperature Over Days")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45) #Rotates x-axis labels by 45 degrees so they dont overlap 
plt.tight_layout() #automatically adjusting the spacing between and around the subplots
plt.show()


plt.figure()
plt.bar(df["Date"], df["Rainfall"])
plt.title("Rainfall Over Days")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.axhline(df["Temperature"].mean(), linestyle='--') #axis horizontal line 
plt.title("Temperature with Average Line")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Histogram shows frequency distribution , How many values fall into certain ranges
#bins number of buckets , spilt temp into 5 intervals
plt.figure()
plt.hist(df["Temperature"], bins=5)
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")
plt.show()


heatwave_days = df[df["Temperature"] > 33]
print("Heatwave Days:")
print(heatwave_days)  #printing dataframe


#correlation - When one value changes, does the other also change 
#vale changes bw 1 0 or -1 (+1 both increases together, 0 no relation, -1 one increase other decrease)
correlation = df["Temperature"].corr(df["Rainfall"])
print("Correlation between Temperature and Rainfall:", correlation)

#feature engineering 
def weather_type(row):
    if row["Rainfall"] > 0:
        return "Rainy"
    elif row["Temperature"] > 33:
        return "Hot"
    else:
        return "Normal"

df["Weather_Type"] = df.apply(weather_type,axis=1) #usually axis=0 is done, applies to column...but here we need row wise checking so axis=1
print(df)
