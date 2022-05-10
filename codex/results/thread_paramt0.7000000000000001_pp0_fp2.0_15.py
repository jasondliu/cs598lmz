import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

def get_default_file_name():
    return time.strftime('%Y-%m-%d_%H-%M-%S.csv')

def create_base_df(df_dict, df_col_order, index_col_order, index_col_name, verbose):
    df = pd.DataFrame(df_dict, index=index_col_order)

    df.index.rename(index_col_name, inplace=True)

    df = df.reindex(columns=df_col_order)

    if verbose:
        print(df)
    return df

def plot_df(df, df_start_date, df_end_date, df_col_order, plot_title, plot_col_title, plot_file_name, verbose):
    plot_df = df[df.index >= df_start_date][df.index <= df_end_date]

    plot_df.plot(
        xlim=[df_start_date, df_
