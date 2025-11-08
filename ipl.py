import pandas as pd

# 1️⃣ Load validated IPL dataset (has numeric team IDs)
ipl = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\IPL_2008_2025\IPL_Cleaned_2008_2025.csv")

# 2️⃣ Load team reference file (the one you showed)
teams = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\IPL_2008_2025\teams_data.csv")

# 3️⃣ Rename columns for clarity (if needed)
teams.rename(columns={'team_id': 'team_id', 'team_name': 'TeamName'}, inplace=True)

print("✅ Teams reference loaded:")
print(teams.head())

# 4️⃣ Merge for batting team
ipl = pd.merge(
    ipl,
    teams[['team_id', 'TeamName']],
    left_on='batting_team',
    right_on='team_id',
    how='left'
)
ipl.rename(columns={'TeamName': 'batting_team_name'}, inplace=True)
ipl.drop(columns=['team_id'], inplace=True)

# 5️⃣ Merge for bowling team
ipl = pd.merge(
    ipl,
    teams[['team_id', 'TeamName']],
    left_on='bowling_team',
    right_on='team_id',
    how='left'
)
ipl.rename(columns={'TeamName': 'bowling_team_name'}, inplace=True)
ipl.drop(columns=['team_id'], inplace=True)

# 6️⃣ Merge for match winner (optional but highly recommended)
ipl = pd.merge(
    ipl,
    teams[['team_id', 'TeamName']],
    left_on='winner',
    right_on='team_id',
    how='left'
)
ipl.rename(columns={'TeamName': 'winner_team_name'}, inplace=True)
ipl.drop(columns=['team_id'], inplace=True)

# 7️⃣ Drop old numeric columns (optional)
ipl.drop(columns=['batting_team', 'bowling_team', 'winner'], inplace=True, errors='ignore')

# 8️⃣ Save the final cleaned dataset
ipl.to_csv(r"C:\Users\Admin\OneDrive\Desktop\IPL_2008_2025\IPL_Final_2008_2025.csv", index=False)

print("✅ Team names successfully mapped to Batting, Bowling, and Winner columns!")
print("✅ Cleaned dataset saved as IPL_Final_2008_2025.csv")

# 9️⃣ Quick check of results
print("\n🏏 Unique Batting Teams:", ipl['batting_team_name'].unique())
print("🏏 Unique Bowling Teams:", ipl['bowling_team_name'].unique())
print("🏆 Unique Winner Teams:", ipl['winner_team_name'].unique())
