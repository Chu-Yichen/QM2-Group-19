import json

file_path = 'C:\\Users\\Chuyi\\Pictures\\QM2 2024 UCL\\Top 60 busiest Airports.json'
with open(file_path, 'r') as file:
    airport_data = json.load(file)

# Filter for airports in the United States and select the top 10 by passengers
us_airports = [entry for entry in airport_data if entry["Country"] == "United States"]
top_10_us_airports = sorted(us_airports, key=lambda x: x["Number of Passengers"], reverse=True)[:10]


for airport in top_10_us_airports:
    print(f"Rank {airport['Rank']}: {airport['Airport']}")

