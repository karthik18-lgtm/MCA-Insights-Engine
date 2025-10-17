import os
import pandas as pd
import streamlit as st

# === Local CSV paths - update for your machine ===
file_paths = [
    "/Users/karthikravala/Aadiswan/maharastra.csv",
    "/Users/karthikravala/Aadiswan/Gujarat.csv",
    "/Users/karthikravala/Aadiswan/Delhi.csv",
    "/Users/karthikravala/Aadiswan/Tamilnadu.csv",
    "/Users/karthikravala/Aadiswan/Karnataka.csv"
]

required_columns = [
    "cin", "companyname", "companyclass", "companyregistrationdate_date",
    "authorizedcapital", "paidupcapital", "companystatus",
    "companyindustrialclassification", "nic_code", "registered_office_address",
    "companyroccode", "companystatecode"
]

def normalize_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "").str.replace("-", "")
    return df

# Load and concatenate master CSVs
dfs = []
for file in file_paths:
    if not os.path.exists(file):
        st.warning(f"File not found: {file}")
        continue
    try:
        df = pd.read_csv(file, on_bad_lines="skip", engine='python', encoding='utf-8')
        if df.empty:
            st.warning(f"Empty file skipped: {file}")
            continue
        df = normalize_columns(df)
        for col in required_columns:
            if col not in df.columns:
                df[col] = ""
        df_filtered = df[required_columns]
        dfs.append(df_filtered)
    except Exception as e:
        st.error(f"Error reading {file}: {e}")

if not dfs:
    st.stop()

master_df = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=["cin"])
master_df["authorizedcapital"] = pd.to_numeric(master_df["authorizedcapital"], errors='coerce').fillna(0)
master_df["paidupcapital"] = pd.to_numeric(master_df["paidupcapital"], errors='coerce').fillna(0)
master_df = master_df.dropna(subset=["cin", "companyname"])

st.title("MCA Full Company Master Dataset")

search_query = st.text_input("Search by CIN or Company Name")

filtered_df = master_df

if search_query:
    mask = (
        master_df['cin'].str.contains(search_query, case=False, na=False) |
        master_df['companyname'].str.contains(search_query, case=False, na=False)
    )
    filtered_df = master_df[mask]

max_rows = 1000
st.dataframe(filtered_df.head(max_rows).reset_index(drop=True))
st.write(f"Showing first {max_rows} records only. Please filter your search to view more.")

st.write(f"Total companies matching: {len(filtered_df)}")

