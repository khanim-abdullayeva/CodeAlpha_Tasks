import requests
import json
import pandas as pd

def scrape_category_2(content,cat_code,category_name):
    url = f"https://api.worldarchery.sport/?content={content}&CompId=24448&CatCode={cat_code}&RBP=All&v=3"
    response = requests.get(url)
    data = response.json()
    results = data["items"][0]["Results"]

    new_list = []

    for athlete in results:
        athlete_copy = athlete.copy()

        team_members = []

        for member in athlete["Members"]:

            if member["WNameOrd"]:
                full_name = f"{member['FName']} {member['GName']}"
            else:
                full_name = f"{member['GName']} {member['FName']}"

            team_members.append(full_name)

        athlete_copy["Team_Members"] = ", ".join(team_members)

        athlete_copy.pop("Members")

        new_list.append(athlete_copy)

    df1 = pd.DataFrame(new_list)
    df1["Category"] = category_name
    df1=df1[["Rnk", "Category","NOC","Team_Members", "Score", "Gold", "Xnine"]]
    df1.rename(columns={"Rnk":"Rank"},inplace=True)
    return df1

df_rm_team = scrape_category_2(content="QUATEAM",cat_code="RM",category_name="Recurve Men Team")
df_rw_team = scrape_category_2(content="QUATEAM",cat_code="RW",category_name="Recurve Women Team")
df_recurve_mixed_team = scrape_category_2(content="QUATEAM",cat_code="RX",category_name="Recurve Mixed Team")
df_cm_team = scrape_category_2(content="QUATEAM",cat_code="CM",category_name="Compound Men Team")
df_cw_team = scrape_category_2(content="QUATEAM",cat_code="CW",category_name="Compound Women Team")
df_compound_mixed_team = scrape_category_2(content="QUATEAM",cat_code="CX",category_name="Compound Mixed Team")

final_team = pd.concat([df_rm_team,df_rw_team,df_recurve_mixed_team,df_cm_team,df_cw_team,df_compound_mixed_team],ignore_index=True)

if __name__ == "__main__":
    print(final_team)








