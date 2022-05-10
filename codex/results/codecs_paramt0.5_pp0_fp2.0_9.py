import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

# Load the model that you have fine-tuned
model_state_dict = torch.load(os.path.join(args.model_path, args.model_file))
model = BertForMultipleChoice.from_pretrained(args.model_name, state_dict=model_state_dict, num_choices=4)
model.to(device)

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained(args.model_name, do_lower_case=args.do_lower_case)

# Evaluate
eval_examples = read_race_examples(os.path.join(args.data_dir, 'dev', 'middle'))
eval_features = convert_examples_to_features(
    eval_examples, tokenizer, args.max_seq_length, True)
logger.info("***** Running evaluation *****")
logger.info("  Num examples = %d", len(eval_examples))
logger.info("  Batch size
