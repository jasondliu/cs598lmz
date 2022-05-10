import types
types.SimpleNamespace = SimpleNamespace

# parser = argparse.ArgumentParser()
# parser.add_argument('--input', type=str, required=True)
# parser.add_argument('--output', type=str, required=True)
# args = parser.parse_args()
#
# validate_input_file(args.input, require_igv_output=True)

print('hello world')
df = pd.read_csv(genespark_demo, sep='\t')
df['tumor_content'] = df['percontumor'].round()
df.columns = ['1', '2', '3', '4', 'target_freq', 'color_by', 'log2', '8', '9', '10']
df2 = pd.read_csv(genespark_demo2, sep='\t')
df2.columns = ['1', '2', '3', 'color_by']
df3 = pd.read_csv(genespark_demo3, sep='\t')
