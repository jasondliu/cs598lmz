import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

#Read the data and create a list of lists
with codecs.open(data_file, 'r', 'utf-8', 'replace_with_space') as f:
    data_list = []
    for line in f:
        line = line.strip()
        if line:
            line = line.split('\t')
            data_list.append(line)

#Split data into train and test
train_data, test_data = train_test_split(data_list, test_size=0.2, random_state=1234)

#Create the dictionaries
word_to_id, id_to_word, label_to_id, id_to_label = create_dictionaries(train_data)

#Save the dictionaries
pickle.dump(word_to_id, open(dictionaries_path + 'word_to_id.pkl', 'wb'))
pickle.dump(id_to_word, open(dictionaries_path + 'id_to_
