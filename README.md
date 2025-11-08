# -IPL-2008-2025-Cricket-Data-Analytics-Dashboard-

# 🏏 IPL 2008–2025 Cricket Data Analytics Dashboard  

## 📊 Project Overview  
This project analyzes **18 seasons of IPL (2008–2025)** data to uncover batting, bowling, and team performance trends using **Python** and **Power BI**.  
It’s designed as a **Data Analyst portfolio project**, showcasing end-to-end data cleaning, transformation, visualization, and insight generation.

---

## 🧰 Tools & Technologies  
- **Python (Pandas)** → Data cleaning, merging, transformation  
- **Power BI** → Interactive data visualization and dashboard design  
- **Microsoft Excel** → Data inspection and initial review  
- **DAX** → Custom KPI and measure calculations  

---

## 📁 Dataset  
**Source:** Self-collected IPL data (2008–2025)  
**Files Used:**  
1. `ball_by_ball_data.csv`  
2. `ipl_matches_data.csv`  
3. `players_data_updated.csv`  
4. `team_aliases.csv`  
5. `teams_data.csv`  

All datasets were cleaned and merged into a single master file:  
👉 `IPL_Final_2008_2025.csv`  

---

## ⚙️ Data Cleaning (Python)  
Performed using **Pandas**:
- Merged 5 datasets on relevant keys (`match_id`, `team_id`, etc.)
- Converted team IDs to human-readable names
- Renamed inconsistent columns (`batter_runs` → `runs_off_bat`)
- Filtered data from **2008–2025**
- Filled missing values (`extras`, `runs_off_bat`)
- Exported cleaned dataset for Power BI:
  ```python
  ipl.to_csv("IPL_Final_2008_2025.csv", index=False)
Live Dashboard  
Explore the interactive dashboard live: [View on Power BI](https://app.powerbi.com/links/tKeXGPtC9O?ctid=bb4e68cd-fdbb-4789-82e5-1584d60de7f4&pbi_source=linkShare)

> **Note:** If you’re prompted to sign in or access is restricted, please let me know so I can enable guest access or share an exported PDF version.



Page 1: Overview

<img width="1431" height="806" alt="Screenshot 2025-11-08 114111" src="https://github.com/user-attachments/assets/734cecab-b1e3-448b-956a-efcab5f13e09" />


Page 2: Batting Analysis

<img width="1828" height="911" alt="Screenshot 2025-11-08 114426" src="https://github.com/user-attachments/assets/ec2ff589-805c-4d79-b97c-92219776f79f" />

Page 3: Bowling Analysis

<img width="1493" height="871" alt="Screenshot 2025-11-08 115305" src="https://github.com/user-attachments/assets/776d7c60-013d-4e1e-bad8-da9ec4de5125" />






