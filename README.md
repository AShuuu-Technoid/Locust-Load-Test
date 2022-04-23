# Locust Load Test

- ## STEP 1:
    `git clone https://github.com/AShuuu-Technoid/Locust-Load-Test.git`

- ## STEP 2:
    `cd Locust-Load-Test`

- ## STEP 3:
    `docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile1.py`

- ## STEP 4:
    Open browser `http://localhost:8089`