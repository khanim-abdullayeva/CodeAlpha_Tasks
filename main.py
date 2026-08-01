import requests
import json 
import pandas as pd

def scrape_category_1(cat_code,category_name):
    url = f"https://api.worldarchery.sport/?content=QUAIND&CompId=24448&CatCode={cat_code}&RBP=All&v=3"
    response = requests.get(url)
    data = response.json()

    results = data["items"][0]["Results"]

    new_list = []

    for athlete in results:
        athlete_copy = athlete.copy()                 
        athlete_copy.update(athlete["Athlete"])      
        athlete_copy.pop("Athlete")                   
        new_list.append(athlete_copy)


    df = pd.DataFrame(new_list)
    df["Full_Name"] = df["FName"] +" "+ df["GName"]
    df.drop(columns=["FName","GName","WNameOrd"],inplace=True)
    df["Category"] = category_name
    df=df[["Rnk", "Category","NOC","Full_Name", "Score", "Gold", "Xnine"]]
    df.rename(columns={"Rnk":"Rank"},inplace=True)
    return df

df_rm = scrape_category_1("RM","Recurve Men")
df_rw = scrape_category_1("RW","Recurve Women")
df_cm = scrape_category_1("CM","Compound Men")
df_cw = scrape_category_1("CM","Compound Women")

final_individual = pd.concat([df_rm,df_rw,df_cm,df_cw],ignore_index=True)

if __name__ == "__main__":
    print(final_individual)








