import pandas as pd
from main import final_individual
from scrape_2 import final_team

with pd.ExcelWriter("world_archery_results.xlsx") as writer:
    final_individual.to_excel(writer, sheet_name="Individual", index=False)
    final_team.to_excel(writer, sheet_name="Team", index=False)