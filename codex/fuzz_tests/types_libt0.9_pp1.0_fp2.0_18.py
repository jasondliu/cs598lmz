import types
types_split = types.Split(types.Split.training | types.Split.validation, types.DataFrame)

# pylint:disable=no-member
label_key = types.FeatureName("birth_weight")

# Remove the label from column_names and add it to a list named 'label_name'
column_names.remove(label_key)
label_name = [label_key]

cols = []
for i in column_names:
  cols.append(types.FeatureName(i))
generator_dict = {col.name: col for col in cols}
# generator_dict ?
 
# Get the feature columns
def _transformer(cols):
  """ transformer """
  input_tensor = {
      key: tf.keras.layers.Input(name=key, shape=(), dtype=tf.float32)
      for key in cols
  }
  output_tensor = tf.feature_column.input_layer(input_tensor, cols)
  return tf.keras.Model(input_tensor, output
