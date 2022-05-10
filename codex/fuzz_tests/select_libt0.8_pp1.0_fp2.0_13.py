import selectionStatuses from '../../selectionStatuses';

test('test run results are filtered by selection status', () => {
  const apiData = {
    results: [
      {
        job_id: 'abc',
        label: 'passed'
      },
      {
        job_id: 'abc',
        label: 'passed'
      },
      {
        job_id: 'abc',
        label: 'passed'
      },
      {
        job_id: 'abc',
        label: 'failed'
      },
      {
        job_id: 'abc',
        label: 'failed'
      },
      {
        job_id: 'abc',
        label: 'failed'
      },
      {
        job_id: 'abc',
        label: 'pending'
      },
      {
        job_id: 'abc',
        label: 'pending'
      },
      {
        job_id: 'abc',
        label: 'pending'
      },
      {
        job_id: 'abc',

