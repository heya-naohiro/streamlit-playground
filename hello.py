import streamlit as st
import json
import pandas as pd

st.write("こんにちは")

upload_jsonfile = st.file_uploader("SBOM/JSONファイルを選択してください", type='json')

if upload_jsonfile is not None:
    d = json.load(upload_jsonfile)
    if "packages" in d.keys():
        df = pd.DataFrame.from_dict(d["packages"])
        df
    else:
        print("有効なJSON/SBOMファイルをアップロードしてください")

