fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

with pytest.raises(RuntimeError):
    tf.nest.flatten(fn)


@pytest.mark.parametrize(*EXAMPLES[0])
def test_flatten_dict(example, expected_elements):
    my_dict = collections.OrderedDict()
    for k, v in example:
        my_dict[k] = random_value(v)

    with tf.Graph().as_default(), tf.Session():
        flat = tf.nest.flatten_dict(my_dict)

    assert flat.keys() == expected_elements.keys()
    for k, v in flat.items():
        assert np.array_equal(v.eval(), expected_elements[k].eval())


def test_flatten_dict_with_list():
    my_dict = collections.OrderedDict()
    for k, v in EXAMPLES[0][0]:
        my_dict[k] = random_value(v)
    my_dict['list'] = [1, 2, 3]


