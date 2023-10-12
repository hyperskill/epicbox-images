import json

FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin '
OK_CODE = '0'
ASSERTION_ERROR_LINE = 'AssertionError:'

if __name__ == '__main__':
    score = 1
    feedback = ''
    output = []
    capture_feedback = False
    code = open('code.txt').read().strip()
    stdout = open('stdout.txt').read().splitlines()
    stderr = open('stderr.txt').read().splitlines()
    if code != OK_CODE:
        score = 0
        for line in stderr:
            if line.startswith(ASSERTION_ERROR_LINE):
                capture_feedback = True
                output.append(line[len(ASSERTION_ERROR_LINE):])
                continue
            if capture_feedback:
                output.append(line)
        feedback = '\n'.join(output).strip()
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
