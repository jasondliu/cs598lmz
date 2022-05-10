import codecs
codecs.register_error("strict", codecs.ignore_errors)
import json


def get_df(table):
    schema = cobol.read_schema(table)
    df = cobol.read_file(table, format_='df', schema_=schema)
    return df


def ge_df_with_mask(table, mask):
    schema = cobol.read_schema(table)
    df = cobol.read_file(table, format_='df', schema_=schema, mask=mask)
    return df


def do_box(df, label=None, xlabel=None, ylabel=None, title=None, alpha=1.0, lw=1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index)).sort_index()
    g = sns.catplot(x=xlabel, y=ylabel,
                    data=df, kind="violin",
                    bw=.1, cut=0,
                    palette="Set3", alpha=alpha, legend=False)
   
