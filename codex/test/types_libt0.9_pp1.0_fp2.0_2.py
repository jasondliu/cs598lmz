import types
types.ModuleType.pipeline_preprocess_synset_array = lambda self: self.result_list

@patch.object(proc.Pipeline, "run_processes")
@patch.object(proc.TranslateDownloader, "download")
def test_init_with_custom_source_url(mock_download, mock_run_processes, tmpdir):

    # Download test file
    mock_download.return_value = str(tmpdir.join("test.txt"))

    # Fake result
    mock_result = {}
    # Fake run_processes
    def fake_run_processes(self, process_class_list, sources, results):
        self.result_list = process_class_list
        return mock_result

