import argparse

from bs4 import BeautifulSoup

def get_all_testsuites(soup):
  return soup.find_all('testsuites')


def get_testsuite(test_suites) -> dict:
  test_suite_all = test_suites.find_all('testsuite')
  ts = test_suite_all[0]
  test_suite_results = {
    'name' : ts.get('name', None),
    'exec_time' : ts.get('time', None),
    'ts' : ts.get('timestamp', None),
    'name' : ts.get('name', None),
    'tests' : ts.get('tests', None),
    'errors' : ts.get('errors', None),
    'failures' : ts.get('failures', None),
    'skipped' : ts.get('skipped', None),
    'hostname' : ts.get('hostname', None),
    'test_cases': [],
  }

  test_cases = ts.find_all('testcase')
  for tc in test_cases:
    case_results = {}
    status = 'success'
    if len(tc) > 0:
      failures = tc.find_all('failure')
      if len(failures) > 0:
        status = 'failed'
      else:
        status = 'unknown'

    case_results = {
      'name': tc.get('name', None),
      'classname': tc.get('classname', None),
      'exec_time': tc.get('time', None),
      'status': status,
    }

    test_suite_results['test_cases'].append(case_results.copy())

  return test_suite_results


def dict_to_md(tdict):
  '''
    Quick way to get this into markdown format.
    Won't be able to handle multiple testsuites.
  '''
  summary_header_md = f'''## Test Summary\n### {tdict['name']}\n'''
  summary_table_header_md = '|Execution Time | Number of Tests | Errors | Failures | Skipped |\n| --- | --- | --- | --- | --- |\n'
  summary_table_results_md =f'''|{tdict['exec_time']} | {tdict['tests']} | {tdict['errors']} | {tdict['failures']} | {tdict['skipped']} |\n'''

  results_table_header_md = '''\n|Name | Execution Time | Status |\n|--- | --- | --- |\n'''
  results_table_results_md = ''
  for case in tdict['test_cases']:
    case_result = f'''|{case['name']} | {case['exec_time']} | {case['status']} |\n'''
    results_table_results_md = results_table_results_md + case_result

  read_me_file = open('/code/summary.md', 'w')
  read_me_file.write(summary_header_md)
  read_me_file.write(summary_table_header_md)
  read_me_file.write(summary_table_results_md)
  read_me_file.write(results_table_header_md)
  read_me_file.write(results_table_results_md)
  read_me_file.close()

if __name__ == '__main__':
  with open('/code/summary.xml' ,'r') as f:
    data = f.read()

  soup = BeautifulSoup(data, 'xml')

  test_suites = get_all_testsuites(soup)
  test_suite_results = get_testsuite(test_suites[0])
  dict_to_md(test_suite_results)
