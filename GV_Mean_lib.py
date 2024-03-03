import pandas as pd

file_name = '~/Downloads/MembraneExperiments_CTR shScramble Exp1.xlsx'
sheet_name = 'C2Rednew_CTR (2)'

def print_new_file(file_name):
    print(f'- The file "{file_name}" was just created.')

def get_mean_gv_percentage(file_name: str, sheet_name, verbose = False):
    df = pd.read_excel(f'{file_name}', sheet_name, )  

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Remove rows filled with NaN (Not a number)
    df = df.dropna(how='all')

    # Calculate the mean using {window_size} values
    window_size = 10
    mean_df = pd.DataFrame();
    for column in df:
        mean_df[column.replace('Value', 'Mean')] = [df[column][i:i + window_size].mean() for i in range(0, len(df), window_size)]

    # Export only means to excel
    file_means = file_name + '__means.xlsx'
    mean_df.to_excel(file_means)

    if verbose:
        print_new_file(file_means)

    columns = mean_df.columns[1:]
    for idx, column in enumerate(columns[::-1]):
        index = len(columns) - idx
        # Calculate GV - min
        # For each Groove mean value do: Mean - Min(Groove X)
        gv_min = [mean_df[column][i] - min(mean_df[column]) for i in range(0, len(mean_df))]

        # Calculate %GV
        # For each Groove mean value do: (GV_min * 100) - Min(Groove X)
        p_min = [(gv_min[i] * 100) - min(mean_df[column]) / max(mean_df[column]) for i in range(0, len(mean_df))]
        mean_df.insert(loc=index+1, column=f"GV-min {column}", value = gv_min)
        mean_df.insert(loc=index+2, column=f"%GV {column}", value = p_min)

    # Get only columns that start with '%GV'
    mean_gv_df = mean_df.loc[:, mean_df.columns.str.contains(f'^%GV')]

    # Calculate mean for each row
    mean_gv = [i[1].mean() for i in mean_gv_df.iterrows()]
    mean_gv_df.insert(loc=len(mean_gv_df.columns),column=f'MeanGV %GV',value=mean_gv)

    # Export %GV and Final Mean %GV to excel
    file_p_gv_means = file_name + '__final' + '.xlsx'
    mean_gv_df.to_excel(file_p_gv_means)

    if verbose:
        print_new_file(file_p_gv_means)