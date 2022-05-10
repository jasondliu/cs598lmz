import codecs
codecs.register_error("strict", codecs.ignore_errors)

class ResultTransformer(Transformer):
    def __init__(self, labels):
        Transformer.__init__(self)
        self.labels = labels
    
    def transform(self, results):
        transformed_results = []
        for result in results:
            transformed_results.append({label: result[i] for (label, i) in zip(self.labels, xrange(len(self.labels)))})
        return transformed_results
    
    def show_examples(self, #@UnusedVariable
                      table_type,
                      selection_vector,
                      example_ids,
                      instance_ids,
                      instances,
                      labels,
                      predictions,
                      hilite_selection,
                      results_dir,
                      data_dir):
        """ Output should contain an html table with the correct answers on the left, and
        the system's predictions on the right.  Hilight the correct answers in green and
        the incorrect answers in red. """
        def make_row(labels, inputs, predictions, instance_
