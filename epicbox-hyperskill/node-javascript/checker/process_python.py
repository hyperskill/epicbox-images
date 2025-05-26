import json
import os

from util import TASK_ROOT, run_process

FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin '
OK_CODE = '0'
ASSERTION_ERROR_LINE = 'AssertionError: '


TESTS_FILES = [
    f'{TASK_ROOT}/test/tests.py'
]


def is_python_tests() -> bool:
    return any(os.path.isfile(f) for f in TESTS_FILES)

def process_python():
    score = 1
    feedback = ''
    output = []

    code, stdout, stderr = run_process([
        'python3', '-m', 'unittest', 'discover', '-s', 'test'
    ])
    stdout = stdout.splitlines()
    stderr = stderr.splitlines()

    if code != OK_CODE:
        score = 0
        for line_index, line in enumerate(stderr):
            if line.startswith(ASSERTION_ERROR_LINE):
                feedback = '\n'.join([
                    line[len(ASSERTION_ERROR_LINE):],
                    *stderr[line_index + 1:]
                ]).strip()
                feedback = (feedback.split('----------------------------------------------------------------------')[0]
                            .strip())
                break
        if not feedback:
            feedback = (
                'Cannot check the submission.\n\nPerhaps your program '
                'has fallen into an infinite loop or created too many objects in memory. '
                'If you are sure that this is not the case, please send the report to support@hyperskill.org\n'
                'stdout:\n{stdout}\n\nstderr:\n{stderr}'
                .format(stdout='\n'.join(stdout), stderr='\n'.join(stderr))
            )

    elif any(line.startswith(FAILED_TEST_BEGIN) for line in stdout):
        score = 0
        output_started = False
        for line in stdout:
            if output_started and line.startswith(FAILED_TEST_CONTINUE):
                output.append(line[len(FAILED_TEST_CONTINUE):])

            if not output_started and line.startswith(FAILED_TEST_BEGIN):
                output_started = True
                output.append(line[len(FAILED_TEST_BEGIN):])

        feedback = '\n'.join(output).strip()

    result = {
        'score': score,
        'feedback': feedback,
    }
    print(json.dumps(result))
