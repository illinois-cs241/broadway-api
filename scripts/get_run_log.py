import json
import requests
import sys

PROTOCOL = "http"
HOST = "127.0.0.1:1470"
COURSE = "malloc"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python start_run_script.py "
            "<grade run id> <token>"
        )
        exit(1)
    run_id = sys.argv[1]
    token = sys.argv[2]
    headers = {"Authorization": "Bearer {}".format(token)}

    r = requests.get(
        "{}://{}/api/v1/grading_job_log/{}/{}".format(PROTOCOL, HOST, COURSE, run_id),
        headers=headers,
    )
    if r.status_code != 200:
        print("Error in getting run log: {}".format(r.text))
        exit(1)

    res = json.loads(r.text)["data"]
    print(res)
