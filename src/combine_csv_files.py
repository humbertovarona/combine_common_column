def combine_csv_files(basefilename, referencefilename, columnname, outputfilename):
    df1 = pd.read_csv(basefilename)
    df2 = pd.read_csv(referencefilename)
    df_combined = df1.merge(df2, on=columnname)
    df_combined.to_csv(outputfilename, index=False)
